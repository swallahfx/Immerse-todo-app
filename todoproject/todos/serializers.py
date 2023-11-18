from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user', 'title', 'description', 'created_at', 'updated_at')

    def validate_user(self, value):
        """
        Check if the user associated with the to-do item is the request user.
        """
        request = self.context.get('request')
        if value != request.user:
            raise serializers.ValidationError("User mismatch. You can only create to-do items for yourself.")
        return value
