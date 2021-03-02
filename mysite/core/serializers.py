# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import get_object_or_404
from core.models import MessageModel
from rest_framework.serializers import ModelSerializer, CharField
from webaccount.models import Client_Personal_Info



class MessageModelSerializer(ModelSerializer):
    user = CharField(source='user.username', read_only=True)
    recipient = CharField(source='recipient.Email')

    def create(self, validated_data):
        user = self.context['request'].user
        recipient = get_object_or_404(
            Client_Personal_Info, Email=validated_data['recipient']['Email'])
        msg = MessageModel(recipient=recipient,
                           body=validated_data['body'],
                           user=user)
        msg.save()
        return msg

    class Meta:
        model = MessageModel
        fields = ('id', 'user', 'recipient', 'timestamp', 'body')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = Client_Personal_Info
        fields = ('Email',)
