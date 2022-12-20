from flask import Flask, render_template
import requests


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

    return prefix_google + "Hello World, welcome on Driss Bensaid websites. \nAll pages: /  \n /logger \n /cookies \n /ganalytics"

@app.route('/logger')
def logger():
    # Print a log on python
    print("Logger accessed!")


    # Print a log on the browser
    return "This is a log on the browser" 

# @app.route('/logger_improved')
#Texbox attemps
# def logger():
#     # Print a log on python
#     print("Logger accessed!")


#     # Print a log on the browser
#     return render_template('/template.html')

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
    req = requests.get("https://analytics.google.com/analytics/web/?authuser=1#/p344251322/reports/intelligenthome?params=_u..nav%3Dmaui")
    # Return the response as text
    return req.text 

#ganalytic attemps( blocked because i wasn't able to do any new pip install and find the key find location on g api)

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


