def computepay(h,r):
    if h <= 40:
        return h*r
    else:
        return 40*r+(h-40)*(1.5*r)

hrs = float(raw_input("Enter Hours:"))
rph = float(raw_input("Rate per Hours:"))

p = computepay(hrs,rph)
print '%.2f'%(p)