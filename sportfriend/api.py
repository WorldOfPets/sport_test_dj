from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ChatViewSet(viewsets.ModelViewSet):
    """ViewSet for the Chat class"""

    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImagesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Images class"""

    queryset = models.Images.objects.all()
    serializer_class = serializers.ImagesSerializer
    permission_classes = [permissions.IsAuthenticated]


class LogErrorsViewSet(viewsets.ModelViewSet):
    """ViewSet for the LogErrors class"""

    queryset = models.LogErrors.objects.all()
    serializer_class = serializers.LogErrorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeetingViewSet(viewsets.ModelViewSet):
    """ViewSet for the Meeting class"""

    queryset = models.Meeting.objects.all()
    serializer_class = serializers.MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Message class"""

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet for the News class"""

    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticated]


class SportCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the SportCategory class"""

    queryset = models.SportCategory.objects.all()
    serializer_class = serializers.SportCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class SportFriendsViewSet(viewsets.ModelViewSet):
    """ViewSet for the SportFriends class"""

    queryset = models.SportFriends.objects.all()
    serializer_class = serializers.SportFriendsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserChatViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserChat class"""

    queryset = models.UserChat.objects.all()
    serializer_class = serializers.UserChatSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserInfo class"""

    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
