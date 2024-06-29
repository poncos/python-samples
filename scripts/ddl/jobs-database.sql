
create table jobs (
    job_id INTEGER PRIMARY KEY,
    group_id INTEGER NOT NULL,
    type VARCHAR(50) NOT NULL,
    description VARCHAR(250),
    status TEXT CHECK( status IN ('PENDING', 'PROCESSING', 'SUCCESSFUL', 'FAILED')) NOT NULL DEFAULT 'PENDING',
    error_msg VARCHAR(250),
    created_at TIMESTAMP,
    started_at TIMESTAMP,
    finished_at TIMESTAMP
);