#!/usr/bin/env python3

import subprocess
from os import linesep
import json
from rofi import Rofi

r = Rofi()
subprocess.run("whoami > /tmp/whoami",shell=True)
with open("/tmp/whoami","r") as whoami: user = whoami.read().replace(linesep,"")
home = str(f"/home/{user}")
multimc_folder = f"{home}/.local/share/multimc/instances" # replace with wherever multimc folder is, if this isn't it

try:
	with open(f"{multimc_folder}/instgroups.json", "r") as raw_inst_groups:
		instgroups = json.loads(raw_inst_groups.read())
except:
	r.exit_with_error("MultiMC folder not found. Please add it to the code.")

instances = []
instances_grouped = []
for group in instgroups["groups"]:
	for instance in instgroups["groups"][group]["instances"]:
		instances.append(instance)
		instances_grouped.append(f"{instance} ({group})")

index, key = r.select('instance', instances_grouped)
if (key == -1):
	exit()
print(f"launching {instances[index]}")
subprocess.run(f"multimc -l {instances[index]}".split(" "))