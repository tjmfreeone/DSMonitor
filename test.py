from DSMonitor import func_monitor
import time
from functools import * 
import ast

@func_monitor(level="DEBUG")
def add(b):
    #time.sleep(1)
    a = 1+b
    return 2

for i in range(10):
    res1 = add(i)



