
class groceryGoods:
    def __init__(self,no,code,name,price):
        self.no = no
        self.code = code
        self.name = name
        self.price = price

    def print(self):
        print(self.no,self.code,self.name,self.price)


def readcsv(inpath):
    file = open(inpath,"r")
    lines = file.readlines()
    l = Linkedlist()
    isFirstLine = True
    for line in lines:
        if isFirstLine == True:
            isFirstLine = False
            continue
        else:
            info = line.strip().split(",")
            grocery = groceryGoods(info[0],info[1],info[2],int(info[3]))
            l.append(grocery)
    return l

def txt_reader(file):
    with open(file,"r") as f:
        data = f.readlines()
        data =[i.strip("\n") for i in f]
        for i in range(len(data)):
            data[i][1] = float(data[i][1])
        return data



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    # append fuction
    def append(self,data):
        newnode= Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current=current.next
            current.next=newnode


    def print(self):
        current = self.head
        while current is not None:
            current.data.print()
            current = current.next

    def max(self,dumpinto):
        ls= []
        current =self.head
        if current is None:
            return
        ls.append([current.data.code,current.data.price])
        while current.next is not None:
            current = current.next
            ls.append([current.data.code,current.data.price])

        tmp = sorted(ls, key= lambda x:x[1],reverse=True)
        ans=[]
        maxprice= tmp[0][1]
        for i in ls:
            if i[1]== maxprice:
                ans.append(i[0])
        ans=  "\n".join(ans)
        with open(dumpinto,"w") as f:
            f.write(ans)
            f.close()


    def update(self,code,price):
        new_update = txt_reader("update.txt")
        print(new_update)
        dict_update={}
        for _code, _price in new_update:
            if _code not in dict_update:
                dict_update[_code]= _price
            else:
                dict_update[_code]=_price

        current = self.head
        while current is not None:
            if current.data.code in dict_update:
                current.data.price= dict_update[current.code]
            current=current.next

    def deteletduplicate(self):
        ls = []
        static_lk = []
        cur = self.head
        if cur is None:
            return
        ls.append([cur.code, cur.no])
        static_lk.append(cur)
        while cur.next is not None:
            cur = cur.next
            ls.append([cur.code, cur.no])
            static_lk.append(cur)

        store = {}
        ans = []
        for _code, _no in ls:
            if _code in store:
                ans.append(_no)
            else:
                store[_code] = 1
        ans = [str(i) for i in ans]
        ans = "\n".join(ans)
        with open("./f.txt", "w") as f:
            f.write(ans)
            f.close()

        ans = ans.split("\n")
        ans = [int(i) for i in ans]
        tmp = list(filter(lambda gro: gro.no not in ans, static_lk))
        for i in range(len(tmp)):
            tmp[i] = [tmp[i].no, tmp[i].code, tmp[i].name, tmp[i].price]
        cur.head = None




if __name__ == "__main__":
    file = "groceryGoods7.csv"
    f = readcsv(file)
    # f.print()
    f.max("update.txt")
    f.update("se21330",947)
    f.deteletduplicate()
