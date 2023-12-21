from pathlib import Path

from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import dagshub


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        dagshub.init(repo_owner='param-unik', repo_name='end_to_end-ML_Project_with_MLFLOW',
                     mlflow=True)

    def eval_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return rmse, mae, r2

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            prediction = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, prediction)

            scores = {'rmse': rmse, 'mae': mae, 'r2': r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticModel")
            else:
                mlflow.sklearn.log_model(model, "model")