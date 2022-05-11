import json
from Students import Students

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.students = None
f = open("data.json", "r")
json_string = f.read()
f.close()
app.students_data = json.loads(json_string)
app.students = Students(**app.students_data)


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

    elif password != users[username]:
        return jsonify({"Message": "Invalid password. Please try again."}), 400
    else:
        f = open("data.json", "r")
        json_string = f.read()
        f.close()
        dataDict = json.loads(json_string)

        return render_template("homePage.html"), 200


@app.route('/student1Chart')
def student1Chart():
    sData = app.students.studentsList
    return render_template("student1Charts.html", sData=sData)


sleepList = []
total = 0
valDay = 0
for i in range(len(app.students.studentsList)):
    sleepList.append(app.students.studentsList[i].get_sleepList())
    for k in range(len(sleepList[i])):
        total += sleepList[i][k]
        valDay += 1


@app.route('/studentGraphs')
def studentGraphs():
    sList = app.students.get_avg()
    return render_template("studentGraphs.html", sList=sList)


@app.route('/studentStatistics')
def studentMean():
    meanList = app.students.get_mean()
    maxList = app.students.get_Max()
    minList = app.students.get_min()
    sDev = app.students.get_sDev()
    variance = app.students.get_variance()
    median = app.students.get_median()
    nameList = app.students.get_infoNames()

    return render_template("studentStatistics.html", mlist=meanList, nList=nameList, maxList=maxList, minList=minList,
                           sDev=sDev, variance=variance, median=median)


@app.route('/studentHealth', methods=['GET', 'POST'])
def studentHealth():
    if request.method == 'POST':
        id = request.form.get('Name')
        try:
            string_id = int(id)
            print(string_id)
        except ValueError:
            return render_template("studentHealth.html")
        if (int(id) >= 0 and int(id) < (len(app.students.studentsList))):
            studentData = app.students.studentsList[int(id) - 1].get_singleStudentAvg()
            return render_template("studentHealth.html", sD=studentData, id=id)
        else:
            return render_template("studentHealth.html")
    else:
        return render_template("studentHealth.html")

@app.route('/compareStudents', methods=['GET', 'POST'])
def compareStudents():
    if request.method == 'POST':
        id = request.form.get('Name')
        try:
            string_id = int(id)
            print(string_id)
        except ValueError:
            return render_template("studentHealth.html")
        if (int(id) >= 0 and int(id) < (len(app.students.studentsList))):
            studentData = app.students.studentsList[int(id) - 1].get_singleStudentAvg()
            return render_template("studentHealth.html", sD=studentData, id=id)
        else:
            return render_template("studentHealth.html")
    else:
        return render_template("studentHealth.html")




if __name__ == '__main__':
    app.run()
