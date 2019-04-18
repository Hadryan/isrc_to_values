# isrc_to_values
takes isrc and returns audio features as determined by spotify 
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
