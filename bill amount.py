qty = float(input("Enter the quantity of item sold : "))
val = float(input("Enter the value of item: "))
discount = float(input ("Enter the discount percentage : "))
tax = float (input ("Enter the tax : "))
amt = qty*val
discount_amt = (amt*discount) /100
sub_total = amt-discount_amt
tax_amt = (sub_total*tax)/100
total_amt = sub_total + tax_amt
print("**********BILL************")
print("Quantity sold : \t",qty)
print("Price per item : \t",val)
print("\n\t\t\t ----------")
print("Amount : \t\t" , amt)
print("Discount :\t\t-", discount_amt)
print("\t\t\t ---------- ")
print("Discounted Total : \t " , sub_total)
print("Tax :\t\t\t+",tax_amt)
print( " \t\t\t -----------")
print("Total amount to be paid ",total_amt)
