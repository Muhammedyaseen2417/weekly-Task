headset=[{'name': 'Boat', 'bid': 1, 'model':'Airpods','stock': 5, 'price': 2000},{'name': 'Realme', 'bid': 2,'model':'Neckbant','stock': 7, 'price': 2500},{'name': 'Noice', 'bid': 3,'model':'Airpods', 'stock': 4, 'price': 3000},{'name': 'GoVo', 'bid': 4,'model':'Neckbant', 'stock': 8, 'price': 4000}]
while True:
    print('''
          1.headset  Detailes
          2.View the headset Detailes
          3.update Headset
          4.Remove the headset
          5.search the headset
          6.exit''')
    choice=int(input("Enter the Choice : "))
    if choice==1:
        name=str(input("Name of headset : "))
        bid=int(input("Headset  Id : "))
        model=str(input("headset Model: "))
        stock=int(input("headset Stock: "))
        price=int(input("headset Price"))
        headset.append({'name':name,'id':bid,model:'model','model':model,'stock':stock,'price':price})

    elif choice==2:
        for i in headset:
            print(i)
    
    elif choice==3:
        print('''
                1.Boat
                2.Realme
                3.Noice
                4.GoVo
                        ''')
        id=int(input("Enter the Id of Product : "))
        f=0
        for i in headset:
            if id==i['bid']:
                    while True:
                        print('''
                        1.headset Name
                        2.Stock of headset
                        3.Headset Price
                        4.Exit
                    ''')
                    
                        choice=int(input("Enter the Choice"))
                        if choice==1:
                            name=str(input("Headset name :"))
                            i['name']=name                                               
                        elif choice==2:
                            stock=int(input("stock of Headset :"))
                            i['stock']=stock
                        elif choice==3:
                            price=int(input("Headset price :"))
                            i['price']=price
                        elif choice==4:
                            break
                        else:
                            print("Invalid choice")
                        f=1
        if f==0:
            print(" invalid id ")
    elif choice==4:
        id=int(input("Enter the id"))
        f=0                                                                      
        for i in headset:
            if id==i['bid']:
                headset.remove(i)
                f=1
        if f==0:
            print("Invalid id")

    elif choice==5:
        id=int(input("Enter the Id "))
        f=0
        for i in headset:
            if id==i['bid']:                                                          
                print(i)
                f=1
        if f==0:
            print("Invalid id")

    elif choice==6:
        break
    else:
        print("invalid choice")