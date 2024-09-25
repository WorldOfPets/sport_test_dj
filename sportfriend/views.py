from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ChatListView(generic.ListView):
    model = models.Chat
    form_class = forms.ChatForm


class ChatCreateView(generic.CreateView):
    model = models.Chat
    form_class = forms.ChatForm


class ChatDetailView(generic.DetailView):
    model = models.Chat
    form_class = forms.ChatForm


class ChatUpdateView(generic.UpdateView):
    model = models.Chat
    form_class = forms.ChatForm
    pk_url_kwarg = "pk"


class ChatDeleteView(generic.DeleteView):
    model = models.Chat
    success_url = reverse_lazy("sportfriend_Chat_list")


class ImagesListView(generic.ListView):
    model = models.Images
    form_class = forms.ImagesForm


class ImagesCreateView(generic.CreateView):
    model = models.Images
    form_class = forms.ImagesForm


class ImagesDetailView(generic.DetailView):
    model = models.Images
    form_class = forms.ImagesForm


class ImagesUpdateView(generic.UpdateView):
    model = models.Images
    form_class = forms.ImagesForm
    pk_url_kwarg = "pk"


class ImagesDeleteView(generic.DeleteView):
    model = models.Images
    success_url = reverse_lazy("sportfriend_Images_list")


class LogErrorsListView(generic.ListView):
    model = models.LogErrors
    form_class = forms.LogErrorsForm


class LogErrorsCreateView(generic.CreateView):
    model = models.LogErrors
    form_class = forms.LogErrorsForm


class LogErrorsDetailView(generic.DetailView):
    model = models.LogErrors
    form_class = forms.LogErrorsForm


class LogErrorsUpdateView(generic.UpdateView):
    model = models.LogErrors
    form_class = forms.LogErrorsForm
    pk_url_kwarg = "pk"


class LogErrorsDeleteView(generic.DeleteView):
    model = models.LogErrors
    success_url = reverse_lazy("sportfriend_LogErrors_list")


class MeetingListView(generic.ListView):
    model = models.Meeting
    form_class = forms.MeetingForm


class MeetingCreateView(generic.CreateView):
    model = models.Meeting
    form_class = forms.MeetingForm


class MeetingDetailView(generic.DetailView):
    model = models.Meeting
    form_class = forms.MeetingForm


class MeetingUpdateView(generic.UpdateView):
    model = models.Meeting
    form_class = forms.MeetingForm
    pk_url_kwarg = "pk"


class MeetingDeleteView(generic.DeleteView):
    model = models.Meeting
    success_url = reverse_lazy("sportfriend_Meeting_list")


class MessageListView(generic.ListView):
    model = models.Message
    form_class = forms.MessageForm


class MessageCreateView(generic.CreateView):
    model = models.Message
    form_class = forms.MessageForm


class MessageDetailView(generic.DetailView):
    model = models.Message
    form_class = forms.MessageForm


class MessageUpdateView(generic.UpdateView):
    model = models.Message
    form_class = forms.MessageForm
    pk_url_kwarg = "pk"


class MessageDeleteView(generic.DeleteView):
    model = models.Message
    success_url = reverse_lazy("sportfriend_Message_list")


class NewsListView(generic.ListView):
    model = models.News
    form_class = forms.NewsForm


class NewsCreateView(generic.CreateView):
    model = models.News
    form_class = forms.NewsForm


class NewsDetailView(generic.DetailView):
    model = models.News
    form_class = forms.NewsForm


class NewsUpdateView(generic.UpdateView):
    model = models.News
    form_class = forms.NewsForm
    pk_url_kwarg = "pk"


class NewsDeleteView(generic.DeleteView):
    model = models.News
    success_url = reverse_lazy("sportfriend_News_list")


class SportCategoryListView(generic.ListView):
    model = models.SportCategory
    form_class = forms.SportCategoryForm


class SportCategoryCreateView(generic.CreateView):
    model = models.SportCategory
    form_class = forms.SportCategoryForm


class SportCategoryDetailView(generic.DetailView):
    model = models.SportCategory
    form_class = forms.SportCategoryForm


class SportCategoryUpdateView(generic.UpdateView):
    model = models.SportCategory
    form_class = forms.SportCategoryForm
    pk_url_kwarg = "pk"


class SportCategoryDeleteView(generic.DeleteView):
    model = models.SportCategory
    success_url = reverse_lazy("sportfriend_SportCategory_list")


class SportFriendsListView(generic.ListView):
    model = models.SportFriends
    form_class = forms.SportFriendsForm


class SportFriendsCreateView(generic.CreateView):
    model = models.SportFriends
    form_class = forms.SportFriendsForm


class SportFriendsDetailView(generic.DetailView):
    model = models.SportFriends
    form_class = forms.SportFriendsForm


class SportFriendsUpdateView(generic.UpdateView):
    model = models.SportFriends
    form_class = forms.SportFriendsForm
    pk_url_kwarg = "pk"


class SportFriendsDeleteView(generic.DeleteView):
    model = models.SportFriends
    success_url = reverse_lazy("sportfriend_SportFriends_list")


class UserChatListView(generic.ListView):
    model = models.UserChat
    form_class = forms.UserChatForm


class UserChatCreateView(generic.CreateView):
    model = models.UserChat
    form_class = forms.UserChatForm


class UserChatDetailView(generic.DetailView):
    model = models.UserChat
    form_class = forms.UserChatForm


class UserChatUpdateView(generic.UpdateView):
    model = models.UserChat
    form_class = forms.UserChatForm
    pk_url_kwarg = "pk"


class UserChatDeleteView(generic.DeleteView):
    model = models.UserChat
    success_url = reverse_lazy("sportfriend_UserChat_list")


class UserInfoListView(generic.ListView):
    model = models.UserInfo
    form_class = forms.UserInfoForm


class UserInfoCreateView(generic.CreateView):
    model = models.UserInfo
    form_class = forms.UserInfoForm


class UserInfoDetailView(generic.DetailView):
    model = models.UserInfo
    form_class = forms.UserInfoForm


class UserInfoUpdateView(generic.UpdateView):
    model = models.UserInfo
    form_class = forms.UserInfoForm
    pk_url_kwarg = "pk"


class UserInfoDeleteView(generic.DeleteView):
    model = models.UserInfo
    success_url = reverse_lazy("sportfriend_UserInfo_list")
