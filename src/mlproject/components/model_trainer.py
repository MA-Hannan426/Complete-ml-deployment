import os
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from mlproject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        # Load training data
        train_data = pd.read_csv(self.config.train_data_path)
        
        X_train = train_data.drop(columns=[self.config.target_column])
        y_train = train_data[self.config.target_column]

        # Initialize and train the model
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        model.fit(X_train, y_train)

        # Save the trained model
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model, model_path)

        return model_path 