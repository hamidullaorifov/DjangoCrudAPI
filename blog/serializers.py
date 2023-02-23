from rest_framework.serializers import ModelSerializer

from .models import Blog




class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','description','thumbnail']


class BlogGetSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','description','thumbnail']