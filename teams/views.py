from django.shortcuts import render
from rest_framework.views import APIView, Response, Request
from django.forms.models import model_to_dict
from teams.models import Team

# Create your views here.


class TeamView(APIView):
    def post(self, request: Request):
        team = Team.objects.create(**request.data)
        return Response(model_to_dict(team), 201)

    def get(self, request: Request):
        teams_dict = [
            model_to_dict(team)
            for team in Team.objects.all()
        ]

        return Response(teams_dict, 201)
