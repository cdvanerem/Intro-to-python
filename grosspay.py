def computepay(h, r):
    if h <= 40:
        pay = h*r
    elif h > 40:
         pay = ((h-40)*(1.5*r) + (40*r))
    return pay

hrs = input("Enter Hours:")
rate = input("enter rate per hour")
hrs_worked = float(hrs)
hrly_rate = float(rate)

p = computepay(hrs_worked, hrly_rate)
print("Pay", p)