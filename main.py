import asyncio

import uvicorn
import graphene
from fastapi import FastAPI
from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp,make_playground_handler
from schemas import BlogMutation
from query import QueryBlog
import models
from database import engine

app=FastAPI()

models.Base.metadata.create_all(engine)



@app.get('/')
def index():
    return {'data': {'message': 'you can access to api with /ghraph address'}}




# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query,mutation=BlogMutation),on_get=make_graphiql_handler()))
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=QueryBlog,mutation=BlogMutation),on_get=make_playground_handler()))

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)


