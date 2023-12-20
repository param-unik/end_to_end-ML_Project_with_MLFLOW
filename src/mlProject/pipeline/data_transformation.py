from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger

STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            configuration_manager = ConfigurationManager()
            data_transformation_config = configuration_manager.get_data_transformation()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.train_test_splitting()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} in the DataTransformationTrainingPipeline <<<<<< ")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Finished {STAGE_NAME} in the DataTransformationTrainingPipeline <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e