FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends tmux asciinema ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY task.yaml solution.sh run-tests.sh data/ ./

RUN chmod +x /app/solution.sh /app/run-tests.sh
