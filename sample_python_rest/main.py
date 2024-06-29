from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Job API": "Job API v1.0"}


@app.get("/jobs/{job_group}/")
def get_jobs(job_groupd_id: int):
    return {"job_groupd_id": job_groupd_id}


@app.post("/jobs/{job_group_id}/{job_id}")
def update_item(job_group_id: int, job_id: int, item: Item):
    return {"job_group_id": job_group_id, "job_id": job_id}
