import graphene
from create import CreateBlog
from delete import DeleteBlog
from edit import UpdateBlog
from query import QueryBlog
from users.query import UserQuery
from users.mutation import CreateUser


class Query(QueryBlog,UserQuery):
    pass





class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()
    delete_blog = DeleteBlog.Field()
    create_user = CreateUser.Field()