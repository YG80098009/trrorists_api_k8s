from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
from models import Threat, ResponseThreat
from db import collection

app = FastAPI()

@app.post("/top_threats", response_model=ResponseThreat)
def get_top_threats(file: UploadFile = File(...)):
    try:
        contents = file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        df_sorted = df.sort_values(by="danger_rate")
        top_5_df = df_sorted.head(5)
        
        top_threats_list = []
        for i, row in top_5_df.iterrows():
            threat_data = {
                "name": row["name"],
                "location": row["location"],
                "danger_rate": int(row["danger_rate"])
            }
          
            object_threat = Threat(**threat_data)
            top_threats_list.append(object_threat.dict())

        if top_threats_list:
            collection.insert_many(top_threats_list)

        return {
            "count": len(top_threats_list),
            "top": top_threats_list
        }

    except:
        raise HTTPException(status_code=422, detail=str(Exception))

