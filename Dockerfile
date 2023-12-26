FROM python:3.11.5

SHELL '/bin/bash' '-c'
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev

RUN useradd -rms /bin/bash DikosAs && chmod 777 /opt /run

WORKDIR /DikosAs

RUN mkdir /DikosAs/static && mkdir /DikosAs/media && chown -R DikosAs:DikosAs /DikosAs && chmod 755 /DicosAs

COPY --chown=DiksoAs:DokosAs . .

#RUN