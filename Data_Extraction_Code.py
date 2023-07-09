import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import boto3


def lambda_handler(event, context):
    
    
    client_id = os.environ.get('')            # Environment Vaiables
    client_secret = os.environ.get('')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotipy')
    
    Play_list_link = 'https://open.spotify.com/playlist/4hOKQuZbraPDIfaGbM3lKI'
    Play_list_uri = Play_list_link.split("/")[-1]
    
    data = sp.playlist_tracks(Play_list_uri)
    
    
    # using boto3 & creating s3 client to write extacted data to target folder
    
    client = boto3.client('s3')   
    
    filename = 'spotify_raw_' + str(datetime.now()) + '.json' 
    
    client.put_object(
        Bucket = 'etl-vighnesh',   
        Key = 'raw_data/data_to_be_processed /' + filename,
        Body =  json.dumps(data))
        
    
    
