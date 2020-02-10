# app.py
from flask import Flask, request, jsonify
from scrape import scrape
from scrape import scrapeSecond
from scrape import scrapeThird
from scrape import scrapeFourth
from scrape import getListOfShows
from scrape import getDates
from scrape import scrapeDailyMotion
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return jsonify({"ok": "200"})

@app.route('/listShows')
def listShows():
    return jsonify(getListOfShows())

@app.route('/watchShow')
def watchShow():
    return jsonify(scrape(request.args.get('showLink')))

@app.route('/watchShowDm')
def watchShowDm():
    return jsonify(scrapeDailyMotion(request.args.get('showLink')))

@app.route('/showDates')
def showDates():
    link = request.args.get("showLink")
    print(link)
    return jsonify(getDates(request.args.get('showLink')))

@app.route('/bhabiji')
def bhabiji():
    return jsonify({"latestEppisode: ": scrapeSecond()})

@app.route('/kullfi')
def kulfi():
    return jsonify({"latestEppisode: ": scrapeThird()})

@app.route('/KapilSharmaShow')
def kapil():
    return jsonify({"latestEppisode: ": scrapeFourth()})

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)