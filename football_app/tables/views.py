from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from . import sportmonks_session_tables
import datetime


def index(request):
    return redirect("/tables")


def tables(request):
    sm = sportmonks_session_tables.start_session()

    # http request fields
    base_url = "https://api.sportmonks.com/v3/football/standings/seasons/19686"
    query_string_params = {"include": "participant"}

    # http request
    r = sm.get(url=base_url, params=query_string_params)
    print(r.url)
    print(r.status_code)

    print(r.json())

    # clean API tables data
    table_data = {}

    for row in r.json()["data"]:
        table_data[row["participant_id"]] = row

    # print(table_data.keys())
    # print(table_data.values())

    # page data dictionary
    context = {
        "tables": table_data.values()
    }

    return render(request, "tables/tables.html", context)

