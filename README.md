# eks-ai-platform

EKS AI Platform Decision Engine - A FastAPI-based service for infrastructure decision management.

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=infra_platform --cov-report=term-missing
```

Generate HTML coverage report:
```bash
pytest --cov=infra_platform --cov-report=html
```

View the HTML coverage report by opening `htmlcov/index.html` in a browser.

## Running the API

```bash
uvicorn infra_platform.api.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `GET /decision/{profile_name}` - Get decision for a specific profile

Available profiles:
- `dev-public`
- `dev-internal`
- `prod-public-critical`
- `prod-internal-critical`
