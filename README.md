# Hawaii Vacation Weather

Using precipitation and weather data from a variety of stations in Hawaii I first loaded these CSV's into a sqlite database and then designed a number of queries to analyze the data. I then built a flask app that can be used to query start dates or a start and end date that will return a JSON list of the minimum, maximum, and average temperature for a given start or start-end range. 

### query to retrieve last 12 months of precipitation data: 

![prcp_data](/README_images/12month_prcp_summary.PNG)

precipitation histogram 

![prcp_histo](/README_images/12month_prcp.PNG)

### query to retrieve available stations: 

![station_count](/README_images/station_count.PNG)

### query to obtain descriptive statistics for last 12 months of temperature observation data(tobs):

![tobs](/README_images/max_min_avg_temp.PNG)

temperature histogram

### histogram of temperatures at station with most recordings: 

![temp_histo](/README_images/temperature_histogram.PNG)


## Climate App 


###### Home Page
displays available routes 

![homepage](/README_images/home_page.PNG)

###### Precipitation JSON 
displays JSON data of precipitation 

![prcp_page](/README_images/prcp_json.PNG)

###### Stations JSON 
displays available stations 

![station_json](/README_images/station_json.PNG)

###### tobs JSON 
displays temperature data from each station 

![tobs_json](/README_images/tobs_json.PNG)

###### start and start/end JSON 
When entering a start date will return the minimum, maximum, and average temperatures for all dates greater than and equal to the start date. 
for date 2010-01-01:

![start](/README_images/start_json.PNG)


When entering a start and end date will return the minimum, maximum, and average temperatures for all dates inclusive. 
for dates 2010-01-05 to 2010-01-15:

![start_end](/README_images/start_end_json.PNG)

