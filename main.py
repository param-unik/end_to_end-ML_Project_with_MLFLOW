from mlProject import logger
from mlProject.pipeline.Stage_2_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

logger.info("welcome to our custom logging")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} in the DataIngestionTrainingPipeline <<<<<< ")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Finished {STAGE_NAME} in the DataIngestionTrainingPipeline <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} in the DataValidationTrainingPipeline <<<<<< ")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Finished {STAGE_NAME} in the DataValidationTrainingPipeline <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e