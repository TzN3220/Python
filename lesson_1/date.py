import time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)
print("{0}/{1}/{2} {3}:{4}:{5}".format(localtime.tm_mday,localtime.tm_mon,localtime.tm_year,localtime.tm_hour,localtime.tm_min,localtime.tm_sec))