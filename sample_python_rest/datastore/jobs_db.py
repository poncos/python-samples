from sample_python_rest.config import config
from sample_python_rest.model.job import Job

import sqlite3

from typing import List


class JobsDb:

    def __init__(self, app_config: config.ApplicationConfig):
        self.__db_config = app_config.datastore("sqllite")

        self.__create_job_stm = """insert into jobs
        (group_id, type, status, description)
        values
        (?, ?, 'PENDING', ?) 
        """
        # RETURNING id,group_id,type,description,status,created_at,started_at,finished_at)

        self.__list_jobs_stm = """
        select job_id, group_id, type, description, status, error_msg, created_at, started_at, finished_at
        from jobs where group_id=?
        """

        self.__select_job_stm = """
            select job_id,group_id,type,description,status,created_at,started_at,finished_at
            from jobs where job_id=?
        """

        self.__db_con = None

    def create_job(self, group_id, description, job_type) -> Job:
        connection = self.__get_db_connection()

        cursor = connection.cursor()
        params = (group_id, job_type, description)
        cursor.execute(self.__create_job_stm, params)
        connection.commit()

        # Retrieve the ID of the inserted row
        last_row_id = cursor.lastrowid
        record = self.__get_job_record(last_row_id, cursor)
        return Job(id=record[0], group_id=record[1], type=record[2],
                   description=record[3], status=record[4], error_msg=record[5], created_at=record[6],
                   started_at=None, finished_at=None)

    def __get_job_record(self, job_id, cursor):
        cursor.execute(self.__select_job_stm, (job_id, ))
        return cursor.fetchone()

    def list_jobs(self, group_id) -> List[Job]:
        connection = self.__get_db_connection()

        cursor = connection.cursor()
        cursor.execute(self.__list_jobs_stm, (group_id, ))
        records = cursor.fetchall()

        jobs = [None] * len(records)
        row_number = 0

        # try to substitute this look with list comprehension
        for row in records:
            jobs[row_number] = Job(id=row[0], group_id=row[1], type=row[2], description=row[3], status=row[4],
                                   error_msg=row[5], created_at=row[6], started_at=row[7], finished_at=row[8])
            row_number += 1

        cursor.close()
        return jobs

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
