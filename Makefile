.PHONY: help install dev-install test lint format clean run docker-build docker-run

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt

dev-install:  ## Install development dependencies
	pip install -r requirements.txt

test:  ## Run all tests
	pytest infra_platform/ -v --cov=infra_platform --cov-report=html --cov-report=term

test-fast:  ## Run tests without coverage
	pytest infra_platform/ -v

lint:  ## Run all linting checks
	@echo "Running Black..."
	black --check infra_platform/
	@echo "Running isort..."
	isort --check-only infra_platform/
	@echo "Running flake8..."
	flake8 infra_platform/
	@echo "Running mypy..."
	mypy infra_platform/ --ignore-missing-imports

format:  ## Format code with black and isort
	black infra_platform/
	isort infra_platform/

clean:  ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov/ dist/ build/ *.egg-info

run:  ## Run the development server
	uvicorn infra_platform.api.main:app --reload --host 0.0.0.0 --port 8000

docker-build:  ## Build Docker image
	docker build -t eks-ai-platform:latest .

docker-run:  ## Run Docker container
	docker run -p 8000:8000 eks-ai-platform:latest

docker-test:  ## Build and test Docker image
	docker build -t eks-ai-platform:test .
	docker run -d -p 8000:8000 --name test-container eks-ai-platform:test
	sleep 5
	curl -f http://localhost:8000/decision/dev-public || (docker stop test-container && docker rm test-container && exit 1)
	docker stop test-container
	docker rm test-container
	@echo "Docker test passed!"
