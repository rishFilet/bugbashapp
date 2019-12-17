from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Leaderboard
from .tables import LeaderBoardTable


# Create your views here.
def leaderboard_list(request):
    table = LeaderBoardTable(Leaderboard.objects.all())
    table.order_by = "rank"
    RequestConfig(request).configure(table)

    return render(request, "leaderboard.html", {
        "table": table
    })


def update_lb(request):
    total = Leaderboard.objects.get(first_name = request.user.first_name,
                                    last_name = request.user.last_name).total + 1
    data = {"total": total}
    obj, created = Leaderboard.objects.update_or_create(first_name = request.user.first_name,
                                                        last_name = request.user.last_name,
                                                        defaults = data)
    print(obj, created)
