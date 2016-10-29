#!/bin/bash
docker run -t -i -P -d \
    --name electroinv_postgres \
    -e POSTGRES_DB=electroinv \
    -e POSTGRES_USER=electroinv \
    -e POSTGRES_PASSWORD=password \
    postgres:9.2