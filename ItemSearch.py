class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return self.__str__()   #obj is in container (predefined class), so to call UDT you must first tell the container where to find __str__ 
    def __str__(self):
        return "Name: " + self.name + " , Price: $" + super.__str__(self.price) #super. to access python built-in methods for st()
    def __lt__(self, other):
        return self.name < other.name

class masterList(object):
    def __init__(self):
        self.masterlist = [[] for i in range(26)] #makes empty list 26 times // list comprehension
    def input(self, productList):
        for product in productList:
            index = ord(product.name[0]) % 65
            self.masterlist[index].append(product)
    def __str__(self):
        for item in self.masterlist:
            print(item)
        return " "

#binary search can only be use if list is sorted
def binary(user_input, listSection, lowerBound, upperBound):
        if (upperBound >= lowerBound):
            mid = (upperBound + lowerBound) // 2
            string = listSection[mid].name.upper()
            if (string == user_input):
                print(listSection[mid])
                return True
            elif (string > user_input):
                return binary(user_input, listSection, lowerBound, mid-1)
            else:
                return binary(user_input, listSection, mid+1, upperBound)
        else:
            print("Your item is not found")
            return False        


file_handle = open("UProducts.csv", "r")
productList = []                                    # empty list that will hold entire product list
for line in file_handle:
    lists = line.split(",")                         # lists is a list convoy - a filer var that is reassigned each time in order to append or create (eg an obj)
    createObj = product(lists[0],float(lists[1]))   # using createObj as a convoy to create each obj. lists[0] --> name; lists[1] --> price.
    productList.append(createObj)                   # adds each product obj (which has 1 - product name, and 2 - product price) to end of productList
productList.sort()                                  # sort() sorts by unicode value.

mList = masterList()                                # now, we're using mList as a convoy to create 
mList.input(productList)
                                                    #print(mList) to check




user_input = input("Please enter a product name: ")
user_input = user_input.upper()                     # make case insensitive
listSection = ord(user_input[0]) % 65               #find out first letter of user search, puts it in listSection.
binary(user_input,mList.masterlist[listSection], 0, len(mList.masterlist[listSection]) - 1)

#OUTPUT EXAMPLE
#Please enter a product name: [User enters 'yeast']
#Name: Yeast , Price: $16.48
