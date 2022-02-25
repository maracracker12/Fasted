from fastapi import FastAPI

app = FastAPI()

#qamar = [{"Name":"Qamar","Age":19,"Location":"Kirkuk"}]

@app.get("/")
def index():
    return {"Status":"ok"}
