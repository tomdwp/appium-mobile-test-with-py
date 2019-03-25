
import os, json

class Util:

    @classmethod
    def read_desired_capabilities_data(cls, file_name_without_path):
        path_of_parent_of_current_file = os.path.dirname(os.path.realpath(__file__))
        full_path_of_desired_capabilities = path_of_parent_of_current_file + os.path.sep + file_name_without_path
        with open(full_path_of_desired_capabilities, 'r') as f:
            config_data = json.load(f)
        return config_data