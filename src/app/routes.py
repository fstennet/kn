from flask import Blueprint, request, Response
from models import command

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/")
def index():
    return {"message": "Welcome to kn!"}

@api_routes.route("/talk", methods=["POST"])
def hey():
    if request.is_json:
        request_content = request.get_json()
        current_talk = command(request_content.domain, request_content.question)

    return Response(status=404)