"""Server file
Attributes:
    app (fastapi.applications.FastAPI): Fast API app
"""
import os
import dotenv
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

dotenv.load_dotenv()

from core.classifiers import BOWSubclassPredictor, BERTSubclassPredictor

app = FastAPI()


class ClassificationRequest(BaseModel):
    """Class for defining input parameters data type"""

    text: str
    n: str
    model: str


@app.post("/classify")
async def classify(item: ClassificationRequest):
    """Find relevant CPC technology subclasses for a given text snippet.

    Returns:
    list: Array of subclass codes, most relevant first.
    """

    data = item
    text = data.text
    n_sub_classes = int(data.n)
    if data.model == "BOWSubclassPredictor":
        model = BOWSubclassPredictor()
    else:
        model = BERTSubclassPredictor()

    sub_classes = model.predict_subclasses(text, n_sub_classes)
    return sub_classes


if __name__ == "__main__":
    port = int(os.environ["PORT"])
    uvicorn.run(app, host="0.0.0.0", port=port)
