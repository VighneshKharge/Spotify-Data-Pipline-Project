# Spotify-Data-Pipeline-Project
 
## Problem statement 
- Client wants to collect Top Global Songs on Spotify every week. Building an ETL(Extract Transform Load) pipeline for this problem.

## Introduction

- This whole project is executed on the AWS cloud Platform
  
- This project is executed in 3 phases. Phase-1 extracting data from Spotify API with AWS Lambda(Python) & storing it into an S3 bucket.
  
- Phase-2 Transformation as data will be in a JSON format Again using AWS lambda to transform data stored in the S3 bucket in phase-1 such as extracting required information from the data then saving it into a list & creating a dataframe from it and again saving it into CSV format to S3 Bucket.

- Phase-3 Loading data to a target location in this project transformed data is loaded into AWS Athena which is an analytics engine on AWS where we can run business queries on data.
  

  ## Architecture Diagram 

  ![This is architecture](https://github.com/VighneshKharge/Spotify-Data-Pipline-Project/blob/main/Architecture.png)

  ## Complete execution of Spotify data pipeline project

  **Create S3 Bucket with required folders to store extracted data & transformed data**

  ![S3 Buckets](https://github.com/VighneshKharge/Spotify-Data-Pipline-Project/blob/main/S3%20Folders.png)

  

 **Integrating with Spotify API & extracting data**
  - First Login/signup to developer.spotify.com & create a app to get Client id & Secret id.
  - Then refer Spotify-Data-Pipeline-Project.ipynb we will get data in JSON format (key, value pair). same code is being deployed on AWS Lambda & trigger is added to automate the extraction process. Extracted data is stored in an S3 bucket.
 
 - Note: while running extraction in layers add provided 'etl-spofify-layer'. Unzip spotify_layer.zip for the file.

 - And Before running the code do the necessary setting
1. In configuration --> change Timeout to 1 min as by default it is 3 sec.
2. Create Environment variables for 'client_id' & 'client_secret'(As to use this sensitive info directly into code is advisable).
3. Add IAM Role which allows lambda to write data to the s3 bucket by going to permission.

    
 **Deploying Transformation Code in AWS Lambda for extracted data**

 - From extracted data of the playlist, information about the song, album & artist needs to be extracted.

 - In this code, data is converted from JSON format to CSV & it is stored in an S3 bucket. Refer Data_Transformation_Code.py

 - Here trigger is added as soon as data gets into the target folder in the S3 transformation code will run as a result data Extraction & Transformation process is fully automated. 

 - Note:
  1. In configuration --> change Timeout to 1 min as by default it is 3 sec.
  2. In Permission --> Add IAM Role to allow lambda to access S3 Bucket
  3. In layers add  'AWSSDKPandas-Python38'

 **Creating tables from files stored in s3 using AWS Glue & AWS Athena**

- Using Glue Crawler, it will infer the schema of the data in this case three crawlers are created for the song_data, album_dta & artist_data folder but the database will the same.

- Using Glue Data Catalog which stores the metadata will help AWS Athena to create a table.

- In Athena, in the respective database we can see the tables created, now to avoid errors while running queries in Athena create a new S3 bucket & add it's path in Athena-->setting-->manage-->Give Newly created S3 Bucket Path. In this bucket Athena will store query results.
 
 

 
 
   
    
  

  
