import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from sportfriend import models as sportfriend_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_sportfriend_Chat(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return sportfriend_models.Chat.objects.create(**defaults)
def create_sportfriend_Images(**kwargs):
    defaults = {}
    defaults["filePath"] = ""
    defaults["is_private"] = ""
    defaults.update(**kwargs)
    return sportfriend_models.Images.objects.create(**defaults)
def create_sportfriend_LogErrors(**kwargs):
    defaults = {}
    defaults["error_time"] = datetime.now()
    defaults["user_id"] = ""
    defaults["description"] = ""
    defaults["type"] = ""
    defaults["error_uuid"] = ""
    defaults.update(**kwargs)
    return sportfriend_models.LogErrors.objects.create(**defaults)
def create_sportfriend_Meeting(**kwargs):
    defaults = {}
    defaults["loaction_name"] = ""
    defaults["longitude"] = ""
    defaults["date_start"] = datetime.now()
    defaults["description"] = ""
    defaults["date_end"] = datetime.now()
    defaults["is_private"] = ""
    defaults["latitude"] = ""
    if "users_list" not in kwargs:
        defaults["users_list"] = create_User()
    if "category_id" not in kwargs:
        defaults["category_id"] = create_sportfriend_SportCategory()
    defaults.update(**kwargs)
    return sportfriend_models.Meeting.objects.create(**defaults)
def create_sportfriend_Message(**kwargs):
    defaults = {}
    defaults["body"] = ""
    if "user_id" not in kwargs:
        defaults["user_id"] = create_User()
    if "chat_id" not in kwargs:
        defaults["chat_id"] = create_sportfriend_Chat()
    defaults.update(**kwargs)
    return sportfriend_models.Message.objects.create(**defaults)
def create_sportfriend_News(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["main_image"] = ""
    defaults["description"] = ""
    if "user_id" not in kwargs:
        defaults["user_id"] = create_User()
    if "images_many" not in kwargs:
        defaults["images_many"] = create_sportfriend_Images()
    defaults.update(**kwargs)
    return sportfriend_models.News.objects.create(**defaults)
def create_sportfriend_SportCategory(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["sport_icon"] = ""
    defaults.update(**kwargs)
    return sportfriend_models.SportCategory.objects.create(**defaults)
def create_sportfriend_SportFriends(**kwargs):
    defaults = {}
    defaults["is_confirm"] = ""
    if "user_fr_id" not in kwargs:
        defaults["user_fr_id"] = create_User()
    if "user_id" not in kwargs:
        defaults["user_id"] = create_User()
    defaults.update(**kwargs)
    return sportfriend_models.SportFriends.objects.create(**defaults)
def create_sportfriend_UserChat(**kwargs):
    defaults = {}
    if "user_id" not in kwargs:
        defaults["user_id"] = create_User()
    if "chat_id" not in kwargs:
        defaults["chat_id"] = create_sportfriend_Chat()
    defaults.update(**kwargs)
    return sportfriend_models.UserChat.objects.create(**defaults)
def create_sportfriend_UserInfo(**kwargs):
    defaults = {}
    defaults["find_area"] = ""
    defaults["second_name"] = ""
    defaults["latitude"] = ""
    defaults["description"] = ""
    defaults["profile_photo"] = ""
    defaults["birthday"] = datetime.now()
    defaults["longitude"] = ""
    if "user_id" not in kwargs:
        defaults["user_id"] = create_User()
    if "sport_categories_list" not in kwargs:
        defaults["sport_categories_list"] = create_sportfriend_SportCategory()
    if "images_list" not in kwargs:
        defaults["images_list"] = create_sportfriend_Images()
    if "meetings_list" not in kwargs:
        defaults["meetings_list"] = create_sportfriend_Meeting()
    defaults.update(**kwargs)
    return sportfriend_models.UserInfo.objects.create(**defaults)
