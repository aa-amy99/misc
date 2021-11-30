gcloud dataproc clusters create spark-etl \
 --scopes=default \
 --optional-components=ZOOKEEPER,ANACONDA,JUPYTER \
 --region "us-east1" --zone "us-east1-b" \
 --master-machine-type n1-standard-2 \
 --master-boot-disk-size 200 \
  --num-workers 2 \
--worker-machine-type n1-standard-2 \
--worker-boot-disk-size 200 \
--image-version 1.3