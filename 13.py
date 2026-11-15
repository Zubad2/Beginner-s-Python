#-   Input marks for three subjects and calculate the average.
History= int(input("Enter marks for history: "))
Maths= int(input("Enter marks for maths: "))
Science= int(input("Enter marks for science: "))

Average= (History + Maths + Science) / 3
print("Average marks:", Average)

if History >= 80 and History <=100:
    print("You have scored A grade in History.")
elif History >= 70 and History < 80:
    print("You have scored B grade in History.")
elif History >= 60 and History < 70:
    print("You have scored C grade in History.")
elif History >= 40 and History < 60:
    print("You have scored D grade in History.")
else:
    print("You have scored F grade in History.")

if Maths >= 80 and Maths <=100:
    print("You have scored A grade in Maths.")
elif Maths >= 70 and Maths < 80:
    print("You have scored B grade in Maths.")
elif Maths >= 60 and Maths < 70:
    print("You have scored C grade in Maths.")
elif Maths >= 40 and Maths < 60:
    print("You have scored D grade in Maths.")  
else:
    print("You have scored F grade in Maths.")      

if Science >= 80 and Science <=100: 
    print("You have scored A grade in Science.")
elif Science >= 70 and Science < 80:
    print("You have scored B grade in Science.")
elif Science >= 60 and Science < 70:
    print("You have scored C grade in Science.")
elif Science >= 40 and Science < 60:
    print("You have scored D grade in Science.")
else:
    print("You have scored F grade in Science.")
    
