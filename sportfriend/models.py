from django.db import models
from django.urls import reverse
import uuid

class Chat(models.Model):

    # Fields
    new_messages = models.IntegerField(null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("sportfriend_Chat_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_Chat_update", args=(self.pk,))



class Images(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    filePath = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    is_private = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_Images_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_Images_update", args=(self.pk,))



class LogErrors(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    error_time = models.DateTimeField(null=True)
    user_id = models.BigIntegerField(null=True)
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.TextField(blank=True)
    error_uuid = models.TextField(blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_LogErrors_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_LogErrors_update", args=(self.pk,))



class Meeting(models.Model):

    # Relationships
    users_list = models.ManyToManyField("auth.User")
    category_id = models.ForeignKey("sportfriend.SportCategory", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    loaction_name = models.CharField(max_length=100)
    longitude = models.FloatField(null=True)
    date_start = models.DateTimeField(null=True)
    description = models.TextField(blank=True)
    date_end = models.DateTimeField(null=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    is_private = models.BooleanField(default=True)
    latitude = models.FloatField(null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_Meeting_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_Meeting_update", args=(self.pk,))



class Message(models.Model):

    # Relationships
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    chat_id = models.ForeignKey("sportfriend.Chat", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_Message_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_Message_update", args=(self.pk,))



class News(models.Model):

    # Relationships
    user_id = models.ForeignKey("auth.User", related_name="fk_user_id", on_delete=models.CASCADE)
    images_many = models.ManyToManyField("sportfriend.Images")
    liked_user_list = models.ManyToManyField("auth.User", related_name="mm_liked_user_list")

    # Fields
    name = models.CharField(max_length=100)
    main_image = models.FileField(upload_to="upload/files/")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("sportfriend_News_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_News_update", args=(self.pk,))



class SportCategory(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    sport_icon = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("sportfriend_SportCategory_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_SportCategory_update", args=(self.pk,))



class SportFriends(models.Model):

    # Relationships
    user_fr_id = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="user_fr_set")
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="user_set")

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_confirm = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_SportFriends_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_SportFriends_update", args=(self.pk,))



class UserChat(models.Model):

    # Relationships
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    chat_id = models.ForeignKey("sportfriend.Chat", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_UserChat_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_UserChat_update", args=(self.pk,))



class UserInfo(models.Model):

    # Relationships
    sport_categories_list = models.ManyToManyField("sportfriend.SportCategory")
    user_disliked_list = models.ManyToManyField("auth.User", related_name="user_disliked_list_many")
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    meetings_list = models.ManyToManyField("sportfriend.Meeting")
    images_list = models.ManyToManyField("sportfriend.Images")
    user_liked_list = models.ManyToManyField("auth.User", related_name="user_liked_list_many")

    # Fields
    profile_photo = models.FileField(upload_to="upload/files/")
    longitude = models.FloatField(null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(blank=True)
    second_name = models.CharField(max_length=50, null=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    find_area = models.FloatField(default=10.0)
    latitude = models.FloatField(null=True)
    birthday = models.DateTimeField(null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("sportfriend_UserInfo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("sportfriend_UserInfo_update", args=(self.pk,))

