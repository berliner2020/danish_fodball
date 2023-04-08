from django.shortcuts import render, redirect

from . import sportmonks_session_tables


def index(request):
    return redirect("/stats")


def stats(request):
    sm = sportmonks_session_tables.start_session()

    # http request fields
    base_url = "https://api.sportmonks.com/v3/football/seasons/19686"
    query_string_params = {"include": "statistics.type"}

    # http request
    r = sm.get(url=base_url, params=query_string_params)
    print(r.url)
    print(r.status_code)

    # page data dictionary
    context = {
        "statistics": r.json()["data"]
    }

    return render(request, "stats/stats.html", context)

