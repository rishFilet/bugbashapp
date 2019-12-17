import django_tables2 as tables

from bugreport.models import Features
from .models import Leaderboard


class LeaderBoardTable(tables.Table):
    class Meta:
        model = Leaderboard
        fields = ('rank', 'first_name', 'last_name', Features.TSTAT, Features.LS, Features.THEIA,
                  Features.ECO, Features.SENSORS, Features.IRIS, 'total')
        attrs = {"class": "table", "thead": {"class": "thead-dark"}}
