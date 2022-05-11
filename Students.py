import statistics




class Students:
    def __init__(self, students):
        self.students = students
        self.studentsList = []
        for s in students:
            self.studentsList.append(Student(**s))

    def getStudents(self):
        return self.studentsList

    def get_avg(self):
        sList = []
        for i in range(len(self.studentsList)):
            sList.append([])
            sList[i].append((self.studentsList[i].get_avgSleep()).__round__())
            sList[i].append((self.studentsList[i].get_avgSugar()).__round__())
            sList[i].append((self.studentsList[i].get_avgPhone()).__round__())
            sList[i].append((self.studentsList[i].get_avgFruit()).__round__())
            sList[i].append((self.studentsList[i].get_avgVegetables()).__round__())
            sList[i].append((self.studentsList[i].get_avgCaffeine()).__round__())
            sList[i].append((self.studentsList[i].get_avgStrength()).__round__())
            sList[i].append((self.studentsList[i].get_avgModerate()).__round__())
            sList[i].append((self.studentsList[i].get_avgHigh()).__round__())
            sList[i].append((self.studentsList[i].get_avgSteps()).__round__())
        return sList

    def get_mean(self):
        totalSleep = 0
        totalSugar = 0
        totalPhone = 0
        totalFruit = 0
        totalVegetable = 0
        totalCaffeine = 0
        totalModerate = 0
        totalStrength = 0
        totalHigh = 0
        totalStep = 0
        valDay = 0
        meanList = []

        for i in range(len(self.studentsList)):
            for j in range(len(self.studentsList[i].daysList)):
                valDay += 1
                totalSleep += self.studentsList[i].daysList[j].sleep
                totalSugar += self.studentsList[i].daysList[j].sugar
                totalPhone += self.studentsList[i].daysList[j].phone
                totalFruit += self.studentsList[i].daysList[j].fruit
                totalVegetable += self.studentsList[i].daysList[j].vegetables
                totalCaffeine += self.studentsList[i].daysList[j].caffeine
                totalModerate += self.studentsList[i].daysList[j].moderate
                totalStrength += self.studentsList[i].daysList[j].strength
                totalHigh += self.studentsList[i].daysList[j].high
                totalStep += self.studentsList[i].daysList[j].steps
        sleepMean = (totalSleep / valDay).__round__()
        sugarMean = (totalSugar / valDay).__round__()
        phoneMean = (totalPhone / valDay).__round__()
        fruitMean = (totalFruit / valDay).__round__()
        vegetableMean = (totalVegetable / valDay).__round__()
        caffeineMean = (totalCaffeine / valDay).__round__()
        moderateMean = (totalModerate / valDay).__round__()
        strengthMean = (totalStrength / valDay).__round__()
        highMean = (totalHigh / valDay).__round__()
        stepMean = (totalStep / valDay).__round__()
        meanList.append(sleepMean)
        meanList.append(sugarMean)
        meanList.append(phoneMean)
        meanList.append(fruitMean)
        meanList.append(vegetableMean)
        meanList.append(caffeineMean)
        meanList.append(moderateMean)
        meanList.append(strengthMean)
        meanList.append(highMean)
        meanList.append(stepMean)
        return meanList

    def get_infoNames(self):
        infoNames = []
        infoNames.append("Sleep")
        infoNames.append("Sugar")
        infoNames.append("Phone")
        infoNames.append("Fruit")
        infoNames.append("Vegetable")
        infoNames.append("Caffeine")
        infoNames.append("Moderate")
        infoNames.append("Strength")
        infoNames.append("High")
        infoNames.append("Steps")
        return infoNames

    def get_Max(self):
        maxSleep = 0
        maxSugar = 0
        maxPhone = 0
        maxFruit = 0
        maxVegetables = 0
        maxCaffeine = 0
        maxModerate = 0
        maxStrength = 0
        maxHigh = 0
        maxSteps = 0
        maxList = []
        for i in range(len(self.studentsList)):
            for j in range(len(self.studentsList[i].daysList)):
                if ((self.studentsList[i].daysList[j].sleep) > maxSleep):
                    maxSleep = self.studentsList[i].daysList[j].sleep
                if ((self.studentsList[i].daysList[j].sugar) > maxSugar):
                    maxSugar = self.studentsList[i].daysList[j].sugar
                if ((self.studentsList[i].daysList[j].phone) > maxPhone):
                    maxPhone = self.studentsList[i].daysList[j].phone
                if ((self.studentsList[i].daysList[j].fruit) > maxFruit):
                    maxFruit = self.studentsList[i].daysList[j].fruit
                if ((self.studentsList[i].daysList[j].vegetables) > maxVegetables):
                    maxVegetables = self.studentsList[i].daysList[j].vegetables
                if ((self.studentsList[i].daysList[j].caffeine) > maxCaffeine):
                    maxCaffeine = self.studentsList[i].daysList[j].caffeine
                if ((self.studentsList[i].daysList[j].moderate) > maxModerate):
                    maxModerate = self.studentsList[i].daysList[j].moderate
                if ((self.studentsList[i].daysList[j].strength) > maxStrength):
                    maxStrength = self.studentsList[i].daysList[j].strength
                if ((self.studentsList[i].daysList[j].high) > maxHigh):
                    maxHigh = self.studentsList[i].daysList[j].high

                if ((self.studentsList[i].daysList[j].steps) > maxSteps):
                    maxSteps = self.studentsList[i].daysList[j].steps

        maxList.append(maxSleep)
        maxList.append(maxSugar)
        maxList.append(maxPhone)
        maxList.append(maxFruit)
        maxList.append(maxVegetables)
        maxList.append(maxCaffeine)
        maxList.append(maxModerate)
        maxList.append(maxStrength)
        maxList.append(maxHigh)
        maxList.append(maxSteps)
        return maxList

    def get_min(self):
        minSleep = self.studentsList[0].daysList[0].sleep
        minSugar = self.studentsList[0].daysList[0].sugar
        minPhone = self.studentsList[0].daysList[0].phone
        minFruit = self.studentsList[0].daysList[0].fruit
        minVegetables = self.studentsList[0].daysList[0].vegetables
        minCaffeine = self.studentsList[0].daysList[0].caffeine
        minModerate = self.studentsList[0].daysList[0].moderate
        minStrength = self.studentsList[0].daysList[0].strength
        minHigh = self.studentsList[0].daysList[0].high
        minSteps = self.studentsList[0].daysList[0].steps
        minList = []
        for i in range(len(self.studentsList)):
            for j in range(len(self.studentsList[i].daysList)):
                if (len(self.studentsList[i].daysList) == 0):
                    continue
                if ((self.studentsList[i].daysList[j].sleep) < minSleep):
                    minSleep = self.studentsList[i].daysList[j].sleep
                if ((self.studentsList[i].daysList[j].sugar) < minSugar):
                    minSugar = self.studentsList[i].daysList[j].sugar
                if ((self.studentsList[i].daysList[j].phone) < minPhone):
                    minPhone = self.studentsList[i].daysList[j].phone
                if ((self.studentsList[i].daysList[j].fruit) < minFruit):
                    minFruit = self.studentsList[i].daysList[j].fruit
                if ((self.studentsList[i].daysList[j].vegetables) < minVegetables):
                    minVegetables = self.studentsList[i].daysList[j].vegetables
                if ((self.studentsList[i].daysList[j].caffeine) < minCaffeine):
                    minCaffeine = self.studentsList[i].daysList[j].caffeine
                if ((self.studentsList[i].daysList[j].moderate) < minModerate):
                    minModerate = self.studentsList[i].daysList[j].moderate
                if ((self.studentsList[i].daysList[j].strength) < minStrength):
                    minStrength = self.studentsList[i].daysList[j].strength
                if ((self.studentsList[i].daysList[j].high) < minHigh):
                    minHigh = self.studentsList[i].daysList[j].high
                if ((self.studentsList[i].daysList[j].steps) < minSteps):
                    minSteps = self.studentsList[i].daysList[j].steps

        minList.append(minSleep)
        minList.append(minSugar)
        minList.append(minPhone)
        minList.append(minFruit)
        minList.append(minVegetables)
        minList.append(minCaffeine)
        minList.append(minModerate)
        minList.append(minStrength)
        minList.append(minHigh)
        minList.append(minSteps)
        return minList

    def get_sDev(self):
        sleepDev = []
        sugarDev = []
        phoneDev = []
        fruitDev = []
        vegetableDev = []
        caffeineDev = []
        moderateDev = []
        strengthDev = []
        highDev = []
        stepsDev = []
        allDev = []
        for i in range(len(self.studentsList)):
            for j in range(len(self.studentsList[i].daysList)):
                if (len(self.studentsList[i].daysList) == 0):
                    continue
                else:
                    sleepDev.append(self.studentsList[i].daysList[j].sleep)
                    sugarDev.append(self.studentsList[i].daysList[j].sugar)
                    phoneDev.append(self.studentsList[i].daysList[j].phone)
                    fruitDev.append(self.studentsList[i].daysList[j].fruit)
                    vegetableDev.append(self.studentsList[i].daysList[j].vegetables)
                    caffeineDev.append(self.studentsList[i].daysList[j].caffeine)
                    moderateDev.append(self.studentsList[i].daysList[j].moderate)
                    strengthDev.append(self.studentsList[i].daysList[j].strength)
                    highDev.append(self.studentsList[i].daysList[j].high)
                    stepsDev.append(self.studentsList[i].daysList[j].steps)
        sleepDev = statistics.stdev(sleepDev).__round__()
        sugarDev = statistics.stdev(sugarDev).__round__()
        phoneDev = statistics.stdev(phoneDev).__round__()
        fruitDev = statistics.stdev(fruitDev).__round__()
        vegetableDev = statistics.stdev(vegetableDev).__round__()
        caffeineDev = statistics.stdev(caffeineDev).__round__()
        moderateDev = statistics.stdev(moderateDev).__round__()
        strengthDev = statistics.stdev(strengthDev).__round__()
        highDev = statistics.stdev(highDev).__round__()
        stepsDev = statistics.stdev(stepsDev).__round__()

        allDev.extend((sleepDev, sugarDev, phoneDev, fruitDev, vegetableDev, caffeineDev, moderateDev, strengthDev,
                       highDev, stepsDev))
        return allDev

    def get_variance(self):
        sleepVariance = []
        sugarVariance = []
        phoneVariance = []
        fruitVariance = []
        vegetableVariance = []
        caffeineVariance = []
        moderateVariance = []
        strengthVariance = []
        highVariance = []
        stepsVariance = []
        allVariance = []
        for i in range(len(self.studentsList)):
            for j in range(len(self.studentsList[i].daysList)):
                if (len(self.studentsList[i].daysList) == 0):
                    continue
                else:
                    sleepVariance.append(self.studentsList[i].daysList[j].sleep)
                    sugarVariance.append(self.studentsList[i].daysList[j].sugar)
                    phoneVariance.append(self.studentsList[i].daysList[j].phone)
                    fruitVariance.append(self.studentsList[i].daysList[j].fruit)
                    vegetableVariance.append(self.studentsList[i].daysList[j].vegetables)
                    caffeineVariance.append(self.studentsList[i].daysList[j].caffeine)
                    moderateVariance.append(self.studentsList[i].daysList[j].moderate)
                    strengthVariance.append(self.studentsList[i].daysList[j].strength)
                    highVariance.append(self.studentsList[i].daysList[j].high)
                    stepsVariance.append(self.studentsList[i].daysList[j].steps)
        sleepVariance = statistics.variance(sleepVariance).__round__()
        sugarVariance = statistics.variance(sugarVariance).__round__()
        phoneVariance = statistics.variance(phoneVariance).__round__()
        fruitVariance = statistics.variance(fruitVariance).__round__()
        vegetableVariance = statistics.variance(vegetableVariance).__round__()
        caffeineVariance = statistics.variance(caffeineVariance).__round__()
        moderateVariance = statistics.variance(moderateVariance).__round__()
        strengthVariance = statistics.variance(strengthVariance).__round__()
        highVariance = statistics.variance(highVariance).__round__()
        stepsVariance = statistics.variance(stepsVariance).__round__()

        allVariance.extend((sleepVariance, sugarVariance, phoneVariance, fruitVariance, vegetableVariance,
                            caffeineVariance, moderateVariance, strengthVariance,
                            highVariance, stepsVariance))

        return allVariance


    def get_median(self):
        sleepMedian = []
        sugarMedian = []
        phoneMedian = []
        fruitMedian = []
        vegetableMedian = []
        caffeineMedian = []
        moderateMedian = []
        strengthMedian = []
        highMedian = []
        stepsMedian = []
        allMedian = []
        for i in range(len(self.studentsList)):
            for j in range(len(self.studentsList[i].daysList)):
                if (len(self.studentsList[i].daysList) == 0):
                    continue
                else:
                    sleepMedian.append(self.studentsList[i].daysList[j].sleep)
                    sugarMedian.append(self.studentsList[i].daysList[j].sugar)
                    phoneMedian.append(self.studentsList[i].daysList[j].phone)
                    fruitMedian.append(self.studentsList[i].daysList[j].fruit)
                    vegetableMedian.append(self.studentsList[i].daysList[j].vegetables)
                    caffeineMedian.append(self.studentsList[i].daysList[j].caffeine)
                    moderateMedian.append(self.studentsList[i].daysList[j].moderate)
                    strengthMedian.append(self.studentsList[i].daysList[j].strength)
                    highMedian.append(self.studentsList[i].daysList[j].high)
                    stepsMedian.append(self.studentsList[i].daysList[j].steps)
        sleepMedian = statistics.median(sleepMedian).__round__()
        sugarMedian = statistics.median(sugarMedian).__round__()
        phoneMedian = statistics.median(phoneMedian).__round__()
        fruitMedian = statistics.median(fruitMedian).__round__()
        vegetableMedian = statistics.median(vegetableMedian).__round__()
        caffeineMedian = statistics.median(caffeineMedian).__round__()
        moderateMedian = statistics.median(moderateMedian).__round__()
        strengthMedian = statistics.median(strengthMedian).__round__()
        highMedian = statistics.median(highMedian).__round__()
        stepsMedian = statistics.median(stepsMedian).__round__()

        allMedian.extend((sleepMedian, sugarMedian, phoneMedian, fruitMedian, vegetableMedian, caffeineMedian,
                          moderateMedian, strengthMedian,
                          highMedian, stepsMedian))

        return allMedian


class Student:
    def __init__(self, id, days):
        self.id = id
        self.days = days
        self.daysList = []
        print(days)
        for d in days:
            if d:
                self.daysList.append(Day(**d))
            else:
                print("Empty record")

    def get_sleepList(self):  # get rid of after testing
        sleepList = []
        for day in self.daysList:
            sleepList.append(day.sleep)
        return sleepList

    def get_singleStudentAvg(self):
        list = []
        list.append(self.get_avgSleep().__round__())
        list.append(self.get_avgSugar().__round__())
        list.append(self.get_avgPhone().__round__())
        list.append(self.get_avgFruit().__round__())
        list.append(self.get_avgVegetables().__round__())
        list.append(self.get_avgCaffeine().__round__())
        list.append(self.get_avgModerate().__round__())
        list.append(self.get_avgStrength().__round__())
        list.append(self.get_avgHigh().__round__())
        list.append(self.get_avgSteps().__round__())
        return list

    def get_avgSleep(self):
        totalSleep = 0
        for day in self.daysList:
            totalSleep += day.sleep
        if len(self.daysList) == 0:
            avgSleep = -1

        else:
            avgSleep = totalSleep / len(self.daysList)
        return avgSleep.__round__()

    def get_avgPhone(self):
        totalPhone = 0
        for day in self.daysList:
            totalPhone += day.phone
        if len(self.daysList) == 0:
            avgPhone = -1

        else:
            avgPhone = totalPhone / len(self.daysList)
        return avgPhone

    def get_avgSugar(self):
        totalSugar = 0
        for day in self.daysList:
            totalSugar += day.sugar
        if len(self.daysList) == 0:
            avgSugar = -1

        else:
            avgSugar = totalSugar / len(self.daysList)
        return avgSugar

    def get_avgFruit(self):
        totalFruit = 0
        for day in self.daysList:
            totalFruit += day.fruit
        if len(self.daysList) == 0:
            avgFruit = -1

        else:
            avgFruit = totalFruit / len(self.daysList)
        return avgFruit

    def get_avgVegetables(self):
        totalVegetables = 0
        for day in self.daysList:
            totalVegetables += day.vegetables
        if len(self.daysList) == 0:
            avgVegetables = -1

        else:
            avgVegetables = totalVegetables / len(self.daysList)
        return avgVegetables

    def get_avgCaffeine(self):
        totalCaffeine = 0
        for day in self.daysList:
            totalCaffeine += day.caffeine
        if len(self.daysList) == 0:
            avgCaffeine = -1

        else:
            avgCaffeine = totalCaffeine / len(self.daysList)
        return avgCaffeine

    def get_avgStrength(self):
        totalStrength = 0
        for day in self.daysList:
            totalStrength += day.strength
        if len(self.daysList) == 0:
            avgStrength = -1

        else:
            avgStrength = totalStrength / len(self.daysList)
        return avgStrength

    def get_avgModerate(self):
        totalModerate = 0
        for day in self.daysList:
            totalModerate += day.moderate
        if len(self.daysList) == 0:
            avgModerate = -1

        else:
            avgModerate = totalModerate / len(self.daysList)
        return avgModerate

    def get_avgHigh(self):
        totalHigh = 0
        for day in self.daysList:
            totalHigh += day.high
        if len(self.daysList) == 0:
            avgHigh = -1

        else:
            avgHigh = totalHigh / len(self.daysList)
        return avgHigh

    def get_avgSteps(self):
        totalSteps = 0
        for day in self.daysList:
            totalSteps += day.steps
        if len(self.daysList) == 0:
            avgSteps = -1

        else:
            avgSteps = totalSteps / len(self.daysList)
        return avgSteps

    def getDays(self):
        return self.days


class Day:
    def __init__(self, sleep, sugar, phone, fruit, vegetables, caffeine, strength, moderate, high, steps):
        self.sleep = sleep
        self.sugar = sugar
        self.phone = phone
        self.fruit = fruit
        self.vegetables = vegetables
        self.caffeine = caffeine
        self.strength = strength
        self.moderate = moderate
        self.high = high
        self.steps = steps

    def getDay(self):
        return self.sleep, self.sugar, self.phone, self.fruit, self.vegetables, self.caffeine, self.strength, self.moderate, self.steps, self.high


'''f = open("data.json", "r")
json_string = f.read()
f.close()
dataDict = json.loads(json_string)


def customDataDecoder(dataDict):
    return namedtuple('X', dataDict.keys())(*dataDict.values())


dataObj = json.loads(json_string, object_hook=customDataDecoder)

student = dataObj.students[0].days[0].sleep


print (student)'''
