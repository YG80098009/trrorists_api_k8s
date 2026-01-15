from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
from models import Threat, ResponseThreat
from db import collection

app = FastAPI()

@app.post("/big_threats", response_model=ResponseThreat)
def get_big_threats(file: UploadFile = File(...)):
    try:
        contents = file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        df_sorted = df.sort_values(by="risk_level")
        top_5_df = df_sorted.head(5)
        
        big_threats_list = []
        for i, row in top_5_df.iterrows():
            threat_data = {
                "name": row["name"],
                "location": row["location"],
                "risk_level": int(row["risk_level"])
            }
          
            object_threat = Threat(**threat_data)
            big_threats_list.append(object_threat.dict())

        if big_threats_list:
            collection.insert_many(big_threats_list)

        return {
            "count": len(big_threats_list),
            "top": big_threats_list
        }

    except:
        raise HTTPException(status_code=422, detail=str(Exception))

