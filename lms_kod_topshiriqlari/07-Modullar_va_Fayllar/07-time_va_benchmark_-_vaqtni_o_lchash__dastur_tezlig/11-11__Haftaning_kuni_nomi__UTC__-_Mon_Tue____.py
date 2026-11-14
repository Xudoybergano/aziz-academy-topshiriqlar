import time
t = int(input())
tm = time.gmtime(t)
names = ["Mon", "Tue", "Wed", "Thu",
"Fri", "Sat", "San"]
print(names[tm.tm_wday])