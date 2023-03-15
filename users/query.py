import graphene
from .. import database,models
from user_types import UserType



class UserQuery(graphene.ObjectType):
    users=graphene.List(UserType)
    user=graphene.Field(UserType,id=graphene.ID())


    def resolve_users(self, info):
        db = database.SessionLocal()
        users=db.query(models.User).all()
        db.close()
        return users


    def resolve_user(self, info, id):
        db = database.SessionLocal()
        user=db.query(models.User).filter(models.User.id==id).first()
        return user