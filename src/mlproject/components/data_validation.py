import os
from mlproject import logger
import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"column Validation status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"column Validation status: {validation_status}\n")
        
            return validation_status
        
        except Exception as e:
            raise e


    def validate_data_types(self) -> bool:
        """Check if each column has the correct datatype as per schema."""
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            validation_status = True

            for col, expected_dtype in self.config.all_schema.items():
                if col in data.columns:
                    actual_dtype = str(data[col].dtype)
                    if expected_dtype not in actual_dtype:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'a') as f:
                            f.write(f"Datatype mismatch in column '{col}': expected {expected_dtype}, got {actual_dtype}\n")

            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Data Type Validation Status: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e