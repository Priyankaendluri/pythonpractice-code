def is_first_digit_divisible_by_last(num):
     num_str=str(num)
     first_digit=int(num_str[0])
     last_digit=int(num_str[-1])
     return last_digit!=0 and first_digit%last_digit==0
def find_greatest_and_smallest_digit(num):
   digits=[int(d)for d in str(num)]
   return max(digits),min(digits)
def is_palindrome(num):
   return str(num)==str(num)[::-1]
def main():
  try:
    num=int(input("Enter a number:"))
    divisible=is_first_digit_divisible_by_last(num)
    print(f"is the first divisible by the last?{'yes' if divisible else 'No'}")
    greatest,smallest=find_greatest_and_smallest_digit(num)
    print(f"Greatest digit:{greatest},Smallest digit:{smallest}")
    palindrome=is_palindrome(num)
    print(f"Is the number a palindrome?{'yes' if palindrome else 'no'}")
  except ValueError:
      print("Invalid input!please enter a valid numeric value.")
if __name__=="__main__":
   main()
