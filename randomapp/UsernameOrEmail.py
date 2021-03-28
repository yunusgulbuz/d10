from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

UserModel = get_user_model()


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, *args, **kwargs):
        try:
            if '@' in kwargs["username"]:
                user = UserModel.objects.get(email=kwargs["username"])
            else:
                user = UserModel.objects.get(username=kwargs["username"])
            if user.check_password(kwargs["password"]):
                return user
            return None
        except UserModel.DoesNotExist:
            user = None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None
