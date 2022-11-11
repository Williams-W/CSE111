def main():
    start_miles = float(input("Starting odometer:"))
    end_miles = float(input("Ending odometer:"))
    amount_gallons = float(input("Gallons used: "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k_from_mpg(mpg)

    
def miles_per_gallon(start_miles, end_miles, amount_gallons):

    mpg = float(abs(end_miles - start_miles)/ amount_gallons)
    print(f"{mpg:.1f} miles per gallon")

    return mpg

def lp100k_from_mpg(mpg):

    lp100k= float(235.215/mpg)
    print(f"{lp100k:.2f} liters per 100 kilometers")
    return lp100k

main()