from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    path("<int:id>/like/", view=views.LikeImage.as_view(), name='like_image'),
    path("<int:id>/comment/", view=views.CommentOnImage.as_view(), name='comment_image')
]

#/images/3/like/

#2 we want to find an image with this id
#3 we want to create a like for that image