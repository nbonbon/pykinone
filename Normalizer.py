from datetime import datetime
from dateutil import tz

class Normalizer:
    def normalizeTimedData(self, times, data, desiredTimespanInSeconds):
        if len(times) != len(data):
            return None
        if len(times) == 1:
            timeResult = [self._formatTimeString(times[0])]
            return timeResult, data

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
        imputedTimes = [self._formatTimeString(oldTimes[0])]
        previousTimestamp = self.convertTimeStringToTimestamp(oldTimes[0])
        for i in range(len(oldTimes)):
            if (i == 0):
                continue

            currentTimestamp = self.convertTimeStringToTimestamp(oldTimes[i])
            while (currentTimestamp - previousTimestamp) > (desiredTimespanInSeconds):
                previousTimestamp = previousTimestamp + (desiredTimespanInSeconds)
                previousTimeString = self.convertTimestampToTimeString(previousTimestamp)
                imputedTimes.append(previousTimeString)

            imputedTimes.append(self._formatTimeString(oldTimes[i]))
            previousTimestamp = currentTimestamp

        return imputedTimes

    def _formatTimeString(self, timeStr):
        return timeStr + "+00:00"

    def convertTimeStringToTimestamp(self, timeString):
        dateTime = datetime.fromisoformat(timeString).replace(tzinfo=tz.gettz('UTC'))
        return datetime.timestamp(dateTime)

    def convertTimestampToTimeString(self, timestamp):
        dt = datetime.fromtimestamp(timestamp, tz=tz.gettz('UTC'))
        return dt.isoformat(" ","seconds")

    def indexOf(self, collection, item):
        for i in range(len(collection)):
            if collection[i].replace("+00:00", "") == item:
                return i
        return None


        
