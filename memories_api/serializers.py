from rest_framework import serializers
from memories_api import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['id', 'tag']


class MemorySerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tag'
    )

    class Meta: 
        model = models.Memory
        fields = ['id', 'title', 'description', 'photo', 'date', 'tags']
