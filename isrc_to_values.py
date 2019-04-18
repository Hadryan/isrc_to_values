
# coding: utf-8

# In[1]:


### isrc_to_values documentation
###
### description: 
### this code takes isrc and 2 optional parameters and uses Spotify and consolidates these values with the Spotify URI and its features
### in the code, it currently tracks danceability, but refer to https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
### for other features such as key, energy, liveness, loudness, etc. 
###
### notes:
### -- ISRC values that do not return Spotify URI using data request are consequently not considered and are NOT given blank values
### -- Date value is gathered from first data set returned for search request -- many songs have multiple albums the song is on, the date refers to
###    the first value for which the search returns
### 
### input: excel file with 'ISRC', 'TRACK NAME', AND 'TRACK ARTIST' as columns with data underneath (can change name but isrc must be one of them)
### output: list of dictionaries with vetted values of data provided in input with "release year" and "danceability" values addeded and all rows filtered for 
### values with data ranges within determined release year and danceability ranges


# In[2]:


import pandas as pd
import sys
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from xlrd import open_workbook, cellname
import csv


# In[3]:


#spotipy client
SPOTIPY_CLIENT_ID = 'INSERT CLIENT ID'
SPOTIPY_CLIENT_SECRET = 'INSERT CLIENT SECRET'


# In[4]:


client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[6]:


#import excel
                ####path to file####  
df = pd.read_excel(r'INSERT PATH TO FILE', sheet_name = 0)
                ####################
    
                         #######COLUMN NAMES (ONE MUST CONTAIN ISRC)######## 
data = pd.DataFrame(df, columns = ['ISRC', 'TRACK NAME', 'TRACK ARTIST']) #EXCEL FILE COLUMN TITLES MUST BE NAMED AS SUCH#
                        ####################################################
check = data.to_dict('records')
print len(check) #verifies data amount


# In[8]:


isrc_to_values = []

for row in check: #CHECKS EVERY ROW VALUE 
    try:
        isrc = "isrc:" + row["isrc"]
        seek = client.search(isrc)
        try: 
            uri = str(seek["tracks"]["items"][0]['uri'])
            try:
                date = seek['tracks']['items'][0]['album']['release_date'] 
                date = int(date[0:4])    
                ### date >= 0 and date <= 9999 if no need for date verification ###
                if date >= 1990 and date <= 2001:
                    feature = client.audio_features(uri)
                    ### REFER TO SPOTIFY DOCUMENTATION FOR ADDITIONAL FEATURES ###
                    dance = feature[0]["danceability"] 
                    ###FILTER FOR VALUES###
                         ### INT VALUE ### 
                    if dance > 0.00 : 
                         ################
                        sd = {"uri" : uri,
                              "isrc": row["ISRC"],
                              "title" : row["COLUMN 2"],
                              "artist" : row["COLUMN 3"],
                              "dance" : dance, 
                              "date" : date}                             
                        uri_to_title.append(sd)
                        print "..."
            except: 
                print "no date"
        except:
            print "no uri"
    except:
        print "no isrc"
        
print "DONE"


# to export to xslx, use code below, changing the column value to any defined in the 'sd' dictionary. it will print in order all of the values of a column, copy and paste that into csv, xlsx, or wherever. Data structure is list of dictionaries, can find way to migrate straight to xlsx and add to code if needed. 

# In[12]:


for row in isrc_to_values:
             ### FIELD VALUE ###
    print row['FIELD VALUE']
             ###################

