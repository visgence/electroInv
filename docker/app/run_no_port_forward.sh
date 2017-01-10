#!/bin/bash
ELECTROINV=$(cd $(dirname "${BASH_SOURCE[0]}")/../../ && pwd -P)
docker run -t -i -P \
    -v $ELECTROINV:/home/electroinv/electroinv \
    --link electroinv_postgres:pg \
    electroinv/app \
    bash
