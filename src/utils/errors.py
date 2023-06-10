from fastapi import HTTPException


def default_exception_error(err):
    """Default error checking for any raised errors else returns error 500 with the respective error message"""
    error_code = (
        err.__dict__.get("status_code") if err.__dict__.get("status_code") else 500
    )
    error_message = (
        err.__dict__.get("detail") if err.__dict__.get("detail") else str(err)
    )
    header = (
        err.__dict__.get("headers")
        if err.__dict__.get("headers")
        else {"WWW-Authenticate": "Bearer"}
    )

    raise HTTPException(error_code, detail=str(error_message), headers=header)
