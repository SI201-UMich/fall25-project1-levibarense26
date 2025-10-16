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
    import random
    import os   
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
            


        

def revPerRegion(data):
    totalRev = 0
    quant = 0
    for x in data.values():
        totalRev += float(x[6])
        quant += 1
        # print (totalRev)
    return totalRev / quant

def retrieveCategory(data):
    cats = []
    for x in data.values():
        if x[4] not in cats:
            cats.append(x[4])
    if cats  == []:
        continue
    print (cats)
    catSelect = input(f"Select a category")
    return catSelect

def revPerCategory(data):
    totalRev = 0
    quant = 0
    category = retrieveCategory(data)
    for x in data.values():
        if x[4] == category:
            totalRev += float(x[6])
            quant += 1
    return totalRev / quant



def conclusion():
    raw = starter()
    regionD = retrieveRegion(raw)
    avgRegionRev = revPerRegion(regionD)
    avgRegion = (f" The average revenue for the region is {avgRegionRev}")
    print (avgRegion)
    avgCatRev = revPerCategory(regionD)
    avgCat = (f" The average revenue of the category is {avgCatRev}")
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
    productSum = (f"Your product has sold  {regionD[num][8]} units, more info availbe in productinfo{num}.txt")
    productInfo = (f"Your selected product is in the {regionD[num][4]}, and are {regionD[num][5]}, with {regionD[num][6]} dollars of revenue. They've earned a profit of {regionD[num][7]} dollars by selling this product.")
    print (productSum)
    with open ("productinfo.txt", "a") as f:
        f.write(f"Product Number{num}")
        f.write(f"{avgRegion}\n")
        f.write(f"{avgCat}\n")
        f.write(f"{productInfo}\n")

"""
['South', 'Miami', 'Florida', '33180', 'Furniture', 'Product: Furnishings', '25.248']
9981: ['South', 'Lafayette', 'Louisiana', '70506', 'Furniture', {'Tables'}, '85.98'], 
9988: ['South', 'Athens', 'Georgia', '30605', 'Technology', {'Accessories'}, '79.99']
['East', 'City', 'State', 'Postal Code', 'Category', 'Sub-Category', 'Sales']
"""
conclusion()

if __name__ == "__main__":
    # starter() tests
    try:
        data = starter()
        print("starter Test 1:", len(data) > 0)
    except Exception as e:
        print("starter Test 1 failed:", e)

    print("starter Test 2:", isinstance(data[0], list))

 
    import csv
    open("empty.csv", "w").close()
    with open("empty.csv") as f:
        reader = csv.reader(f)
        empty_data = list(reader)
    print("starter Test 4:", empty_data == [])

    # retrieveRegion() tests
    mock_data = [
        ["Row", "Test", "Data", "Code", "Category", "SubCat", "East", "Other", "Values", "Etc", "Etc", "Etc", "123"],
        ["Row", "Test", "Data", "Code", "Category", "SubCat", "West", "Other", "Values", "Etc", "Etc", "Etc", "456"]
    ]
    print("retrieveRegion Test 1:", isinstance(retrieveRegion([["Header"], *mock_data]), dict))
    print("retrieveRegion Test 2:", "East" in str(retrieveRegion([["Header"], *mock_data])))

    print("retrieveRegion Test 3:", retrieveRegion([["Header"], *mock_data]) != {"North": []})
    
    print("retrieveRegion Test 4:", retrieveRegion([]) == {})

#    revPerRegion() tests
    mock_dict = {0: ["", "", "", "", "", "", 100.0], 1: ["", "", "", "", "", "", 300.0]}
    print("revPerRegion Test 1:", round(revPerRegion(mock_dict), 2) == 200)

    mock_dict2 = {0: ["", "", "", "", "", "", 50.0], 1: ["", "", "", "", "", "", 50.0], 2: ["", "", "", "", "", "", 50.0]}
    print("revPerRegion Test 2:", revPerRegion(mock_dict2) == 50.0)

    try:
        revPerRegion({})
    except ZeroDivisionError:
        print("revPerRegion Test 3 passed: Caught ZeroDivisionError")

    mock_dict3 = {0: ["", "", "", "", "", "", "abc"]}
    try:
        revPerRegion(mock_dict3)
    except ValueError:
        print("revPerRegion Test 4 passed: Caught ValueError")

# retrieceCat()
    mock_dict = {
        0: ["", "", "", "", "Furniture", "", 100],
        1: ["", "", "", "", "Technology", "", 200]
    }
    print("retrieveCategory Test 1:", "Furniture" in str(retrieveCategory(mock_dict)))
    print("retrieveCategory Test 2:", "Technology" in str(retrieveCategory(mock_dict)))


    print("retrieveCategory Test 3:", retrieveCategory({}) == [])
    
    bad_dict = {0: ["", "", "", "", "", 100]}
    try:
        retrieveCategory(bad_dict)
    except IndexError:
        print("retrieveCategory Test 4 passed: Caught IndexError")



# revPerCategory()
    mock_data = {
        0: ["", "", "", "", "Furniture", "", 100],
        1: ["", "", "", "", "Furniture", "", 300],
        2: ["", "", "", "", "Technology", "", 500]
    }
    print("revPerCategory Test 1:", revPerCategory(mock_data) >= 0)
    print("revPerCategory Test 2:", isinstance(revPerCategory(mock_data), float))

    try:
        revPerCategory({})
    except ZeroDivisionError:
        print("revPerCategory Test 3 passed")

    bad_data = {0: ["", "", "", "", "Furniture", "", "abc"]}
    try:
        revPerCategory(bad_data)
    except ValueError:
        print("revPerCategory Test 4 passed")

        mock_dict = {
        0: ["", "", "", "", "Furniture", "", 100],
        1: ["", "", "", "", "Technology", "", 200]
    }
    
    print("retrieveCategory Test 1:", "Furniture" in str(retrieveCategory(mock_dict)))
    print("retrieveCategory Test 2:", "Technology" in str(retrieveCategory(mock_dict)))

    print("retrieveCategory Test 3:", retrieveCategory({}) == [])
    
    bad_dict = {0: ["", "", "", "", "", 100]}
    try:
        retrieveCategory(bad_dict)
    except IndexError:
        print("retrieveCategory Test 4 passed: Caught IndexError")

    # retrie