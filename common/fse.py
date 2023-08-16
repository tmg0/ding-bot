import yaml

def read_yaml (path):
  with open(path, 'r') as yaml_file:
    yml_data = yaml.safe_load(yaml_file)
  return yml_data

