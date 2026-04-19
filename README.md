# Sample Python REST API

A sample REST API built with FastAPI for managing jobs and job groups. This application demonstrates a basic CRUD API with database integration and Prometheus monitoring.

## Features

- RESTful API for job management
- SQLite database integration
- Prometheus metrics endpoint
- Health check endpoint
- Docker support
- Kubernetes deployment configuration

## Prerequisites

- Python 3.9+
- pip
- SQLite (for local development)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sample-python-rest
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
sqlite3 resources/jobs.db < scripts/ddl/jobs-database.sql
```

## Configuration

The application uses a YAML configuration file. By default, it looks for `config/config-dev.yaml`.

Key configuration options:
- Database: SQLite (default) or PostgreSQL
- Application name and settings

## Running the Application

### Local Development

```bash
python -m uvicorn sample_python_rest.main:app --host 0.0.0.0 --port 8081
```

### Using Docker

```bash
docker build -t sample-python-rest .
docker run -p 8081:8081 sample-python-rest
```

## API Endpoints

### Root
- `GET /v1` - API information

### Jobs
- `GET /v1/jobs/{job_group_id}` - Retrieve all jobs for a specific job group
- `POST /v1/jobs/{job_group_id}` - Create a new job in a job group

Request body for POST:
```json
{
  "type": "string",
  "description": "string"
}
```

### Health Check
- `GET /health` - Application health status

### Monitoring
- `GET /prometheus` - Prometheus metrics endpoint

## API Documentation

When running, visit `http://localhost:8081/docs` for interactive API documentation powered by Swagger UI.

## Monitoring

The application exposes Prometheus metrics at `/prometheus`. Configure your Prometheus server to scrape this endpoint for monitoring API performance and health.

## Deployment

### Docker

Use the provided Dockerfile to build and run the application in a container.

### Kubernetes

Kubernetes deployment manifests are available in the `k8s/` directory.

## Development

### Project Structure

```
sample-python-rest/
├── sample_python_rest/
│   ├── main.py              # FastAPI application
│   ├── config/              # Configuration management
│   ├── datastore/           # Database layer
│   ├── handlers/            # Business logic
│   └── model/               # Data models
├── config/                  # Configuration files
├── resources/               # Static resources
├── scripts/                 # Database scripts
├── k8s/                     # Kubernetes manifests
├── Dockerfile               # Docker configuration
└── requirements.txt         # Python dependencies
```

### Adding New Features

1. Define data models in `sample_python_rest/model/`
2. Implement business logic in `sample_python_rest/handlers/`
3. Add API endpoints in `sample_python_rest/main.py`
4. Update database schema in `scripts/ddl/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
