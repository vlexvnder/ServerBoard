from pathlib import Path
import os
from subprocess import call
import json

with open('config.json') as f:
    config = json.load(f)
with open('containers.json') as c:
    containers = json.load(c)
 
def createContainer(app_name):
    global config
    global containers
    install_path = config['install_path'] + app_name

    if(not Path(install_path).exists()):
        call('mkdir '+install_path, shell=True)

    with open(install_path+'/docker-compose.yml', "w") as f:
        with open(containers[app_name]['compose_file'], 'w') as c:
            f.write(c)

    with Path(install_path) as p:
            working_dir = Path().absolute
            os.chdir(p)
            call('docker-compose up -d', shell=True)
            os.chdir(working_dir)
createContainer("Heimdall")