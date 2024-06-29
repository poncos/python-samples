from sample_python_rest.config import config
from sample_python_rest.model.job import Job

import sqlite3

from typing import List

class JobsDb:

    def __init__(self, app_config: config.ApplicationConfig):
        self.__db_config = app_config.datastore("sqllite")

        self.__create_job_stm = """insert into jobs
        (job_group_id, job_type, status, description)
        values
        (%(groupid)s, %(job_type)s, 'created', %(description)s)
        RETURNING job_id,job_group_id,job_type,description,status,created_at)
        """

        self.__list_jobs_stm = """
        select job_id, job_group_id, job_type, description, status, created_at, started_at, finished_at
        from jobs
        """

    def create_job(self, group_id, description, job_type) -> Job:
        connection = self.__get_db_connection()

        cursor = connection.cursor()
        cursor.execute(self.__create_job_stm, {"groupid": group_id, "description": description, "job_type": job_type})
        connection.commit()

        record = cursor.fetchone()
        print(f"Record created: {record}")

        return Job(id=record[0], group_id=record[1], type=record[2],
                   description=record[3], status=record[4], created_at=record[5],
                   started_at=None, finished_at=None)

    def list_jobs(self, group_id) -> List[Job]:
        None

    def __get_db_connection(self):
        if self.__db_con is None:
            self.__db_con = self.__create_connection()
        return self.__db_con

    def __create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.__db_config['url'])
        except Exception as e:
            print(f"Unable to create connection to jobs database, Error {str(e)}")
        return conn
