FROM python:3.6.1-onbuild
COPY . /usr/src/app
ENV SQUASH_CUSTOM_VAR1=$SQUASH_CUSTOM_VAR1
CMD ["python", "server.py"]
