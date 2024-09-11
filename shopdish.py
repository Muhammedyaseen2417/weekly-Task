headset=[{'hsid':1,'name':'Boat','model':"Airpod","color":"white","driver":'13mm',"year":"1year","price":2000,},{'hsid':2,'name':'Realme','model':"Neckbant","color":"Black","driver":'11mm',"year":"1year","price":1000,},{'hsid':3,'name':'Oneplus','model':"Neckbant","color":"blue","driver":'10mm',"year":"1year","price":2500,},{'hsid':4,'name':'Noice','model':"Airpod","color":"white","driver":'12mm',"year":"1year","price":3500,}]
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
        hsid=int(input(" Headsett Id : "))
        name=str(input(" Headst Name :"))
        model=str(input("Headset Model"))
        color=str(input("Color of Headset : "))
        driver=str(input(" Headset Driver : "))
        waranty=str(input(" Headset waranty : "))
        price=int(input(" HeadsetPrice :"))
        headset.append({'hsid':id,'name':name,'model':model,'color':color,'driver':driver,'waranty':waranty,'price':price})
elif choice==2:
        for i in headset:
            print(i)

elif choice==3:
        print('''
              1.Boat
              2.Realme
              3.Oneplus
              4.Noice''')
        
        id=int(input("Enter the Id of Headset : "))
        f=0
        for i in headset:
            if id==i['hsid']:
                    while True:
                        print('''
                        1.Headset Name
                        2.Headset color
                        3.Headset price
                        4.Exit
                    ''')
                    
                        choice=int(input("Enter the Choice"))
                        if choice==1:
                            name=str(input(" Headset Name :"))
                            i['name']=name                                               
                        elif choice==2:
                            color=str(input("Headset color:"))
                            i['color']=color
                        elif choice==3:
                            price=int(input("Headset price :"))
                            i['price']=price
                        else:
                            print("Invalid choice")
                        f=1
        if f==0:
            print(" invalid id ")
