# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == 'S':
  S = 15
  if add_pepperoni == 'Y':
    S += 2
    if extra_cheese == 'Y':
      S += 1
  print(f'your final bill is: ${S}')
elif size == 'M':
  M = 20
  if add_pepperoni == 'Y':
    M += 3
    if extra_cheese == 'Y':
      M += 1
  print(f'your final bill is: ${M}')
elif size == 'L':
  L = 25
  if add_pepperoni == 'Y':
    L += 3
    if extra_cheese == 'Y':
      L += 1
  print(f'your final bill is: ${L}')
else:
  print("size not known")






