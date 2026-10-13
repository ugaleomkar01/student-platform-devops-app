# Student Platform DevOps App

A Flask-based student and academic records platform with a web dashboard for browsing student profiles, courses, and marks. The application serves HTML pages and JSON responses, and includes a health endpoint for deployment checks.

## Features

- Dashboard with student, course, and marks summaries
- Student directory and individual student records
- Course catalog and student marks views
- JSON responses for the application data endpoints
- Health check at `/health`

## Technology

- Python and Flask
- Pytest
- Docker
- Jenkins pipeline for dependency installation, tests, and image builds
- Kubernetes Deployment and NodePort Service manifests

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000> in a browser. Run the test suite with:

```powershell
pytest
```

## Run with Docker

```powershell
docker build -t student-platform:v1.0.0 .
docker run --rm -p 5000:5000 student-platform:v1.0.0
```

The Kubernetes manifests are in the `k8s/` directory. The Service uses NodePort `30080`.
