from rest_framework.serializers import ModelSerializer
from base.models import Jobs


class JobSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
