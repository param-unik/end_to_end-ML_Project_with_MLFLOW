from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger
from pathlib import Path

STAGE_NAME = "ML Model Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status:
                config_manager = ConfigurationManager()
                model_evaluation_config = config_manager.get_model_evaluation_config()
                model_evaluation = ModelEvaluation(config=model_evaluation_config)
                model_evaluation.log_into_mlflow()
            else:
                raise Exception("Your schema is not valid! Kindly correct before re-running this "
                                "pipeline.")
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} in the ModelEvaluationPipeline <<<<<< ")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> Finished {STAGE_NAME} in the ModelEvaluationPipeline <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e