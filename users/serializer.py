from rest_framework.serializers import ModelSerializer
from users.models import Core


class CoreSerializer(ModelSerializer):
    class Meta:
        model = Core
        fields = [
            'coins',
            'click_power'
        ]