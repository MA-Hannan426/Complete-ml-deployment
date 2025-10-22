import os
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
import numpy as np
import joblib
from mlproject.entity.config_entity import  ModelEvaluatorConfig
from pathlib import Path
from mlproject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluatorConfig):
        self.config = config

    def evaluate_model(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2_square = r2_score(actual, pred)
        return rmse, mae, r2_square

    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns=[self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        predicted_qualities = model.predict(test_x)

        (rmse, mae, r2_square) = self.evaluate_model(test_y, predicted_qualities)

        #savingmetrics as local
        scores = {
            "RMSE": rmse,
            "MAE": mae,
            "R2_Square": r2_square
        }

        save_json(path=Path(self.config.metric_file_name), data=scores)
