import os
from typing import Optional
import uvicorn
from fastapi import FastAPI
import dotenv

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
