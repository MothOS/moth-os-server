import bottle
import yaml
from .routes import index, version, ping, monitor


def init(config_file_path: str):
    # GET API CONFIG
    with open(config_file_path, "r") as config_file:
        api_config = yaml.load(config_file, Loader=yaml.FullLoader)["api"]

    print(api_config)
    bottle.run(host=api_config["host"], port=api_config["port"], debug=True)
