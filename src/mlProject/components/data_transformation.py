import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # here we can add different data transformation techniques such as Standard Scaler, MinMax
    # Scaler, PCA, Embedding techniques such as OHE, Label encoding etc. etc.
    # we can apply PCA, t-SNE as well and missing value treatments if required.

    # as of now, we only need train split only as data does not requiured any other
    # transformation to get applied for now.

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # split the data into training and test set as 75% and 25%

        train, test = train_test_split(data, test_size=0.25, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Data split into train and test successfully!")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)