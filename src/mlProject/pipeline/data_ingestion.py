from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_data()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} in the DataIngestionTrainingPipeline <<<<<< ")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Finished {STAGE_NAME} in the DataIngestionTrainingPipeline <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e