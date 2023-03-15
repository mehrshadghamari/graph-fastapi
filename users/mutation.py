import graphene
from .. import database,models
from user_types import UserInput,Response
from passlib.context import CryptContext



pwd_cxt=CryptContext(schemes=['bcrypt'],deprecated='auto')

class CreateUser(graphene.Mutation):
    class Arguments:
        input=UserInput()

    OutPut=Response

    def mutate(root,info,input):
        db = database.SessionLocal()
        hashed_passwrod=pwd_cxt.hash(input.password)
        new_user=models.User(name=input.name,email=input.email,password=hashed_passwrod)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()
        return Response(
            ok=True,
            status_code=201,
            message="created",
        )
