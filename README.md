# EKS AI Platform

A FastAPI-based decision engine for managing Amazon EKS infrastructure profiles with AI-driven recommendations.

## Overview

The EKS AI Platform provides an intelligent decision engine that helps teams select the right infrastructure configuration based on their workload requirements. It uses predefined profiles to recommend optimal settings for compute, networking, autoscaling, security, and availability.

## Features

- 🚀 **FastAPI-based REST API** - Fast, modern, and async-ready
- 🧠 **Decision Engine** - Smart profile-based infrastructure recommendations
- 🔒 **Security Profiles** - Built-in security best practices
- 📈 **Autoscaling Configurations** - Flexible scaling options
- 🌐 **Network Profiles** - Public and private networking options
- 🏗️ **Multi-AZ Support** - High availability configurations

## Architecture

```
eks-ai-platform/
├── infra_platform/
│   ├── api/
│   │   └── main.py          # FastAPI application
│   └── core/
│       ├── decision_engine.py     # Decision logic
│       └── test_decision_engine.py # Unit tests
```

## Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SaraIravani/eks-ai-platform.git
cd eks-ai-platform
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the development server:
```bash
uvicorn infra_platform.api.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available Profiles

### Development Profiles

- **dev-public**: Public development environment with cost optimization
- **dev-internal**: Private development environment with normal security

### Production Profiles

- **prod-public-critical**: Public production with full autoscaling and multi-AZ
- **prod-internal-critical**: Private production with strict security and multi-AZ

## API Usage

### Get Decision by Profile

```bash
curl http://localhost:8000/decision/dev-public
```

Response:
```json
{
  "profile": "dev-public",
  "decision": {
    "compute_profile": "cheap",
    "network_profile": "public",
    "autoscaling_profile": "limited",
    "security_profile": "strict",
    "availability_profile": "single_az"
  }
}
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=infra_platform --cov-report=html

# Run specific test file
python infra_platform/core/test_decision_engine.py
```

### Code Quality

```bash
# Format code
black infra_platform/

# Lint code
flake8 infra_platform/

# Type checking
mypy infra_platform/
```

## Docker Support

Build and run with Docker:

```bash
# Build image
docker build -t eks-ai-platform .

# Run container
docker run -p 8000:8000 eks-ai-platform
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.