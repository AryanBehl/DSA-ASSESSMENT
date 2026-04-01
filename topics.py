# QUES-1: COUNT THE DIGITS OF NUMBER.
# ANS-1 ->
# num = int(input("Enter a number : "))

# def count_digit(n):
#     count = 0
#     while n != 0:
#         n = n // 10
#         count += 1
#     return count
# print("Digits : ", count_digit(num))

# QUES-2: REVERSE THE DIGITS OF NUMBER.
# ANS-2 ->
# num = int(input("Enter a number : "))

# def reverse_number(n):
#     rev = 0
#     while n != 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     return rev
# print("Number = ", reverse_number(num))

# QUES-3: CHECK NUMBER IS PRIME OR NOT.
# ANS-3 ->
# num = int(input("Enter a number : "))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) +1):
#         if n % i == 0:
#             return False
#         return True
# print("Prime = ", is_prime(num))

# QUES-4: CHECK THE NUMBER ARMSTRONG ON NOT.
# ANS-4 ->
# num = int(input("Enter a number : "))

# def is_armstrong(n):
#     temp = n
#     sum = 0
#     digits = len(str(n))

#     while temp != 0:
#         digit = temp % 10
#         sum += digit ** digits
#         temp //= 10
#     return sum == n
# print("num : ", is_armstrong(num))

# QUES-5: CHECK THE NUMBER IS PALINDROMIC OR NOT.
# ANS-5 ->
# num = int(input("Enter a number : "))

# def is_palindrome(n):
#     temp = n
#     rev = 0

#     while temp != 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp //= 10
#     return rev == n
# print("Palindrome : ", is_palindrome(num))

# QUES-6: CHECK THE NUMBER IS POWER OF TWO OR NOT.
# ANS-6 ->
# num = int(input("Enter a number : "))

# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     return (n & (n - 1)) == 0
# print("power : ", is_power_of_two(num))

# QUES-7: CALCULATE THE SUM OF THE DIGITS.
# ANS-7 ->
num = int(input("Enter a number : "))

def sum_of_digits(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total
print("Sum = ", sum_of_digits(num))