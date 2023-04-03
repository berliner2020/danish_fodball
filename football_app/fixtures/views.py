from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from . import sportmonks_session
import datetime


def index(request):
    return redirect("/fixtures/today")


def fixtures(request):
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
        "fixtures": r.json()["data"],
        "datetime": current_date
    }

    return render(request, "fixtures/fixtures.html", context)


def scores_by_timestamp(request, timestamp):  # TODO(jeremy) this does not work as expected yet
    current_date_unformatted = datetime.datetime.now()
    current_date = current_date_unformatted.strftime("%Y%m%d")
    print(timestamp)
    print(current_date)

    if current_date:
        redirect_path = reverse("fixtures", args=["today"])
        # return HttpResponseRedirect("/fixtures/today")
        return render(request, "fixtures/fixtures.html")
    else:
        return HttpResponseNotFound(
            "<h1>404 - Sorry, no fixtures can be returned for this date. \
                                    Try searching for yesterday, today, or tomorrow instead</h1>"
        )


def scores_by_word(request, date_word):
    # start api session
    sm = sportmonks_session.start_session()

    # http request fields
    base_url = "https://api.sportmonks.com/v3/football/seasons/19686"
    query_string_params = {"include": "fixtures"}

    # http request
    r = sm.get(url=base_url, params=query_string_params)
    print(r.url)
    print(r.status_code)

    # page data dictionary
    context = {
        "date": date_word,
        "results": r.json()["data"]
    }

    if date_word == "today" or date_word == "tomorrow" or date_word == "yesterday":
        return render(request, "fixtures/fixtures.html", context)
    else:
        return HttpResponseNotFound(
            "<h1>404 - Sorry, no fixtures can be returned for this date. \
                                    Try searching for yesterday, today, or tomorrow instead</h1>"
        )
