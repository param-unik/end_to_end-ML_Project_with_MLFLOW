from mlProject import logger
from mlProject.pipeline.data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.model_evaluation import ModelEvaluationPipeline
from mlProject.pipeline.model_training import ModelTrainingPipeline

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


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} in the DataTransformationTrainingPipeline <<<<<< ")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Finished {STAGE_NAME} in the DataTransformationTrainingPipeline <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "ML Model Training Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} in the ModelTrainingPipeline <<<<<< ")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Finished {STAGE_NAME} in the ModelTrainingPipeline <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "ML Model Evaluation Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} in the ModelEvaluationPipeline <<<<<< ")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> Finished {STAGE_NAME} in the ModelEvaluationPipeline <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e