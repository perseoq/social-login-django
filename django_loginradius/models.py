from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class LR_sociallogin(models.Model):

    email = models.CharField(max_length=36, default='')
    provider_id = models.TextField(blank= True, null=True)
    provider = models.TextField(blank= True, null=True)

    def id_generator(self):
        """
        Generate random number
        """
        import random
        return random.randint(1,10000000)

    def get_lr_username(self, profile):
        """
        Generate username using loginradius profile data.
        """
        try:
            if profile['FirstName'] is not None and profile['LastName'] is not None :
                username = profile['FirstName'] + "-" + profile['LastName']
            elif profile['FullName'] is not None :
                username = profile['FullName']
                username = str.replace(username, ' ', '-')
            elif profile['ProfileName'] is not None :
                username = profile['ProfileName']
            elif profile['NickName'] is not None :
                username = profile['NickName']
            else:
                import string
                value =string.split(profile['email'], '@')
                username = value[0]
        except:
            """
            Handle username issue and get random value for username.
            """
            username = str(self.id_generator())
        return username

    def check_lr_username(self, profile):
        """
        Check username is also exist and generate unique username.
        """
        username = self.get_lr_username(profile)
        user_name = username
        index = 0
        nameexists = True
        while nameexists:
            try:
                User.objects.get(username=user_name)
                index += 1
                user_name = username + str( index )
            except User.DoesNotExist:
                nameexists = False
        return user_name

    def create_lr_user(self, profile):
        """
        Insert new user to Django Database.
        """
        username = self.check_lr_username(profile)
        password = str(self.id_generator())
        user = User.objects.create_user(username, profile['email'], password)
        if profile['LastName'] is not None:
            user.last_name = profile['LastName']
        if profile['FirstName'] is not None:
            user.first_name = profile['FirstName']
        user.save()
        return user
        
        
           
        

