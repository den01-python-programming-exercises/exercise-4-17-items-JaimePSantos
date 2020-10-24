from item import Item
def main():
    #write your code below this line
    itemList = []
    while(True):
      string = input("Name: ")
      if not string:
        break
      itemList.append(Item(string))
    
    for item in itemList:
      print(item)

if __name__ == '__main__':
    main()
