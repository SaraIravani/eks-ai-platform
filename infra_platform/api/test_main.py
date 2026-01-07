from fastapi.testclient import TestClient
from infra_platform.api.main import app

client = TestClient(app)


def test_get_decision_dev_public():
    """Test getting decision for dev-public profile"""
    response = client.get("/decision/dev-public")
    assert response.status_code == 200
    data = response.json()
    assert data["profile"] == "dev-public"
    assert data["decision"]["compute_profile"] == "cheap"
    assert data["decision"]["network_profile"] == "public"


def test_get_decision_dev_internal():
    """Test getting decision for dev-internal profile"""
    response = client.get("/decision/dev-internal")
    assert response.status_code == 200
    data = response.json()
    assert data["profile"] == "dev-internal"
    assert data["decision"]["compute_profile"] == "cheap"
    assert data["decision"]["network_profile"] == "private"


def test_get_decision_prod_public_critical():
    """Test getting decision for prod-public-critical profile"""
    response = client.get("/decision/prod-public-critical")
    assert response.status_code == 200
    data = response.json()
    assert data["profile"] == "prod-public-critical"
    assert data["decision"]["compute_profile"] == "stable"
    assert data["decision"]["autoscaling_profile"] == "full"
    assert data["decision"]["availability_profile"] == "multi_az"


def test_get_decision_prod_internal_critical():
    """Test getting decision for prod-internal-critical profile"""
    response = client.get("/decision/prod-internal-critical")
    assert response.status_code == 200
    data = response.json()
    assert data["profile"] == "prod-internal-critical"
    assert data["decision"]["compute_profile"] == "stable"
    assert data["decision"]["network_profile"] == "private"


def test_get_decision_invalid_profile():
    """Test getting decision for invalid profile returns 404"""
    response = client.get("/decision/invalid-profile")
    assert response.status_code == 404
    data = response.json()
    assert "Unknown profile" in data["detail"]
