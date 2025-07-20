from stats import *
import sys
if len(sys.argv)==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def main(path):
        get_book_text(path)
        #print(Ccounter(path))
        print(ssortings(path))
    main(sys.argv[1])
