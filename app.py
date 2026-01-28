from fastapi import FastAPI
import random

app = FastAPI()

pets = [
    {"name": "Mochi", "emoji": "🐶"},
    {"name": "Luna", "emoji": "🐱"},
    {"name": "Boba", "emoji": "🐰"},
    {"name": "Pudding", "emoji": "🐼"}
]

moods = ["happy 😄", "sleepy 😴", "excited 🤩", "hungry 🍪"]

@app.get("/")
def home():
    pet = random.choice(pets)
    mood = random.choice(moods)
    return {"message": f"{pet['emoji']} {pet['name']} is feeling {mood} today!"}


@app.get("/pet")
def get_pet():
    return random.choice(pets)

@app.get("/feed")
def feed_pet():
    return {"message": "Your pet is eating :)"}

@app.get("/sleep")
def sleep_pet():
    return {"message": "Your pet is sleeping"}
