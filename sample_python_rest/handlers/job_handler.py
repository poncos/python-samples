import logging
from typing import List

from sample_python_rest.datastore.jobs_db import JobsDb
from sample_python_rest.model.job_group import JobGroup
from sample_python_rest.model.job import Job


class JobHandler:

    def __init__(self, ds_jobs: JobsDb):
        self.__ds_jobs = ds_jobs

    def load_jobs_by_group(self, group_id) -> List[Job]:
        logging.debug(f"Loading jobs for group id {group_id}")

        jobs = self.__ds_jobs.list_jobs(group_id=group_id)
        group = JobGroup(jobs)

        #print(f"returning jobs {jobs}")
        #print(f"returning group: {group}")
        return group

    def create_job(self, group_id, type, description):
        logging.debug(f"Creating job with description {description}")

        job = self.__ds_jobs.create_job(group_id, description, type)
        return job
