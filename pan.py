while (1):
    name = input("\n Enter your name : ")
    if name.isalpha() == False:
        print("Invalid Name, Sorry you cannot proceed." )
        break
    else:
        pan_card_no = input("\n Enter your PAN card number : ")
        if pan_card_no.isalnum() == False:
            print ("Invalid PAN card Number, Sorry you cannot proceed.")
            break
    print("Please check, "+name+", your PAN card number is : "+pan_card_no)
    break
