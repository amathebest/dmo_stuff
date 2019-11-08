import sys

class Page:
    keys = []
    index = 0
    overflow = []

    def __init__(self, index):
        self.keys = []
        self.index = index
        self.bitmap = False
        self.overflow = []

    def __str__(self):
        out = ""
        if len(self.overflow) == 0:
            out = "Page " + str(self.index) + ": [" + ",".join(map(str, self.keys)) + "]"
        else:
            out = "Page " + str(self.index) + ": [" + ",".join(map(str, self.keys))+ "], Overflow: [" + ",".join(map(str, self.overflow)) + "]"
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
p = 0                           # starting index of the page to be splitted
pages = []                      # array that will contain the pages

# initial allocation of d pages
for i in range(0, d + 1):
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

    if len(pages[hash_val].keys) < max_len:                # non-overflow code
        pages[hash_val].keys.append(value)
    else:                                                   # overflow code
        pages[hash_val].overflow.append(value)
        new_page = Page(len(pages))
        pages.append(new_page)
        all_keys = pages[p].keys + pages[p].overflow        # defining all the keys to re-map

        for key in all_keys:
            old_hash = hash_fun(key, d)
            new_hash = hash_fun(key, d+1)
            if new_hash != old_hash:                        # moving keys only if their new hash is different from the old one
                if key in pages[p].keys:
                    pages[p].keys.remove(key)
                else:
                    pages[p].overflow.remove(key)
                if len(pages[new_hash].keys) < max_len:
                    pages[new_hash].keys.append(key)
                else:
                    pages[new_hash].overflow.append(key)
            else:                                           # if the new hash is the same but it was in the overflow list
                if key in pages[new_hash].overflow:
                    if len(pages[new_hash].keys) < max_len:
                        pages[new_hash].keys.append(key)
                    else:
                        pages[new_hash].overflow.append(key)
                    pages[new_hash].overflow.remove(key)

        p = p + 1
        if p == pow(2, d):
            p = 0
            d = d + 1

    print("Current values of p and d: p = " + str(p) + ", d = " + str(d))
    for idx, page in enumerate(pages):
        print(page)
