# from turtle import title
from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn


# use huggingface pipeline to use model
generator = pipeline('text-generation',model='gpt2')

# define fastapi
app = FastAPI(
    title = "Fast API App for LLM model",
    description = " A text generation app",
    version ="1.0"
)



class Body(BaseModel):
    text:str



@app.get('/')
def index():
    # return HTMLResponse("<h1> WELCOME TO LLMOPS COURSE WITH GP2 MODEL </h1>")
    return "This is index changed response."
@app.post('/generate')
def predict(body:Body):
    results = generator(body.text,max_length=350,num_return_sequence=1)
    return results[0]['generated_text']


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)