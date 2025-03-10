import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer

from app.supabase import supabase_client, SUPABASE_JWT_SECRET

security = HTTPBearer()

def verify_supabase_user(token: str):
    try:   
        decoded_token = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        
        user_uuid = decoded_token.get("sub")
        if not user_uuid:
            raise HTTPException(status_code=401, detail="Invalid token: missing user ID")

        # Verify if the user exists in the database
        try:
            response = supabase_client.auth.get_user(token)
            if user_uuid != response.user.id:
                raise HTTPException(status_code=401, detail="Token user ID mismatch")
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid user token")
        
        return response.user
           
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception:
        raise HTTPException(status_code=500, detail="Error verifying user")

def get_current_user(auth = Security(security)):
    token = auth.credentials
    return verify_supabase_user(token)