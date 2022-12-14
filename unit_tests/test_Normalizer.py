from matplotlib import test
from Normalizer import Normalizer

def test_normalizeTimedData_lengthsNotEqual():
    testTimes = []
    testData = [1]
    normalizer = Normalizer()
    result = normalizer.normalizeTimedData(testTimes, testData, 3*60)
    assert result is None

def test_normalizeTimedData_oneItem():
    testTimes = ["2022-10-25 16:01:43"]
    testData = [1]
    normalizer = Normalizer()
    timeResult, dataResult = normalizer.normalizeTimedData(testTimes, testData, 3*60)
    assert len(timeResult) == len(dataResult)
    assert len(timeResult) == 1
    assert timeResult[0] == "2022-10-25 16:01:43+00:00"

def test_normalizeTimedData_twoConsecutiveItems():
    testTimes = ["2022-10-25 16:01:43", "2022-10-25 16:04:43"]
    testData = [1, 2]
    normalizer = Normalizer()
    timeResult, dataResult = normalizer.normalizeTimedData(testTimes, testData, 3*60)
    assert len(timeResult) == len(dataResult)
    assert len(timeResult) == 2
    assert timeResult[0] == "2022-10-25 16:01:43+00:00"
    assert timeResult[1] == "2022-10-25 16:04:43+00:00"

def test_normalizeTimedData_MissingTimesAndDataFromPreviousTimeAreAdded():
    testTimes = [
        "2022-10-25 16:01:43",
        "2022-10-25 16:10:44"
    ]
    testData = [10, 20]
    normalizer = Normalizer()
    timeResult, dataResult = normalizer.normalizeTimedData(testTimes, testData, 3*60)
    assert len(timeResult) == len(dataResult)
    assert len(timeResult) == 5
    assert len(dataResult) == 5
    assert dataResult[0] == 10
    assert dataResult[1] == 10
    assert dataResult[2] == 10
    assert dataResult[3] == 10
    assert dataResult[4] == 20

def test_timeValueImputation_shouldFillInMissingTimes():
    testTimes = [
        "2022-10-25 16:01:43",
        "2022-10-25 16:10:44"
    ]
    normalizer = Normalizer()
    result = normalizer.timeValueImputation(testTimes, 3*60)
    assert len(result) == 5
    assert result[0] == "2022-10-25 16:01:43+00:00"
    assert result[1] == "2022-10-25 16:04:43+00:00"
    assert result[2] == "2022-10-25 16:07:43+00:00"
    assert result[3] == "2022-10-25 16:10:43+00:00"
    assert result[4] == "2022-10-25 16:10:44+00:00"

def test_timeValueImputation_shouldNotFillInWhenNoTimesMissing():
    testTimes = [
        "2022-10-25 16:01:43",
        "2022-10-25 16:04:43"
    ]
    normalizer = Normalizer()
    result = normalizer.timeValueImputation(testTimes, 3*60)
    assert len(result) == 2

def test_convertTimeStringToTimestamp_shouldConvertTimeStringToTimestamp():
    testTime = "2022-10-25 13:39:53"
    normalizer = Normalizer()
    result = normalizer.convertTimeStringToTimestamp(testTime)
    assert result == float(1666705193)

def test_convertTimeStringToTimestamp_shouldConvertTimeStringToTimestamp_ZeroPadded():
    testTime = "2022-01-01 01:01:01"
    normalizer = Normalizer()
    result = normalizer.convertTimeStringToTimestamp(testTime)
    assert result == float(1640998861)

def test_convertTimestampToTimeString_shouldConvertTimestampToTimeString():
    testTime = 1666719593
    normalizer = Normalizer()
    result = normalizer.convertTimestampToTimeString(testTime)
    assert result == "2022-10-25 17:39:53+00:00"

def test_convertTimestampToTimeString_shouldConvertTimestampToTimeString_ZeroPadded():
    testTime = 1641016861
    normalizer = Normalizer()
    result = normalizer.convertTimestampToTimeString(testTime)
    assert result == "2022-01-01 06:01:01+00:00"

def test_indexOf_shouldReturnNoneIfItemDoesntExist():
    testValues = ["0", "1", "2", "3", "4", "6"]
    normalizer = Normalizer()
    result = normalizer.indexOf(testValues, "5")
    assert result is None

def test_indexOf_shouldReturnIndexOfItemThatExists():
    testValues = ["0", "1", "2", "3", "5", "4", "6"]
    normalizer = Normalizer()
    result = normalizer.indexOf(testValues, "5")
    assert result == 4
