from channels.consumer import SyncConsumer


class sportfriendConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass