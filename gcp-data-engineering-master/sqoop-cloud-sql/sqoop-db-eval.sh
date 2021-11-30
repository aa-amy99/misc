#!/bin/bash

bucket="gs://amy_data_etl"

#pwd_file=$bucket/sqoop-pwd/pwd.txt

cluster_name="ephemeral-spark-cluster-20211120"

gcloud dataproc jobs submit hadoop \
--cluster=$cluster_name --region=us-central1 \
--class=org.apache.sqoop.Sqoop \
--jars=$bucket/sqoop_jars/sqoop_sqoop-1.4.7.jar,file:///usr/share/java/mysql-connector-java-5.1.49.jar \
-- eval \
-Dmapreduce.job.user.classpath.first=true \
--driver com.mysql.jdbc.Driver \
--connect="jdbc:mysql://localhost:3307/airport" \
--username=root --password-file=$pwd_file \
--query "select count(*) from flights limit 10"
