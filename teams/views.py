from django.shortcuts import render
from rest_framework.views import APIView, Response, Request
from django.forms.models import model_to_dict
from teams.models import Team
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError

# Create your views here.


class TeamView(APIView):
    def post(self, request: Request):
        try:
            data_processing(request.data)

        except NegativeTitlesError as error:
            return Response({"error": error.message}, 400)

        except InvalidYearCupError as error:
            return Response({"error": error.message}, 400)

        except ImpossibleTitlesError as error:
            return Response({"error": error.message}, 400)

        team = Team.objects.create(**request.data)

        return Response(model_to_dict(team), 201)

    def get(self, request: Request):
        teams_dict = [
            model_to_dict(team)
            for team in Team.objects.all()
        ]

        return Response(teams_dict, 200)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team_dict = model_to_dict(team)

        return Response(team_dict, 200)

    def delete(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team.delete()

        return Response(status=204)

    def patch(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        for key, value in request.data.items():
            if key != "id":
                setattr(team, key, value)
        team.save()

        team_dict = model_to_dict(team)

        return Response(team_dict, 200)

