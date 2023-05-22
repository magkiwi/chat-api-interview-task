from rest_framework import serializers

from chat.models import Conversation


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            "id",
            "user_question",
            "bot_answer",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
