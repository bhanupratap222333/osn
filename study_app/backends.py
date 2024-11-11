# # backends.py

# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class EmailOrMobileBackend(ModelBackend):
#     """
#     Custom authentication backend that allows users to authenticate
#     using either their email or mobile number.
#     """

#     def authenticate(self, request, username=None, password=None, **kwargs):
#         email = kwargs.get('email')
#         mobile = kwargs.get('mobile')

#         user = None
#         if email:
#             user = User.objects.filter(email=email).first()
#         elif mobile:
#             user = User.objects.filter(mobile=mobile).first()

#         if user and user.check_password(password):
#             return user

#         return None
