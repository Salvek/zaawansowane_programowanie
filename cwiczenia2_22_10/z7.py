# Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informacje
# o browarach (dokumentacja https://www.openbrewerydb.org/documentation).
# Należy w pythonie zrobić klasę
# Brewery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
# odpowiednim typowaniem.
# W klasie należy zaimplementować magiczną metodę
# __str__ która będzie opisywała dane przechowywane w obiekcie.
# Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
# utworzyć listę 20 instancji klasy
# Brewery , którą przeiteruje i wyświetli każdy obiekt z osobna.

import requests
from typing import Optional

class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: Optional[str],
        address_2: Optional[str],
        address_3: Optional[str],
        city: str,
        state_province: Optional[str],
        postal_code: str,
        country: str,
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str],
        state: Optional[str],
        street: Optional[str],
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return (
            f"Brewery '{self.name}' ({self.brewery_type})\n"
            f"Address: {self.street or 'N/A'}, {self.city}, {self.state or 'N/A'}, {self.country}\n"
            f"Phone: {self.phone or 'N/A'}\n"
            f"Website: {self.website_url or 'N/A'}\n"
            f"Coordinates: ({self.latitude or 'N/A'}, {self.longitude or 'N/A'})\n"
        )

def main():
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    response = requests.get(url)
    data = response.json()

    breweries = []
    for item in data:
        brewery = Brewery(
            id=item.get("id"),
            name=item.get("name"),
            brewery_type=item.get("brewery_type"),
            address_1=item.get("address_1"),
            address_2=item.get("address_2"),
            address_3=item.get("address_3"),
            city=item.get("city"),
            state_province=item.get("state_province"),
            postal_code=item.get("postal_code"),
            country=item.get("country"),
            longitude=item.get("longitude"),
            latitude=item.get("latitude"),
            phone=item.get("phone"),
            website_url=item.get("website_url"),
            state=item.get("state"),
            street=item.get("street"),
        )
        breweries.append(brewery)

    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()