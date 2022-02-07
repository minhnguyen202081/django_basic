from rest_framework import viewsets
from memories_api import  models,serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
class MemoryViewSet(viewsets.ModelViewSet):
     queryset = models.Memory.objects.all()
     serializer_class = serializers.MemorySerializer
     permission_classes=(IsAuthenticated,)
     authentication_classes=(TokenAuthentication,)
     filter_backends = (filters.SearchFilter,)
     search_fields=('title','tags__tag')
     def perform_create(self, serializer):
          serializer.save(owner=self.request.user)
class TagViewSet(viewsets.ModelViewSet):
     queryset = models.Tag.objects.all()
     serializer_class =  serializers.TagSerializer