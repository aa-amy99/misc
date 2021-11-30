gcloud dataproc clusters create kafka-etl \
 --scopes=default \
 --region "us-east1" --zone "us-east1-b" \
 --initialization-actions=gs://amy_data_etl/dataproc_init-action/zookeeper/zookeeper.sh,gs://amy_data_etl/dataproc_init-action/kafka/kafka.sh \
 --master-machine-type n1-standard-2 \
 --master-boot-disk-size 200 \
  --num-workers 2 \
--worker-machine-type n1-standard-2 \
--worker-boot-disk-size 200 \
--image-version 1.3