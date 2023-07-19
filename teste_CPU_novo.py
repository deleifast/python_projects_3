import shutil

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Usado: %d GiB" % (used // (2**30)))
print("Livre: %d GiB" % (free // (2**30)))
