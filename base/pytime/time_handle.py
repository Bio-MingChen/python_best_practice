import time as tm
import datetime as dt

time_str = "2021-10-10 12:14:00"
# time string to struct time
struct_time = tm.strptime(time_str,"%Y-%m-%d %H:%M:%S")
print(struct_time)
print(dir(struct_time))

back_to_str = tm.strftime("%Y-%m-%d %H:%M:%S",struct_time)
print(back_to_str)


# get current time
print(tm.ctime()) # current local time string
print(tm.time())  # current timestamp
print(dt.datetime.now()) # current time with datetime class

# struct_time to timestamp
timestamp = tm.mktime(struct_time)
print(timestamp)
#timestamp to struct_time
back_to_struct_l = tm.localtime(timestamp) # local time
back_to_struct_g = tm.gmtime(timestamp) # global time

#time.localtime and time.mktime are related
print(back_to_struct_l)
print(back_to_struct_g)


old_time = "1910-06-01"
old_time_struct = tm.strptime(old_time,"%Y-%m-%d")
# print(old_time_struct)
# old_timestamp = tm.mktime(old_time_struct) # timestamp is negative before 1970-1-1
# print(old_timestamp)

datetime_class = dt.datetime.fromtimestamp(tm.time())
timestamp = dt.datetime.timestamp(datetime_class)

print(type(datetime_class))
print(timestamp)

print(datetime_class.strftime("%Y-%m-%d"))
dateime_class = dt.datetime.strptime(time_str,"%Y-%m-%d %H:%M:%S")
back_to_time_str = datetime_class.strftime("%Y-%m-%d")
print(datetime_class)
print(back_to_time_str)
