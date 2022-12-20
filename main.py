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

    return prefix_google + "Hello World, welcome on Driss Bensaid websites"


@app.route('/logger')
def logger():
    # Print a log on python
    print("Logger accessed!")


    # Print a log on the browser
    return "This is a log on the browser" #render_template('/template.html')



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