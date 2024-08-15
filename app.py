from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.stage_05_prediction import PredictionPipeline

text:str = "What is text summarization"
app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    """
    asynchronous function is a type of function that allows for non-blocking execution, 
    meaning it can perform tasks without waiting for other tasks to complete before 
    moving on to the next one. 
    """
    return RedirectResponse(url = "/docs")# In FastAPI, /docs is the default path for the auto-generated 
    #interactive API documentation (Swagger UI).

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Successfully Trained the Model!!")
    
    except Exception as e:
        return Response(f"Error Occured: {e}")
    
@app.post("/prediction")
async def prediction_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    
@app.on_event("shutdown")
async def shutdown_event():
    print("Application is shutting down!!")
    
if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port=8080)


