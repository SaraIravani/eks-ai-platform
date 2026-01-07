"""
API integration tests for the EKS Decision Engine.

This module contains tests for the FastAPI endpoints.
"""

import pytest
from fastapi.testclient import TestClient

from infra_platform.api.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Test cases for the health check endpoint."""

    def test_health_check_returns_200(self):
        """Test that health check endpoint returns 200 status."""
        response = client.get("/")
        assert response.status_code == 200

    def test_health_check_response_structure(self):
        """Test that health check returns correct response structure."""
        response = client.get("/")
        data = response.json()
        assert "status" in data
        assert "version" in data
        assert data["status"] == "healthy"
        assert data["version"] == "0.1.0"


class TestProfilesEndpoint:
    """Test cases for the profiles listing endpoint."""

    def test_list_profiles_returns_200(self):
        """Test that profiles endpoint returns 200 status."""
        response = client.get("/profiles")
        assert response.status_code == 200

    def test_list_profiles_response_structure(self):
        """Test that profiles endpoint returns correct structure."""
        response = client.get("/profiles")
        data = response.json()
        assert "profiles" in data
        assert "total" in data
        assert isinstance(data["profiles"], list)
        assert isinstance(data["total"], int)

    def test_list_profiles_contains_expected_profiles(self):
        """Test that all expected profiles are returned."""
        response = client.get("/profiles")
        data = response.json()
        profiles = data["profiles"]

        expected_profiles = [
            "dev-public",
            "dev-internal",
            "prod-public-critical",
            "prod-internal-critical",
        ]

        for profile in expected_profiles:
            assert profile in profiles

    def test_list_profiles_total_matches_count(self):
        """Test that total field matches the number of profiles."""
        response = client.get("/profiles")
        data = response.json()
        assert data["total"] == len(data["profiles"])


class TestDecisionEndpoint:
    """Test cases for the decision endpoint."""

    def test_decision_dev_public_returns_200(self):
        """Test that decision endpoint returns 200 for valid profile."""
        response = client.get("/decision/dev-public")
        assert response.status_code == 200

    def test_decision_response_structure(self):
        """Test that decision endpoint returns correct structure."""
        response = client.get("/decision/dev-public")
        data = response.json()

        assert "profile" in data
        assert "decision" in data

        decision = data["decision"]
        assert "compute_profile" in decision
        assert "network_profile" in decision
        assert "autoscaling_profile" in decision
        assert "security_profile" in decision
        assert "availability_profile" in decision

    def test_decision_dev_public_values(self):
        """Test that dev-public profile returns expected values."""
        response = client.get("/decision/dev-public")
        data = response.json()

        assert data["profile"] == "dev-public"
        decision = data["decision"]
        assert decision["compute_profile"] == "cheap"
        assert decision["network_profile"] == "public"
        assert decision["autoscaling_profile"] == "limited"
        assert decision["security_profile"] == "strict"
        assert decision["availability_profile"] == "single_az"

    def test_decision_dev_internal_values(self):
        """Test that dev-internal profile returns expected values."""
        response = client.get("/decision/dev-internal")
        data = response.json()

        assert data["profile"] == "dev-internal"
        decision = data["decision"]
        assert decision["compute_profile"] == "cheap"
        assert decision["network_profile"] == "private"
        assert decision["security_profile"] == "normal"

    def test_decision_prod_public_critical_values(self):
        """Test that prod-public-critical profile returns expected values."""
        response = client.get("/decision/prod-public-critical")
        data = response.json()

        assert data["profile"] == "prod-public-critical"
        decision = data["decision"]
        assert decision["compute_profile"] == "stable"
        assert decision["network_profile"] == "public"
        assert decision["autoscaling_profile"] == "full"
        assert decision["security_profile"] == "strict"
        assert decision["availability_profile"] == "multi_az"

    def test_decision_invalid_profile_returns_404(self):
        """Test that invalid profile returns 404 status."""
        response = client.get("/decision/invalid-profile")
        assert response.status_code == 404

    def test_decision_invalid_profile_error_message(self):
        """Test that invalid profile returns helpful error message."""
        response = client.get("/decision/invalid-profile")
        data = response.json()
        assert "detail" in data
        assert "Unknown profile" in data["detail"]
        assert "Available profiles" in data["detail"]


class TestAPIDocumentation:
    """Test cases for API documentation endpoints."""

    def test_openapi_schema_accessible(self):
        """Test that OpenAPI schema is accessible."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert data["info"]["title"] == "EKS Decision Engine API"

    def test_swagger_ui_accessible(self):
        """Test that Swagger UI is accessible."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_redoc_accessible(self):
        """Test that ReDoc is accessible."""
        response = client.get("/redoc")
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
