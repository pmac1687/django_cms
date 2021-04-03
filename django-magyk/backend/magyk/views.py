from rest_framework import generics

from .models import Article, Cards, MarketSegments, Project
from .serializers import ArticleSerializer, CardsSerializer, MarketSegmentsSerializer, ProjectSerializer



class ListArticle(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailArticle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListCards(generics.ListCreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer


class DetailCards(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

class ListMarketSegments(generics.ListCreateAPIView):
    queryset = MarketSegments.objects.all()
    serializer_class = MarketSegmentsSerializer


class DetailMarketSegments(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketSegments.objects.all()
    serializer_class = MarketSegmentsSerializer

class ListProject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DetailProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer