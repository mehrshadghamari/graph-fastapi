import database
import graphene
import models


class DeleteBlog(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    status_code = graphene.Int()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, id):
        db = database.SessionLocal()
        blog_instance = db.query(models.Blog).filter(models.Blog.id == id)
        if not blog_instance.first():
            ok = False
            status_code = 404
            message = "blog does not exist"
            return DeleteBlog(ok=ok, message=message, status_code=status_code)
        blog_instance.delete(synchronize_session=False)
        db.commit()
        db.close()
        ok = True
        status_code = 204
        message = "blog delete"
        return DeleteBlog(ok=ok, message=message, status_code=status_code)
