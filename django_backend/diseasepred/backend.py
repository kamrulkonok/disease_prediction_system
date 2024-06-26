# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.models import Permission
# from .models import User
# UserModel = User
# class MyBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         if username is None or password is None:
#             return
#         try:
#             user = UserModel.objects.get(username=username)
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a nonexistent user (#20760).
#             UserModel().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user

#     def get_user(self, user_id):
#         return super().get_user(user_id)