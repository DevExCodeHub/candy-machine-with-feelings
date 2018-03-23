import os
import json
import serial
import sys
import logging
import glob
from dotenv import load_dotenv
from flask import Flask
from flask import request
from pymongo import MongoClient
from watson_developer_cloud import AuthorizationV1 as WatsonAuthorization
from watson_developer_cloud import SpeechToTextV1 as SpeechToText
from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

logger = logging.getLogger('candy_logger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('candy.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

load_dotenv(os.path.join(os.path.dirname(__file__), "crd.env"))
alchemy = AlchemyLanguage(api_key=os.environ.get("ALCHEMY_API_KEY"))
auth = WatsonAuthorization(
    username=os.environ.get("STT_USERNAME"),
    password=os.environ.get("STT_PASSWORD")
)
language_translator = LanguageTranslator(
    username=os.environ.get("LT_USERNAME"),
    password=os.environ.get("LT_PASSWORD")
)


has_arduino = False # Stays False if "python server.py"
if len(sys.argv) > 1 and sys.argv[1] == 'arduino':
    has_arduino = True # True if user runs "python server.py arduino"

if has_arduino:
    # configure the serial connections 
    # (Parameters differ depending on the device being connected)
    ser = serial.Serial(
        port=glob.glob("/dev/tty*")[0],
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    ser.isOpen()
    ser.flush()

app = Flask(__name__, static_url_path="/static", static_folder="static")

def get_text_translation_to_english(text):
    translation = language_translator.translate(
        text=text,
        source='ar',
        target='en')
    return translation

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/english")
def english():
    return app.send_static_file("english.html")

@app.route("/arabic")
def arabic():
    return app.send_static_file("arabic.html")

@app.route("/token")
def getToken():
    return auth.get_token(url=SpeechToText.default_url)

@app.route("/arabic-sentiment", methods=["POST"])
def getSentiment():
    global has_arduino
    text = request.form["transcript"]
    englishText = get_text_translation_to_english(text)
    result = alchemy.sentiment(text=englishText)
    sentiment = result["docSentiment"]["type"]

    if sentiment == "neutral":
        score = 0
    else:
        score = result["docSentiment"]["score"]
        if has_arduino:
            if score != 0:
                if float(score) > 0:
                    ser.write(bytes('p', 'UTF-8'))
                else:
                    ser.write(bytes('n','UTF-8'))
                ser.flush()

    logger.info(text + " - " + sentiment + " - " + str(score))
    return json.dumps({"sentiment": sentiment, "score": score})

@app.route("/english-sentiment", methods=["POST"])
def getEnglishSentiment():
    global has_arduino
    text = request.form["transcript"]
    result = alchemy.sentiment(text=text)
    sentiment = result["docSentiment"]["type"]

    if sentiment == "neutral":
        score = 0
    else:
        score = result["docSentiment"]["score"]
        if has_arduino:
            if score != 0:
                if float(score) > 0:
                    ser.write(bytes('p', 'UTF-8'))
                else:
                    ser.write(bytes('n','UTF-8'))
                ser.flush()

    logger.info(text + " - " + sentiment + " - " + str(score))
    return json.dumps({"sentiment": sentiment, "score": score})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
