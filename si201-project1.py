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
            data.append(x)
        
    return data


def revPerRegion(region, data):
    # print (data)
    totalRev = 0
    quant = 0
    for x in data:
        if x[6] == region:
            totalRev += float(x[-1])
            quant += 1
            # print (totalRev)
    return totalRev / quant

def revPerCategory(category, data):
    totalRev = 0
    quant = 0
    for x in data:
        if x[7] == category:
            totalRev += float(x[-1])
            quant += 1
    return totalRev / quant

            
data = starter()
print(revPerRegion("East", data))
print(revPerCategory("Technology", data))

