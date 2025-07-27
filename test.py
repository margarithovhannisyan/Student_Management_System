try:
    num=int(input("Enter a number"))
    result=10/num
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Result is", result)
finally:
    print("Execution completed")