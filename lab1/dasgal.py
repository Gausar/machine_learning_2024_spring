#1. Өгөгдсөн хүснэгтээс нийт ялгаатай утгатай элемэнтүүдийн тоог ол.
def count(table):
    unique_el = set()
    for row in table:
        for element in row:
            unique_el.add(element)
    return len(unique_el)

def find_unique_el():
    print("1 dehi asuult : ")
    table = []
    n = int(input("Moriin too: "))
    m = int(input("Baganii too: "))
    for i in range(n):
        row = []
        for j in range(m):
            ele = input()
            row.append(ele)
        table.append(row)
    t = count(table)
    print("yalgaatai utguud :", t)

#2. Өгөгдсөн өгүүлбэрийн үг бүр нь хэдэн удаа давтагдсанг ол.
def sentence():
    dawt = {}
    print("Oguulberee oruulaarai : ")
    str = input()
    words = str.split()
    for i in words:
        if i in dawt:
            dawt[i] += 1
        else:
            dawt[i] = 1
    for i, dawt in dawt.items():
        print(f"{i} = {dawt}")


#3. Өгөгдсөн хүснэгтээс 'xyz' тэмдэгт мөрийг агуулсан тэмдэгт мөрүүдийг хэвлэ.
def paragraph():
    print("3 dahi asuult : ")
    table = []
    n = int(input("Moriin too: "))
    m = int(input("Baganii too: "))
    print("ugnuudee oruul : ")
    for i in range(n):
        for j in range(m):
            data = input()
            r = data.split()
            if len(r) == m:
                table.append(r)
                break
    print("xyz-iig aguulsan ugs : ")
    for i in table:
        for j in i:
            if 'xyz' in j:
                print(j)

#4. Өгөгдсөн хүснэгтээс 'xyz' тэмдэгт мөрөөр эхэлсэн эсвэл төгссөн тэмдэгт мөрүүдийг хэвлэ.
def start_end_xyz():
    print("4 dehi asuult : ")
    table = []
    n = int(input("Moriin too: "))
    m = int(input("Baganii too: "))
    print("ugnuudee oruul : ")
    for i in range(n):
        for j in range(m):
            data = input()
            r = data.split()
            if len(r) == m:
                table.append(r)
                break
    print("xyz-eer ehlesen esvel togsson ugs : ")
    for i in table:
        for j in i:
            if j.startswith('xyz') or j.endswith('xyz'):
                print(j)

#5. Хамгийн эхний анхны 50 тоог олох функц бич.
def prime_num():
    print("5 : ekhnii 50-n ankhnii toonuud : ")
    prime = []
    too = 2
    i = 1
    while len(prime) < 51:
        is_prime = 0
        for i in range(2, int(too/2) + 1):
            if too % i == 0:
                is_prime = 1
                break
        if is_prime == 0:
            prime.append(too)
        too = too + 1
    print(prime)
   
def main():
    print("1. Yalgaatai element oloh\n2. Ug buriin dawtalt\n3. xyz oloh\n4. start & end xyz\n5. First 50 prime number\n6. Exit")
    while(1):
        k = int(input())
        if k == 1:
            find_unique_el()
        elif k == 2:
            sentence()
        elif k == 3:
            paragraph()
        elif k == 4:
            start_end_xyz()
        elif k == 5:
            prime_num()
        elif k > 5:
            quit()

if __name__ == "__main__":
    main()
