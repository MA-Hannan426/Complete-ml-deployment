from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open("artifacts/data_validation/status.txt", 'r') as f:
                status = f.read().lower()
    
            if "column validation status: true" in status and "data type validation status: true" in status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("Data Validation Failed. Cannot proceed to Data Transformation, as the schema is not valid")
            
        except Exception as e:
            logger.exception(e)
            raise e 
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        Data_Transformation = DataTransformationPipeline()
        Data_Transformation.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
