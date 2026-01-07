from infra_platform.core.decision_engine import get_decision


def test_dev_public():
    decision = get_decision("dev-public")
    expected = {
        "compute_profile": "cheap",
        "network_profile": "public",
        "autoscaling_profile": "limited",
        "security_profile": "strict",
        "availability_profile": "single_az",
    }
    assert decision == expected


def test_dev_internal():
    decision = get_decision("dev-internal")
    expected = {
        "compute_profile": "cheap",
        "network_profile": "private",
        "autoscaling_profile": "limited",
        "security_profile": "normal",
        "availability_profile": "single_az",
    }
    assert decision == expected


def test_prod_public_critical():
    decision = get_decision("prod-public-critical")
    expected = {
        "compute_profile": "stable",
        "network_profile": "public",
        "autoscaling_profile": "full",
        "security_profile": "strict",
        "availability_profile": "multi_az",
    }
    assert decision == expected


def test_prod_internal_critical():
    decision = get_decision("prod-internal-critical")
    expected = {
        "compute_profile": "stable",
        "network_profile": "private",
        "autoscaling_profile": "full",
        "security_profile": "strict",
        "availability_profile": "multi_az",
    }
    assert decision == expected


def test_invalid_profile():
    try:
        get_decision("unknown-profile")
        assert False, "Expected ValueError for unknown profile"
    except ValueError as e:
        assert "Unknown profile" in str(e)


def test_decision_immutability():
    """Test that modifying returned decision doesn't affect the original data."""
    decision1 = get_decision("dev-public")
    original_compute = decision1["compute_profile"]
    
    # Modify the returned decision
    decision1["compute_profile"] = "modified"
    
    # Get the same profile again
    decision2 = get_decision("dev-public")
    
    # Verify the original data is unchanged
    assert decision2["compute_profile"] == original_compute
    assert decision2["compute_profile"] != "modified"


if __name__ == "__main__":
    test_dev_public()
    test_dev_internal()
    test_prod_public_critical()
    test_prod_internal_critical()
    test_invalid_profile()
    test_decision_immutability()
    print("✅ All decision engine tests passed")

