import yaml
from yaml.resolver import BaseResolver
import json
import csv
import os
from pathlib import Path

from paths import DATA_DIRECTORY


class AsLiteral(str):
  pass


def convert_to_yaml_literal(data):
    """
    Converts yaml output to string literal with style "|"
    """
    return AsLiteral(yaml.dump(data))

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

def read_yaml(file_path):
    """
    Reads yaml file and returns data in python dictionary format.
    """

    with open(os.path.join(DATA_DIRECTORY, file_path), 'r') as yaml_file:
        try:
            return yaml.safe_load(yaml_file)
        except yaml.YAMLError as err:
            print(err)

def read_csv(file_path):
    """
    Reads csv file and returns data in python list format.
    """

    with open(os.path.join(DATA_DIRECTORY, file_path), 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            row = [i for i in row if i]
            data.append(row)
        return data

def read_json(file_path):
    """ Reads json file and returns data in python dictionary format. """

    with open(os.path.join(DATA_DIRECTORY, file_path), 'r') as json_file:
        return json.load(json_file)
        
def save_data_to_json(data, file_path):
    """
    Saves python dictionary data to json file. 
    """

    create_missing_path_directories(file_path)

    if ".json" not in file_path:
        file_path = file_path + ".json"

    with open(os.path.join(DATA_DIRECTORY, file_path), 'w') as file:
        json.dump(data, file)
        print("Data saved to file: " + file_path)

def save_data_to_yaml(data, file_path):
    """
    Save python dictionary data to yaml file.
    """

    def represent_literal(dumper, data):
        return dumper.represent_scalar(BaseResolver.DEFAULT_SCALAR_TAG, data, style="|")

    yaml.add_representer(AsLiteral, represent_literal)

    create_missing_path_directories(file_path)

    if ".yml" not in file_path and ".yaml" not in file_path:
        file_path = file_path + ".yml"

    with open(os.path.join(DATA_DIRECTORY, file_path), 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False, sort_keys=False)
        print("Data saved to file: " + file_path)
