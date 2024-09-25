from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)

class ChatViewSet(viewsets.ModelViewSet):
    """ViewSet for the Chat class"""

    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["description", "type"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"


class MeetingViewSet(viewsets.ModelViewSet):
    """ViewSet for the Meeting class"""

    queryset = models.Meeting.objects.all()
    serializer_class = serializers.MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["loaction_name", "description"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Message class"""

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["body"]
    filterset_fields = "__all__"
    ordering_fields = "__all__"



class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet for the News class"""

    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]
    filterset_fields = ["user_id", "name",  "last_updated", "created", "uuid", "description"]
    ordering_fields = ["user_id", "name", "last_updated", "created", "uuid", "description"]


class SportCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the SportCategory class"""

    queryset = models.SportCategory.objects.all()
    serializer_class = serializers.SportCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["name",  "last_updated", "created", "uuid"]
    ordering_fields = ["name",  "last_updated", "created", "uuid"]


class SportFriendsViewSet(viewsets.ModelViewSet):
    """ViewSet for the SportFriends class"""

    queryset = models.SportFriends.objects.all()
    serializer_class = serializers.SportFriendsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = "__all__"
    ordering_fields = "__all__"


class UserChatViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserChat class"""

    queryset = models.UserChat.objects.all()
    serializer_class = serializers.UserChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    


class UserInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserInfo class"""

    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ["user_id",  "longitude", "last_updated", "description", "second_name", "uuid", "created", "find_area", "latitude", "birthday"]
    ordering_fields = ["user_id",  "longitude", "last_updated", "description", "second_name", "uuid", "created", "find_area", "latitude", "birthday"]

class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserInfo class"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ["first_name",  "last_name", "username", "email"]
    ordering_fields = ["first_name",  "last_name", "username", "email"]
    
