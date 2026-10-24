name = input ("What is your name? :")
age = int(input ("How old are you? :"))
country = input ("counry of residence? :")
citizenship = input ("country of citizenship? :")
print (f" Hello {name} welcome to the station.Thank you very much {name} for your patience .if you are under 25 years old and a kenyan citizen please proceed toterminal A")
print (f"for over 25 years of age , please proceed to terminal B")
print (f"For all non citizens , please proceed to terminal C")
if age < 25 and citizenship.lower () == "kenya": 
    print ("proceed to terminal A")
elif citizenship.lower() !="kenya":  
    print ("proceed to terminal C")  
else :
    print ("please proceed to terminal B")    