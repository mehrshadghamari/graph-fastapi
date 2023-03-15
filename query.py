import graphene
import database,models





class Blog(graphene.ObjectType):
    id=graphene.ID()
    title=graphene.String()
    body=graphene.String()



class QueryBlog(graphene.ObjectType):

    blogs=graphene.List(Blog)
    blog=graphene.Field(Blog,id=graphene.Int())


    def resolve_blogs(self, info):
        db = database.SessionLocal()
        blogs=db.query(models.Blog).all()
        db.close
        return  blogs
    
    def resolve_blog(self, info,id):
        db = database.SessionLocal()
        blog= db.query(models.Blog).filter(models.Blog.id == id).first()
        db.close
        return blog