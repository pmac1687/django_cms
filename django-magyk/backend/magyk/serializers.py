from rest_framework import serializers
from .models import Article, Cards, MarketSegments, Project



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'header',
            'created',
            'updated',
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
            'description',

        )
        model = MarketSegments

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'content',
            'image',
            'introduction',
            'industry',
            '_type',
            'platforms',
            'duration',
            'challenge',
            'step1',
            'step2',
            'step3',
            'step4',
            'solution',

        )
        model = Project