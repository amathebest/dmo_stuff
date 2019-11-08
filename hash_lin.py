import sys

class Page:
    keys = []
    index = 0
    bitmap = False
    overflow = []

    def __init__(self, index):
        self.keys = []
        self.index = index
        self.bitmap = False
        self.overflow = []

    def __str__(self):
        return ("Page " + str(self.index) + ": [" + ",".join(map(str, self.keys))+ "] " + str(self.bitmap))

# function that returns the module of the whole division between the value and the d-power of 2
def hash_fun(value, d):
    return value % pow(2, d)


# initial parameters
if len(sys.argv) < 3:
    d = 1
    max_len = 2
else:
    d = sys.argv[1]         # initial number of pages
    max_len = sys.argv[2]   # max lenght of the pages
d = int(d)                  # casting d to int because sys.argv by default returns a string
p = 0                       # starting index of the page to be splitted
bitmap = []                 # array that stores if the page has already been splitted
pages = []                  # array that will contain the pages

# initial allocation of d pages
for i in range(0, d+1):
    page = Page(i)
    pages.append(page)

# infinite loop that asks the user to input a value that will be stored in the pages
while True:
    value = input("Input a number (e to terminate): ")
    if value == "e":
        print("Exiting program..")
        break
    value = int(value)
    hash_val = hash_fun(value, d)
    if len(pages[hash_val].keys) != max_len:
        pages[hash_val].keys.append(value)
    else:
        pages[hash_val].overflow.append(value)
        new_page = Page(len(pages))
        pages.append(new_page)
        all_keys = pages[p].keys + pages[p].overflow
        for key in all_keys:
            new_hash = hash_fun(key, d+1)
            if len(pages[new_hash].keys) != max_len:
                pages[new_hash].keys.append(key)
            else:
                pages[new_hash].overflow.append(key)
        p = p+1
        if p == pow(2, d):
            p = 0
            d = d+1

    for idx, page in enumerate(pages):
        print(page)
