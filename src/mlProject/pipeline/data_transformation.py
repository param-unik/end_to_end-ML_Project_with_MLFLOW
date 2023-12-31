from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status:
                configuration_manager = ConfigurationManager()
                data_transformation_config = configuration_manager.get_data_transformation()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your schema is not valid! Kindly correct before re-running this "
                                "pipeline.")
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