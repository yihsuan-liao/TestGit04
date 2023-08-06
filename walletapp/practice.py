
def count():
    txt = "Kamisato Ayaka"
    num = 0

    for x in txt:
        if (x.lower() in ['a', 'e', 'i', 'o', 'u']):
         num += 1

    print(num)

def firstname():
    name = "Yihsuan Liao"
    print(name[0:7])

class nam:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    def display(self):
        print(self.__first)






def run():
    #count()
    #firstname()
    #judy = nam("Yihsuan", "Liao")
    #judy.display()

