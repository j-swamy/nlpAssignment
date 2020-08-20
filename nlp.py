from textblob import TextBlob 
import sys
import re

# Read and sort data from files into a list of dictionaries-- makes it easy to search
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

# Iterate through the dictionary and find the polarity of the company description
def getSentiment(companyList):
	for c in companyList:
		pol = TextBlob(c["purpose"]).sentiment.polarity
		c["polarity"] = pol
	# Sorts the dictionary by polarity key, from lowest to highest
	sortedList = sorted(companyList, key = lambda i: i["polarity"])
	return sortedList


if __name__ == "__main__":
	companyList = []
	# Read both files
	readData("results.txt", companyList)
	readData("mydata.csv", companyList)
	# Get sentiment
	sortedList = getSentiment(companyList)
	# 'Worst' 10 companies have lowest polarity
	b10 = sortedList[:10]
	# 'Best' 10 Companies have highest polarity
	t10 = sortedList[-10:]
	# Reverse top 10 so it counts down while printing (for readability)
	t10.reverse()

	# Printing and formatting output.
	print("'Worst' 10 Companies:")
	count = 1
	for d in b10:
		print(str(count) + ". " + d["name"] + " | Polarity: " + str(d["polarity"]))
		count = count + 1
	count = 1
	print("-----------------------------")
	print("'Best' 10 Companies:")
	for d in t10:
		print(str(count) + ". " + d["name"] + " | Polarity: " + str(d["polarity"]))
		count = count + 1








