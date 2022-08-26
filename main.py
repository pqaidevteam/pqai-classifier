import os
import dotenv
import uvicorn
from pydantic import BaseModel
from typing import Union, Optional
from fastapi import FastAPI, Response

dotenv.load_dotenv()

# pylint: disable=wrong-import-position
from core.classifiers import BOWSubclassPredictor, BERTSubclassPredictor

app = FastAPI()


@app.get("/subclasses")
async def predict_subclasses(
    text: str,
    n: Optional[int] = 5,
    predictor: Optional[str] = "bert-subclass-predictor",
):
    """Return subclass predictions for given text snippet"""
    classifier = BERTSubclassPredictor()
    return classifier.predict_subclasses(text, n)


if __name__ == "__main__":
    port = int(os.environ["PORT"])
    uvicorn.run(app, host="0.0.0.0", port=port)
