# ## Step 2 - Climate App

# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

# * Use Flask to create your routes.

# ### Routes

# * `/`

#   * Home page.

#   * List all routes that are available.

# * `/api/v1.0/precipitation`

#   * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

#   * Return the JSON representation of your dictionary.

# * `/api/v1.0/stations`

#   * Return a JSON list of stations from the dataset.

# * `/api/v1.0/tobs`
#   * Query the dates and temperature observations of the most active station for the last year of data.
  
#   * Return a JSON list of temperature observations (TOBS) for the previous year.

# * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route('/')
def welcome():
    return(
        f"""Available routes<br/>
            /api/v1.0/precipitation<br/>
            /api/v1.0/station<br/>
            /api/v1.0/tobs<br/>
            /api/v1.0/startDate<br/>
            /api/v1.0/startDate/endDate<br/>"""
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    all_prcp = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['precipitation'] = prcp
        all_prcp.append(precipitation_dict)
    return jsonify(all_prcp)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)

    results = session.query(Station.station).all()

    session.close()

    all_stations = list(np.ravel(results))
    return jsonify(all_stations)
# * `/api/v1.0/tobs`
#   * Query the dates and temperature observations of the most active station for the last year of data.
  
#   * Return a JSON list of temperature observations (TOBS) for the previous year.

# * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    temp_data = session.query(Measurement.tobs, Measurement.date).order_by(Measurement.date.desc())

    highest_station = temp_data.filter(Measurement.station == "USC00519281")
    year_data = highest_station.filter(Measurement.date >= '2016-08-23' )

    session.close()
    all_temps = []
    for i in year_data:
        last_year_dict = {}
        last_year_dict['Date'] = i.date
        last_year_dict['Tobs'] = i.tobs
        all_temps.append(last_year_dict)
    return jsonify(all_temps)
#return min, max, avg for given start date 
@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)

    min_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).all()
    max_temp = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()
    all_temps = [] 
    temp_dict = {
        "Minimum Temp" : min_temp, 
        "Maximum Temp" : max_temp,
        "Average Temp" :avg_temp
    }
    all_temps = [temp_dict]
    return jsonify(all_temps)
#return min, max, avg for given start/end date 
@app.route("/api/v1.0/<start>/<end>")
def date_range(start, end):
    session = Session(engine)

    min_temp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    max_temp = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    avg_temp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()   
    all_temps = []
    temp_dict = {
        "Minimum Temp" : min_temp,
        "Maximum Temp" : max_temp,
        "Average Temp" : avg_temp
    }
    all_temps = [temp_dict]
    return jsonify(all_temps)

if __name__ == "__main__":
    app.run(debug=True)