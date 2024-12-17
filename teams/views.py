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
