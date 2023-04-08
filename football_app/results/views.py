import datetime
from django.shortcuts import render, redirect

from . import sportmonks_session


def index(request):
    return redirect("/results/")


def results(request):
    # start api session
    sm = sportmonks_session.start_session()

    # http request fields
    base_url = "https://api.sportmonks.com/v3/football/schedules/seasons/19686"

    # http request
    # r = sm.get(url=base_url, params=query_string_params)
    r = sm.get(url=base_url)
    print(r.url)
    print(r.status_code)

    # current date and time
    current_date_unformatted = datetime.datetime.now()
    current_date = current_date_unformatted.strftime("%Y-%m-%d %x")

    # page data dictionary
    context = {
        "results": r.json()["data"],
        "datetime": current_date
    }

    return render(request, "results/results.html", context)

