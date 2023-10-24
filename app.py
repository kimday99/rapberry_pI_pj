from flask import Flask, render_template, request
import requests 
from urllib.parse import urlencode, unquote
import json
import csv
from dotenv import load_dotenv
import os

load_dotenv()
myWeatherKey = os.environ.get("WEATHER_FORECAST_KEY")
print(myWeatherKey)

app = Flask(__name__)  

city_dict = {}

with open("exam/city.csv", mode="r", encoding="UTF8") as inp:
    reader = csv.reader(inp)
    city_dict = {rows[0]: rows[1] for rows in reader}

print(city_dict)


def getWhen(city_id):
    url = "http://apis.data.go.kr/B490007/qualExamSchd/getQualExamSchdList"
    queryString = "?" + urlencode(
        {
            "ServiceKey": unquote(myWeatherKey),
            "numOfRows": "10",
            "pageNo": "1",
            "dataFormat": "JSON",
            "implYy": "2023",
            "qualgbCd": "T",
            "jmCd": city_id,
        }
    )
    response = requests.get(url + queryString)    
    r_dict = json.loads(response.text)
    r_body = r_dict.get("body")
    item_list = r_body.get("items")

    for item in item_list:
        if item.get("implYy") == "2023":
            temp = item.get("docRegStartDt")
            docExamStartDt = item.get("docExamStartDt")
            weather = item.get("description")
            docPassDt = item.get("docPassDt")
            break

    return temp, weather, docExamStartDt, docPassDt

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["name"]
        city_id = city_dict.get(city_name)
        print(city_id)

        if city_id == None:
            return render_template("index.html")

        temp, weather, docExamStartDt, docPassDt = getWhen(city_id)

        return render_template(
            "index.html",
            temp=temp,
            weather=weather,
            city_name=city_name,
            docExamStartDt=docExamStartDt,
            docPassDt=docPassDt,
        )
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)