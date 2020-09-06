import functools
import time
import logging
import sys
import inspect
from hashlib import md5

from .func_hash_cache import func_hash_cache
from .utils import Exceptions

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(message)s",
                    datefmt = '[%Y-%m-%d  %H:%M:%S]'
                    )

class async_generator_monitor(object):
    
    def __init__(self, level='INFO', show_output=False):
        if level not in ["INFO", "DEBUG"]:
            raise Exceptions.ParamsError("level must be 'INFO' or 'DEBUG'")
        self.level = level
        self.show_output = show_output
        self.fhc = func_hash_cache()

    def __call__(self, func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            input_params = inspect.getcallargs(func, *args, **kwargs)
            
            self.func_obj_key = "f"+self._hash_it(func.__name__)
            temp = {}
            temp.update(func.__globals__)
            temp.update(globals())
            globals().update(temp)
            globals()[self.func_obj_key] = None

            new_func = self.fhc.get_func_obj(self.func_obj_key)
            if not new_func:
                new_func = self._new_func_obj(func, "new_func")
                self.fhc.append_new_func(self.func_obj_key, new_func)
            start_ts = time.time()
            res = new_func(*args, **kwargs)
            cost_time = time.time() - start_ts
            cost_memory = func.__sizeof__()

            if isinstance(res, list) or isinstance(res, dict) or isinstance(res, tuple) or isinstance(res, set) or isinstance(res, str):
                res_length = len(res)
                res_type = str(type(res)).strip(">").strip("<").replace("class","type")
                logging_info = "{} (async)func: {}, input: {}, output: {}, length: {}, memory cost: {}, time cost: {:.3f}".format(
                    self.level, func.__name__, input_params, res_type, res_length, cost_memory, cost_time)
            else:
                 res_type = str(type(res)).strip(">").strip("<").replace("class","type")
                 logging_info = "{} (async)func: {}, input: {}, output: {}, memory cost: {}, time cost: {:.3f}".format(
                         self.level, func.__name__, input_params, res_type, cost_memory, cost_time)

            if self.level == "DEBUG":
                logging_info += ", locals:'cannot get async generator\'s locals'"

            if self.show_output:
                logging_info += ", output detail: {}".format(res)
            logging.info(logging_info)
            yield res
        return wrapper
        
    def _new_func_obj(self, func, new_func_name):
        src = inspect.getsource(func)
        src_list = src.splitlines()
        if src_list[1].split("def")[0].strip() != "async":
            raise Exceptions.DecoratorTypeError("async_func_monitor cannot be used for synchronizations functions, use func_monitor instead")
        src_list[1] = src_list[1].replace(func.__name__, new_func_name)
        src_list.insert(2,"    global {}".format(self.func_obj_key))
        src_list.insert(3,"    {} = inspect.currentframe()".format(self.func_obj_key))
        src_list.pop(0)
        code = "\n".join(src_list)
        exec(code)
        return eval(new_func_name) 

    def _hash_it(self, str_obj):
        hash_obj = md5()
        hash_obj.update(str_obj.encode('utf-8'))
        return hash_obj.hexdigest()
