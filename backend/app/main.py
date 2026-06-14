import streamlit as st

st.write("✅ Streamlit started")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from .routers import chatbot, alerts, reminders, upload

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot.router)
app.include_router(alerts.router)
app.include_router(reminders.router)
app.include_router(upload.router)

@app.get("/")

def home():

    return {
        "msg": "AI Healthcare Backend Running"
    }
