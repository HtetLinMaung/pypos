from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
from ..utils.bcrypt import hash_passwod


def get_user_by_user_id(db: Session,  user_id: str):
    return db.query(User).filter(User.user_id == user_id and User.deleted_at != None).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(userid=user.user_id, password=hash_passwod(
        user.password), name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
