# This snippet that can be used to time a 
import time

def timeme(method):
     def wrapper(*args,**kw):
          startTime=int(round(time.time()*1000))
          result=method(*args,**kw)
          endTime=int(round(time.time()*1000))
          print("Execution time:{}se".format((endTime-startTime)/1000))
          return result
     return wrapper

# Call the timing the function using the @ sign just before the function you want to time
# Example '@timeme'