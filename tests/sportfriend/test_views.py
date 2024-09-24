import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Chat_list_view(client):
    instance1 = test_helpers.create_sportfriend_Chat()
    instance2 = test_helpers.create_sportfriend_Chat()
    url = reverse("sportfriend_Chat_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Chat_create_view(client):
    url = reverse("sportfriend_Chat_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Chat_detail_view(client):
    instance = test_helpers.create_sportfriend_Chat()
    url = reverse("sportfriend_Chat_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Chat_update_view(client):
    instance = test_helpers.create_sportfriend_Chat()
    url = reverse("sportfriend_Chat_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Images_list_view(client):
    instance1 = test_helpers.create_sportfriend_Images()
    instance2 = test_helpers.create_sportfriend_Images()
    url = reverse("sportfriend_Images_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Images_create_view(client):
    url = reverse("sportfriend_Images_create")
    data = {
        "filePath": "aFile",
        "is_private": True,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Images_detail_view(client):
    instance = test_helpers.create_sportfriend_Images()
    url = reverse("sportfriend_Images_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Images_update_view(client):
    instance = test_helpers.create_sportfriend_Images()
    url = reverse("sportfriend_Images_update", args=[instance.pk, ])
    data = {
        "filePath": "aFile",
        "is_private": True,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_LogErrors_list_view(client):
    instance1 = test_helpers.create_sportfriend_LogErrors()
    instance2 = test_helpers.create_sportfriend_LogErrors()
    url = reverse("sportfriend_LogErrors_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_LogErrors_create_view(client):
    url = reverse("sportfriend_LogErrors_create")
    data = {
        "error_time": datetime.now(),
        "user_id": 1,
        "description": "text",
        "type": "text",
        "error_uuid": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_LogErrors_detail_view(client):
    instance = test_helpers.create_sportfriend_LogErrors()
    url = reverse("sportfriend_LogErrors_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_LogErrors_update_view(client):
    instance = test_helpers.create_sportfriend_LogErrors()
    url = reverse("sportfriend_LogErrors_update", args=[instance.pk, ])
    data = {
        "error_time": datetime.now(),
        "user_id": 1,
        "description": "text",
        "type": "text",
        "error_uuid": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Meeting_list_view(client):
    instance1 = test_helpers.create_sportfriend_Meeting()
    instance2 = test_helpers.create_sportfriend_Meeting()
    url = reverse("sportfriend_Meeting_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Meeting_create_view(client):
    users_list = test_helpers.create_User()
    category_id = test_helpers.create_sportfriend_SportCategory()
    url = reverse("sportfriend_Meeting_create")
    data = {
        "loaction_name": "text",
        "longitude": 1.0f,
        "date_start": datetime.now(),
        "description": "text",
        "date_end": datetime.now(),
        "is_private": True,
        "latitude": 1.0f,
        "users_list": users_list.pk,
        "category_id": category_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Meeting_detail_view(client):
    instance = test_helpers.create_sportfriend_Meeting()
    url = reverse("sportfriend_Meeting_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Meeting_update_view(client):
    users_list = test_helpers.create_User()
    category_id = test_helpers.create_sportfriend_SportCategory()
    instance = test_helpers.create_sportfriend_Meeting()
    url = reverse("sportfriend_Meeting_update", args=[instance.pk, ])
    data = {
        "loaction_name": "text",
        "longitude": 1.0f,
        "date_start": datetime.now(),
        "description": "text",
        "date_end": datetime.now(),
        "is_private": True,
        "latitude": 1.0f,
        "users_list": users_list.pk,
        "category_id": category_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Message_list_view(client):
    instance1 = test_helpers.create_sportfriend_Message()
    instance2 = test_helpers.create_sportfriend_Message()
    url = reverse("sportfriend_Message_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Message_create_view(client):
    user_id = test_helpers.create_User()
    chat_id = test_helpers.create_sportfriend_Chat()
    url = reverse("sportfriend_Message_create")
    data = {
        "body": "text",
        "user_id": user_id.pk,
        "chat_id": chat_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Message_detail_view(client):
    instance = test_helpers.create_sportfriend_Message()
    url = reverse("sportfriend_Message_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Message_update_view(client):
    user_id = test_helpers.create_User()
    chat_id = test_helpers.create_sportfriend_Chat()
    instance = test_helpers.create_sportfriend_Message()
    url = reverse("sportfriend_Message_update", args=[instance.pk, ])
    data = {
        "body": "text",
        "user_id": user_id.pk,
        "chat_id": chat_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_News_list_view(client):
    instance1 = test_helpers.create_sportfriend_News()
    instance2 = test_helpers.create_sportfriend_News()
    url = reverse("sportfriend_News_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_News_create_view(client):
    user_id = test_helpers.create_User()
    images_many = test_helpers.create_sportfriend_Images()
    url = reverse("sportfriend_News_create")
    data = {
        "name": "text",
        "main_image": "aFile",
        "description": "text",
        "user_id": user_id.pk,
        "images_many": images_many.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_News_detail_view(client):
    instance = test_helpers.create_sportfriend_News()
    url = reverse("sportfriend_News_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_News_update_view(client):
    user_id = test_helpers.create_User()
    images_many = test_helpers.create_sportfriend_Images()
    instance = test_helpers.create_sportfriend_News()
    url = reverse("sportfriend_News_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "main_image": "aFile",
        "description": "text",
        "user_id": user_id.pk,
        "images_many": images_many.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SportCategory_list_view(client):
    instance1 = test_helpers.create_sportfriend_SportCategory()
    instance2 = test_helpers.create_sportfriend_SportCategory()
    url = reverse("sportfriend_SportCategory_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SportCategory_create_view(client):
    url = reverse("sportfriend_SportCategory_create")
    data = {
        "name": "text",
        "sport_icon": "aFile",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SportCategory_detail_view(client):
    instance = test_helpers.create_sportfriend_SportCategory()
    url = reverse("sportfriend_SportCategory_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SportCategory_update_view(client):
    instance = test_helpers.create_sportfriend_SportCategory()
    url = reverse("sportfriend_SportCategory_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "sport_icon": "aFile",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SportFriends_list_view(client):
    instance1 = test_helpers.create_sportfriend_SportFriends()
    instance2 = test_helpers.create_sportfriend_SportFriends()
    url = reverse("sportfriend_SportFriends_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SportFriends_create_view(client):
    user_fr_id = test_helpers.create_User()
    user_id = test_helpers.create_User()
    url = reverse("sportfriend_SportFriends_create")
    data = {
        "is_confirm": True,
        "user_fr_id": user_fr_id.pk,
        "user_id": user_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SportFriends_detail_view(client):
    instance = test_helpers.create_sportfriend_SportFriends()
    url = reverse("sportfriend_SportFriends_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SportFriends_update_view(client):
    user_fr_id = test_helpers.create_User()
    user_id = test_helpers.create_User()
    instance = test_helpers.create_sportfriend_SportFriends()
    url = reverse("sportfriend_SportFriends_update", args=[instance.pk, ])
    data = {
        "is_confirm": True,
        "user_fr_id": user_fr_id.pk,
        "user_id": user_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_UserChat_list_view(client):
    instance1 = test_helpers.create_sportfriend_UserChat()
    instance2 = test_helpers.create_sportfriend_UserChat()
    url = reverse("sportfriend_UserChat_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_UserChat_create_view(client):
    user_id = test_helpers.create_User()
    chat_id = test_helpers.create_sportfriend_Chat()
    url = reverse("sportfriend_UserChat_create")
    data = {
        "user_id": user_id.pk,
        "chat_id": chat_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_UserChat_detail_view(client):
    instance = test_helpers.create_sportfriend_UserChat()
    url = reverse("sportfriend_UserChat_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_UserChat_update_view(client):
    user_id = test_helpers.create_User()
    chat_id = test_helpers.create_sportfriend_Chat()
    instance = test_helpers.create_sportfriend_UserChat()
    url = reverse("sportfriend_UserChat_update", args=[instance.pk, ])
    data = {
        "user_id": user_id.pk,
        "chat_id": chat_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_UserInfo_list_view(client):
    instance1 = test_helpers.create_sportfriend_UserInfo()
    instance2 = test_helpers.create_sportfriend_UserInfo()
    url = reverse("sportfriend_UserInfo_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_UserInfo_create_view(client):
    user_id = test_helpers.create_User()
    sport_categories_list = test_helpers.create_sportfriend_SportCategory()
    images_list = test_helpers.create_sportfriend_Images()
    meetings_list = test_helpers.create_sportfriend_Meeting()
    url = reverse("sportfriend_UserInfo_create")
    data = {
        "find_area": 1.0f,
        "second_name": "text",
        "latitude": 1.0f,
        "description": "text",
        "profile_photo": "aFile",
        "birthday": datetime.now(),
        "longitude": 1.0f,
        "user_id": user_id.pk,
        "sport_categories_list": sport_categories_list.pk,
        "images_list": images_list.pk,
        "meetings_list": meetings_list.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_UserInfo_detail_view(client):
    instance = test_helpers.create_sportfriend_UserInfo()
    url = reverse("sportfriend_UserInfo_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_UserInfo_update_view(client):
    user_id = test_helpers.create_User()
    sport_categories_list = test_helpers.create_sportfriend_SportCategory()
    images_list = test_helpers.create_sportfriend_Images()
    meetings_list = test_helpers.create_sportfriend_Meeting()
    instance = test_helpers.create_sportfriend_UserInfo()
    url = reverse("sportfriend_UserInfo_update", args=[instance.pk, ])
    data = {
        "find_area": 1.0f,
        "second_name": "text",
        "latitude": 1.0f,
        "description": "text",
        "profile_photo": "aFile",
        "birthday": datetime.now(),
        "longitude": 1.0f,
        "user_id": user_id.pk,
        "sport_categories_list": sport_categories_list.pk,
        "images_list": images_list.pk,
        "meetings_list": meetings_list.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
