import re
zip_code_filter = r"([0-9]{0,}\W)([A-Za-z]\D+)([A-Z]{2}\s[0-9]{5})"

def zip_code_in_adresses(adresses: list[tuple[str, str, str]], zipcode: str) -> bool:

    for adress in adresses:
        if zipcode in adress:
            return True

    return False

def filter_for_zipcode(adresses: list[tuple[str, str, str]], zipcode: str) -> list[tuple[str, str, str]]:
    filtered = list()
    
    for adress in adresses:
        if zipcode in adress:
            filtered.append(adress)

    return filtered

def finalize_return_string(adresses: list[tuple[str, str, str]]) -> str:
    housenumber, street_adress, zipcode = adresses[0]
    housenumber = housenumber.strip()
    street_adress= street_adress.strip()
    result_string = zipcode + ":"
    
    for adress in adresses[1:]:
        street_adress += f",{adress[1].strip()}"
        housenumber += f",{adress[0].strip()}"

    result_string += f"{street_adress}/{housenumber}"
    return result_string


def travel(adresses: str, zipcode: str) -> str:

    raw_adress_groups = re.findall(r"([0-9]{1,}?\W)([A-Za-z]\D+)([A-Z]{2}\s[0-9]{5})", adresses) 
    # extracts all infromation. first number is housenumber, 2nd is street, 3rd is zipcode
    

    filtered= filter_for_zipcode(adresses= raw_adress_groups, zipcode= zipcode)
    if not zip_code_in_adresses(filtered, zipcode):
        return f"{zipcode}:/"

    return finalize_return_string(adresses= filtered)
        


ad = ("123 Main Street St. Louisville OH 43071 ,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")



print(travel(ad,"AE 56210"))