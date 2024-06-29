import os
import yaml


class ApplicationConfig:

    def __init__(self):
        env = os.getenv('ENVIRONMENT', 'dev')
        conf_file = 'config/config-%s.yaml' % env

        self.__yamlConfig = self.__get_yaml_cfg(conf_file)

    def __get_yaml_cfg(self, file_location):
        cfg_file = file_location
        with open(cfg_file,  'r') as yml_file:
            cfg = yaml.safe_load(yml_file)
        return cfg

    def datastore(self, store_name):
        return self.__yamlConfig['datastore'][store_name]
