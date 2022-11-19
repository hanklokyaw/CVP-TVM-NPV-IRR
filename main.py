from CVP import CVP


choice = int(input("What do you want to calculate?\n "
                   "1.Present Value\n "
                   "2.Future Value\n "
                   "3.Interest Rate\n "
                   "4.Year(Payment times)\n"))

if choice == 1:
    fv = float(input("What is your Future Value: "))
    rate = float(input("What is your Interest Rate (such as 0.01 or 0.5): "))
    nper = float(input("What is your Year: "))
    cvp = CVP(0,fv,rate,nper,0)
    print("$",round(cvp.PV()))

elif choice == 2:
    prst_v = float(input("What is your Present Value: "))
    rate = float(input("What is your Interest Rate (such as 0.01 or 0.5): "))
    nper = float(input("What is your Year: "))
    cvp = CVP(prst_v,0,rate,nper,0)
    print("$",cvp.FV())

elif choice == 3:
    prst_v = float(input("What is your Present Value: "))
    fv = float(input("What is your Future Value: "))
    nper = float(input("What is your Year: "))
    cvp = CVP(prst_v,fv,0,nper,0)
    print(int(cvp.RATE() *100),"%")

else:
    prst_v = float(input("What is your Present Value: "))
    fv = float(input("What is your Future Value: "))
    rate = float(input("What is your Interest Rate (such as 0.01 or 0.5): "))
    cvp= CVP(prst_v,fv,rate,0,0)
    print(cvp.NPER(),"years")



# prst_v = float(input("What is your Present Value: "))
# fv = float(input("What is your Future Value: "))
# rate = float(input("What is your Interest Rate: "))
# nper = float(input("What is your Year: "))


