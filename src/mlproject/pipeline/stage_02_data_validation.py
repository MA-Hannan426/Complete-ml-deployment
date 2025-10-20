from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_validation import DataValidation
from mlproject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize config
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        # Initialize Data Validation
        data_validation = DataValidation(config=data_validation_config)

        # Run validation steps
        columns_valid = data_validation.validate_all_columns()
        dtypes_valid = data_validation.validate_data_types()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e