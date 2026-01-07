# Contributing to EKS AI Platform

Thank you for your interest in contributing to the EKS AI Platform! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:
- A clear description of the feature
- The problem it solves
- Possible implementation approaches
- Any alternatives you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Make your changes** following our coding standards:
   - Write clear, self-documenting code
   - Add docstrings to functions and classes
   - Follow PEP 8 style guide
   - Use type hints where appropriate

4. **Test your changes**:
   ```bash
   # Run tests
   pytest
   
   # Check code formatting
   black infra_platform/
   
   # Check import sorting
   isort infra_platform/
   
   # Run linter
   flake8 infra_platform/
   
   # Run type checker
   mypy infra_platform/
   ```

5. **Commit your changes** with a clear commit message:
   ```bash
   git commit -m "feat: add new decision profile for staging"
   ```

   Use conventional commit format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `test:` for test additions or changes
   - `refactor:` for code refactoring
   - `chore:` for maintenance tasks

6. **Push to your fork** and submit a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **In your pull request**:
   - Describe what changed and why
   - Reference any related issues
   - Include screenshots for UI changes
   - Ensure all CI checks pass

## Development Setup

### Prerequisites

- Python 3.12+
- pip
- git

### Setup Steps

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/eks-ai-platform.git
   cd eks-ai-platform
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   uvicorn infra_platform.api.main:app --reload
   ```

## Coding Standards

### Python Style Guide

- Follow PEP 8
- Use 100 characters max line length
- Use type hints for function parameters and return values
- Write docstrings for all public modules, functions, classes, and methods

### Example

```python
def get_decision(profile_name: str) -> dict:
    """
    Returns the decision contract for a given profile.
    
    Args:
        profile_name: The name of the infrastructure profile
        
    Returns:
        A dictionary containing the decision contract
        
    Raises:
        ValueError: If the profile name is unknown
    """
    if profile_name not in DECISION_CONTRACT:
        raise ValueError(f"Unknown profile: {profile_name}")
    
    return DECISION_CONTRACT[profile_name]
```

### Testing Guidelines

- Write tests for all new features
- Maintain or improve test coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

### Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Update API documentation as needed
- Include code examples where helpful

## Project Structure

```
eks-ai-platform/
├── .github/
│   └── workflows/         # CI/CD workflows
├── infra_platform/
│   ├── api/              # FastAPI application
│   └── core/             # Core business logic
├── .dockerignore
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── Dockerfile
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Questions?

If you have questions, feel free to:
- Open an issue for discussion
- Reach out to maintainers
- Check existing issues and PRs

Thank you for contributing! 🎉
