import requests
import ollama
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Query(BaseModel):
    api_prompt: str = "Ciao come ti chiami?"
    api_model: str = "llama3.1"

@app.get('/')
def home():
    return {"Chat": "AI CHAT"}

@app.get('/generate') 
async def ollama_chat(api_prompt: str = "Ciao come ti chiami?", api_model: str = "llama3.1"):
    try:
        system_prompt= {"role": "system", "content": "ti chiami Gigi e sei un assitente molto cordiale e preparato"}
        user_messages = {"role": "user", "content": api_prompt}
        
        api_message = [system_prompt, user_messages]
        res = ollama.chat(
            model=api_model,
            messages=api_message,
            stream=False
        )
        
        return Response(content=res["message"]["content"].strip(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))