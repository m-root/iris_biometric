from typing import List, Optional
from pydantic import BaseModel


class Registration(BaseModel):
    redirect_uris: List[str]
    client_name: Optional[str] = None
    logo_url: Optional[str] = None
    application_type: Optional[str] = "web"
    grant_types: Optional[List[str]] = ["authorization_code"]
    response_type: Optional[List[str]] = ["id_token"]


class ActionCreate(BaseModel):
    external_nullifier: str
    name: str
    action: str
    description: str
    max_verifications: int
    max_accounts_per_user: int


class AppCreate(BaseModel):
    id: str
    is_staging: bool
    is_verified: bool
    logo_url: str
    name: str
    verified_app_logo: str
    engine: str
    sign_in_with_world_id: bool
    can_user_verify: str
    action: ActionCreate


class SignupRequest(BaseModel):
    identity_commitment: str
