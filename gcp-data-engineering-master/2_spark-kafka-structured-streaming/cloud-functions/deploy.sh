#!/bin/sh

FUNCTION="update_user_cart"
BUCKET="gs://amy_stream"

gcloud functions deploy ${FUNCTION} \
    --runtime python37 \
    --trigger-resource ${BUCKET} \
    --trigger-event google.storage.object.finalize
