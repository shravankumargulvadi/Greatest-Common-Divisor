
# coding: utf-8

# In[3]:


def gcd(p,q):
    if p>q:
        a=p
        b=q
    else:
        a=q
        b=p
    r=a%b
    if r==0:
        return b
    else:
        while r!=0:
            c=b%r
            b=r
            r=c
        return b
    

if __name__ == '__main__':
    input_n = 2
    input_numbers = [int(x) for x in input().split()]
    print(gcd(input_numbers[0],input_numbers[1]))
        
    

