from rest_framework import serializers

from .models import AccountOwner


class AccountOwnerSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AccountOwner
        fields = (
            'id', 'email', 'password', 'is_staff',
            'is_active', 'date_joined')

    def create(self, validated_data):
        # TODO do i really need to do this?
        return AccountOwner.objects.create_user(**validated_data)
