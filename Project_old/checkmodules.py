import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
print (installed_packages)

print('Checking for dependent modules :' )
if 'tinydb' in installed_packages:
    print("tinydb : installed ")
else:
    print("tinydb : not installed ")

if 'requests' in installed_packages:
    print("requests : installed ")
else:
    print("requests : not installed ")
    

