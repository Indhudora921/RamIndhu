print("*******welcome to taj hotel in mumbai***********")
print("******purely non veg & kfc foods are available***************")

print("1.chicken biriyani")
print("2.mutton biriyani")
print("3.chicken lollipop")
print("4.butter chicken")
print("5.dhanthoori")
print("6.fish pakkoda")
print("7.chicken burger")
print("8.shawarma")
 
def data1(price_ch1,price_ch2):
    if price1<=100:
       
        print("only plain biriyani available for your budjet")
        print(f"chicken plain biriyani price is{price_ch1}")

    else:

        print(" chicken  biriyani  available")
        print(f"chicken biriyani price is{price_ch2}")

def data2(price_mb1,price_mb2):
    if price2<=170:
       
        print("only half mutton biriyani is available now")
        print(f"mutton biriyani price is{price_mb1}")

    else:

       print("mutton biriyani available")
       print(f"mutton biriyani price is{price_mb2}")

def data3(price_cl1,price_cl2):
    if price3<=80:
       
        print("only 4 piece chicken lollipop available now")
        print(f"chicken lollipop price is{price_cl1}")

    else:

        print("20 piece chicken lollipop available")
        print(f"chicken lollipop price is{price_cl2}")

def data4(price_bc1,pricebc2):
    if price4<=140:
        
        print("only half butter chicken is available is now")
        print(f"butter chicken price is{price_bc1}")

    else:

        print("butter chicken available")
        print(f"butter chicken price is{price_bc2}")
        
def data5(price_dt1,price_dt2):
    if price5<=160:
       
        print("only half dhanthoori is available now")
        print(f"dhanthoori price is{price_dt1}")

    else:
       
        print("full dhanthoori is available")
        print(f"dhanthoori price is{price_dt2}")

def data6(price_fp1,price_fp2):
    if price6<=60:

     print("only 2piece fish pakkoda available now")
     print(f"fish pakkoda price is{price_fp1}")

    else:

     print("fish pakkoda is available")
     print(f"fish pakkoda price is{price_fp2}")

def data7(price_cb1,price_cb2):
    if price7<=320:
    
      print("only veg burger is available now")
      print(f"chicken burger price is{price_cb1}")

    else:

     print("chicken burger is available")
     print(f"chicken burger price is{price_cb2}")

def data8(price_sa1,price_sa2):
    if price8<=210:

        print("only veg shawarma is available now")
        print(f"shawarma price is{price_sa1}")
    else:

        print("shawarma is available ")
        print(f"shawarma price is{price_sa2}")

user=int(input("enter your number:"))

if user==1:

        price1=int(input("enter your budget"))
        data1(100,200)

elif user==2:

       price2=int(input("enter your budget"))
       data2(170,270)

elif user==3:
    
      price3=int(input("enter your budget"))
      data3(80,180)

elif user==4:
    
      price4=int(input("enter your budget"))
      data4(140,240)

elif user==5:
    
     price5=int(input("enter your budget"))
     data5(160,260)

elif user==6:
   
     price6==int(input("enter your budget"))
     data6(60,120)

elif user==7:
   
     price7=int(input("enter your budget"))
     data7(320,420)

elif user==8:

     price8=int(input("enter your budget"))
     data(210,310)

else:
     print("only 1 to 8") 






   