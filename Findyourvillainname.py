import datetime
FORMAT_STRING = '%d/%m/%Y'

def get_villain_name(birthdate: datetime) -> str: 

        first = [ "The Evil","The Vile", "The Cruel", "The Trashy","The Despicable", "The Embarrassing", 
                "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
        last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]

        month_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        days_counter = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


        def return_name_mapping_lists(mapping_list_1: list, mapping_list_2: list) -> dict:
                return dict(zip(mapping_list_1, mapping_list_2))
                        

        def format_datetime_object(birthdate: datetime) -> datetime:
                return birthdate.month, birthdate.day

        
        month, day = format_datetime_object(birthdate)

        month_mapping = return_name_mapping_lists(month_numbers, first)
        day_mapping = return_name_mapping_lists(days_counter, last)
       

        return f'{month_mapping[str(month)]} {day_mapping[str(day % 10)]}'


print(get_villain_name(datetime.datetime.strptime("07/11/1996", FORMAT_STRING)))