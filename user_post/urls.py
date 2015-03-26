from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from user_post import views
from yagoapp.urls import router

router.register(r'reported_posts', views.ReportedPostViewSet)
router.register(r'likes', views.LikeViewSet)

urlpatterns = patterns('',

    url(r'^like_post/$', csrf_exempt(views.like_post)),
    url(r'^report_post/$', csrf_exempt(views.report_post)),

    url(r'^$', csrf_exempt(views.PostList.as_view())),
    url(r'^(?P<pk>[0-9]+)/$', csrf_exempt(views.PostDetail.as_view())),
)