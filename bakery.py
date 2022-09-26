new=int(input("enter the no.of new loaves:"))
old=int(input("enter the no.of old loaves:"))
rate_new=185*new
rate_old = (185-(0.60*185))*old
if(new<=0):
    print("enter real amount")
else:
    print("regular amount: 185")
    print("amount new loaves:",rate_new)
    print("amount old loaves:",rate_old)
    print("total amount:",rate_new+ rate_old)
