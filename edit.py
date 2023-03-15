import graphene

# from .types import BlogInput
import database,models




class BlogInput(graphene.InputObjectType):
    title=graphene.String()
    body=graphene.String()




class Response(graphene.ObjectType):
    ok=graphene.Boolean()
    status_code=graphene.Int()
    message=graphene.String()





class UpdateBlog(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input=BlogInput()

    ok=graphene.Boolean()
    status_code=graphene.Int()
    message=graphene.String()

    @staticmethod
    def mutate(root,info,input,id):
        db = database.SessionLocal()
        blog_instance=db.query(models.Blog).filter(models.Blog.id==id)
        if not blog_instance.first():
            ok=False
            status_code=404
            message='blog does not exist'
            return UpdateBlog(ok=ok,message=message,status_code=status_code)
        
        blog_instance.update(title=input.title,blog=input.body)
        db.commit()
        db.close()
        ok=True
        status_code=200
        message='blog updated'
        return UpdateBlog(ok=ok,message=message,status_code=status_code)