from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from . import sportmonks_session
import datetime


def index(request):
    response_data = render_to_string("scores/scores.html")
    return HttpResponse(response_data)


def scores_by_timestamp(request, timestamp):  # TODO(jeremy) this does not work as expected yet
    current_date_unformatted = datetime.datetime.now()
    current_date = current_date_unformatted.strftime("%Y%m%d")
    print(timestamp)
    print(current_date)

    if current_date:
        redirect_path = reverse("fixtures", args=["today"])
        # return HttpResponseRedirect("/scores/today")
        return render(request, "scores/scores.html")
    else:
        return HttpResponseNotFound(
            "<h1>404 - Sorry, no scores can be returned for this date. \
                                    Try searching for yesterday, today, or tomorrow instead</h1>"
        )


def scores_by_word(request, date_word):
    # start api session
    sm = sportmonks_session.start_session()

    # http request fields
    base_url = "https://api.sportmonks.com/v3/football/fixtures"

    # http request
    r = sm.get(url=base_url)
    print(r.status_code)

    if date_word == "today" or date_word == "tomorrow" or date_word == "yesterday":
        return render(request, "scores/scores.html")
        # return HttpResponse(f"<h1>Scores for {date_word}: {r.json()}!</h1>")
    else:
        return HttpResponseNotFound(
            "<h1>404 - Sorry, no scores can be returned for this date. \
                                    Try searching for yesterday, today, or tomorrow instead</h1>"
        )
