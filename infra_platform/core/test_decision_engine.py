"""
Tests for the Decision Engine module.

This module contains unit tests for the decision engine functionality,
including profile retrieval and error handling.
"""

import pytest
from infra_platform.core.decision_engine import (
    get_decision,
    get_available_profiles,
    DECISION_CONTRACT,
)


class TestGetDecision:
    """Test cases for the get_decision function."""

    def test_dev_public_profile(self):
        """Test that dev-public profile returns correct configuration."""
        decision = get_decision("dev-public")
        assert decision["compute_profile"] == "cheap"
        assert decision["network_profile"] == "public"
        assert decision["autoscaling_profile"] == "limited"
        assert decision["security_profile"] == "strict"
        assert decision["availability_profile"] == "single_az"

    def test_dev_internal_profile(self):
        """Test that dev-internal profile returns correct configuration."""
        decision = get_decision("dev-internal")
        assert decision["compute_profile"] == "cheap"
        assert decision["network_profile"] == "private"
        assert decision["autoscaling_profile"] == "limited"
        assert decision["security_profile"] == "normal"
        assert decision["availability_profile"] == "single_az"

    def test_prod_public_critical_profile(self):
        """Test that prod-public-critical profile returns correct configuration."""
        decision = get_decision("prod-public-critical")
        assert decision["compute_profile"] == "stable"
        assert decision["network_profile"] == "public"
        assert decision["autoscaling_profile"] == "full"
        assert decision["security_profile"] == "strict"
        assert decision["availability_profile"] == "multi_az"

    def test_prod_internal_critical_profile(self):
        """Test that prod-internal-critical profile returns correct configuration."""
        decision = get_decision("prod-internal-critical")
        assert decision["compute_profile"] == "stable"
        assert decision["network_profile"] == "private"
        assert decision["autoscaling_profile"] == "full"
        assert decision["security_profile"] == "strict"
        assert decision["availability_profile"] == "multi_az"

    def test_invalid_profile_raises_value_error(self):
        """Test that requesting an unknown profile raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            get_decision("unknown-profile")
        assert "Unknown profile: 'unknown-profile'" in str(exc_info.value)
        assert "Available profiles:" in str(exc_info.value)

    def test_empty_profile_name_raises_value_error(self):
        """Test that empty profile name raises ValueError."""
        with pytest.raises(ValueError):
            get_decision("")

    def test_all_profiles_have_required_keys(self):
        """Test that all profiles have the required configuration keys."""
        required_keys = {
            "compute_profile",
            "network_profile",
            "autoscaling_profile",
            "security_profile",
            "availability_profile",
        }

        for profile_name, decision in DECISION_CONTRACT.items():
            assert set(decision.keys()) == required_keys, (
                f"Profile '{profile_name}' missing required keys"
            )


class TestGetAvailableProfiles:
    """Test cases for the get_available_profiles function."""

    def test_returns_all_profiles(self):
        """Test that get_available_profiles returns all defined profiles."""
        profiles = get_available_profiles()
        expected_profiles = sorted(DECISION_CONTRACT.keys())
        assert profiles == expected_profiles

    def test_returns_sorted_list(self):
        """Test that profiles are returned in sorted order."""
        profiles = get_available_profiles()
        assert profiles == sorted(profiles)

    def test_contains_expected_profiles(self):
        """Test that the expected profiles are present."""
        profiles = get_available_profiles()
        assert "dev-public" in profiles
        assert "dev-internal" in profiles
        assert "prod-public-critical" in profiles
        assert "prod-internal-critical" in profiles


if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])

