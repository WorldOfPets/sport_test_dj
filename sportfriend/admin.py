from django.contrib import admin
from django import forms

from . import models


class ChatAdminForm(forms.ModelForm):

    class Meta:
        model = models.Chat
        fields = "__all__"


class ChatAdmin(admin.ModelAdmin):
    form = ChatAdminForm
    list_display = [
        "new_messages",
        "last_updated",
        "uuid",
        "created",
        "name",
    ]
    readonly_fields = [
        "new_messages",
        "last_updated",
        "uuid",
        "created",
        "name",
    ]


class ImagesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Images
        fields = "__all__"


class ImagesAdmin(admin.ModelAdmin):
    form = ImagesAdminForm
    list_display = [
        "last_updated",
        "filePath",
        "created",
        "uuid",
        "is_private",
    ]
    readonly_fields = [
        "last_updated",
        "filePath",
        "created",
        "uuid",
        "is_private",
    ]


class LogErrorsAdminForm(forms.ModelForm):

    class Meta:
        model = models.LogErrors
        fields = "__all__"


class LogErrorsAdmin(admin.ModelAdmin):
    form = LogErrorsAdminForm
    list_display = [
        "created",
        "error_time",
        "user_id",
        "description",
        "last_updated",
        "type",
        "error_uuid",
    ]
    readonly_fields = [
        "created",
        "error_time",
        "user_id",
        "description",
        "last_updated",
        "type",
        "error_uuid",
    ]


class MeetingAdminForm(forms.ModelForm):

    class Meta:
        model = models.Meeting
        fields = "__all__"


class MeetingAdmin(admin.ModelAdmin):
    form = MeetingAdminForm
    list_display = [
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
    ]
    readonly_fields = [
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
    ]


class MessageAdminForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = "__all__"


class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    list_display = [
        "last_updated",
        "uuid",
        "body",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "uuid",
        "body",
        "created",
    ]


class NewsAdminForm(forms.ModelForm):

    class Meta:
        model = models.News
        fields = "__all__"


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = [
        "name",
        "main_image",
        "last_updated",
        "created",
        "uuid",
        "description",
    ]
    readonly_fields = [
        "name",
        "main_image",
        "last_updated",
        "created",
        "uuid",
        "description",
    ]


class SportCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.SportCategory
        fields = "__all__"


class SportCategoryAdmin(admin.ModelAdmin):
    form = SportCategoryAdminForm
    list_display = [
        "name",
        "uuid",
        "sport_icon",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "uuid",
        "sport_icon",
        "created",
        "last_updated",
    ]


class SportFriendsAdminForm(forms.ModelForm):

    class Meta:
        model = models.SportFriends
        fields = "__all__"


class SportFriendsAdmin(admin.ModelAdmin):
    form = SportFriendsAdminForm
    list_display = [
        "last_updated",
        "created",
        "is_confirm",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "is_confirm",
    ]


class UserChatAdminForm(forms.ModelForm):

    class Meta:
        model = models.UserChat
        fields = "__all__"


class UserChatAdmin(admin.ModelAdmin):
    form = UserChatAdminForm
    list_display = [
        "created",
        "last_updated",
        "uuid",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "uuid",
    ]


class UserInfoAdminForm(forms.ModelForm):

    class Meta:
        model = models.UserInfo
        fields = "__all__"


class UserInfoAdmin(admin.ModelAdmin):
    form = UserInfoAdminForm
    list_display = [
        "profile_photo",
        "longitude",
        "last_updated",
        "description",
        "second_name",
        "uuid",
        "created",
        "find_area",
        "latitude",
        "birthday",
    ]
    readonly_fields = [
        "profile_photo",
        "longitude",
        "last_updated",
        "description",
        "second_name",
        "uuid",
        "created",
        "find_area",
        "latitude",
        "birthday",
    ]


admin.site.register(models.Chat, ChatAdmin)
admin.site.register(models.Images, ImagesAdmin)
admin.site.register(models.LogErrors, LogErrorsAdmin)
admin.site.register(models.Meeting, MeetingAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.SportCategory, SportCategoryAdmin)
admin.site.register(models.SportFriends, SportFriendsAdmin)
admin.site.register(models.UserChat, UserChatAdmin)
admin.site.register(models.UserInfo, UserInfoAdmin)
