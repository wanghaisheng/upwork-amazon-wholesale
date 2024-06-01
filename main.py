from scraper import job_alerts
from fastapi import FastAPI


app = FastAPI()


@app.get("/jobs/{keywords}")
async def job_feed(keywords):
    return {"jobs": await job_alerts(keywords)}
