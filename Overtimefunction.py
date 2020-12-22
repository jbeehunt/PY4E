def computepay(h,r):
    if h <= 40:
        grosspay = h * r
    elif h > 40:
        OT= h - 40
        grosspay = OT * 15.75 + 40 * r
    return grosspay

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)
