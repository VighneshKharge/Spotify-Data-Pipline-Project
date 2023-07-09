import json
import os
from datetime import datetime
import boto3 
from io import StringIO    #for converting dataframe into string so, we can convert it into csv format
import pandas as pd 

def album(data): 

    album_list = []
    for row in data['items']:
        album_id = row['track']['album']['id']
        album_name = row['track']['album']['name']
        album_release_date = row['track']['album']['release_date']
        album_total_tracks = row['track']['album']['total_tracks']
        album_url = row['track']['album']['external_urls']['spotify']
        album_element = {'album_id':album_id,'name':album_name,'release_date':album_release_date,
                            'total_tracks':album_total_tracks,'url':album_url}
        album_list.append(album_element)
    return album_list
        
    
def artist(data):

    artist_list = []
    for row in data['items']:
        for key, value in row.items():
            if key == "track":
                for artist in value['artists']:
                    artist_dict = {'artist_id':artist['id'], 'artist_name':artist['name'], 'external_url': artist['href']}
                    artist_list.append(artist_dict)
    return artist_list
    

def song(data):



def lambda_handler(event, context):
    
    #First List files to be processed 
    
    s3 = boto3.client("s3")
    Bucket = "etl-vighnesh"
    Key = "raw_data/data_to_be_processed /"
    
     

    spotify_data = []
    spotify_keys = []
    
    
    for file in s3.list_objects(Bucket=Bucket, Prefix=Key)['Contents']:  #listing all files/objects that are to be processed i.e. raw data (json files)
    
        file_key = file['Key']
        if file_key.split(".")[-1] == "json":
            response = s3.get_object(Bucket = Bucket, Key = file_key)  # Getting files from bucket
            content = response['Body']  # Actual json_data
            jsonObject = json.loads(content.read())  # using json.load fuction to read data as it is in json format
            print(jsonObject)
            spotify_data.append(jsonObject)  # Appending json data into empty list 
            spotify_keys.append(file_key)    # 
            
            
    for data in spotify_data:
        
        album_list = album(data)   # calling defined transformation functions  & converting json data into lists 
        artist_list = artist(data)
        song_list = song(data) 
        
        
        # Now converting lists into dataframe
        
        album_df = pd.DataFrame.from_dict(album_list)
        album_df = album_df.drop_duplicates(subset=['album_id'])
    
        
        artist_df = pd.DataFrame.from_dict(artist_list)
        artist_df = artist_df.drop_duplicates(subset=['artist_id'])
        
        song_df = pd.DataFrame.from_dict(song_list)
        song_df = song_df.drop_duplicates(subset=['song_id'])
        
        

        

        
        
        #Now after creating dataframes putting it into tranformed data folder in csv format
        
        song_key = "transformed_data/song_data/song_transformed" + str(datetime.now()) + ".csv" # path in s3 bucket to save csv file
        song_buffer = StringIO()   #creating stringio object as song_buffer as it will covert df to string
        song_df.to_csv(song_buffer, index=False) #Now apply song_buffer to song_df as it convert it to csv & "index=False" is to avoid index col in csv as glue crawler will not detect it
        song_content = song_buffer.getvalue()  #Actual .csv file 
        s3.put_object(Bucket=Bucket, Key=song_key, Body = song_content ) #putting data into targeted folder in s3 bucket
        
        album_key = "transformed_data/album_data/album_transformed" + str(datetime.now()) + ".csv"
        album_buffer = StringIO()
        album_df.to_csv(album_buffer, index=False)
        album_content = album_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=album_key, Body= album_content) 
        
        artist_key = "transformed_data/artist_data/artist_transformed" + str(datetime.now()) + ".csv"
        artist_buffer = StringIO()
        artist_df.to_csv(artist_buffer, index=False)
        artist_content = artist_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=artist_key, Body= artist_content)
        
        
        # To avoid data in To_be_processed folder being tranfoemed again and again, Copy it after tranformation & paste it to Processed folder
        
            
    s3.resource = boto3.resource("s3")
    for key in spotify_keys:
                copy_source = {
                    "Bucket" : Bucket,
                    "Key" : key 
                }                             #copysource #tgtBucket   #tgtfolder
                s3.resource.meta.client.copy(copy_source, Bucket,  "raw_data/processed_data/" + key.split("/")[-1] )
                s3.resource.Object(Bucket, key).delete() 
                    
        
    
    
        
        
        
            
        
    
    
