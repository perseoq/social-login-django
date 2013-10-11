from LoginRadiusSDK import LoginRadius
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.db.models import get_model

lr_sociallogin = get_model('django_loginradius', 'LR_sociallogin')

class LoginRadiusAuthBackend(object):
    def authenticate(self, token):
        """
        Authenticate existing or new user.
        """
        login = LoginRadius(settings.LOGINRADIUS_API_SECRET,token)
        Access_Token = login.loginradius_get_accesstoken()
        if 'access_token' in Access_Token:
            accessToken = Access_Token['access_token']
            #Let us try getting the user's profile information
            profile = login.loginradius_get_userprofile(accessToken)
            if profile['Email'] is not None:
                for item in profile['Email']:
                    profile['email'] = item["Value"]
            else:
                value = str ( profile['ID'] )
                value = str.replace(value, 'http://', '')
                value = str.replace(value, 'https://', '')
                value = str (value[:7])
                profile['email'] = value + '@' + profile['Provider'] + '.com'

            u, created = lr_sociallogin.objects.get_or_create(email=profile['email'], provider_id=profile['ID'], provider=profile['Provider'])
            if created:
                try:
                    """
                    Check email address is exist and get user profile if exist.
                    """
                    user = User.objects.get(email=u.email)
                except User.DoesNotExist:
                    """
                    New user.
                    """
                    user = u.create_lr_user(profile)

            else:
                try:
                    user = User.objects.get(email = profile['email'])
                except User.DoesNotExist:
                    """
                    New User
                    """
                    user = u.create_lr_user(profile)
            return user
        
        elif 'errorCode' in Access_Token:
            """
            Request Token has been Expired.
            """
            raise ValueError(Access_Token['description'])
            

    
    def get_user(self, user_id):
        """
        Retrieve user by user ID
        :param user_id: User ID
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
