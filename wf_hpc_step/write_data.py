import os
import time
import random
import base64

workdir = os.getenv("PBS_O_WORKDIR")
if workdir:
    basedir = workdir
else:
    basedir = os.path.dirname(__file__)
data_path = basedir + "/somedata.txt"
if os.path.exists(data_path):
    os.unlink(data_path)

iterations = random.randint(120, 240)


print("Generate %s" % data_path)
print("Running %s iterations" % data_path)
for i in range(1, iterations + 1):
    msg = base64.b64encode(os.urandom(512 * 2**10))
    print("Add data: %s" % msg[:10])
    with open(data_path, "ab") as fp:
        fp.write(msg)
        fp.write(b'\n')
    time.sleep(1)
