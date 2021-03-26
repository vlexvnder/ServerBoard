from pathlib import Path
import os
from subprocess import call
import json
import docker

with open('config.json') as f:
    config = json.load(f)

with open('containers.json') as c:
    containers = json.load(c)

client = docker.from_env()
 
def compose(app_name):
    global config
    global containers
    install_path = config['install_path'] + app_name

    if(not Path(install_path).exists()):
        call('mkdir '+install_path, shell=True)

    call('/bin/cp '+containers[app_name]['compose_file']+' '+install_path+'/docker-compose.yml ', shell=True)


    with Path(install_path) as p:
            working_dir = Path().absolute()
            os.chdir(p)
            call('docker-compose up -d', shell=True)
            os.chdir(working_dir)
            
def deleteContainer(id):
    global client
    container = client.containers.get(id)
    container.remove(force=True)

def deleteCompose(name):
    global containers
    for n in containers[name]["service_names"]:
        deleteContainer(n)