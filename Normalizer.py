import datetime

class Normalizer:
    def normalizeTimedData(self, times, data, desiredTimespanInSeconds):
        if len(times) != len(data):
            return None

        timeResult = self.timeValueImputation(times, desiredTimespanInSeconds)

        dataResult = []
        for i in range(len(times)):
            if (i + 1) > len(times):
                break
            else:
                currentData = data[i]
                startIndex = self.indexOf(timeResult, times[i])

                if (i + 1) < len(times):
                    stopIndex = self.indexOf(timeResult, times[i+1])
                else:   
                    dataResult.insert(startIndex, currentData)

                for j in range(startIndex, stopIndex):
                    dataResult.insert(j, currentData)

        return timeResult, dataResult

    def timeValueImputation(self, oldTimes, desiredTimespanInSeconds):
        imputedTimes = [oldTimes[0]]
        previousTimestamp = self.convertTimeStringToTimestamp(oldTimes[0])
        for i in range(len(oldTimes)):
            if (i == 0):
                continue

            currentTimestamp = self.convertTimeStringToTimestamp(oldTimes[i])
            while (currentTimestamp - previousTimestamp) > (desiredTimespanInSeconds):
                previousTimestamp = previousTimestamp + (desiredTimespanInSeconds)
                previousTimeString = self.convertTimestampToTimeString(previousTimestamp)
                imputedTimes.append(previousTimeString)

            imputedTimes.append(oldTimes[i])
            previousTimestamp = currentTimestamp

        return imputedTimes

    def convertTimeStringToTimestamp(self, timeString):
        dateTime = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
        return datetime.datetime.timestamp(dateTime)

    def convertTimestampToTimeString(self, timestamp):
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def indexOf(seld, collection, item):
        for i in range(len(collection)):
            if collection[i] == item:
                return i
        return None


        
