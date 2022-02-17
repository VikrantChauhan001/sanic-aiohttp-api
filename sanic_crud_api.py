from sanic import Sanic
from sanic.response import json as json_response
from sanic.exceptions import NotFound
from sanic_motor import BaseModel
from bson import ObjectId
import urllib
import aiohttp
import os

app = Sanic(__name__)

settings = dict(
    MOTOR_URI="mongodb+srv://vikrant:"+ urllib.parse.quote(os.environ['MONGO_PASSWORD']) +"@cluster0.8yztj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
)
app.config.update(settings)

BaseModel.init_app(app)


class User(BaseModel):
    __coll__ = "users"


@app.route("/", methods=["POST"])
async def create_user(request):
    user = request.json
    user["_id"] = str(ObjectId())

    new_user = await User.insert_one(user)
    created_user = await User.find_one(
        {"_id": new_user.inserted_id}, as_raw=True
    )

    return json_response(created_user, 201)


@app.route("/", methods=["GET"])
async def list_users(request):
    users = await User.find(as_raw=True)
    return json_response(users.objects)


@app.route("/<id>", methods=["GET"])
async def show_user(request, id):
    if (user := await User.find_one({"_id": id}, as_raw=True)) is not None:
        return json_response(user)
    return json_response({"error": f"User {id} not found"}, 404)



@app.route("/<id>", methods=["PUT"])
async def update_user(request, id):
    user = request.json
    update_result = await User.update_one({"_id": id}, {"$set": user})

    if update_result.modified_count == 1:
        if (
            updated_user := await User.find_one({"_id": id}, as_raw=True)
        ) is not None:
            return json_response(updated_user)

    if (
        existing_user := await User.find_one({"_id": id}, as_raw=True)
    ) is not None:
        return json_response(existing_user)

    return json_response({"error": f"User {id} not found"}, 404)


@app.route("/<id>", methods=["DELETE"])
async def delete_user(request, id):
    delete_result = await User.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return json_response({}, status=204)
    return json_response({"error": f"User {id} not found"}, 404)


@app.route("/random", methods=["GET"])
async def random(request):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.boredapi.com/api/activity") as response:
            return json_response(await response.json(), 200)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)