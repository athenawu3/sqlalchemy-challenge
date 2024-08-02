# Import the dependencies.

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model

path = "Resources/hawaii.sqlite"
engine = create_engine(f"sqlite:///{path}")

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with=engine)

# Save references to each table

Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB

session = Session(bind=engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    return (
        "All available routes:"
        "Precipitation Analysis: http://127.0.0.1:5000/api/v1.0/precipitation"
        "List of Stations: http://127.0.0.1:5000/api/v1.0/stations"
        "Temperature Observations for Most Active Station: http://127.0.0.1:5000/api/v1.0/tobs"
        "Temperature Data for Specified Start Date: http://127.0.0.1:5000/api/v1.0/<start>"
        "Temperature Data for Specified Start and End Dates: http://127.0.0.1:5000/api/v1.0/<start>/<end>"
    )

#@app.route("/api/v1.0/precipitation")

#@app.route("/api/v1.0/stations")

#@app.route("/api/v1.0/tobs")

#@app.route("/api/v1.0/<start>")

#@app.route("/api/v1.0/<start>/<end>")

if __name__ == "__main__":
    app.run(debug=True)



























