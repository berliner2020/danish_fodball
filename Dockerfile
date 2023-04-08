FROM python:3.11-buster
LABEL "title"="fodball app" \
        "maintainer"="Jeremy Lykken" \
        "version"="0.1" \
        "description"="A django soccer app"
EXPOSE 8080
WORKDIR /fodball
COPY requirements.txt /fodball
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /fodball
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8080"]