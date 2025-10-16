# Name: Levi Barense
# Dataset: Sample Superstore Dataset
# Calculation #1: Calculate the average revenue per region given
# Calculation #2: Calculate the average revenue per given product category
# Column #1: Category
# Column #2: Sales
# Column #3: Region



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

def retrieveRegion(data):
    regions = []
    for x in data:
        if x[6] not in regions:
            regions.append(x[6])
    print (regions)
    regionSel = input(f"Select a Region")
    print (regionSel)
    dict = {}
    for x in range(len(data)):
        # print (x)
        if (data[x][6]) == regionSel:
            dict[x] = [regionSel, (data[x][3]), (data[x][4]), (data[x][5]), (data[x][7]), f"Product: {data[x][8]}", (data[x][9])]
    # max_key = max(dict.keys())
    # print("max key:" , max_key)
    return dict
            


        

def revPerRegion(data):
    # print (data)
    totalRev = 0
    quant = 0
    for x in data.values():
        totalRev += float(x[-1])
        quant += 1
        # print (totalRev)
    return totalRev / quant

def revPerCategory(category, data):
    totalRev = 0
    quant = 0
    for x in data.values():
            totalRev += float(x[-1])
            quant += 1
    return totalRev / quant


raw = starter()
regionD = retrieveRegion(raw)
avgRegionRev = revPerRegion(regionD)

 

# ['West', 'Anaheim', 'California', '92804', 'West', 'Office Supplies']

# def main(regSelection):                
#     raw = starter()
#     print 
#     regionD = (retrieveRegion(raw))
#     revPerRegion(regSelection, regionD)
    #
    # print(revPerCategory(, data))
#
# main(regionSelection 