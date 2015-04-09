from django.conf.urls import patterns, url
from account import views
from yagoapp.urls import router


router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',

    url(r'^register-by-token/$', views.social_register, name='register')

    # Attempt to register a new user
    # url(r'^register/$', views.register_user, name='register'),

    # Attempt to log user into session
    # ex. /user/login/
    # url(r'^login/$', views.login_user, name='login'),

    # Log user out of the session
    # ex. /user/logout/
    # url(r'^logout/$', views.logout_user, name='logout'),

)