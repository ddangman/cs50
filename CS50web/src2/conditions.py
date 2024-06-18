n = input("Number: ")

def is_float(value):
  if value is None:
      return False
  try:
      float(value)
      return True
  except:
      return False

if is_float(n):
    n = float(n)
    if n > 0:
        print("n is positive")
    elif n < 0:
        print("n is negative")
    else:
        print("n is 0")
else:
    print("n is not a number")
