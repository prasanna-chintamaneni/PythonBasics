"""
    PRIORITY ORDER
    1.()
    2. **
    3. * / // %
    4. + -
"""
print(10-3**2//2*10+1)
"""At first go with power i.e., 3**2=9
now we can see that * and // have the same priority so go from left hand side then 9//2-->4 and now multiply 4*10-->40
next again we have same priority for - and + so come from left hand side
10-40-->-30 then finally -30+1
we get output as -29"""