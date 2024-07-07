from dataclasses import dataclass
from enum import Enum

# JobStatus = Enum('Status', ['PENDING', 'PROCESSING', 'SUCCESSFUL', 'FAILED'])
PENDING = 'PENDING'
PROCESSING = 'PROCESSING'
SUCCESSFUL = 'SUCCESSFUL'
FAILED = 'FAILED'


@dataclass(frozen=True)
class Job:
    id: int
    group_id: int
    type: str
    description: str
    status: str
    error_msg: str
    created_at: str
    started_at: str
    finished_at: str

    def is_job_pending(self):
        return (
                self.status is None or
                self.status == PENDING or
                self.status == PROCESSING
        )

    def is_job_successful(self):
        return self.status == SUCCESSFUL

    def is_job_failed(self):
        return self.status == FAILED
