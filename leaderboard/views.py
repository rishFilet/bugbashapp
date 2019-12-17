from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django_tables2 import RequestConfig

from accounts.models import CustomUser
from bugreport.models import BugLogStructure, Features
from .models import Leaderboard
from .tables import LeaderBoardTable


# Create your views here.
def leaderboard_list(request):
    # all_entries_ranked = Leaderboard.objects.order_by('total')
    clear_leaderboard()
    update_lb()
    table = LeaderBoardTable(Leaderboard.objects.all())
    table.order_by = 'rank'
    RequestConfig(request).configure(table)

    return render(request, "leaderboard.html", {
        "table": table
    })


def update_lb():
    all_users = CustomUser.objects.all()
    temp_rank = 0
    for user in all_users:
        temp_rank = temp_rank + 1
        print(user.user_uuid)
        bug_count = BugLogStructure.objects.filter(user_id = user.user_uuid).count()
        try:
            e = Leaderboard.objects.get(first_name = user.first_name, last_name = user.last_name)
            print(e)
        except ObjectDoesNotExist:
            u = Leaderboard.objects.create(first_name = user.first_name, last_name = user.last_name,
                                           rank = temp_rank)
            u.save()
        Leaderboard.objects.filter(first_name = user.first_name, last_name =
        user.last_name).update(total = bug_count)
        update_features_count(user)

    update_rank(Leaderboard.objects)


def update_rank(entries):
    entries_list = list(entries.order_by('-total'))
    objs = []
    for e in entries_list:
        try:
            objs.append(entries.get(first_name = e.first_name, last_name = e.last_name))
        except:
            print("User does not exist to update rank")
    for obj in objs:
        obj.rank = objs.index(obj) + 1
    entries.bulk_update(objs, ['rank'])
    print(entries.all())


def update_features_count(user):
    features_list = [Features.IRIS, Features.SENSORS, Features.ECO, Features.IRIS,
                     Features.THEIA, Features.LS, Features.TSTAT]
    for feature in features_list:
        bug_count = BugLogStructure.objects.filter(user_id = user.user_uuid, feature =
        feature).count()
        if feature == "Camera":
            Leaderboard.objects.filter(first_name = user.first_name, last_name =
            user.last_name).update(Camera = bug_count)
        if feature == "Tstat":
            Leaderboard.objects.filter(first_name = user.first_name, last_name =
            user.last_name).update(Tstat = bug_count)
        if feature == "Sensors":
            Leaderboard.objects.filter(first_name = user.first_name, last_name =
            user.last_name).update(Sensors = bug_count)
        if feature == "Ls":
            Leaderboard.objects.filter(first_name = user.first_name, last_name =
            user.last_name).update(Ls = bug_count)
        if feature == "Eco_plus":
            Leaderboard.objects.filter(first_name = user.first_name, last_name =
            user.last_name).update(Eco_plus = bug_count)
        if feature == "Iris":
            Leaderboard.objects.filter(first_name = user.first_name, last_name =
            user.last_name).update(Iris = bug_count)
        

def clear_leaderboard():
    Leaderboard.objects.all().delete()
