
import resource
resource.setrlimit(resource.RLIMIT_DATA, (0,16*1000*1000))

### Uncomment either this section:

# L = []
# i = 0
# while True:
#     L.append(i)

### or this section:

# child = ["python", "child.py"]
# import subprocess
# try:
#     subprocess.check_call(child)
# except subprocess.CalledProcessError as e:
#     print(str(e))
