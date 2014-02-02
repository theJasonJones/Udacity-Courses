#import time library to use time.clock()
import time

def time_execution(code):
  start = time.clock()
  result = eval.clock()
  run_time = time.clock() - start
  return result, run_time

def spin_loop(n):
  i = 0
  while i < n:
    i += 1

#test cases
print time_execution('spin_loop(1000)')
print time_execution('spin_loop(100000)')
print time_execution('spin_loop(1000000)')
