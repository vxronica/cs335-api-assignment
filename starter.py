import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_info():
    url = f"{BASE_URL}/pokemon/pikachu"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Pokemon Info ---")
        print(f"Name: {data.get('name').title()}")
        print(f"Height: {data.get('height')}")
        print(f"Weight: {data.get('weight')}")

        abilities = [a["ability"]["name"] for a in data.get("abilities", [])]
        print(f"Abilities: {', '.join(abilities)}")

        types = [t["type"]["name"] for t in data.get("types", [])]
        print(f"Types: {', '.join(types)}")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


def get_ability_info():
    url = f"{BASE_URL}/ability/static"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Ability Info ---")
        print(f"Ability: {data.get('name').title()}")

        for entry in data.get("effect_entries", []):
            if entry["language"]["name"] == "en":
                print(f"Effect: {entry.get('effect')}")
                break
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


def get_pokemon_locations():
    url = f"{BASE_URL}/pokemon/pikachu/encounters"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Where to Find Pikachu ---")

        if not data:
            print("No encounter data available.")
            return

        locations = [
            loc["location_area"]["name"]
            for loc in data
        ]
        unique_locations = list(set(locations))

        for location in unique_locations:
            print(f"- {location}")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")

def main():
    get_pokemon_info()
    get_ability_info()
    get_pokemon_locations()


if __name__ == "__main__":
    main()