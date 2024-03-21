from mlopslib import MLOpsGCSClient
import gcp_key

GCP_KEY_FILE = gcp_key.GCP_KEY_FILE

client = MLOpsGCSClient(GCP_KEY_FILE)

client.upload_model(
    bucket_name="mlops-model-bucket-0",
    model_name="nlp-model",
    local_dir_path="../model"
)