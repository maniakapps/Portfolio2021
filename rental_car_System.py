rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
if rentalCode == 'B' or rentalCode == 'D':
    rentalPeriod = int(input("Number of Days Rented:\n"))
else:
    rentalPeriod = int(input("Number of Weeks Rented:\n"))

budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

if rentalCode == 'B':
    baseCharge = float(rentalPeriod * budget_charge)
elif rentalCode == 'D':
    baseCharge = float(rentalPeriod * daily_charge)
elif rentalCode == 'W':
    baseCharge = float(rentalPeriod * weekly_charge)

odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")

totalMiles = int(odoEnd) - int(odoStart)

if rentalCode == 'B':
    mileCharge = 0.25 * totalMiles

averageDayMiles = totalMiles / rentalPeriod
if rentalCode == 'D':
    averageDayMiles = int(totalMiles) / int(rentalPeriod)
    if averageDayMiles <= 100:
        totalMiles = 0
    elif averageDayMiles > 100:
        extraMiles = int(averageDayMiles) - 100
        mileCharge = 0.25 * (extraMiles)

averageWeekMiles = totalMiles / rentalPeriod
if rentalCode == 'W':
    averageWeekMiles = int(totalMiles) / int(rentalPeriod)
if averageWeekMiles <= 900:
    mileCharge = 0
elif averageWeekMiles > 900:
    mileCharge = 100.00 * int(rentalPeriod)

amtDue = int(baseCharge) + int(mileCharge)

print('Rental Summary')
print('Rental Code: ' + str(rentalCode))
print('Rental Period: ' + str(rentalPeriod))
print('Starting Odometer: ' + str(odoStart))
print('Ending Odometer: ' + str(odoEnd))
print('Miles Driven: ' + str(totalMiles))
print('Amount Due: ' + '${:,.2f}'.format(amtDue))