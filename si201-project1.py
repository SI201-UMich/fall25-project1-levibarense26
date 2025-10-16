# Name: Levi Barense
# Dataset: Sample Superstore Dataset
# Calculation #1: Calculate the average revenue per region given
# Calculation #2: Calculate the average revenue per given product category
# Column #1: Category
# Column #2: Sales
# Column #3: Region


import random
import os

    


def starter():
    import csv
    data = []
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "SampleSuperstore.csv")
    with open(file_path, newline = '') as f:
        reader = csv.reader(f)
        for x in reader:
            # print(x)
            data.append(x)
        
    return data

def retrieveRegion(datawithheader):
    data = datawithheader[1:]
    regions = []
    for x in data:
        if x[6] not in regions:
            regions.append(x[6])
    print (regions)
    regionSel = input(f"Select a Region")
    # account for typos and test
    print (regionSel)
    dict = {}
    reg = []
    for x in range(len(data)):
        # print (x)
        if (data[x][6]) == regionSel:
            reg.append(x)
    print (f" There are {(len(reg))} rows in this region")
    for x in range(len(reg)):
        dict[x] = [regionSel, (data[x][3]), (data[x][4]), (data[x][5]), (data[x][7]), (data[x][8]), (data[x][9]), (data[x][12]), (data[x][10])]

    return dict
            

['East', 'City', 'State', 'Postal Code', 'Category', 'Sub-Category', 'Sales']
        

def revPerRegion(data):
    # print (data)
    totalRev = 0
    quant = 0
    for x in data.values():
        totalRev += float(x[6])
        quant += 1
        # print (totalRev)
    return totalRev / quant

def revPerCategory(category, data):
    totalRev = 0
    quant = 0
    for x in data.values():
        if x[4] == category:
            totalRev += float(x[6])
            quant += 1
    return totalRev / quant

def retrieveCategory(data):
    cats = []
    for x in data.values():
        if x[4] not in cats:
            cats.append(x[4])
    print (cats)
    catSelect = input(f"Select a category")
    return catSelect

def conclusion():
    raw = starter()
    regionD = retrieveRegion(raw)
    avgRegionRev = revPerRegion(regionD)
    avgRegion = (f" The average revenue for the region is {avgRegionRev}")
    print (avgRegion)
    catSelect = retrieveCategory(regionD)
    avgCatRev = revPerCategory(catSelect, regionD)
    avgCat = (f" The average revenye of the {catSelect} category is {avgCatRev}")
    print (avgCat)
    # for x in regionD.keys():
    #     print (x) 
    keysList = list(regionD.keys())
    randKeys = random.sample(keysList, 5) 
    for x in randKeys:
        print(x, regionD[x][0])
    num = input(f"pick a number:")
    # if num isnt a int
    num = int(num)
    productInfo = (f"Your selected product is in the {regionD[num][4]}, and are {regionD[num][5]}, with {regionD[num][6]} dollars of revenue. They've earned a profit of {regionD[num][7]} dollars by selling {regionD[num][8]} units.")
    print (productInfo)


# ['South', 'Miami', 'Florida', '33180', 'Furniture', 'Product: Furnishings', '25.248']
"""
9981: ['South', 'Lafayette', 'Louisiana', '70506', 'Furniture', {'Tables'}, '85.98'], 
9988: ['South', 'Athens', 'Georgia', '30605', 'Technology', {'Accessories'}, '79.99']
"""
