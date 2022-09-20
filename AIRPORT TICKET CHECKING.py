user_name=input("enter your name:")
ticket_number="5656"
if "user_name" and "ticket_number":
    print("your ticket is valid")
if "user_name" or "ticket_number":
    print("you can travel")
else:
    print("sorry,your ticket is unvalid")
covid19_result=input("enter your covid19 result:")
if covid19_result=="positive":
    print("you are not allowed")
else:
    print("you can continue the journey")
if covid19_result=="negative":
    print("you are allowed")
else:
    print("you cannot continue the journey")
verification_proof=("passport,visa,boarding pass,corona certificate")
if verification_proof=="passport"and "visa"and"boarding pass"and"corona certificate":
    print("you are proof is vallid")
if verification_proof==(not("passport"or "visa"or"boarding pass"or"corona certificate")):
    print("please add your original proof")
else:
    print("please check your correct proof")
luggage_weight="20"
if"luggage_weight"<"30":
    print("you are not allowed")
luggage_weight="20"
if"luggage_weight">"20":
    print("you are allowed") 
else:
    print("please reduce your weight untill you pay the penality")
flight_name="vistara"
print("enter your flight name")
if flight_name=="vistara":
    print("your flight name is valid")
else:
    print("not valid")
    seat_number="65"
if"seat_number"=="seat_number"and"65":
    print("your seat is available")
else:
    print("please check your seat number")
boarding_pass="verified"
if"boarding_pass"or"verified":
    print("your boarding pass is successfully verified")
    print("welcome to vistra airlines")
    print("enjoy your journey")
else:
    print("your pass is unvalid")








