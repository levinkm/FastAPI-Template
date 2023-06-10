from pydantic import BaseModel

class AuthRes(BaseModel):
    """This is the response schema model for the authentication"""

    user_id: str
    email: str
    is_admin: bool
    is_propertymanager: bool
    is_tenant: bool
    is_landlord: bool
