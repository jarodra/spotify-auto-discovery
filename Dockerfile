FROM python:3.8-alpine
ENV PROJ_DIR="/app"
ENV LOG_FILE="${PROJ_DIR}/app.log"  
ENV CRON_SPEC="0 8 * * 1"
WORKDIR ${PROJ_DIR}
COPY . ${PROJ_DIR}
RUN pip3 install -r requirements.txt
RUN echo "${CRON_SPEC} python3 ${PROJ_DIR}/main.py" >> ${PROJ_DIR}/crontab
RUN crontab ${PROJ_DIR}/crontab
CMD ["crond", "-f"]
EXPOSE 8083