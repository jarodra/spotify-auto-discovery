FROM python:3.8-alpine
ENV CRON_SPEC="0 8 * * 1"
WORKDIR app
COPY app/ .
RUN pip3 install -r requirements.txt
RUN echo "${CRON_SPEC} python3 main.py" >> crontab
RUN crontab crontab
CMD ["crond", "-f"]