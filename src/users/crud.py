from sqlalchemy.orm import Session
from users import models, schemas

import uuid
from typing import Optional

def create_user(db: Session, user: schemas.CreateUser) -> Optional[models.usersT]:
    accessToken = str(uuid.uuid4())[:8]
    db.user = models.usersT(login=user.login, password=user.password, accessToken=accessToken)
    db.add(db.user)
    db.commit()
    db.refresh(db.user)
    return db.user

def find_user(db: Session, login: str) -> Optional[models.usersT]:
    user = db.query(models.usersT).filter_by(login=login).first()
    return user

def check_password(db: Session, login: str, password: str) -> Optional[models.usersT]:
    user = db.query(models.usersT).filter_by(login=login).first()

    if password == user.password:
        return user
    else:
        return None

def check_token(db: Session, login: str, accessToken: str) -> Optional[models.usersT]:
    user = db.query(models.usersT).filter_by(login=login).first()

    if accessToken == user.accessToken:
        return user
    else:
        return None

def create_task(db: Session, task: schemas.CreateTask) -> Optional[models.usersT]:
    db.task = models.tasksT(user_token=task.accessToken, colar_id=task.colar_id, text=task.text)
    db.add(db.task)
    db.commit()
    db.refresh(db.task)
    return db.task
