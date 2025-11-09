from configparser import ConfigParser
from .func import *
import json
import os

async def generate_command_auto(websocket, config):
    models = await listvtsmodel(websocket)
    runs = models["data"]["numberOfModels"]
    n = len(config["COMMANDS"])
    num_of_models = runs - n
    if n >= num_of_models:
        return
    with open("commands.ini", "w") as configfile:
        for i in range(runs):
            ff = models["data"]["availableModels"][i]["modelName"]
            gg = models["data"]["availableModels"][i]["modelID"]
            name = "!" + ff
            mdss = mdch.__name__ + "(websocket,'" + str(gg) + "')"
            config["COMMANDS"][name] = mdss
        config.write(configfile)

async def setup_token(websocket):
    if os.path.exists("token.json"):
        print("Loading authtoken From File...")
        with open("token.json", "r") as json_file:
            data = json.load(json_file)
            authtoken = (data["authenticationkey"])
            confirm = await authen(websocket,authtoken)
            if authtoken == "" or confirm["data"]["authenticated"] == False:
                print("Error Token Invalid")
                print("Fetching New Tokens...")
                authtoken = await token(websocket)
                print(authtoken)
                print("Saving authtoken for Future Use...")
                data["authenticationkey"] = authtoken
                json_file.close()
                json_file = open("token.json", "w")
                json_file.write(json.dumps(data))
                json_file.close()
                print("Saving finished")
            else:
                json_file.close()
        return
    print("Fetching New Tokens...")
    authtoken = await token(websocket)
    print(authtoken)
    print("Saving authtoken for Future Use...")
    with open("token.json", "w") as json_file:
        jsonfilecon = {
            "chatspeed": 0.1,
            "authenticationkey": authtoken
        }
        json_file.write(json.dumps(jsonfilecon))
        json_file.close()
    await authen(websocket, authtoken)

def setup_commands():
    if os.path.exists("commands.ini"):
        config = ConfigParser()
        config.read("commands.ini")
    else:
        config = ConfigParser()
        with open("commands.ini", "w") as configfile:
            config["COMMANDS"] = {
                    "!spin": "spin(websocket, x, y, s)",
                    "!reset": "mdmv(websocket, 0.2, False, 0, 0, 0, -76)",
                    "!rainbow": "rainbow(websocket)"
                }
            config.write(configfile)
    return config

async def setup(websocket):
    await setup_token(websocket)
    config = setup_commands()
    await generate_command_auto(websocket, config)
    print("Successfully Loaded")
    print("Detected Commands")
    for key in config["COMMANDS"]:
        print(key)
    return config