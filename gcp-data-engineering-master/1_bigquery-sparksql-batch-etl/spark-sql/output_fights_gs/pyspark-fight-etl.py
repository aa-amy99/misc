
# coding: utf-8

# In[1]:


import pyspark 
from pyspark import SparkContext


# In[2]:


from pyspark.sql import SQLContext
from pyspark.conf import SparkConf
from pyspark.sql.session import SparkSession


# In[4]:


sc = SparkContext()



# # Extract

# In[5]:


spark = SQLContext(sc)


# In[23]:


flights_data = spark.read.json("gs://amy_data_etl/fight-data/2019-05-06.json") #df


# In[24]:


flights_data.registerTempTable("flights_data")#to run sql


# ## Understand data

# In[25]:


# spark.sql("select * from flights_data limit 10").show()


# In[26]:


# spark.sql("select distinct flight_num from flights_data" ).show()


# In[27]:


# spark.sql("select count(*) from flights_data" ).show()


# In[28]:


# spark.sql("select max(distance) from flights_data limit 10").show()


# # Transform

# ## 1. find average delay by fight number and date

# In[29]:


qry = """
        select 
            flight_date , 
            round(avg(arrival_delay),2) as avg_arrival_delay,
            round(avg(departure_delay),2) as avg_departure_delay,
            flight_num 
        from 
            flights_data 
        group by 
            flight_num , 
            flight_date 
      """


# In[30]:


avg_delays_by_flight_nums = spark.sql(qry)


# In[32]:


# avg_delays_by_flight_nums.show()


# ## 2. find average delay by distance (1196 values, so you need to bucket them)

# In[33]:


# spark.sql("select count(distinct distance) from flights_data").show()


# In[34]:


# spark.sql("select max(distance) from flights_data limit 10").show()


# ## 2.1 bucket them and save it to new coloumn

# In[37]:


qry = """
        select 
            *,
            case 
                when distance between 0 and 500 then 1 
                when distance between 501 and 1000 then 2
                when distance between 1001 and 2000 then 3
                when distance between 2001 and 3000 then 4 
                when distance between 3001 and 4000 then 5 
                when distance between 4001 and 5000 then 6 
            END distance_category 
        from 
            flights_data 
        """


# In[39]:


# spark.sql(qry).show(5)


# ## 2.2 add distance_category to original dataset and register for table

# In[40]:


# add distance_category to original dataset
flights_data = spark.sql(qry)


# In[42]:


flights_data.registerTempTable("flights_data")


# ## 2.3 calculate average

# In[43]:


# calculate average
qry = """
        select 
            flight_date , 
            round(avg(arrival_delay),2) as avg_arrival_delay,
            round(avg(departure_delay),2) as avg_departure_delay,
            distance_category 
        from 
            flights_data 
        group by 
            distance_category , 
            flight_date 
      """


# spark.sql(qry).show()
avg_delays_by_distance_category = spark.sql(qry)


# In[44]:


# avg_delays_by_distance_category.show()


# # Load to Bucket with timestamp

# In[45]:


from datetime import date 
current_date = date.today()
file_name = str(current_date)


# In[53]:


bucket_name = "gs://amy_data_etl"
output_flight_nums = bucket_name+"/flights_data_output/"+file_name+"_flight_nums"
output_distance_category = bucket_name+"/flights_data_output/"+file_name+"_distance_category"

avg_delays_by_flight_nums.coalesce(1).write.format("json").save(output_flight_nums)
avg_delays_by_distance_category.coalesce(1).write.format("json").save(output_distance_category)


# In[48]:


# output_flight_nums


# In[49]:


# output_distance_category

