# Pocket Parse
This is a simple Python script that parses the `ril_export.html` file from [Pocket web app](https://getpocket.com/options) and writes the data to a csv file.

## Output
The csv file has eight columns. Each pocketed webpage is on a seperate row.

**status** - Either `Unread` or `Read Archive`

**title** - The title of the webpage pocketed 

**href** - full URL of the webpage pocketed 

**domain** - the root or sub domain of the webpage pocketed 

**date_added** - The calendar date that the webpage was pocketed 

**time_added** - The time of day that the webpage was pocketed 

**day_of_week_added** - The day of the week that the webpage was pocketed 

**tags** - A comma seperated list of tags assigned to the webpage 

## Requirements
* Python 2.x
* csv
* codecs
* datetime
* BeautifulSoup

## Usage
1. Save the `ril_export.html` file exported from Pocket in the same directory as `pocket_parse.py`
2. Run the script from the terminal `python pocket_parse.py`
