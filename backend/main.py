from fastapi import FastAPI, HTTPException

from telegram_api.chats import get_chats, get_chat

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/telegram/chats")
async def telegram_chats():
    chats = get_chats()
    return chats

@app.get("/telegram/chats/{chat_id}")
async def telegram_chat(chat_id: int):
    chat = get_chat(chat_id)
    if not chat:
        # Updates cached chats with get_chats
        _ = get_chats()
        chat = get_chat(chat_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found") 
    return chat