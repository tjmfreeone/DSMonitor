

class func_hash_cache(object):
    def __init__(self):
        self.func_map = dict()

    def get_func_obj(self, func_obj_key):
        if func_obj_key not in self.func_map:
            return 
        return self.func_map[func_obj_key]

    def append_new_func(self, func_obj_key, func_obj):
        self.func_map[func_obj_key] = func_obj

    def clear_func_map(self):
        self.func_map.clear()
