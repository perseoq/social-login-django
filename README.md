django-social-auth
==================

Django social auth (django_loginradius) app eliminate traditional registration form and let your users sign-up in few seconds with their existing social IDs such as Facebook, Twitter, Google, Amazon, Yahoo, Vkontakte and over 25 more. However, you can keep both traditional login system as well as social login.

Requirement
===
Django >=1.4 

Installation Setup
===

Add this app (django_loginradius) to your project directory.

Configuration:

1. settings.py
  
    Add django_loginradius to INSTALLED_APPS, make sure you have django.contrib.auth enabled:
    
            INSTALLED_APPS = (
                    'django.contrib.auth',
                    # . . .
                    'django_loginradius',
                )
    
    Add the authentication backend::
    
            AUTHENTICATION_BACKENDS = ('django_loginradius.loginradius_auth.LoginRadiusAuthBackend',)
    
    Configure LoginRadius:
    **YOUR-LOGINRADIUS-SECRET-KEY** you can get from LoginRadius account.
            
          LOGINRADIUS_API_SECRET = 'YOUR-LOGINRADIUS-SECRET-KEY'

2. urls.py

    Add the following URL pattern to your **urlpatterns** tuple:
    
            url(r'^loginradius/', include('django_loginradius.urls'))
            
    This should enable you to use the callback view at **/loginradius/connect/**

3. Template setup - Follow the steps below to add Social Login interface inside your login template:

    a. Add the following code to < head > tag
    
      Add the **loginradius-api-key** that you get from your LoginRadius account.
      
      For Django <1.5
      Set  **$ui.callback** attribute of the LoginRadius callback view. Example **"http://yourdomain.com{% url  lr_connect %}"**
      
      For Django >= 1.5 
      Set  **$ui.callback** attribute of the LoginRadius callback view. Example **"http://yourdomain.com{% url  'lr_connect' %}"**
      
      Note: Be sure to add **$ui.callback** attribute in following code is according to the django version.
        
        <script src="http://hub.loginradius.com/include/js/LoginRadius.js"></script>
        <script type="text/javascript">      var options={};      options.login=true;       
        LoginRadius_SocialLogin.util.ready(function () { $ui = LoginRadius_SocialLogin.lr_login_settings;$ui.interfacesize = "";$ui.apikey = "your-loginradius-api-key";$ui.callback="http://yourdomain.com{% url  lr_connect  %}"; $ui.lrinterfacecontainer ="interfacecontainerdiv"; LoginRadius_SocialLogin.init(options);  }); </script>
    
    b. Add the following code to < body > tag:
    
          <div id="interfacecontainerdiv" class="interfacecontainerdiv"></div>

If you have any questions/issues about the django app, please contact us at community.loginradius.com.
