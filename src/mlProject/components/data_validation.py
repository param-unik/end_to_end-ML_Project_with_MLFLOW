import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status for {col} in the data : {validation_status} ")
                        break
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status : {validation_status}")
        except Exception as e:
            logger.info(f"Error while validating as {e.message}")
            logger.exception(e)
            raise e

        return validation_status