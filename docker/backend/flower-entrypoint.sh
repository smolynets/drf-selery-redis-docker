#!/bin/sh

until cd /app/backend
do
    echo "Waiting for flower..."
done

# run a flower :)
celery  -A backend flower
