from rest_framework import serializers
from .models import Article, Cards, MarketSegments, Project



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = Article


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'title',
            'tag',
            'color'
        )
        model = Cards


class MarketSegmentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'svg',

        )
        model = MarketSegments

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'content',
            'image',
            'background'

        )
        model = Project