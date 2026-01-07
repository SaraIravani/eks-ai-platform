# infra_platform/core/decision_engine.py
"""
Decision Engine Module

This module contains the core decision logic for EKS infrastructure configuration.
It provides profile-based recommendations for compute, networking, autoscaling,
security, and availability settings.
"""

from typing import Dict, TypedDict


class DecisionContract(TypedDict):
    """Type definition for a decision contract."""

    compute_profile: str
    network_profile: str
    autoscaling_profile: str
    security_profile: str
    availability_profile: str


# Decision contract mapping for different infrastructure profiles
DECISION_CONTRACT: Dict[str, DecisionContract] = {
    "dev-public": {
        "compute_profile": "cheap",
        "network_profile": "public",
        "autoscaling_profile": "limited",
        "security_profile": "strict",
        "availability_profile": "single_az",
    },
    "dev-internal": {
        "compute_profile": "cheap",
        "network_profile": "private",
        "autoscaling_profile": "limited",
        "security_profile": "normal",
        "availability_profile": "single_az",
    },
    "prod-public-critical": {
        "compute_profile": "stable",
        "network_profile": "public",
        "autoscaling_profile": "full",
        "security_profile": "strict",
        "availability_profile": "multi_az",
    },
    "prod-internal-critical": {
        "compute_profile": "stable",
        "network_profile": "private",
        "autoscaling_profile": "full",
        "security_profile": "strict",
        "availability_profile": "multi_az",
    },
}


def get_decision(profile_name: str) -> DecisionContract:
    """
    Returns the decision contract for a given profile.

    This function retrieves the recommended infrastructure configuration
    based on the specified profile name. Each profile defines specific
    settings for compute resources, networking, autoscaling behavior,
    security level, and availability zones.

    Args:
        profile_name: The name of the infrastructure profile. Must be one of:
            - 'dev-public': Public development environment
            - 'dev-internal': Private development environment
            - 'prod-public-critical': Public production with high availability
            - 'prod-internal-critical': Private production with high availability

    Returns:
        A dictionary containing the decision contract with keys:
            - compute_profile: Compute resource configuration
            - network_profile: Network accessibility configuration
            - autoscaling_profile: Autoscaling behavior settings
            - security_profile: Security level settings
            - availability_profile: Availability zone configuration

    Raises:
        ValueError: If the provided profile_name is not found in DECISION_CONTRACT

    Examples:
        >>> get_decision("dev-public")
        {
            'compute_profile': 'cheap',
            'network_profile': 'public',
            'autoscaling_profile': 'limited',
            'security_profile': 'strict',
            'availability_profile': 'single_az'
        }
    """
    if profile_name not in DECISION_CONTRACT:
        available_profiles = ", ".join(sorted(DECISION_CONTRACT.keys()))
        raise ValueError(
            f"Unknown profile: '{profile_name}'. " f"Available profiles: {available_profiles}"
        )

    return DECISION_CONTRACT[profile_name]


def get_available_profiles() -> list[str]:
    """
    Returns a list of all available profile names.

    Returns:
        A sorted list of profile names that can be used with get_decision()

    Examples:
        >>> get_available_profiles()
        ['dev-internal', 'dev-public', 'prod-internal-critical', 'prod-public-critical']
    """
    return sorted(DECISION_CONTRACT.keys())
