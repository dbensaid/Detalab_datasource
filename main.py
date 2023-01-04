from collections import Counter
import collections
from datetime import datetime
from pytrends.request import TrendReq
from flask import Flask, render_template, send_file
import requests
import time


app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-HSQTDR354L"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' G-HSQTDR354L');
    </script>
    """
    # adding some cool button and text on my page
    text = """

  
  <html>
<head>
<style>
.button {
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;

  background-color:  #AFEEEE /* cyant */ #doesn't work
}

.button1 {background-color: #4CAF50;} /* Green */
.button2 {background-color: #008CBA;} /* Blue */


</style>
</head>
<body>

<h1>Hello World</h1>
<p>Welcome on Driss Bensaid websites, brows on the differents pages with those buttons</p>

<a href= "https://px0vzh.deta.dev/logger">
<button class="button button1" >/logger</button>
</a>

<a href= "https://px0vzh.deta.dev/logger_improved">
<button class="button button2">/logger_improved</button>
</a>

<a href= "https://px0vzh.deta.dev/cookies">
<button class="button button1">/cookies</button>
</a>

<a href= "https://px0vzh.deta.dev/ganalytics">
<button class="button button2">/ganalytics</button>
</a>

<a href= "https://px0vzh.deta.dev/google_trend_covid">
<button class="button button1">/google_trend_covid</button>
</a>

<a href= "https://px0vzh.deta.dev/timer_decorator">
<button class="button button2">/timer_decorator</button>
</a>

</body>
</html>


    
    """
    return prefix_google + text


@app.route('/logger')
def logger():
    # Print a log on python
    print("Logger accessed!")

    # Print a log on the browser
    return "This is a log on the browser"


@app.route('/logger_improved', methods=["GET"])
# Texbox attemps
def logger_improved():
    # Print a log on python
    print("Logger accessed!")

    # Print a log on the browser
    return render_template('template.html')


@app.route('/cookies')
def getcookies():
    # Make a GET request to the Google website
    requests.get("https://www.google.com/")
    req = requests.get("https://www.google.com/")
    # Get the cookies from the response
    cookies = req.cookies.get_dict()

    # Return the cookies as a dictionary
    return cookies


@app.route('/ganalytics')
def ganalytics():
    req = requests.get(
        "https://analytics.google.com/analytics/web/?authuser=1#/p344251322/reports/intelligenthome?params=_u..nav%3Dmaui")
    # Return the response as text
    return req.text

# ganalytic attemps( blocked because i wasn't able to do any new pip install and find the key find location on g api)

# import google.auth
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# @app.route('/ganalytics_improved')

# """A simple example of how to access the Google Analytics API."""

# from apiclient.discovery import build
# from oauth2client.service_account import ServiceAccountCredentials


# def get_service(api_name, api_version, scopes, key_file_location):
#     """Get a service that communicates to a Google API.

#     Args:
#         api_name: The name of the api to connect to.
#         api_version: The api version to connect to.
#         scopes: A list auth scopes to authorize for the application.
#         key_file_location: The path to a valid service account JSON key file.

#     Returns:
#         A service that is connected to the specified API.
#     """

#     credentials = ServiceAccountCredentials.from_json_keyfile_name(
#             key_file_location, scopes=scopes)

#     # Build the service object.
#     service = build(api_name, api_version, credentials=credentials)

#     return service


# def get_first_profile_id(service):
#     # Use the Analytics service object to get the first profile id.

#     # Get a list of all Google Analytics accounts for this user
#     accounts = service.management().accounts().list().execute()

#     if accounts.get('items'):
#         # Get the first Google Analytics account.
#         account = accounts.get('items')[0].get('id')

#         # Get a list of all the properties for the first account.
#         properties = service.management().webproperties().list(
#                 accountId=account).execute()

#         if properties.get('items'):
#             # Get the first property id.
#             property = properties.get('items')[0].get('id')

#             # Get a list of all views (profiles) for the first property.
#             profiles = service.management().profiles().list(
#                     accountId=account,
#                     webPropertyId=property).execute()

#             if profiles.get('items'):
#                 # return the first view (profile) id.
#                 return profiles.get('items')[0].get('id')

#     return None


# def get_results(service, profile_id):
#     # Use the Analytics Service Object to query the Core Reporting API
#     # for the number of sessions within the past seven days.
#     return service.data().ga().get(
#             ids='ga:' + profile_id,
#             start_date='7daysAgo',
#             end_date='today',
#             metrics='ga:sessions').execute()


# def print_results(results):
#     # Print data nicely for the user.
#     if results:
#         print 'View (Profile):', results.get('profileInfo').get('profileName')
#         print 'Total Sessions:', results.get('rows')[0][0]

#     else:
#         print 'No results found'


# def main():
#     # Define the auth scopes to request.
#     scope = 'https://www.googleapis.com/auth/analytics.readonly'
#     #wasn't able to find it
#     key_file_location = '<REPLACE_WITH_JSON_FILE>'

#     # Authenticate and construct service.
#     service = get_service(
#             api_name='analytics',
#             api_version='v3',
#             scopes=[scope],
#             key_file_location=key_file_location)

#     profile_id = get_first_profile_id(service)
#     print_results(get_results(service, profile_id))


#                                                           TP 3
# FINALLY SUCCED TO HAVE SOME PIP IMPORT DETECTED YAAAY! (Changing version of python)

# Google trend part


@app.route('/google_trend_covid', methods=["GET"])
def google_trend_covid():

    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=['covid'])
    interest_over_time_df = pytrends.interest_over_time()
    covid = interest_over_time_df['covid'].values.tolist()
    dates = [datetime.fromtimestamp(int(date/1e9)).date().isoformat()
             for date in interest_over_time_df.index.values.tolist()]

    params = {
        "type": 'line',
        "data": {
            "labels": dates,
            "datasets": [{
                "data": covid,
                "label": "covid",
                "borderColor": "#BB5E5E",
                "fill": 'false'
            }]},

        "options": {
            "title": {
                "display": 'true',
                "text": '"Covid" "intersest" percentage research over time'
            },
            "hover": {
                "mode": 'index',
                "intersect": 'true'
            },
        }
    }

    prefix_google = """


        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
        <canvas id="myChart" width="30" height="30"></canvas>""" + f"""
        <script>
        var ctx = document.getElementById('myChart');
        var myChart = new Chart(ctx, {params});
        </script>



    """

    return prefix_google


# Timer log part

#import problem on the deta deploy this time (not because of windows os)
#import matplotlib.pyplot as plt

#Check the Count_word_dict_and_counter_creator jupyter notbook to see how the image has been created (it is usefull to create it each time we deploy the website)

@app.route('/timer_decorator')
def timer_decorator():

    return send_file("count_word_dict_and_counter.png", mimetype="image/png")
