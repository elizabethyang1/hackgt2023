import csv
from datetime import datetime

necessities = []
nonnecessities = []

with open('consumerData.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        date, name, category, necessity, price = row
        
        price = float(price)
        
        if necessity == 'Yes':
            necessities.append([date, name, price, category])
        else:
            nonnecessities.append([date, name, price, category])
            
necessities = sorted(necessities, key=lambda x: datetime.strptime(x[0], '%m/%d/%Y')) 
nonnecessities = sorted(nonnecessities, key=lambda x: datetime.strptime(x[0], '%m/%d/%Y'))

with open('necessities.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Name', 'Price', 'Category']) 
    writer.writerows(necessities)
    
with open('nonnecessities.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Name', 'Price', 'Category'])
    writer.writerows(nonnecessities)

print('done')
