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
[2020-09-05  15:27:13] DEBUG func: sub, input: {'x': 3}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 6, 'u': 9, 'x': 3}
[2020-09-05  15:27:14] INFO func: add, input: {'b': 4}, output: type 'int', memory cost: 112, time cost: 0.971, output detail: 2
[2020-09-05  15:27:14] DEBUG func: sub, input: {'x': 4}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 12, 'u': 16, 'x': 4}
[2020-09-05  15:27:15] INFO func: add, input: {'b': 5}, output: type 'int', memory cost: 112, time cost: 0.635, output detail: 2
[2020-09-05  15:27:15] DEBUG func: sub, input: {'x': 5}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 20, 'u': 25, 'x': 5}
[2020-09-05  15:27:15] INFO func: add, input: {'b': 6}, output: type 'int', memory cost: 112, time cost: 0.619, output detail: 2
[2020-09-05  15:27:15] DEBUG func: sub, input: {'x': 6}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 30, 'u': 36, 'x': 6}
[2020-09-05  15:27:16] INFO func: add, input: {'b': 7}, output: type 'int', memory cost: 112, time cost: 0.223, output detail: 2
[2020-09-05  15:27:16] DEBUG func: sub, input: {'x': 7}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 42, 'u': 49, 'x': 7}
[2020-09-05  15:27:16] INFO func: add, input: {'b': 8}, output: type 'int', memory cost: 112, time cost: 0.491, output detail: 2
[2020-09-05  15:27:16] DEBUG func: sub, input: {'x': 8}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 56, 'u': 64, 'x': 8}
[2020-09-05  15:27:16] INFO func: add, input: {'b': 9}, output: type 'int', memory cost: 112, time cost: 0.219, output detail: 2
[2020-09-05  15:27:16] DEBUG func: sub, input: {'x': 9}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 72, 'u': 81, 'x': 9}
```

func_monitor 将函数的输入、输出类型、用时、占用内存打印在了终端上，并且可以设置参数level、show_output的值来决定是否将栈帧、返回结果也一并输出

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
[2020-09-05  15:27:13] DEBUG func: sub, input: {'x': 3}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 6, 'u': 9, 'x': 3}
[2020-09-05  15:27:14] INFO func: add, input: {'b': 4}, output: type 'int', memory cost: 112, time cost: 0.971, output detail: 2
[2020-09-05  15:27:14] DEBUG func: sub, input: {'x': 4}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 12, 'u': 16, 'x': 4}
[2020-09-05  15:27:15] INFO func: add, input: {'b': 5}, output: type 'int', memory cost: 112, time cost: 0.635, output detail: 2
[2020-09-05  15:27:15] DEBUG func: sub, input: {'x': 5}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 20, 'u': 25, 'x': 5}
[2020-09-05  15:27:15] INFO func: add, input: {'b': 6}, output: type 'int', memory cost: 112, time cost: 0.619, output detail: 2
[2020-09-05  15:27:15] DEBUG func: sub, input: {'x': 6}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 30, 'u': 36, 'x': 6}
[2020-09-05  15:27:16] INFO func: add, input: {'b': 7}, output: type 'int', memory cost: 112, time cost: 0.223, output detail: 2
[2020-09-05  15:27:16] DEBUG func: sub, input: {'x': 7}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 42, 'u': 49, 'x': 7}
[2020-09-05  15:27:16] INFO func: add, input: {'b': 8}, output: type 'int', memory cost: 112, time cost: 0.491, output detail: 2
[2020-09-05  15:27:16] DEBUG func: sub, input: {'x': 8}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 56, 'u': 64, 'x': 8}
[2020-09-05  15:27:16] INFO func: add, input: {'b': 9}, output: type 'int', memory cost: 112, time cost: 0.219, output detail: 2
[2020-09-05  15:27:16] DEBUG func: sub, input: {'x': 9}, output: type 'int', memory cost: 112, time cost: 0.000, locals: {'y': 72, 'u': 81, 'x': 9}
```
func_monitor prints the input, output type, time used, and memory usage of the function on the terminal, and can set the value of the parameter level and show_output to determine whether to output the stack frame and return result together


## History
### 0.0.30
- func_monitor finished
