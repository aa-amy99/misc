template_name="flights_etl"
cluster_name="spark-job"
current_date=$(date +"%Y-%m-%d")
bucket=gs://amy_data_etl

gcloud dataproc workflow-templates delete -q $template_name --region "us-east1" &&

gcloud beta dataproc workflow-templates create $template_name --region "us-east1" &&

gcloud beta dataproc workflow-templates set-managed-cluster $template_name \
--cluster-name=$cluster_name \
--region "us-east1" --zone "us-east1-b" \
 --scopes=default \
 --master-machine-type n1-standard-2 \
 --master-boot-disk-size 20 \
  --num-workers 2 \
--worker-machine-type n1-standard-2 \
--worker-boot-disk-size 20 \
--image-version 1.3 &&

gcloud dataproc workflow-templates \
 add-job pyspark $bucket/spark-job/pyspark-fight-etl.py \
--step-id flight_delays_etl \
--workflow-template=$template_name \
--region "us-east1" &&

gcloud beta dataproc workflow-templates instantiate $template_name --region "us-east1" && 

bq load --source_format=NEWLINE_DELIMITED_JSON --autodetect \
 data_analysis.avg_delays_by_distance \
 $bucket/flights_data_output/${current_date}"_distance_category/*.json" &&

 bq load --source_format=NEWLINE_DELIMITED_JSON --autodetect \
 data_analysis.avg_delays_by_flight_nums \
 $bucket/flights_data_output/${current_date}"_flight_nums/*.json"


