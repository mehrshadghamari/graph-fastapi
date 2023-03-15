import graphene


class UserType(graphene.ObjectType):
    id=graphene.Int()
    name=graphene.String()
    email=graphene.String()
    password=graphene.String()



class UserInput(graphene.ObjectType):
    name=graphene.String()
    email=graphene.String()
    password=graphene.String()
    


class Response(graphene.ObjectType):
    ok = graphene.Boolean()
    status_code = graphene.Int()
    message = graphene.String()