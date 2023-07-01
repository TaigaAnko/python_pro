import requests
import sqlite3
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

def create_game_title_database():
    """

    データベースを作成するコード

    """
    for generation_id in generations:
        conn = sqlite3.connect(f'game_title_db/{generation_id}.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS pokemon (id INTEGER PRIMARY KEY, name TEXT, en_name, type TEXT, ability TEXT, item TEXT, image TEXT)')
        conn.commit()
        conn.close()

def store_pokemon_names(generation_id):
    """

    データベースファイルを開いて、名前を保存していく。

    """
    response = requests.get(f'https://pokeapi.co/api/v2/pokedex/{generation_id}')
    if response.status_code == 200:
        data = response.json()
        pokemon_entries = data.get('pokemon_entries', [])
        db_filename = f'game_title_db/{generation_id}.db'
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        for entry in pokemon_entries:
            pokemon_species = entry.get('pokemon_species', {})
            pokemon_name = get_pokemon_name(pokemon_species.get('url'))
            en_pokemon_name = get_pokemon_en_name(pokemon_species.get('url'))
            print(pokemon_name, en_pokemon_name)
            cursor.execute('INSERT INTO pokemon (name, en_name) VALUES (?, ?)',(pokemon_name, en_pokemon_name))
        conn.commit()
        conn.close()

def get_pokemon_name(url):
    """

    store_pokemon_names()で使用。
    英語名から日本語名に修正するためのコード

    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        names = data.get('names', [])
        japanese_name = next((n['name'] for n in names if n['language']['name'] == 'ja'), '')
        return japanese_name

def get_pokemon_en_name(url):
    """

    store_pokemon_names()で使用。
    英語名を格納するコード

    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        names = data.get('names', [])
        en_name = next((n['name'] for n in names if n['language']['name'] == 'en'), '')
        return en_name

# ゲームタイトルごとのデータベースの作成とポケモン名の格納
for generation_id in generations:
    store_pokemon_names(generation_id)

"""

1: all
2: Red and Green (1st generation)
3: Gold and Silver (2nd generation)
4: Ruby and Sapphire and Emerald" (3rd generation)
5: Diamond and Pearl (4th generation)
6: Platinum (4th generation)
7: HeartGold and SoulSilver (4th generation)
8: Black and White (5th generation)
9: Black2 and White2 (5th generation)
10: None
11: I'm not sure.
12: X and Y central (6th generation)
13: X and Y coast (6th generation)
14: X and Y mountain (6th generation)
15: Omega Ruby and Alpha Sapphire (6th generation)
16: Sun and Moon (7th generation)
17: Sun and Moon Melemele Island (7th generation)
18: Sun and Moon Akala Island (7th generation)
19: Sun and Moon Ula'ula Island (7th generation)
20: Sun and Moon Poni Island (7th generation)
21: Ultra Sun and Ultra Moon (7th generation)
22: Ultra Sun and Ultra Moon Melemele Island (7th generation)
23: Ultra Sun and Ultra Moon Akala Island (7th generation)
24: Ultra Sun and Ultra Moon Ula'ula Island (7th generation)
25: Ultra Sun and Ultra Moon Poni Island (7th generation)
26: Let's Go, Pikachu! and Let's Go, Eevee! (7th generation)
27: Sword and Shield (8th generation)
28: Sword and Shield The Isle of Armor (8th generation)
29: Sword and Shield The Crown Tundra (8th generation)
30: Pokémon Legends: Arceus (8th generation)
31: Scarlet and Violet (9th generation)
32: coming soon
33: coming soon

"""