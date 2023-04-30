
from sensor.pipeline.training_pipeline import start_training_pipeline


file_path="/home/ali/anaconda3/Coding Playground/ML_Projects_Deployment/aps-fault-detection-main/aps_failure_training_set1.csv"
print(__name__)
if __name__=="__main__":
    try:
        start_training_pipeline()
    except Exception as e:
        print(e)