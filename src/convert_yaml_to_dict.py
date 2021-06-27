import yaml
import json
import os
from pathlib import Path

from paths import DATA_DIRECTORY

def create_missing_path_directories(file_path):
    """
    Checks if path includes any directories. 
    If directories exist, then missing directories are created.
    """

    directories_exists_in_path = False

    if len(file_path.rsplit("\\", 1)) == 2:
        dirs, _ = file_path.rsplit("\\", 1)
        directories_exists_in_path = True

    if len(file_path.rsplit("/", 1)) == 2:
        dirs, _ = file_path.rsplit("/", 1)
        directories_exists_in_path = True

    if directories_exists_in_path:
        directories = os.path.join(DATA_DIRECTORY, dirs)
        Path(directories).mkdir(parents=True, exist_ok=True)

def yaml_to_dict(file_name):

    with open(file_name, 'r') as yaml_file:
        try:
            return yaml.safe_load(yaml_file)
        except yaml.YAMLError as err:
            print(err)

def save_data_to_json(data, file_path):

    create_missing_path_directories(file_path)

    if ".json" not in file_path:
        file_path = file_path + ".json"

    with open(os.path.join(DATA_DIRECTORY, file_path), 'w') as file:
        json.dump(data, file)
        print("Data saved to file: " + file_path)


file_name = "context_rule_revamp.yml"
file_path = os.path.join(DATA_DIRECTORY, file_name)

data = yaml_to_dict(file_name=file_path)
save_data_to_json(data, "gaz/it/test2.json")