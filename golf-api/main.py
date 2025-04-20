 
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 入力データのモデル
class Shot(BaseModel):
    shotNum: int
    club: str
    distance: int
    result: str
    curve: str

class HoleData(BaseModel):
    holeNumber: int
    shots: List[Shot]

class RoundData(BaseModel):
    name: str
    gender: str
    targetScore: str
    holes: int
    data: List[HoleData]

@app.get("/")
def read_root():
    return {"message": "ゴルフラウンドAPIへようこそ！"}

@app.post("/upload")
def upload_round(round: RoundData):
    # 将来的にデータベース保存や分析に使う
    return {"message": "データを受け取りました", "total_holes": len(round.data)}
