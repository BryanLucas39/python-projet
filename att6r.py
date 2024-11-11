school_shift = (input("Enter your school shift time: for Morning insert (m), for Afternoon insert(a), for Evening insert (e):\n"))

if school_shift == "m" or  school_shift == "M":
    print("Your school shift time is at the Morning ")

elif school_shift == "a" or  school_shift == "A":
    print("Your school shift time is at the Afternoon")

elif school_shift == "e" or  school_shift == "E":
    print("Your school shift time are at the Evening")

else:
    print("Please, occured a ERROR during the info insertion, please try again")