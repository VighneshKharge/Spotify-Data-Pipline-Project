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

  
