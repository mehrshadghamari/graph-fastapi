# from .types import BlogInput,Response
import database
import graphene
import models


class BlogInput(graphene.InputObjectType):
    title = graphene.String()
    body = graphene.String()


class Response(graphene.ObjectType):
    ok = graphene.Boolean()
    status_code = graphene.Int()
    message = graphene.String()


class CreateBlog(graphene.Mutation):
    class Arguments:
        input = BlogInput()

    Output = Response

    @staticmethod
    def mutate(root, info, input):
        db = database.SessionLocal()
        blog_instance = models.Blog(title=input.title, body=input.body)
        db.add(blog_instance)
        db.commit()
        db.refresh(blog_instance)
        db.close()
        return Response(
            ok=True,
            status_code=201,
            message="created",
        )
