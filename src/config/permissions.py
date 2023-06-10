# decorator fuction to check permision
from fastapi import HTTPException,status
from schemas.schemas import AuthRes
from utils.roles import is_admin,is_landlord,is_property_manager



def authorize(user:AuthRes,roles:list | None = None)-> AuthRes:
    if not roles:
        pass

    if "admin" in roles:
        if not is_admin(user):
            if "property_manager" in roles:
                if not is_property_manager(user):
                    if "landlord" in roles:
                        if not is_landlord(user):
                            raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="Unauthorised access ",
                            )
    elif "landlord" in roles:
        print(2)
        if not is_landlord(user):
            if "property_manager" in roles:
                if not is_property_manager(user):
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Unauthorised access ",
                        )
    elif "property_manager" in roles:
            print(3)
            if not is_property_manager(user):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Unauthorised access ",
                    )


