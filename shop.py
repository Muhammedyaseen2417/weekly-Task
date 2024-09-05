shop=[['I phone 15',"Matt Black",1,356719534,6,256,85000],['Realme 13',"glozzy green",2,867854298623,8,128,18000,],['Vivo V40 ',"taitanium mint",3,8954678230117,8,128,36000,],["OnePlus Nord 4",'Glozzy Black',4,7890435671286,8,128,44000,]]

while True:
    print('''
          1.Mob Detailes
          2.view
          3.update
          4.delete
          5.add phone
          6.search
          7.exit''')
    choice=int(input("Enter the Choice : "))

    if choice==1:
        Mobile=str(input("Mobile Name :"))
        color=str(input("Mobile Color :"))
        id=int(input("enter the Id : "))
        imei=int(input("IMEI of Mobaile : "))
        ram=int(input("Ram : "))                       
        storage=int(input("Storage :"))
        Price=int(input("Mobile Price :"))
        shop.append([Mobile,color,imei,ram,storage,Price])

    elif choice==2:
        for i in shop:
            print(i)

    elif choice==3:
        id=int(input("Enter the ID : "))
        print(
            '''            1.change the sereis
            2.new colour
            3.new price 
                 ''')
        f=0
        for i in shop:
            if id in i:
                choice=int(input("Enter the Choice"))
                if choice==1:
                    Mobile=str(input("change the seres : "))
                    i[0]==Mobile
                elif choice==2:
                    color=str(input("Color of the Mobile :"))
                    i[1]=color                                                   
                elif choice==3:
                    Price=int(input("New price:"))
                    i[5]=Price
                f=1
        
        if f==0:
            print(" invalid id ")
        
    elif choice==4:
        id=int(input("Enter the Id of Mobile"))
        f=0                                                                       
        for i in shop:
            if id in i:
                shop.remove(i)
                f=1
        if f==0:
            print("Invalid choice")

    elif choice==5:
        id=int(input("Enter the Id of Mobile"))
        for i in shop:
            if id in i:                                                           
                dispaly=str(input("Display Size:",))
                i.append([dispaly])
                print(i)
    
    elif choice==6:
        id=int(input("Enter the Id of Mobile"))
        f=0
        for i in shop:
            if id in i:                                                          
                print(i)
                f=1
        if f==0:
            print("Invalid id")

    elif choice==7:                                                                   
        break
    else:
        print("Invalid choice")
                


        
