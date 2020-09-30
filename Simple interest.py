# program to calculate simple interest
def simple_interest(Principal,Rate,Time):
    SI = (Principal * Rate * Time)/100
    return SI


P =float(input("Enter Principal\n"))
R =float(input("Enter Rate\n"))
T =float(input("Enter Time\n"))
print("Simple Interest is",simple_interest(P,R,T))

