from typing import List

from sample_python_rest.model.job import Job
from sample_python_rest.model.job_group import JobGroup


class JobMapper:

    @classmethod
    def job_to_dict(cls, job: Job):
        print(f"Mapping job: {job}")
        return {
            "id": job.id,
            "group": job.group_id,
            "status": job.status,
            "type": job.type,
            "error": job.error_msg,
            "created_at": job.created_at,
            "started_at": job.started_at,
            "finished_at": job.finished_at
        }

    @classmethod
    def jobs_to_dict(cls, jobs: List[Job]):
        print(f"jobs to dict")
        results = [JobMapper.job_to_dict(job) for job in jobs]

        return results

    @classmethod
    def job_group_to_dict(cls, group: JobGroup):
        return {
            "pending_jobs": JobMapper.jobs_to_dict(group.pending_jobs),
            "failed_jobs": JobMapper.jobs_to_dict(group.failed_jobs),
            "successful_jobs": JobMapper.jobs_to_dict(group.successful_jobs)
        }

