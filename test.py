import os
import time
from datetime import datetime
# path
path = "C:/users/admin/Desktop/New Text Document.txt"

# Get the status of
# the specified path
status = os.stat(path)

# Print the status
# of the specified path
print(status.st_mtime)

# ts stores the time in seconds
ts = time.time()

# print the current timestamp
print(ts)

if status.st_mtime == ts:
    print('All Good')

else:
    print('Error')

timestamp1 = status.st_mtime
timestamp2 = ts

dt_object1 = datetime.fromtimestamp(timestamp1)
dt_object2 = datetime.fromtimestamp(timestamp2)

print("dt_modified =", dt_object1)
print("dt_current =", dt_object2)