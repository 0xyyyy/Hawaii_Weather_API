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

![temp_histo](/README_images/temperature histogram)

### histogram of temperatures at station with most recordings: 


## Climate App 


###### Home Page



###### Precipitation JSON 


###### Stations JSON 



###### tobs JSON 



###### start and start/end JSON 

