from django.urls import path
from socialweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("signin",views.Loginview.as_view(),name="signin"),
    path("profile/add",views.ProfileCreateView.as_view(),name="home"),
    path("profile/view",views.IndexView.as_view(),name="index"),
    path("signout",views.SignoutView.as_view(),name="signout"),
    path("profile/details",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-edit"),
    path("posts/add",views.PostAddView.as_view(),name="post-add"),
    path("posts/<int:pk>/remove",views.PostDeleteView.as_view(),name="post-delete"),
    path("posts/<int:id>/like/add",views.LikeView.as_view(),name="like"),
    path("posts/<int:id>/dislike/add",views.DislikeView.as_view(),name="like-remove"),
    path("posts/<int:id>/comments/add",views.CommentAddView.as_view(),name="comment-add"),
    path("posts/<int:id>/change",views.PostUpdateView.as_view(),name="post-edit"),
    path("comments/<int:pk>/remove",views.CommentDeleteView.as_view(),name="comment-delete"),
    path("comments/<int:id>/upvote/add",views.CommmentUpvoteView.as_view(),name="upvote"),
    path("comments/<int:id>/upvote/remove",views.CommentRemoveView.as_view(),name="upvote-remove"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)