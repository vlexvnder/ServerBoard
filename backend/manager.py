from pathlib import Path
import os
from subprocess import call
import json
import docker

config_file_path = 'config/config.json'
container_file_path = 'config/containers.json'

with open(config_file_path) as f:
    config = json.load(f)

with open(container_file_path) as c:
    containers = json.load(c)

client = docker.from_env()
 
def compose(app_name):
    install_path = config['install_path'] + app_name

    if(not Path(install_path).exists()):
        call('mkdir '+install_path, shell=True)

    call('/bin/cp '+containers[app_name]['compose_file']+' '+install_path+'/docker-compose.yml ', shell=True)


    with Path(install_path) as p:
            working_dir = Path().absolute()
            os.chdir(p)
            call('docker-compose up -d', shell=True)
            os.chdir(working_dir)
            
def deleteContainer(name):
    container = client.containers.get(name)
    container.remove(force=True)

def deleteCompose(name):
    for n in containers[name]["service_names"]:
        deleteContainer(n)