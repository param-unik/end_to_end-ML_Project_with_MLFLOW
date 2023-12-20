import os
import urllib.request as req
import zipfile
from pathlib import Path
from mlProject import logger
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = req.urlretrieve(url=self.config.source_URL,
                                                filename=self.config.local_data_file)
            logger.info(f"{filename} downloaded successfully! here are the details : \n {headers}")
        else:
            logger.info(
                f"File already exist with size of :{get_size(Path(self.config.local_data_file))}")

    def unzip_data(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_dir)