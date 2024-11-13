from fastapi import FastAPI
from API.Routing import Alerts, Subscription


app = FastAPI()

app.include_router(Alerts.router)
app.include_router(Subscription.router)