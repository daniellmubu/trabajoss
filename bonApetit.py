def billApetit(bill,k,b):
    total = sum(bill)
    total -= bill(k)
    if b- bill//2:
        print('Bon Appetit')
    else:
        print(total-b//2)