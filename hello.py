 

class addition:
    sum=0,num=0
    def summation(num):
        
        rem = num%10
        sum += rem
        num = num/10
        if num ==0:
            return sum
        else:
            sum(num)

obj = addition()
obj.summation(123)
    
