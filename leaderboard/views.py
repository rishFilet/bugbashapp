from django.shortcuts import render

from bugreport.models import BugLogStructure
from .models import Leaderboard
from .tables import LeaderBoardTable


# Create your views here.
def leaderboard_list(request):
    bug_data = BugLogStructure.objects.all()
    print(request.user.first_name)
    table = LeaderBoardTable(Leaderboard.objects.all())

    return render(request, "leaderboard.html", {
        "table": table
    })
