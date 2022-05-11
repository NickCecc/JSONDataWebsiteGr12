import json
from collections import namedtuple

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def readJson(path):
    with open(path, 'r') as f:
        data = json.load(f)
        return data


@app.route("/get-cool-page", methods=["POST"])
def get_cool_page():
    data = request.form
    username = data["username"]
    password = data["password"]

    users = readJson("signin.json")
    if not username in users:
        return jsonify({"Message": "Invalid username. Please try again."}), 400

    if password != users[username]:
        return jsonify({"Message": "Invalid password. Please try again."}), 400

    return render_template("homePage.html"), 200


def customDDecoder(dDict):
    return namedtuple('X', dDict.keys())(*dDict.values())


f = open("data.json")
json_string = f.read()
f.close()
py_obj = json.loads(json_string)
dObj = json.loads(json_string, object_hook=customDDecoder)
students = dObj.students

data = []
for i in range(len(dObj.students)):
    data.append([])
    avgSleep = 0
    avgSugar = 0
    avgPhone = 0
    avgFruit = 0
    avgVeg = 0
    avgCaf = 0
    avgStr = 0
    avgMod = 0
    avgHi = 0
    avgStep = 0

    valDay = 0
    for k in range(len(dObj.students[i].days)):
        if (len(dObj.students[i].days[k]) == 0):
            continue
        else:
            avgSleep += dObj.students[i].days[k].sleep
            avgSugar += dObj.students[i].days[k].sugar
            avgPhone += dObj.students[i].days[k].phone
            avgFruit += dObj.students[i].days[k].fruit
            avgVeg += dObj.students[i].days[k].vegetables
            avgCaf += dObj.students[i].days[k].caffeine
            avgStr += dObj.students[i].days[k].strength
            avgMod += dObj.students[i].days[k].moderate
            avgHi += dObj.students[i].days[k].high
            avgStep += dObj.students[i].days[k].steps
            valDay += 1

    if valDay == 0:
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
        data[i].append(0)
    else:
        data[i].append((avgSleep / valDay).__round__())
        data[i].append((avgSugar / valDay).__round__())
        data[i].append((avgPhone / valDay).__round__())
        data[i].append((avgFruit / valDay).__round__())
        data[i].append((avgVeg / valDay).__round__())
        data[i].append((avgCaf / valDay).__round__())
        data[i].append((avgStr / valDay).__round__())
        data[i].append((avgMod / valDay).__round__())
        data[i].append((avgHi / valDay).__round__())
        data[i].append((avgStep / valDay).__round__())
dataAll = []
# each student in own list w/ each day in own list
for i in range(len(dObj.students)):
    dataAll.append([])  # dataAll[i] = []
    for k in range(len(dObj.students[i].days)):
        dataAll.append([])

        if (len(dObj.students[i].days[k]) == 0):
            continue

        else:

            dataAll[k].append(dObj.students[i].days[k].sleep)
            dataAll[k].append(dObj.students[i].days[k].sugar)
            dataAll[k].append(dObj.students[i].days[k].phone)
            dataAll[k].append(dObj.students[i].days[k].fruit)
            dataAll[k].append(dObj.students[i].days[k].vegetables)
            dataAll[k].append(dObj.students[i].days[k].caffeine)
            dataAll[k].append(dObj.students[i].days[k].strength)
            dataAll[k].append(dObj.students[i].days[k].moderate)
            dataAll[k].append(dObj.students[i].days[k].high)
            dataAll[k].append(dObj.students[i].days[k].steps)


maxSleep = 0
ints = []
print(dataAll)
print(data)





@app.route('/graphs')
def graphs():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("studentGraphs.html", studNum=dObj, data=data, dataAll=dataAll)


@app.route('/student1Chart')
def student1Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student1Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student2Chart')
def student2Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student2Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student3Chart')
def student3Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student3Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student4Chart')
def student4Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student4Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student5Chart')
def student5Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student5Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student6Chart')
def student6Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student6Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student7Chart')
def student7Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student7Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student8Chart')
def student8Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student8Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student9Chart')
def student9Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student9Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student10Chart')
def student10Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student10Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student11Chart')
def student11Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student11Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student12Chart')
def student12Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student12Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student13Chart')
def student13Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student13Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student14Chart')
def student14Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student14Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student15Chart')
def student15Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student15Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student16Chart')
def student16Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student16Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student17Chart')
def student17Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student17Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student18Chart')
def student18Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student18Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student19Chart')
def student19Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student19Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student20Chart')
def student20Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student20Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student21Chart')
def student21Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student21Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student22Chart')
def student22Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student22Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student23Chart')
def student23Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student23Charts.html", studNum=dObj, dataAll=dataAll)


@app.route('/student24Chart')
def student24Chart():
    f = open("data.json")
    json_string = f.read()
    f.close()
    py_obj = json.loads(json_string)
    dObj = json.loads(json_string, object_hook=customDDecoder)
    return render_template("student24Charts.html", studNum=dObj, dataAll=dataAll)


if __name__ == '__main__':
    app.run()
