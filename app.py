from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Loading Iris Dataset
iris = load_iris()

# Getting features and targets from the dataset
X = iris.data
Y = iris.target

# Fitting our Model on the dataset
clf = GaussianNB()
clf.fit(X,Y)

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

app = FastAPI()

@app.post("/predict")
async def predict(data: request_body):
    test_data = [[ data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    class_idx = clf.predict(test_data)[0]
    return {"class": iris.target_names[class_idx]}
