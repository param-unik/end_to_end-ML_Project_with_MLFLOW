from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_validation_config = config_manager.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_data()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} in the DataValidationTrainingPipeline <<<<<< ")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Finished {STAGE_NAME} in the DataValidationTrainingPipeline <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e