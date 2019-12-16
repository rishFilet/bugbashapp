from django.shortcuts import render

from .models import Leaderboard
from .tables import LeaderBoardTable


# Create your views here.
def leaderboard_list(request):
    table = LeaderBoardTable(Leaderboard.objects.all())

    return render(request, "leaderboard.html", {
        "table": table
    })
