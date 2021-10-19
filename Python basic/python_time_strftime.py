import time

now_time = time.localtime()

print(time.strftime('%Y%m%d', now_time))
print(time.strftime('%x', now_time))
print(time.strftime('%X', now_time))