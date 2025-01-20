def mortgage_payments(principal,rate,amortization): #defining function mortgage_payments 
    monthly_rate = (1+rate/100/2)**(2/12) - 1 #determine monthly rate
    semi_monthly_rate = (1+rate/100/2)**(2/24) - 1 #determine semi-monthly rate
    bi_weekly_rate = (1+rate/100/2)**(2/26) - 1 #determine bi-weekly rate
    weekly_rate = (1+rate/100/2)**(2/52) - 1 #determine weekly rate
    monthly_payment = principal / ((1-(1+monthly_rate)**(-amortization*12))/monthly_rate)
    semi_monthly_payment = principal / ((1-(1+semi_monthly_rate)**(-amortization*24))/semi_monthly_rate)
    bi_weekly_payment = principal / ((1-(1+bi_weekly_rate)**(-amortization*26))/bi_weekly_rate)
    weekly_payment = principal / ((1-(1+weekly_rate)**(-amortization*52))/weekly_rate)
    rapid_bi_weekly_payment = monthly_payment/2 
    rapid_weekly_payment = monthly_payment/4
    payments = (monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment)
    return payments

principal = float(input("Principal ($): ")) #get user input for principal amount in $, storing value as float
rate = float(input("Rate (%): ")) #get user input for interest rate in %, storing value as float
amortization = float(input("Amortization Period (years): ")) #get user input for amortization period in years, storing value as float

#below print statement runs function and prints required output
print("Monthly Payment: $" + str(format(mortgage_payments(principal,rate,amortization)[0],".2f")),
      "Semi-monthly Payment: $" + str(format(mortgage_payments(principal,rate,amortization)[1],".2f")),
        "Bi-weekly Payment: $" + str(format(mortgage_payments(principal,rate,amortization)[2],".2f")),
            "Weekly Payment: $" + str(format(mortgage_payments(principal,rate,amortization)[3],".2f")),
                "Rapid Bi-weekly Payment: $" + str(format(mortgage_payments(principal,rate,amortization)[4],".2f")),
                    "Rapid Weekly Payment: $" + str(format(mortgage_payments(principal,rate,amortization)[5],".2f")), sep="\n")