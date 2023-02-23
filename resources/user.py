from db import db
from flask.views import MethodView
from models import UserModel
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, create_refresh_token, get_jwt_identity
from passlib.hash import pbkdf2_sha256
from blocklist import BLOCKLIST

blp = Blueprint("Users", "users", description="operations on users.")

@blp.route("/register")
class register(MethodView):

    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username==user_data["username"]).first():
            abort(400, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"])
            )
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully."}
    
@blp.route("/user/<int:user_id>")
class User(MethodView):

    @jwt_required(fresh=True)
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    @jwt_required(fresh=True)
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User Deleted."}
    

@blp.route("/login")
class UserLogin(MethodView):

    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token":access_token, "refresh_token": refresh_token}
        abort(401, message="invalid credentials")


@blp.route("/logout")
class UserLogout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "successfully logged out."}
    

@blp.route("/refresh")
class RefreshToken(MethodView):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": new_token}