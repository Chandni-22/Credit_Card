# Credit card number validation using Luhn’s way:
# Valid: 4532015112830366
# Invalid: 4532015112830365 378282246310006 378282246310005
print("Enter your credit card nuber.")
credit=int(input())
a=str(credit)
l=len(a)
if l==16:
    sum=0
    i,j=0,0
    while i<l:
        if i%2==0:
            intt=int(a[i])
            p=intt*2
            if p>=10:
                c=str(p)
                s=c[0]
                e=c[1]
                P=(int(s)+int(e))
                sum+=P
            else:
                sum+=intt*2
        else:
            intt=int(a[i])
            sum+=intt 
        i+=1
        j+=1
    if sum%10==0:
        print("Valid credit card number.") 
    else:
        print("Invalid credit card number.")       
else:
    print("Invalid credit card number.")