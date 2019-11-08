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
        out = "Page " + str(self.index) + ", b: " + str(self.bitmap) + ", keys: [" + ",".join(map(str, self.keys)) + "]"
        return out

# function that returns the module of the whole division between the value and the d-power of 2
def hash_fun(value, d):
    return value % pow(2, d)

# initial parameters
if len(sys.argv) < 2:
    max_len = 2
else:
    max_len = int(sys.argv[1])  # max lenght of the pages
d = 1                           # initial number of pages
pages = []                      # array that will contain the pages
n_pages = 2                     # int that tracks the total number of pages

# initial allocation of d pages
for i in range(0, n_pages):
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

    reached = False
    while not reached:
        if pages[hash_val].bitmap:



    if len(pages[hash_val].keys) < max_len:                             # non-overflow code
        pages[hash_val].keys.append(value)
    else:                                                               # overflow code

















    if len(pages[hash_val].keys) < max_len:                             # non-overflow code
        pages[hash_val].keys.append(value)
    else:                                                               # overflow code
        d = d + 1
        n_pages = n_pages * 2
        pages[hash_val].overflow.append(value)
        for i in range(d, 2*d):
            new_page = Page(i)
            pages.append(new_page)
        all_keys = pages[hash_val].keys + pages[hash_val].overflow      # defining all the keys to re-map

        for key in all_keys:
            old_hash = hash_fun(key, d-1)
            new_hash = hash_fun(key, d)
            if new_hash != old_hash:                                    # moving keys only if their new hash is different from the original one
                if len(pages[new_hash].keys) < max_len:
                    pages[new_hash].keys.append(key)
                else:
                    pages[new_hash].overflow.append(key)
                if key in pages[old_hash].keys:
                    pages[old_hash].keys.remove(key)
                else:
                    pages[old_hash].overflow.remove(key)
            else:
                if key in pages[new_hash].overflow:
                    if len(pages[new_hash].keys) < max_len:
                        pages[new_hash].keys.append(key)
                    else:
                        pages[new_hash].overflow.append(key)
                    pages[new_hash].overflow.remove(key)

    print("Current value of d = " + str(d))
    for idx, page in enumerate(pages):
        print(page)
