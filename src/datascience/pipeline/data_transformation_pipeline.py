from src.datascience.config.configuration import *
from src.datascience.components.data_ingestion import *
from src.datascience import logger
from src.datascience.components.data_transformation import *

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            print(e)
    