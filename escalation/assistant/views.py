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
        pid = serializer.data['id']
        for cnt in range(4):
            engineer = self.request.data['engineer']
            title = self.request.data['title'] + 'S' + str(cnt+1)
            stageTemplateData = {
                'engineer': engineer,
                'title': title,
                'status': 'OG',
                'commitee_num': 1,
            }
            stg_serializer = StageSerializer(data=stageTemplateData)
            stg_serializer.is_valid()
            stg_serializer.save()

            sid = stg_serializer.data['id']
            plsTemplateData = {
                'process': pid,
                'stage': sid
            }
            pls_serializer = ProcessLinkStageSerializer(data = plsTemplateData)
            pls_serializer.is_valid()
            pls_serializer.save()
            cmt_num = stageTemplateData['commitee_num']
            for cnt1 in range(cmt_num):
                cmtTemplateData = {
                    'engineer': engineer,
                    'stageTitle': title,
                    'result': 'OG',
                    'comment_text': "TBD",
                }
                cmt_serializer = CommentSerializer(data = cmtTemplateData)
                cmt_serializer.is_valid()
                cmt_serializer.save()
                cid = cmt_serializer.data['id']
                slcTemplateData = {
                    'stage': sid,
                    'comment':cid
                }
                slc_serializer = StageLinkCommentSerializer(data = slcTemplateData)
                slc_serializer.is_valid()
                slc_serializer.save()


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
