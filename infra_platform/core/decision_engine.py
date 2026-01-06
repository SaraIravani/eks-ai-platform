# platform/core/decision_engine.py

DECISION_CONTRACT = {
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


def get_decision(profile_name: str) -> dict:
    """
    Returns the decision contract for a given profile.
    """
    if profile_name not in DECISION_CONTRACT:
        raise ValueError(f"Unknown profile: {profile_name}")

    return DECISION_CONTRACT[profile_name]


