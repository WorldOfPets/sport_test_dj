from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from sportfriend.api import SwaggerSchemaView

router = routers.DefaultRouter()
router.register("Chat", api.ChatViewSet)
router.register("Images", api.ImagesViewSet)
router.register("LogErrors", api.LogErrorsViewSet)
router.register("Meeting", api.MeetingViewSet)
router.register("Message", api.MessageViewSet)
router.register("News", api.NewsViewSet)
router.register("SportCategory", api.SportCategoryViewSet)
router.register("SportFriends", api.SportFriendsViewSet)
router.register("UserChat", api.UserChatViewSet)
router.register("UserInfo", api.UserInfoViewSet)
router.register("User", api.UserViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    
    path("sportfriend/Chat/", views.ChatListView.as_view(), name="sportfriend_Chat_list"),
    path("sportfriend/Chat/create/", views.ChatCreateView.as_view(), name="sportfriend_Chat_create"),
    path("sportfriend/Chat/detail/<int:pk>/", views.ChatDetailView.as_view(), name="sportfriend_Chat_detail"),
    path("sportfriend/Chat/update/<int:pk>/", views.ChatUpdateView.as_view(), name="sportfriend_Chat_update"),
    path("sportfriend/Chat/delete/<int:pk>/", views.ChatDeleteView.as_view(), name="sportfriend_Chat_delete"),
    path("sportfriend/Images/", views.ImagesListView.as_view(), name="sportfriend_Images_list"),
    path("sportfriend/Images/create/", views.ImagesCreateView.as_view(), name="sportfriend_Images_create"),
    path("sportfriend/Images/detail/<int:pk>/", views.ImagesDetailView.as_view(), name="sportfriend_Images_detail"),
    path("sportfriend/Images/update/<int:pk>/", views.ImagesUpdateView.as_view(), name="sportfriend_Images_update"),
    path("sportfriend/Images/delete/<int:pk>/", views.ImagesDeleteView.as_view(), name="sportfriend_Images_delete"),
    path("sportfriend/LogErrors/", views.LogErrorsListView.as_view(), name="sportfriend_LogErrors_list"),
    path("sportfriend/LogErrors/create/", views.LogErrorsCreateView.as_view(), name="sportfriend_LogErrors_create"),
    path("sportfriend/LogErrors/detail/<int:pk>/", views.LogErrorsDetailView.as_view(), name="sportfriend_LogErrors_detail"),
    path("sportfriend/LogErrors/update/<int:pk>/", views.LogErrorsUpdateView.as_view(), name="sportfriend_LogErrors_update"),
    path("sportfriend/LogErrors/delete/<int:pk>/", views.LogErrorsDeleteView.as_view(), name="sportfriend_LogErrors_delete"),
    path("sportfriend/Meeting/", views.MeetingListView.as_view(), name="sportfriend_Meeting_list"),
    path("sportfriend/Meeting/create/", views.MeetingCreateView.as_view(), name="sportfriend_Meeting_create"),
    path("sportfriend/Meeting/detail/<int:pk>/", views.MeetingDetailView.as_view(), name="sportfriend_Meeting_detail"),
    path("sportfriend/Meeting/update/<int:pk>/", views.MeetingUpdateView.as_view(), name="sportfriend_Meeting_update"),
    path("sportfriend/Meeting/delete/<int:pk>/", views.MeetingDeleteView.as_view(), name="sportfriend_Meeting_delete"),
    path("sportfriend/Message/", views.MessageListView.as_view(), name="sportfriend_Message_list"),
    path("sportfriend/Message/create/", views.MessageCreateView.as_view(), name="sportfriend_Message_create"),
    path("sportfriend/Message/detail/<int:pk>/", views.MessageDetailView.as_view(), name="sportfriend_Message_detail"),
    path("sportfriend/Message/update/<int:pk>/", views.MessageUpdateView.as_view(), name="sportfriend_Message_update"),
    path("sportfriend/Message/delete/<int:pk>/", views.MessageDeleteView.as_view(), name="sportfriend_Message_delete"),
    path("sportfriend/News/", views.NewsListView.as_view(), name="sportfriend_News_list"),
    path("sportfriend/News/create/", views.NewsCreateView.as_view(), name="sportfriend_News_create"),
    path("sportfriend/News/detail/<int:pk>/", views.NewsDetailView.as_view(), name="sportfriend_News_detail"),
    path("sportfriend/News/update/<int:pk>/", views.NewsUpdateView.as_view(), name="sportfriend_News_update"),
    path("sportfriend/News/delete/<int:pk>/", views.NewsDeleteView.as_view(), name="sportfriend_News_delete"),
    path("sportfriend/SportCategory/", views.SportCategoryListView.as_view(), name="sportfriend_SportCategory_list"),
    path("sportfriend/SportCategory/create/", views.SportCategoryCreateView.as_view(), name="sportfriend_SportCategory_create"),
    path("sportfriend/SportCategory/detail/<int:pk>/", views.SportCategoryDetailView.as_view(), name="sportfriend_SportCategory_detail"),
    path("sportfriend/SportCategory/update/<int:pk>/", views.SportCategoryUpdateView.as_view(), name="sportfriend_SportCategory_update"),
    path("sportfriend/SportCategory/delete/<int:pk>/", views.SportCategoryDeleteView.as_view(), name="sportfriend_SportCategory_delete"),
    path("sportfriend/SportFriends/", views.SportFriendsListView.as_view(), name="sportfriend_SportFriends_list"),
    path("sportfriend/SportFriends/create/", views.SportFriendsCreateView.as_view(), name="sportfriend_SportFriends_create"),
    path("sportfriend/SportFriends/detail/<int:pk>/", views.SportFriendsDetailView.as_view(), name="sportfriend_SportFriends_detail"),
    path("sportfriend/SportFriends/update/<int:pk>/", views.SportFriendsUpdateView.as_view(), name="sportfriend_SportFriends_update"),
    path("sportfriend/SportFriends/delete/<int:pk>/", views.SportFriendsDeleteView.as_view(), name="sportfriend_SportFriends_delete"),
    path("sportfriend/UserChat/", views.UserChatListView.as_view(), name="sportfriend_UserChat_list"),
    path("sportfriend/UserChat/create/", views.UserChatCreateView.as_view(), name="sportfriend_UserChat_create"),
    path("sportfriend/UserChat/detail/<int:pk>/", views.UserChatDetailView.as_view(), name="sportfriend_UserChat_detail"),
    path("sportfriend/UserChat/update/<int:pk>/", views.UserChatUpdateView.as_view(), name="sportfriend_UserChat_update"),
    path("sportfriend/UserChat/delete/<int:pk>/", views.UserChatDeleteView.as_view(), name="sportfriend_UserChat_delete"),
    path("sportfriend/UserInfo/", views.UserInfoListView.as_view(), name="sportfriend_UserInfo_list"),
    path("sportfriend/UserInfo/create/", views.UserInfoCreateView.as_view(), name="sportfriend_UserInfo_create"),
    path("sportfriend/UserInfo/detail/<int:pk>/", views.UserInfoDetailView.as_view(), name="sportfriend_UserInfo_detail"),
    path("sportfriend/UserInfo/update/<int:pk>/", views.UserInfoUpdateView.as_view(), name="sportfriend_UserInfo_update"),
    path("sportfriend/UserInfo/delete/<int:pk>/", views.UserInfoDeleteView.as_view(), name="sportfriend_UserInfo_delete"),

)
