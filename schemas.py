import graphene
from create import CreateBlog
from edit import UpdateBlog
from delete import DeleteBlog




class BlogMutation(graphene.ObjectType):
    create_blog=CreateBlog.Field()
    update_blog=UpdateBlog.Field()
    delete_blog=DeleteBlog.Field()