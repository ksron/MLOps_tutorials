from contextlib import asynccontextmanager

from simplet5 import SimpleT5
from pydantic import BaseModel
from fastapi import FastAPI

from mlopslib import MLOpsGCSClient
import gcp_key

GCP_KEY_FILE = gcp_key.GCP_KEY_FILE

# From Kaggle example text
class Input(BaseModel):
    text: str="""summarize: Twitter’s interim resident grievance officer for India has stepped down, leaving the micro-blogging site without a grievance official as mandated by the new IT rules to address complaints from Indian subscribers, according to a source.

The source said that Dharmendra Chatur, who was recently appointed as interim resident grievance officer for India by Twitter, has quit from the post.

The social media company’s website no longer displays his name, as required under Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021.

Twitter declined to comment on the development.

The development comes at a time when the micro-blogging platform has been engaged in a tussle with the Indian government over the new social media rules. The government has slammed Twitter for deliberate defiance and failure to comply with the country’s new IT rules.
"""

def load_model():
    client = MLOpsGCSClient(GCP_KEY_FILE)
    
    model_list = [
        'config.json', 'eval_results.txt', 'generation_config.json',
        'model_args.json', 'pytorch_model.bin', 'special_tokens_map.json',
        'spiece.model', 'tokenizer_config.json', 'training_args.bin'
        ]
    blob_base = "nlp-model"
    

    for model_name in model_list:
        client.dowload_model(
            bucket_name="mlops-model-bucket-0",
            blob_name=f"{blob_base}/{model_name}",
            dest_file_path=f"./model/{model_name}"
        )
    
    print("start model load")
    model = SimpleT5()
    model.load_model("t5", "/model", use_gpu=False)

    print("finished model load")
    return model

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["nlp_model"] = load_model() 
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()

app = FastAPI(lifespan=lifespan)

@app.post("/predict")
async def predict(input: Input):
    result = ml_models["nlp_model"].predict(input.text)[0]
    return {"result": result}