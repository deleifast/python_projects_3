import psutil
import datetime

### *** CPU FUNCTIONS ***

# Number of logical CPUs in the system
print ("psutil.cpu_count() = ", psutil.cpu_count())


### *** DISK FUNCTIONS ***

# Disk usage statistics
du = psutil.disk_usage('/')
print("psutil.disk_usage('/') = ", du)


### *** MEMORY FUNCTIONS ***

# System memory usage statistics
mem = psutil.virtual_memory()
print("psutil.virtual_memory() = ", mem)

THRESHOLD = 100 * 1024 * 1024  # 100MB
if mem.available <= THRESHOLD:
    print("warning")


# System boot time converted to human readable format
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# Users currently connected on the system
users = psutil.users()
print("psutil.users() = ", users)