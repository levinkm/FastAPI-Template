from fastapi import HTTPException, Request, status

import requests
from jose import jwt
from jose.exceptions import ExpiredSignatureError,JWTError
from config.settings import SERVICE_ROUTES,SECRET_KEY
from utils.errors import default_exception_error

# AUTH_ROUTE = env.get("AUTH_ROUTE ")

AUTH_ROUTE = f"{SERVICE_ROUTES['auth_service']}/current-user"


async def authenticate_user(request: Request):
    """used to check if the user has been authorised to access the endpoimt returning uthorisation details if successful
    else raising an exception
    Args:
        authorization: the authorization header
    Returns:
        the user details if successful
    Raises:
        HTTPException: if the user is not authorised
    """
    auth = request.headers.get("authorization")

    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authorization header provided",
        )
    else:
        response = requests.get(AUTH_ROUTE, headers={"Authorization": auth})
        if response.status_code == status.HTTP_200_OK:
            return response.json()

        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.json()["messages"][0]
            )


# snippet to decode JWT tokenaccess token
async def authorize_user(request: Request):
    """used to decode the jwt token
    Args:
        request: authorization token
    Returns:
        user object
    """
    auth = request.headers.get("authorization")
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authorization header provided",
        )

    else:
        token = auth.split(" ")[1]
        try:
            params = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            user = params.copy()
            del user["exp"], user["token_type"], user["jti"]
            return user
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token verification failed",
            )
        except Exception as err:
            default_exception_error(err)


