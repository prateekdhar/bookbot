from collections import defaultdict
def get_book_text(path):
    with open (path) as f:
        n=len(f.read().split())
        print(f"Found {n} total words")
def Ccounter(path):
    d=defaultdict(int)
    with open (path) as f:
        z=f.read()
        for i in z:
            if i.isalpha():
                d[i.lower()]+=1
    return d
def ssortings(path):
    dictionary = Ccounter(path)
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_items:
        print(f"{char}: {count}")


    

