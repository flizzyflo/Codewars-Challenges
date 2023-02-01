def fortune(deposit: float, interest_rate: float, yearly_withdrawal: float, final_year: int, inflation_rate: float, current_year: int = 1):
    
    if current_year == final_year:
        return 0 <= deposit
    
    deposit = int(deposit * (1 + interest_rate / 100))
    balance = deposit - yearly_withdrawal
    yearly_withdrawal = int(yearly_withdrawal * (1 + inflation_rate/100))

    return fortune(deposit= balance, 
                   interest_rate= interest_rate, 
                   yearly_withdrawal= yearly_withdrawal, 
                   final_year= final_year, 
                   inflation_rate= inflation_rate, 
                   current_year= current_year + 1)

   