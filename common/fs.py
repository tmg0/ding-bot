import yaml
import glob
import importlib
import os


def read_yaml(path):
    with open(path, "r") as yaml_file:
        yml_data = yaml.safe_load(yaml_file)
    return yml_data


def import_glob(pattern):
    module_files = glob.glob(pattern)
    imported_modules = []

    for file_path in module_files:
        module_name = os.path.splitext(file_path)[0]
        module_path = module_name.replace(os.path.sep, ".")

        try:
            imported_module = importlib.import_module(module_path)
            imported_modules.append(imported_module)
        except Exception as e:
            pass

    return imported_modules
