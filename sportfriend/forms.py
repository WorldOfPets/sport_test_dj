from django import forms
from django.contrib.auth.models import User
from sportfriend.models import SportCategory
from django.contrib.auth.models import User
from sportfriend.models import Chat
from django.contrib.auth.models import User
from sportfriend.models import Images
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from sportfriend.models import Chat
from django.contrib.auth.models import User
from sportfriend.models import SportCategory
from sportfriend.models import Images
from sportfriend.models import Meeting
from . import models


class ChatForm(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = [
            "name",
        ]


class ImagesForm(forms.ModelForm):
    class Meta:
        model = models.Images
        fields = [
            "filePath",
            "is_private",
        ]


class LogErrorsForm(forms.ModelForm):
    class Meta:
        model = models.LogErrors
        fields = [
            "error_time",
            "user_id",
            "description",
            "type",
            "error_uuid",
        ]


class MeetingForm(forms.ModelForm):
    class Meta:
        model = models.Meeting
        fields = [
            "loaction_name",
            "longitude",
            "date_start",
            "description",
            "date_end",
            "is_private",
            "latitude",
            "users_list",
            "category_id",
        ]

    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields["users_list"].queryset = User.objects.all()
        self.fields["category_id"].queryset = SportCategory.objects.all()



class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = [
            "body",
            "user_id",
            "chat_id",
        ]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["user_id"].queryset = User.objects.all()
        self.fields["chat_id"].queryset = Chat.objects.all()



class NewsForm(forms.ModelForm):
    class Meta:
        model = models.News
        fields = [
            "name",
            "main_image",
            "description",
            "user_id",
            "images_many",
        ]

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields["user_id"].queryset = User.objects.all()
        self.fields["images_many"].queryset = Images.objects.all()



class SportCategoryForm(forms.ModelForm):
    class Meta:
        model = models.SportCategory
        fields = [
            "name",
            "sport_icon",
        ]


class SportFriendsForm(forms.ModelForm):
    class Meta:
        model = models.SportFriends
        fields = [
            "is_confirm",
            "user_fr_id",
            "user_id",
        ]

    def __init__(self, *args, **kwargs):
        super(SportFriendsForm, self).__init__(*args, **kwargs)
        self.fields["user_fr_id"].queryset = User.objects.all()
        self.fields["user_id"].queryset = User.objects.all()



class UserChatForm(forms.ModelForm):
    class Meta:
        model = models.UserChat
        fields = [
            "user_id",
            "chat_id",
        ]

    def __init__(self, *args, **kwargs):
        super(UserChatForm, self).__init__(*args, **kwargs)
        self.fields["user_id"].queryset = User.objects.all()
        self.fields["chat_id"].queryset = Chat.objects.all()



class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = [
            "find_area",
            "second_name",
            "latitude",
            "description",
            "profile_photo",
            "birthday",
            "longitude",
            "user_id",
            "sport_categories_list",
            "images_list",
            "meetings_list",
        ]

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields["user_id"].queryset = User.objects.all()
        self.fields["sport_categories_list"].queryset = SportCategory.objects.all()
        self.fields["images_list"].queryset = Images.objects.all()
        self.fields["meetings_list"].queryset = Meeting.objects.all()

