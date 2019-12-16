import django_tables2 as tables

from .models import Leaderboard


class LeaderBoardTable(tables.Table):
    class Meta:
        model = Leaderboard
