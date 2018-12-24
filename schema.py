import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='Alice', last_login=datetime.now()),
            User(username='Bob', last_login=datetime.now()),
            User(username='Steven', last_login=datetime.now())
        ][:first]


schema = graphene.Schema(query=Query)
result = schema.execute(
    '''
    {
        users(first:2){
            username
            lastLogin
        }
    }
    '''
)


items = dict(result.data.items())
print(json.dumps(items, indent=4))