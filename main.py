from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return [
  {
    "date": "2018-05-06",
    "temperatureC": 1,
    "summary": "Freezing"
  },
  {
    "date": "2018-05-07",
    "temperatureC": 14,
    "summary": "Bracing"
  },
  {
    "date": "2018-05-08",
    "temperatureC": -13,
    "summary": "Freezing"
  },
  {
    "date": "2018-05-09",
    "temperatureC": -16,
    "summary": "Balmy"
  },
  {
    "date": "2018-05-10",
    "temperatureC": -2,
    "summary": "Chilly"
  }
]


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
