import re

class Inspector:
    
    def __init__(self) -> None:
        
        wanted_criminals = set()
        allowed_countries = set()
        required_documents_for_country = { } # key is the countryname, documents and regular expressions for ID are stored as seperate dicts
        passport_id_check_regex = { } # key is countryname, regex-string is value per country
        required_vaccination_for_country = { } # key is the countryname, vaccinations are values


    def receive_bulletin(self, bulletin: str) -> None:
        information = bulletin.split("\n") # generally, splits the bulletin into single information. base for futher processing


    def extract_entrant_information(self, entrant: dict[str, str]) -> dict[str, str]:
        ...

    def inspect(self, entrant: dict[str, str]) -> str:
        ...


inspector = Inspector()
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector.receive_bulletin(bulletin= bulletin)