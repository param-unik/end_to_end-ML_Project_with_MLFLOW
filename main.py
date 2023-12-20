from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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