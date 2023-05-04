from datetime import *

def check_coupon(entered_code: str, valid_code: str, current_date: str, expiration_date: str):
    
    def code_is_valid(entered_code: str, correct_code: str) -> bool:
        if entered_code == "" or correct_code == "" or type(entered_code) == int:
            return False

        return entered_code == correct_code
        
    def date_formatter(current_date: str, expiration_date: str) -> tuple[datetime, datetime]:
        cur_date_formatted = datetime.strptime(current_date, "%B %d, %Y")
        exp_date_formatted = datetime.strptime(expiration_date, "%B %d, %Y")
        return cur_date_formatted, exp_date_formatted

    def is_expired(current_date: datetime, expiration_date: datetime) -> bool:
        return current_date <= expiration_date

    current, expiration = date_formatter(current_date, expiration_date)

    return (code_is_valid(entered_code, valid_code)) and (is_expired(current, expiration))
