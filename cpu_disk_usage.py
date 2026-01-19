import shutil
import psutil

def check_disk_usage(disk_usage):
    du = shutil.disk_usage(disk_usage)
    free= du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage < 75

print(check_disk_usage("/"))
print(check_cpu_usage())

if not check_disk_usage("/") or not check_cpu_usage():
    print("error")
else:
    print("Both CPU and Disk usage are OK")



