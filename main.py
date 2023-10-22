import json, unittest, datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
    # Given that the 'timestamp' in Type 1 data is in ISO format, the task is to convert it into milliseconds.
    if "timestamp" in jsonObject:
        timestamp = jsonObject["timestamp"]
        try:
            # Convert an ISO timestamp into a datetime object. 
            dt = datetime.datetime.fromisoformat(timestamp)
            # Convert the given datetime to the number of milliseconds                   that have passed since the epoch. 

            milliseconds = int(dt.timestamp() * 1000)
            # Modify the timestamp value inside the JSON object 
            jsonObject["timestamp"] = milliseconds
        except ValueError:
            # Address any erroneous ISO timestamps, if necessary. 
            pass

    return jsonObject


def convertFromFormat2(jsonObject):
    # No conversion is necessary for Type 2 data as long as the 'timestamp' is already in milliseconds format.
    return jsonObject


def main(jsonObject):
    result = {}

if "device" not in jsonObject:
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 1 failed')

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 2 failed')

if __name__ == '__main__':
    unittest.main()
