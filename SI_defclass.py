# SI calculation using  def

def simple_interest(p,n,r):
    print('the principal amt is',p)
    print('the rate of  interest s',n)
    print('the number of years',r)
    si= (p*n*r)/100
    return si

#input from the user

p=int(input("enter the principal amt:"))
n=int(input("enter the number of years:"))
r=float(input("enter the rare of interest:"))
print("the simple interest is:", simple_interest(p,n,r))
