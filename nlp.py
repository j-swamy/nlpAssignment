from textblob import TextBlob 
import sys
import re

def readData(fn, companyList):
	with open(fn, 'r') as file:
		for line in file:
			if line == "name, purpose":
				continue
			else:
				splitLine = re.match("(.+),(.+)", line)
				name = splitLine.groups()[0].strip('"').strip()
				purpose = splitLine.groups()[1]
				addDict = {"name": name, "purpose": purpose}
				companyList.append(addDict)

def readSpecialData(fn, companyList):
	with open(fn, 'r') as file:
		content = file.read()
		content_list = content.split("',")
	for i in range(len(content_list)):
		name = "n"
		purpose = "p"
		if (i % 5 == 1):
			name = content_list[i].strip('"').strip()
		elif (i % 5 == 3):
			purpose = content_list[i]
		addDict = {"name": name, "purpose": purpose}
		companyList.append(addDict)
	return companyList


print(readSpecialData("myresults1.txt", []))



def getSentiment(companyList):
	for c in companyList:
		pol = TextBlob(c["purpose"]).sentiment.polarity
		c["polarity"] = pol
	sortedList = sorted(companyList, key = lambda i: i["polarity"])
	return sortedList

# if __name__ == "__main__":
# 	companyList = []
# 	readData("results.txt", companyList)
# 	readData("mydata.csv", companyList)
# 	sortedList = getSentiment(companyList)
# 	b10 = sortedList[:10]
# 	t10 = sortedList[-10:]
# 	t10.reverse()
# 	print("'Worst' 10 Companies:")
# 	count = 1
# 	for d in b10:
# 		print(str(count) + ". " + d["name"] + " | Polarity: " + str(d["polarity"]))
# 		count = count + 1
# 	count = 1
# 	print("-----------------------------")
# 	print("'Best' 10 Companies:")
# 	for d in t10:
# 		print(str(count) + ". " + d["name"] + " | Polarity: " + str(d["polarity"]))
# 		count = count + 1








