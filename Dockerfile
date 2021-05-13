FROM python:3.6-buster
RUN apt-get update && apt-get upgrade -y
RUN mkdir -p /opt/app/tabibyab
COPY ./ /opt/app/tabibyab
WORKDIR /opt/app/tabibyab
#RUN /bin/bash -c "source ./venv/bin/activate"
RUN pip install -r requirement.txt
RUN chown -R www-data:www-data /opt/app/tabibyab/*
EXPOSE 8009
STOPSIGNAL SIGTERM
CMD ["python" , "./manage.py" , "runserver" , "0.0.0.0:8009"]


