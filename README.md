# <a href="#EN">English</a>
## 安装
```bash
pip3 install DSMonitor
```

## 使用方法
假设有以下这一段代码在服务器上运行，我们希望运行时可以看到程序的运行状况，那么可以使用DSMonitor给你的函数添加装饰器：

```python
from DSMonitor import func_monitor  #0.0.30
import time
import random

@func_monitor(level="INFO",show_output=True)
def add(b):
    time.sleep(random.random())
    a = 1+b
    return 2

@func_monitor(level="DEBUG")
def sub(x):
    u = x**2
    y = u-x
    return y

for i in range(10):
    add(i)
    sub(i)

```

那么我们将在终端看到:

```bash
[2020-09-05  15:27:11] INFO func: add, input: {'b': 0}, output: type 'int', memory cost: 112, time cost: 0.878, output detail: 2
[2020-09-05  15:27:11] DEBUG func: sub, input: {'x': 0}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 0, 'u': 0, 'x': 0}
[2020-09-05  15:27:12] INFO func: add, input: {'b': 1}, output: type 'int', memory cost: 112, time cost: 0.973, output detail: 2
[2020-09-05  15:27:12] DEBUG func: sub, input: {'x': 1}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 0, 'u': 1, 'x': 1}
[2020-09-05  15:27:13] INFO func: add, input: {'b': 2}, output: type 'int', memory cost: 112, time cost: 0.799, output detail: 2
[2020-09-05  15:27:13] DEBUG func: sub, input: {'x': 2}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 2, 'u': 4, 'x': 2}
[2020-09-05  15:27:13] INFO func: add, input: {'b': 3}, output: type 'int', memory cost: 112, time cost: 0.735, output detail: 2
```

func_monitor 将函数的输入、输出类型、用时、占用内存打印在了终端上，并且可以设置参数level、show_output的值来决定是否将栈帧、返回结果也一并输出

上面是在同步函数场景下的用法,如果你希望对异步函数也实现同样的操作,DSMonitor也提供了async_func_monitor,例如:

```python
from DSMonitor import func_monitor, async_func_monitor
import aiohttp
import asyncio

@func_monitor(level="DEBUG",show_output=True)
def func():
    a = 1
    b = 2
    return a+b


@async_func_monitor(level="INFO",show_output=True)
async def async_func(n):
    async with aiohttp.ClientSession() as client:
        res = await client.get('http://httpbin.org/delay/{}'.format(2))
        result = await res.json()


if __name__ == "__main__":
    func()
    loop = asyncio.get_event_loop()
    for i in range(3):
        loop.run_until_complete(async_func(i))
```
运行这段代码,我们将在终端看到:
```bash
[2020-09-06  10:23:07] DEBUG func: func, input: {}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'b': 2, 'a': 1}, output detail: 3
[2020-09-06  10:23:09] INFO (async)func: async_func, input: {'n': 0}, output: type 'NoneType', memory cost: 112, time cost: 2.478, output detail: None
[2020-09-06  10:23:12] INFO (async)func: async_func, input: {'n': 1}, output: type 'NoneType', memory cost: 112, time cost: 2.464, output detail: None
[2020-09-06  10:23:15] INFO (async)func: async_func, input: {'n': 2}, output: type 'NoneType', memory cost: 112, time cost: 3.034, output detail: None
```

<a name="EN"></a>
## EN

## Installation
```bash
pip3 install DSMonitor
```
# Instructions
Assuming that the following piece of code is running on the server, and we want to see the running status of the program at runtime, you can use DSMonitor to add decorators to your functions:

```python
from DSMonitor import func_monitor  #0.0.30
import time
import random

@func_monitor(level="INFO",show_output=True)
def add(b):
    time.sleep(random.random())
    a = 1+b
    return 2

@func_monitor(level="DEBUG")
def sub(x):
    u = x**2
    y = u-x
    return y

for i in range(10):
    add(i)
    sub(i)

```
Then we will see in the terminal:

```bash
[2020-09-05  15:27:11] INFO func: add, input: {'b': 0}, output: type 'int', memory cost: 112, time cost: 0.878, output detail: 2
[2020-09-05  15:27:11] DEBUG func: sub, input: {'x': 0}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 0, 'u': 0, 'x': 0}
[2020-09-05  15:27:12] INFO func: add, input: {'b': 1}, output: type 'int', memory cost: 112, time cost: 0.973, output detail: 2
[2020-09-05  15:27:12] DEBUG func: sub, input: {'x': 1}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 0, 'u': 1, 'x': 1}
[2020-09-05  15:27:13] INFO func: add, input: {'b': 2}, output: type 'int', memory cost: 112, time cost: 0.799, output detail: 2
[2020-09-05  15:27:13] DEBUG func: sub, input: {'x': 2}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 2, 'u': 4, 'x': 2}
[2020-09-05  15:27:13] INFO func: add, input: {'b': 3}, output: type 'int', memory cost: 112, time cost: 0.735, output detail: 2
```
func_monitor prints the input, output type, time used, and memory usage of the function on the terminal, and can set the value of the parameter level and show_output to determine whether to output the stack frame and return result together

The above is the usage in the synchronous function scenario. If you want to implement the same operation for asynchronous functions, dsmonitor also provides async_ func_ Monitor, for example:
```python
from DSMonitor import func_monitor, async_func_monitor
import aiohttp
import asyncio
  
@func_monitor(level="DEBUG",show_output=True)
def func():
    a = 1
    b = 2
    return a+b


@async_func_monitor(level="INFO",show_output=True)
async def async_func(n):
    async with aiohttp.ClientSession() as client:
        res = await client.get('http://httpbin.org/delay/{}'.format(2))
        result = await res.json()


if __name__ == "__main__":
    func()
    loop = asyncio.get_event_loop()
    for i in range(3):
        loop.run_until_complete(async_func(i))
```
Running this code, we will see in the terminal:
```bash
[2020-09-06  10:23:07] DEBUG func: func, input: {}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'b': 2, 'a': 1}, output detail: 3
[2020-09-06  10:23:09] INFO (async)func: async_func, input: {'n': 0}, output: type 'NoneType', memory cost: 112, time cost: 2.478, output detail: None
[2020-09-06  10:23:12] INFO (async)func: async_func, input: {'n': 1}, output: type 'NoneType', memory cost: 112, time cost: 2.464, output detail: None
[2020-09-06  10:23:15] INFO (async)func: async_func, input: {'n': 2}, output: type 'NoneType', memory cost: 112, time cost: 3.034, output detail: None
```

## History
### 0.0.30
- func_monitor finished
### 0.1.10
- add async_func_monitor
