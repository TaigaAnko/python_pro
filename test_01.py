import requests
import json

generations = {
    2: "Red and Green (1st generation)",
    3: "Gold and Silver (2nd generation)",
    4: "Ruby and Sapphire and Emerald (3rd generation)",
    5: "Diamond and Pearl (4th generation)",
    6: "Platinum (4th generation)",
    7: "HeartGold and SoulSilver (4th generation)",
    8: "Black and White (5th generation)",
    9: "Black2 and White2 (5th generation)",
    12: "X and Y central (6th generation)",
    13: "X and Y coast (6th generation)",
    14: "X and Y mountain (6th generation)",
    15: "Omega Ruby and Alpha Sapphire (6th generation)",
    16: "Sun and Moon (7th generation)",
    17: "Sun and Moon Melemele Island (7th generation)",
    18: "Sun and Moon Akala Island (7th generation)",
    19: "Sun and Moon Ula'ula Island (7th generation)",
    20: "Sun and Moon Poni Island (7th generation)",
    21: "Ultra Sun and Ultra Moon (7th generation)",
    22: "Ultra Sun and Ultra Moon Melemele Island (7th generation)",
    23: "Ultra Sun and Ultra Moon Akala Island (7th generation)",
    24: "Ultra Sun and Ultra Moon Ula'ula Island (7th generation)",
    25: "Ultra Sun and Ultra Moon Poni Island (7th generation)",
    26: "Let's Go, Pikachu! and Let's Go, Eevee! (7th generation)",
    27: "Sword and Shield (8th generation)",
    28: "Sword and Shield The Isle of Armor (8th generation)",
    29: "Sword and Shield The Crown Tundra (8th generation)",
    30: "Pokémon Legends: Arceus (8th generation)",
    31: "Scarlet and Violet (9th generation)"
}


def get_japanese_name(url):
    response = requests.get(url)
    data = response.json()
    names = data.get('names', [])
    found_dict = next((item for item in names if item['language']['name'] == 'ja-Hrkt'), None)
    if found_dict:
        # 見つかった場合、'name' の値を取得
        ja_name = found_dict['name']
    else:
        print("見つかりませんでした")

    print(ja_name)
    return ja_name

def get_japanese_types_name(url):
    response = requests.get(url)
    data = response.json()
    types = data.get('types', [])
    type_dict = {'normal': 'ノーマル',
                 'fighting': 'かくとう',
                 'flying': 'ひこう',
                 'poison': 'どく',
                 'ground': 'じめん',
                 'rock': 'いわ',
                 'bug': 'むし',
                 'ghost': 'ゴースト',
                 'steel': 'はがね',
                 'fire': 'ほのお',
                 'water': 'みず',
                 'grass': 'くさ',
                 'electric': 'でんき',
                 'psychic': 'エスパー',
                 'ice': 'こおり',
                 'dragon': 'ドラゴン',
                 'dark': 'あく',
                 'fairy':'フェアリー'}
    for slot in range(len(types)):
        type_name = types[slot]['type']['name']
        # print(type_name)
        type_ja_name = type_dict.get(type_name)
        print(type_ja_name)

def print_pokemon_names(generation_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokedex/{generation_id}/')

    data = response.json()
    pokemon_entries = data.get('pokemon_entries', [])

    for entry in pokemon_entries:
        pokemon_species = entry.get('pokemon_species', {})
        pokemon_name = pokemon_species.get('name')
        pokemon_species_url = pokemon_species.get('url')
        pokemon_url = pokemon_species_url.replace('/pokemon-species/', '/pokemon/')
        ja_name = get_japanese_name(pokemon_species_url)
        get_japanese_types_name(pokemon_url)

if __name__ == '__main__':
    for generation_id in generations:
        print_pokemon_names(generation_id)