import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from chat.models import QuestionAnswer, Conversation

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()
   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        clean_message = self._clean_string(message)

        answer = QuestionAnswer.objects.filter(qText=clean_message).first()

        if answer:
            bot_answer = ', '.join(map(str, answer.answers))
        else: 
            bot_answer = 'More information in Potato Chat Premium!'

        conversation = Conversation(user_question=message, bot_answer=bot_answer)
        conversation.save()


        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_messages',
                'id': conversation.pk,
                'user_question': conversation.user_question,
                'bot_answer': conversation.bot_answer,
                'created_at': str(conversation.created_at)
            }
        )

    def chat_messages(self, event):

        self.send(text_data=json.dumps({
            'id': event['id'],
            'user_question': event['user_question'],
            'bot_answer':  event['bot_answer'],
            'created_at':  event['created_at'],
        }))

    def _clean_string(self, message):
        clean_message = " ".join(message.split()).lower()
        return clean_message
        


