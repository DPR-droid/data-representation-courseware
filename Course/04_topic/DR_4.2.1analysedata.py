from valoffdoa import getall

data  = getall()

totalarea = 0

for entry in data:
    valuationsreports = entry["ValuationReport"]
    # print(valuationsreport)
    for valuationsreport in valuationsreports:
        if valuationsreport["FloorUse"] == "HAIR SALON":
            totalarea += valuationsreport["Area"]

print(round(totalarea))