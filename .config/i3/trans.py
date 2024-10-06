import subprocess
import os
command = "picom-trans --current --get"

output = subprocess.check_output(command, shell=True, universal_newlines=True)

print(output)

if "100" in output:
	os.system("picom-trans --current --opacity 40")
else:
	os.system("picom-trans --current --opacity 100")
