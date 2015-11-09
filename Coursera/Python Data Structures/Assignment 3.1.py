hrs = raw_input("Enter Hours:")
h = float(hrs)
rateHrs = raw_input("Enter hourly rate:")
rate = float(rateHrs)
if h <= 40:
    print '%f'%(h*rate)
else:
    print '%.2f'%(40*rate+(h-40)*(1.5*rate))