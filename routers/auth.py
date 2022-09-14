from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from schemas.user import UserCreate, UserLogin
from dao.user import get_user_by_user_id, create_user
from dependencies import get_db
from utils import bcrypt, jwt

router = APIRouter()


@router.post("/signup", tags=['auth'])
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_user_id(db=db, user_id=user.user_id)
    if (db_user):
        raise HTTPException(status_code=400, detail="User already existed!")

    db_user = create_user(db=db, user=user)

    return {
        "code": 200,
        "message": "Signup successful.",
        "data": db_user
    }


@router.post("/signin", tags=['auth'])
async def signin(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_user_id(db=db, user_id=user.user_id)
    if (db_user == None):
        raise HTTPException(status_code=404, detail="User not found!")

    if bcrypt.verify_password(user.password, db_user.password) == False:
        raise HTTPException(status_code=401, detail="Password is incorrect!")

    token = jwt.create_access_token({"sub": user.user_id})
    return {
        "code": 200,
        "message": "Login successful!",
        "data": {
            "token": token,
            "user_name": db_user.name,
            "profile_image": db_user.profile_image
        }
    }
