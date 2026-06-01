from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse, JSONResponse
import logging
from pydantic import BaseModel

from prometheus_fastapi_instrumentator import Instrumentator

from sample_python_rest.handlers.job_handler import JobHandler
from sample_python_rest.datastore.jobs_db import JobsDb
from sample_python_rest.config.config import ApplicationConfig
from sample_python_rest.model.job_mapper import JobMapper

root_path = "/sample-python-rest"

app = FastAPI(
    docs_url=f"{root_path}/docs",
    openapi_url=f"{root_path}/openapi.json",
    redoc_url=f"{root_path}/redoc",
    root_path="/")

Instrumentator().instrument(app).expose(app, endpoint=f"{root_path}/prometheus")

applicationConfig = ApplicationConfig()
jobsDB = JobsDb(applicationConfig)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.info("Starting FastAPI Application")


class JobRequestModel(BaseModel):
    type: str
    description: str


@app.get(f"{root_path}/v1")
def read_root():
    return {"Job API": "Job API v1.0"}


@app.get(f"{root_path}/v1/jobs/{{job_group_id}}")
def get_jobs(job_group_id: int):
    logger.info(f"Fetching jobs with group id {job_group_id}")
    handler = JobHandler(jobsDB)
    job_group = handler.load_jobs_by_group(job_group_id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=JobMapper.job_group_to_dict(job_group))


@app.post(f"{root_path}/v1/jobs/{{job_group_id}}")
def create_job(job_group_id: int, job_details: JobRequestModel):
    logger.info(f"Creating job group id {job_group_id} and description {job_details.description}")
    handler = JobHandler(jobsDB)
    job = handler.create_job(job_group_id, job_details.type, job_details.description)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=JobMapper.job_to_dict(job))


@app.get(f"{root_path}/health")
async def health():
    return PlainTextResponse(status_code=status.HTTP_200_OK, content="UP")
