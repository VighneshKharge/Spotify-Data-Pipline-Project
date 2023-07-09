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
   2. Create Environment variables for 'client_id' & 'client_secret'
      (As to use this sensitive info directly into code is advisable).

   3. Add IAM Role which allows lambda to write data to the s3 bucket by going to permission.

    
   

 **Deploying Transformation Code in AWS Lambda for extracted data**

 - From extracted data of the playlist, information about the song, album & artist needs to be extracted.

 - In this code, data is converted from JSON format to csv & it is stored in an S3 bucket. Refer Spotify-Data-Pipeline-Project.ipynb

 - Note:
  1. In configuration --> change Timeout to 1 min as by default it is 3 sec.
  2. In Permission --> Add IAM Role to allow lambda to access S3 Bucket

  3. In layers add  'AWSSDKPandas-Python38'
 

 

 
 
   
    
  

  
