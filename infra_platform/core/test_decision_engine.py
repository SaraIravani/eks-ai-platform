from infra_platform.core.decision_engine import get_decision


def test_dev_public():
    decision = get_decision("dev-public")
    assert decision["compute_profile"] == "cheap"
    assert decision["network_profile"] == "public"
    assert decision["autoscaling_profile"] == "limited"
    assert decision["security_profile"] == "strict"
    assert decision["availability_profile"] == "single_az"


def test_dev_internal():
    decision = get_decision("dev-internal")
    assert decision["compute_profile"] == "cheap"
    assert decision["network_profile"] == "private"
    assert decision["autoscaling_profile"] == "limited"
    assert decision["security_profile"] == "normal"
    assert decision["availability_profile"] == "single_az"


def test_prod_public_critical():
    decision = get_decision("prod-public-critical")
    assert decision["compute_profile"] == "stable"
    assert decision["network_profile"] == "public"
    assert decision["autoscaling_profile"] == "full"
    assert decision["security_profile"] == "strict"
    assert decision["availability_profile"] == "multi_az"


def test_prod_internal_critical():
    decision = get_decision("prod-internal-critical")
    assert decision["compute_profile"] == "stable"
    assert decision["network_profile"] == "private"
    assert decision["autoscaling_profile"] == "full"
    assert decision["security_profile"] == "strict"
    assert decision["availability_profile"] == "multi_az"


def test_invalid_profile():
    try:
        get_decision("unknown-profile")
        assert False, "Expected ValueError for unknown profile"
    except ValueError:
        assert True


if __name__ == "__main__":
    test_dev_public()
    test_dev_internal()
    test_prod_public_critical()
    test_prod_internal_critical()
    test_invalid_profile()
    print("✅ All decision engine tests passed")

