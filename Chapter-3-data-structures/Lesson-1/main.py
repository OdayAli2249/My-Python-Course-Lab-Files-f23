# data structure
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

print('___________________')

maxMonthlySales = ('',0)

# print every month and its averege sales of all products
# iterate/loop through dictionary items
for sales in data.items():
    print(sales[0], 'averege: ')
    averege = 0
    sum = 0
    # iterate/loop through spacific dictionary's list items
    for sale in sales[1]:
        # compute total monthly sales across products
       sum += sale[1]
    # compute averege
    averege = sum / len(sales[1])
    # in each loop, we keep tracking the biggest monthly sales
    if(averege > maxMonthlySales[1]):
        maxMonthlySales = (sales[0],averege)
    print(averege)
    
    
print('___________________')
maxSales = ('',0)
# here we compute averege sales for each product type : there three types : tea, coffee, sugar
for i in range(0,3):
    sum = 0
    for sales in data.items():
        sum += sales[1][i][1]
    averege = sum / len(data)
    print('averege for ',sales[1][i][0],' is : ',averege)
    # we keep tracking the product where the biggest sales averege is found
    if(averege > maxSales[1]):
        maxSales = (sales[1][i][0],averege)
    
print('___________________')    
    
print('max monthly sales:',maxMonthlySales[0])

print('___________________')    


print('max sales:',maxSales[0])
        
        
        