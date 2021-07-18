import redfish

config_file_path = 'config/config.json'
with open(config_file_path) as f:
    config = json.load(f)


ip = config["ilo"]["ip"]
user = config["ilo"]["username"]
password = config["ilo"]["password"]

def pushPower():
    REST_OBJ = redfish.LegacyRestClient(base_url=ip, username=user, password=password)
    REST_OBJ.login(auth="session")
    response = REST_OBJ.post("/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/", {'ResetType': 'PushPowerButton'})
    try:
        REST_OBJ.logout()
    except:
        pass
    return response