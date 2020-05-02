from django.urls import path, include
from . import views  #import everything from views module
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
#iserrano0
app_name = 'share'
urlpatterns = [
    path('',views.index, name='index'),
    #iserrano2
    # authentication: signup, login, logout
    path('create', views.create, name='create'),
    path("loguser", views.login_user, name="loguser"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    #iserrano2
    #dashboard & publish_problem
    path("dashboard", views.dashboard, name='dashboard'),
    #iserrano3
    # path('problem/<int:problem_id>/show_my_problem', views.show_my_problem, name='show_my_problem'),
    # path('script/<int:script_id>/show_my_script', views.show_my_script, name='show_my_script'),
    # path('problem/<int:problem_id>/show_problem', views.show_problem, name='show_problem'),
    # path('script/<int:script_id>/show_script', views.show_script, name='show_script'),

    #iserrano4
    path('user/<int:user_id>/edit_profile', views.edit_profile, name='edit_profile'),
    path('user/<int:user_id>/update_profile', views.update_profile, name='update_profile'),
    path('user/<int:user_id>/delete_profile', views.delete_profile, name='delete_profile'),
    path('post/publish', views.publish_post, name='publish_post'),
    path('post/create', views.create_post, name="create_post"),
    path('post/<int:post_id>/edit_post', views.edit_post, name="edit_post"),
    path('post/<int:post_id>/update_post', views.update_post, name="update_post"),
    path('post/<int:post_id>/delete_post', views.delete_post, name="delete_post"),

    #iserrano6
    path('user/<int:user_id>/user_profile', views.user_profile, name="user_profile"),
    path('post/<int:post_id>/show_post', views.show_post, name='show_post'),
    path('comment/<int:post_id>/create_comment', views.create_comment, name="create_comment"),
    path('comment/<int:comment_id>/delete_comment', views.delete_comment, name="delete_comment"),
    path('search', views.search, name='search'),

    #iserrano7
    # path('user/<int:user_id>/add_friends', views.add_friends, name="add_friends"),
    # path('user/<int:user_id>/remove_friends', views.remove_friends, name="remove_friends"),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),

    # s3Integration
    path('upload', views.upload, name='upload'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
