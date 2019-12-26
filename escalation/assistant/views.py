from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .permissions import IsOwner

# Create your views here.
class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class HighLvlViewSet(viewsets.ModelViewSet):
    queryset = HighLvl.objects.all()
    serializer_class = HighLvlSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProcessLinkStageViewSet(viewsets.ModelViewSet):
    queryset = ProcessLinkStage.objects.all()
    serializer_class = ProcessLinkStageSerializer

class StageLinkCommentViewSet(viewsets.ModelViewSet):
    queryset = StageLinkComment.objects.all()
    serializer_class = StageLinkCommentSerializer

class MakeCommentOnViewSet(viewsets.ModelViewSet):
    queryset = MakeCommentOn.objects.all()
    serializer_class = MakeCommentOnSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
