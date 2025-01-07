n = 153
num_str = str(n)
num_digits = len(num_str)
sum_of_powers = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10
if sum_of_powers == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
