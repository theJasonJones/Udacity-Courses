#import time library to use time.clock()
import time

def time_execution(code):
  start = time.clock()
  result = eval(code)
  run_time = time.clock() - start
  return result, run_time

#To be honest, this really doesn't do much of anything
def spin_loop(n):
  i = 0
  while i < n:
    i += 1

#test cases where each should increase by a factor of ~10
print time_execution('spin_loop(10 ** 5)') #ten thousand
print time_execution('spin_loop(10 ** 6)') #ten million
print time_execution('spin_loop(10 ** 7)')
print time_execution('spin_loop(10 ** 8)')