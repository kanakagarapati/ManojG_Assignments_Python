from configparser import ConfigParser
import os

def parse_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")

    parser = ConfigParser()
    parser.read(file_path)

    config_data = {}
    for section in parser.sections():
        config_data[section] = dict(parser.items(section))

    return config_data