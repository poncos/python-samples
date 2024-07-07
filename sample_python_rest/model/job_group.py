
from sample_python_rest.model.job import Job

from typing import List


class JobGroup:

    def __init__(self, jobs: List[Job]):
        self.__jobs = jobs

        self.pending_jobs = [job for job in jobs if job.is_job_pending()]
        self.failed_jobs = [job for job in jobs if job.is_job_failed()]
        self.successful_jobs = [job for job in jobs if job.is_job_successful()]

        print(f"Pending JObs: {self.pending_jobs}")

    def is_done(self):
        pending_jobs = [self.__jobs for job in self.__jobs if job.is_job_pending()]
        return len(pending_jobs) == 0

    def is_successful(self):
        failed_jobs = [self.__jobs for job in self.__jobs if job.is_job_failed()]
        return self.is_done() and len(failed_jobs) == 0

    def is_failed(self):
        failed_jobs = [self.__jobs for job in self.__jobs if job.is_job_failed()]
        return self.is_done() and len(failed_jobs) > 0
