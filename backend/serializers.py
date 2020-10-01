from rest_framework import serializers
from .models import  Tag, Video, VideoPlayList, TagDetail


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDetail
        fields = ['id', 'name', 'detail']


class VideoSerializer(serializers.ModelSerializer):
    tag_type = TagDetailSerializer(read_only=True)
    class Meta:
        model = Video
        fields = ['id', 'name', 'video', 'tag_type']



class TagSerializer(serializers.ModelSerializer):
    tagdetail_set = TagDetailSerializer(many=True, required=False)
    class Meta:
        model = Tag
        fields = ['id', 'name', 'tagdetail_set']



class VideoPlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPlayList
        fields = ['id', 'name', 'video']

