from mlProject.constants import *
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig
from mlProject.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(
            self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH
    ):
        self.config_filepath = read_yaml(config_filepath)
        self.params_filepath = read_yaml(params_filepath)
        self.schema_filepath = read_yaml(schema_filepath)

        create_directories([self.config_filepath.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_filepath.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config_filepath.data_validation
        schema = self.schema_filepath.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_dir=config.unzip_dir,
            all_schema=schema,
        )
        return data_validation_config