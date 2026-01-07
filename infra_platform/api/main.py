from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from infra_platform.core.decision_engine import DECISION_CONTRACT, get_decision
from infra_platform.core.logging_config import logger


class DecisionResponse(BaseModel):
    """Response model for decision endpoint."""

    compute_profile: str = Field(..., description="Compute resources configuration")
    network_profile: str = Field(..., description="Network configuration (public/private)")
    autoscaling_profile: str = Field(..., description="Autoscaling behavior")
    security_profile: str = Field(..., description="Security settings level")
    availability_profile: str = Field(..., description="Availability zone configuration")


class ProfileDecisionResponse(BaseModel):
    """Complete response with profile name and decision."""

    profile: str = Field(..., description="Profile name requested")
    decision: DecisionResponse


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    version: str = "0.1.0"


class ProfileListResponse(BaseModel):
    """Response listing all available profiles."""

    profiles: list[str]
    total: int


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    logger.info("EKS Decision Engine API starting up")
    yield
    # Shutdown
    logger.info("EKS Decision Engine API shutting down")


app = FastAPI(
    title="EKS Decision Engine API",
    description="AI-driven decision engine for Amazon EKS infrastructure configuration",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


@app.get("/", response_model=HealthResponse, tags=["Health"])
def health_check():
    """
    Health check endpoint.

    Returns the API status and version information.
    """
    return HealthResponse(status="healthy")


@app.get("/profiles", response_model=ProfileListResponse, tags=["Profiles"])
def list_profiles():
    """
    List all available infrastructure profiles.

    Returns a list of all supported profile names that can be used
    with the decision endpoint.
    """
    profiles = list(DECISION_CONTRACT.keys())
    logger.info(f"Listed {len(profiles)} available profiles")
    return ProfileListResponse(profiles=profiles, total=len(profiles))


@app.get(
    "/decision/{profile_name}",
    response_model=ProfileDecisionResponse,
    tags=["Decisions"],
    responses={
        200: {
            "description": "Successful decision retrieval",
            "content": {
                "application/json": {
                    "example": {
                        "profile": "dev-public",
                        "decision": {
                            "compute_profile": "cheap",
                            "network_profile": "public",
                            "autoscaling_profile": "limited",
                            "security_profile": "strict",
                            "availability_profile": "single_az",
                        },
                    }
                }
            },
        },
        404: {"description": "Profile not found"},
    },
)
def get_decision_by_profile(profile_name: str):
    """
    Get infrastructure decision for a specific profile.

    Retrieves the recommended infrastructure configuration based on the
    specified profile name.

    Args:
        profile_name: Name of the infrastructure profile (e.g., 'dev-public')

    Returns:
        ProfileDecisionResponse containing the profile name and decision details

    Raises:
        HTTPException: 404 error if the profile name is not found
    """
    try:
        logger.info(f"Fetching decision for profile: {profile_name}")
        decision_data = get_decision(profile_name)
        logger.info(f"Successfully retrieved decision for profile: {profile_name}")
        return ProfileDecisionResponse(
            profile=profile_name, decision=DecisionResponse(**decision_data)
        )
    except ValueError as e:
        logger.warning(f"Profile not found: {profile_name}")
        raise HTTPException(status_code=404, detail=str(e))
