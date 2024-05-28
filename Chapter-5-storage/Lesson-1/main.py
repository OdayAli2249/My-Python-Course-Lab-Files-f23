import json
# the same data structure from previous program
# dictionary that maps month name to list of three tuples: every tuple consists of two elements: product name, price of sales in the month where the list mapped from.

data = {
    'January': [("Tea",4900), ("Coffee",3200), ("Sugar",6000)],
    'February': [("Tea",7030), ("Coffee",6700), ("Sugar",7100)],
    'March': [("Tea",4300), ("Coffee",9800), ("Sugar",3500)],
    'April': [("Tea",2000), ("Coffee",5060), ("Sugar",5700)],
    'May': [("Tea",5020), ("Coffee",2700), ("Sugar",4600)],
    'June': [("Tea",4500), ("Coffee",7700), ("Sugar",4100)],
    'July': [("Tea",4180), ("Coffee",7510), ("Sugar",3600)],
    'August': [("Tea",3000), ("Coffee",6100), ("Sugar",3000)],
    'September': [("Tea",8200), ("Coffee",8400), ("Sugar",2400)],
    'October': [("Tea",1290), ("Coffee",9100), ("Sugar",1430)],
    'November': [("Tea",2150), ("Coffee",9200), ("Sugar",6800)],
    'December': [("Tea",5730), ("Coffee",8950), ("Sugar",10300)],
    }

# functions are named according to its purposes

def averegeMonthlySales(data, month):
    sum = 0
    for item in data[month]:
        sum+=item[1]
    return sum / len(data[month])

# print('February: ', averegeMonthlySales(data, 'February'))
# print('January: ', averegeMonthlySales(data, 'January'))

def averegeProductSales(data, product):
    sum = 0
    for item in data.items():
        for p in item[1]:
            if(p[0] == product):
                sum += p[1]
    return sum / len(data)

# print('Tea: ', averegeProductSales(data, 'Tea'))
# print('Coffee: ', averegeProductSales(data, 'Coffee'))

def maxMonthlySales(data):
    sum = 0
    maxMonth = ('',0)
    for item in data.items():
        sum = 0
        for p in item[1]:
           sum += p[1]
        if(sum > maxMonth[1]):
            maxMonth = (item[0],sum)
    return maxMonth[0]

# print('Max month: ', maxMonthlySales(data))

def maxProductSales(data):
    monthlyTotalSales = {}
    for item in data.items():
        for p in item[1]:
            monthlyTotalSales[p[0]] = 0
    for item in data.items():
        for p in item[1]:
           monthlyTotalSales[p[0]] += p[1]
    maxProduct = ('',0)
    for item in monthlyTotalSales.items():
        if(item[1]> maxProduct[1]):
            maxProduct = (item[0], item[1])
        
    return maxProduct[0]

# print('total product sales : ', maxProductSales(data))


 

def writeDataToFile(data):
    json_object = json.dumps(data, indent=4)
    with open("data.json", "w") as outfile:
          outfile.write(json_object)
          
# writeDataToFile(data)

# when data are restored from the file, we get them as dictionary of list of list
# so we need this function to be applied on each list of list,which result in list of tuples (original format of data structure).
# staying in list of list data structure is not going to make issues with functions though.
def listOfListToListOfTuples(listOfList):
    listOfTuples = []
    for item in listOfList:
        listOfTuples.append((item[0],item[1]))
    return listOfTuples
    

def readDataToFile():
    data = {}
    with open('data.json', 'r') as openfile:
        data = json.load(openfile)
    convertedData = {}
    for item in data.items():
        convertedData[item[0]] = listOfListToListOfTuples(item[1])
    return convertedData

fileData = readDataToFile()

print(fileData)
print('February: ', averegeMonthlySales(fileData, 'February'))
print('January: ', averegeMonthlySales(fileData, 'January'))
print('Tea: ', averegeProductSales(fileData, 'Tea'))
print('Coffee: ', averegeProductSales(fileData, 'Coffee'))
print('total product sales : ', maxProductSales(fileData))


        
    