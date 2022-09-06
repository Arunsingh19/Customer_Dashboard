# from django.conf import settings
# from django.contrib.auth import get_user_model

# from .models import Customer


# class UserAuthBackend(object):    
#     def authenticate(self, username=None, password=None):
#         try:
#             Customer = get_user_model()

#             user = Customer.objects.get(=username)
#             if user:
#                 return user
#         except Customer.DoesNotExist:
#             return "account not found"

#     def get_user(self, user_id):
#        try:
#           account = get_user_model()
#           return account.objects.get(pk=user_id)
#        except User.DoesNotExist:
#           return None