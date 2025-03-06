import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer

from config import SUPABASE_JWT_SECRET

security = HTTPBearer()

def verify_supabase_token(token: str):
    try:   
        decoded_token = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        
        user_uuid = decoded_token.get("sub")
        if not user_uuid:
            raise HTTPException(status_code=401, detail="User not found")
        
        return decoded_token
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception:
        raise HTTPException(status_code=500, detail="Error verifying user")

def get_current_user(auth = Security(security)):
    token = auth.credentials
    return verify_supabase_token(token)