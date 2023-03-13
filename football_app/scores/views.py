from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from . import sportmonks_session


def today(request):
    return HttpResponse(f"Hello, World for TODAY!")


def scores(request, date):
    if date:
        # start api session
        sm = sportmonks_session.start_session()

        # http request fields
        base_url = "https://api.sportmonks.com/v3/football/fixtures"

        # http request
        r = sm.get(url=base_url)
        print(r.status_code)

        return HttpResponse(f"Scores for {date}: {r.json()}!")
    else:
        return HttpResponseNotFound("404 - Sorry, no scores for this date. Try another date")


