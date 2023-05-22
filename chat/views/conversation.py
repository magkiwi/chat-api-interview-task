from chat.serializers.conversation import ConversationSerializer
from chat.models import Conversation
from rest_framework import viewsets


class ConversationViewSet(viewsets.ModelViewSet):

    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
        
