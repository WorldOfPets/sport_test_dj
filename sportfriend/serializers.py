from rest_framework import serializers

from . import models


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Chat
        fields = [
            "name",
            "created",
            "last_updated",
            "uuid",
        ]

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Images
        fields = [
            "last_updated",
            "filePath",
            "created",
            "uuid",
            "is_private",
        ]

class LogErrorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LogErrors
        fields = [
            "created",
            "error_time",
            "user_id",
            "description",
            "last_updated",
            "type",
            "error_uuid",
        ]

class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Meeting
        fields = [
            "last_updated",
            "created",
            "loaction_name",
            "longitude",
            "date_start",
            "description",
            "date_end",
            "uuid",
            "is_private",
            "latitude",
            "users_list",
            "category_id",
        ]

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = [
            "last_updated",
            "uuid",
            "body",
            "created",
            "user_id",
            "chat_id",
        ]

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.News
        fields = [
            "name",
            "main_image",
            "last_updated",
            "created",
            "uuid",
            "description",
            "user_id",
            "images_many",
        ]

class SportCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SportCategory
        fields = [
            "name",
            "uuid",
            "sport_icon",
            "created",
            "last_updated",
        ]

class SportFriendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SportFriends
        fields = [
            "last_updated",
            "created",
            "is_confirm",
            "user_fr_id",
            "user_id",
        ]

class UserChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserChat
        fields = [
            "created",
            "last_updated",
            "uuid",
            "user_id",
            "chat_id",
        ]

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInfo
        fields = [
            "find_area",
            "second_name",
            "uuid",
            "last_updated",
            "latitude",
            "description",
            "created",
            "profile_photo",
            "birthday",
            "longitude",
            "user_id",
            "sport_categories_list",
            "images_list",
            "meetings_list",
        ]
