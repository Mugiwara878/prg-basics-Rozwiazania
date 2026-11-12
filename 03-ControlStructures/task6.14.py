ean = input("Enter EAN-13 article number: ")
if len(ean) == 13 and ean.isdigit() == True:
    print("Article number is correct")
    if ean[0:3] == "590":
            print("Article manufactured in Poland")
    else:
            print("Article manufactured is wrong")
else:
    print("Article number is incorrect")
    
   