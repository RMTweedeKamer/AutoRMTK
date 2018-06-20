FROM python:3.6.5-alpine

RUN function forever() { while true; do $@; done; }

CMD ["forever", "python", "main.py"]
