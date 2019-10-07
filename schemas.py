from settings import cities_scope
import datetime

user_scheme = {
    "facebook_id": {"init": None, "db": "char(100) NOT NULL"},
    "first_name": {"init": None, "db": "varchar(100)"},
    "last_name": {"init": None, "db": "varchar(100)"},
    "gender": {"init": None, "db": "enum('Female','Male')"},
    "language": {"init": None, "db": "varchar(100)"},
    # " query parameters:, "db": "string"},
    "business_type": {"init": None, "db": "varchar(100)"},
    "housing_type": {"init": None, "db": "varchar(100)"},
    "person_type": {"init": None, "db": "varchar(100)"},
    "price_limit": {"init": None, "db": "int(1)"},
    "since": {"init": None, "db": "datetime default current_timestamp"},
    "features": {"init": None, "db": "varchar(1000)"},
    # address:
    "country": {"init": None, "db": "varchar(100)"},
    "city": {"init": None, "db": "varchar(100)"},
    "street": {"init": None, "db": "varchar(100)"},
    "latitude": {"init": 0, "db": "FLOAT"},
    "longitude": {"init": 0, "db": "FLOAT"},
    # dialogue parameters:
    "context": {"init": 'initialization', "db": "varchar(100)"},
    "interactions": {"init": 0, "db": "int(1)"},
    "shown_input": {"init": False, "db": "BOOLEAN"},
    "wants_more_features": {"init": True, "db": "BOOLEAN"},
    "wants_more_locations": {"init": True, "db": "BOOLEAN"},
    "asked_for_restart": {"init": False, "db": "BOOLEAN"},
    "wants_restart": {"init": False, "db": "BOOLEAN"},
    "confirmed_data": {"init": False, "db": "BOOLEAN"},
    "add_more": {"init": False, "db": "BOOLEAN"}
}

user_questions = {
    "interest": {"question": ["Jak mogę Ci dzisiaj pomóc?"],
                 "responses": ['🔎 Szukam pokoju', '🔎 Szukam mieszkania', '💰 Sprzedam', '💰 Kupię']},
    "housing_type": {"question": ["Jakiego typu lokal Cię interesuje?"],
                     "responses": ['🛌 pokój', '🏢 mieszkanie', '🐌 kawalerka', '🏠 dom wolnostojący']},
    "location": {"question": ["Gdzie konkretnie chciałbyś mieszkać?"],
                 "responses": ['🎯 blisko centrum', 'Mokotów', 'Wola']},
    "price_limit": {"question": ["Ile jesteś w stanie płacić? (wraz z ew. czynszem i opłatami)"],
                    "responses": ['<800zł', '<1000zł', '<1500zł', '<2000zł', '💸 dowolna kwota']},
    "city": {"question": ["Które miasto Cię interesuje?"],
             "responses": cities_scope},
    "features": {"question": ["Czy masz jakieś szczególne preferencje?", "Na czymś jeszcze Ci zależy?"],
                 "responses": ['Nie, pokaż oferty', 'od zaraz', 'przyjazne dla 🐶🐱', 'blisko do...', 'ma garaż',
                               '🔨 wyremontowane', 'umeblowane', 'ma 🛀', 'dla 🚬', 'dla 🚭']}
}

bot_phrases = {
    "greeting": ["{greeting} {first_name}! Jestem Roomek i jestem na bieżąco z rynkiem nieruchomości.",
                 "{greeting} {first_name}! Nazywam się Roomek i zajmuję się znajdywaniem najlepszych nieruchomości."],
    "default": ["Przepraszam, nie zrozumiałem",
                "Wybacz, nie rozumiem",
                "Nie do końca rozumiem"],
    "back_to_context": ["O co ja miałem spytać...", "Wracając do pytania"]
}

db_scheme = {
    "beggining": {"text": "CREATE TABLE `{table_name}` ("},
    "end": {"text": "PRIMARY KEY (`{primary_key}`)) ENGINE=InnoDB"}
}

# misc -> coś pozornie bez kategorii, ale pozwalające jednoznacznie zdeklarować, którego pola dotyczy
offer_scheme = {
    "offer_url": {"db": "varchar(700) NOT NULL", 'item_loaders': ['response_to_string'], 'scraping_path_olx': '',
                  'misc': ['Oferta od'], 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "city": {"db": "varchar(50) NOT NULL", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
             'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "housing_type": {"db": "varchar(50) NOT NULL", 'item_loaders': ['translate'], 'scraping_path_olx': '', 'misc': [],
                     'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "business_type": {"db": "varchar(50)", 'item_loaders': ['translate'], 'scraping_path_olx': '', 'misc': [],
                      'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "offer_name": {"db": "varchar(200)", 'item_loaders': ['remove_html_tags', 'remove_unnecessary_spaces'],
                   'scraping_path_olx': '//*[@id="offerdescription"]/div[2]/h1/text()', 'misc': [],
                   'scraping_path_otodom': '//*[@id="root"]/article/header/div[1]/div/div/h1/text()',
                   'scraping_path_olxroom': '//*[@id="offerdescription"]/div[2]/h1/text()'},
    "offer_thumbnail_url": {"db": "varchar(400)", 'item_loaders': ['find_image_url'],
                            'scraping_path_olx': '//*[@id="photo-gallery-opener"]/img', 'misc': [],
                            'scraping_path_otodom': '//*[@id="root"]/article/section[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/picture/img',
                            'scraping_path_olxroom': '//*[@id="photo-gallery-opener"]/img'},
    "price": {"db": "int(1)", 'item_loaders': ['just_numbers', 'integer_the_price'],
              'scraping_path_olx': '//*[@id="offeractions"]/div[1]/strong/text()', 'misc': [],
              'scraping_path_otodom': '//*[@id="root"]/article/header/div[2]/div[1]/div[2]/text()',
              'scraping_path_olxroom': '//*[@id="offeractions"]/div[1]/strong/text()'},
    "street": {"db": "varchar(50)", 'item_loaders': ['street_it'], 'scraping_path_olx': '', 'misc': [],
               'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "district": {"db": "varchar(50)", 'item_loaders': ['district'],
                 'scraping_path_olx': '//*[@id="offerdescription"]/div[2]/div[1]/a/strong/text()', 'misc': [],
                 'scraping_path_otodom': '//*[@id="root"]/article/header/div[1]/div/div/div/a/text()',
                 'scraping_path_olxroom': '//*[@id="offerdescription"]/div[2]/div[1]/a/strong/text()'},
    "date_of_the_offer": {"db": "DATETIME",
                          'item_loaders': ['remove_html_tags', 'remove_unnecessary_spaces', 'datetime_it_olx'],
                          'scraping_path_olx': '//*[@id="offerdescription"]/div[2]/div[1]/em', 'misc': [],
                          'scraping_path_otodom': '',
                          'scraping_path_olxroom': '//*[@id="offerdescription"]/div[2]/div[1]/em'},
    "offer_id": {"db": "LONGTEXT", 'item_loaders': ['just_numbers'],
                 'scraping_path_olx': '//*[@id="offerdescription"]/div[2]/div[1]/em/small/text()', 'misc': [],
                 'scraping_path_otodom': '//*[@id="root"]/article/div[3]/div[1]/div[2]/div/div[1]/text()[1]',
                 'scraping_path_olxroom': '//*[@id="offerdescription"]/div[2]/div[1]/em/small/text()'},
    "offer_text": {"db": "LONGTEXT",
                   'item_loaders': ['remove_unnecessary_spaces', 'remove_html_tags', 'swap_unnecessary_spaces'],
                   'scraping_path_olx': '//*[@id="textContent"]', 'misc': [],
                   'scraping_path_otodom': '//*[@id="root"]/article/div[3]/div[1]/section[2]/div[1]',
                   'scraping_path_olxroom': '//*[@id="textContent"]'},
    "offer_from": {"db": "varchar(25)", 'item_loaders': ['remove_html_tags', 'translate'], 'scraping_path_olx': '',
                   'misc': [], 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "apartment_level": {"db": "smallint(1)",
                        'item_loaders': ['remove_html_tags', 'word_to_numbers', 'just_numbers', 'integer_the_price'],
                        'scraping_path_olx': '', 'misc': ['Poziom'], 'scraping_path_otodom': '',
                        'scraping_path_olxroom': ''},
    "furniture": {"db": "BOOLEAN", 'item_loaders': ['remove_html_tags', 'furniture'], 'scraping_path_olx': '',
                  'misc': ['Umeblowane'], 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "type_of_building": {"db": "varchar(25)", 'item_loaders': ['remove_html_tags', 'translate'],
                         'scraping_path_olx': '', 'misc': ['Rodzaj zabudowy'], 'scraping_path_otodom': '',
                         'scraping_path_olxroom': ''},
    "area": {"db": "smallint(1)", 'item_loaders': ['remove_html_tags', 'just_numbers', 'integer_the_price'],
             'scraping_path_olx': '', 'misc': ['Powierzchnia'], 'scraping_path_otodom': '',
             'scraping_path_olxroom': ''},
    "amount_of_rooms": {"db": "int(1)",
                        'item_loaders': ['remove_html_tags', 'word_to_numbers', 'just_numbers', 'integer_the_price'],
                        'scraping_path_olx': '', 'misc': ['Liczba pokoi'], 'scraping_path_otodom': '',
                        'scraping_path_olxroom': ''},
    "additional_rent": {"db": "int(1)", 'item_loaders': ['remove_html_tags', 'just_numbers', 'integer_the_price'],
                        'scraping_path_olx': '', 'misc': ['Czynsz (dodatkowo)', 'Czynsz - dodatkowo', 'Czynsz'],
                        'scraping_path_otodom': '',
                        'scraping_path_olxroom': ''},
    "price_per_m2": {"db": "int(1)", 'item_loaders': ['remove_html_tags', 'just_numbers', 'integer_the_price'],
                     'scraping_path_olx': '', 'misc': ['Cena za m²'],
                     'scraping_path_otodom': '//*[@id="root"]/article/header/div[2]/div[2]/div/text()',
                     'scraping_path_olxroom': ''},
    "type_of_market": {"db": "varchar(25)", 'item_loaders': ['remove_html_tags', 'translate'], 'scraping_path_olx': '',
                       'misc': ['Rynek'], 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "security_deposit": {"db": "smallint(1)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Kaucja'],
                         'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "building_material": {"db": "varchar(25)", 'item_loaders': [], 'scraping_path_olx': '',
                          'misc': ['Materiał budynku'],
                          'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "windows": {"db": "varchar(25)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Okna'],
                'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "heating": {"db": "varchar(50)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Ogrzewanie'],
                'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "building_year": {"db": "SMALLINT(1)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Rok budowy'],
                      'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "fit_out": {"db": "varchar(50)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Stan wykończenia'],
                'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "ready_from": {"db": "DATETIME", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Dostępne od'],
                   'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "type_of_ownership": {"db": "varchar(50)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Forma własności'],
                          'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "rental_for_students": {"db": 'BOOLEAN', 'item_loaders': [], 'scraping_path_olx': '',
                            'misc': ['Wynajmę również studentom'],
                            'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "location_latitude": {"db": "LONGTEXT", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                          'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "location_longitude": {"db": "FLOAT", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                           'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "type_of_room": {"db": "varchar(50)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Rodzaj pokoju'],
                     'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "preferred_locator": {"db": "varchar(50)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['Preferowani'],
                          'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "non_smokers_only": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                         'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "scraped_ranking": {"db": "FLOAT", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                        'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "parsed_fields": {"db": "varchar(999)", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                      'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "internet": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "cable_tv": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "closed_terrain": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                       'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "monitoring_or_security": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                               'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "entry_phone": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                    'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "antibulglar_doors_windows": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                                  'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "alarm_system": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                     'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "antibulglar_blinds": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                           'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "dishwasher": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                   'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "cooker": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
               'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "fridge": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
               'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "oven": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
             'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "washing_machine": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                        'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "tv": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
           'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "elevator": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "phone": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
              'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "AC": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
           'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "garden": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
               'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "utility_room": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                     'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "parking_space": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                      'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "terrace": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "balcony": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "separate_kitchen": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                         'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "basement": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                 'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "virtual_walk": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                     'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "two_level_apartment": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                            'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "connecting_room": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['pokój przechodni'],
                        'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
    "pet_friendly": {"db": "BOOLEAN", 'item_loaders': [], 'scraping_path_olx': '', 'misc': ['dla zwierzat'],
                     'scraping_path_otodom': '', 'scraping_path_olxroom': ''},
}

query_scheme = {
    "query_no": {"db": "int(1) NOT NULL"},
    "facebook_id": {"db": "char(100) NOT NULL"},
    "city": {"db": "varchar(50)"},
    "housing_type": {"db": "varchar(50)", },
    "business_type": {"db": "varchar(50)"},
    "price": {"db": "int(1)"},
    "street": {"db": "varchar(50)"},
    "district": {"db": "varchar(50)"},
    "date_of_the_offer": {"db": "DATETIME"},
    "offer_from": {"db": "varchar(25)"},
    "apartment_level": {"db": "smallint(1)"},
    "furniture": {"db": "BOOLEAN"},
    "type_of_building": {"db": "varchar(25)"},
    "area": {"db": "smallint(1)"},
    "amount_of_rooms": {"db": "int(1)"},
    "additional_rent": {"db": "int(1)"},
    "price_per_m2": {"db": "int(1)"},
    "type_of_market": {"db": "varchar(25)"},
    "security_deposit": {"db": "smallint(1)"},
    "building_material": {"db": "varchar(25)"},
    "windows": {"db": "varchar(25)"},
    "heating": {"db": "varchar(50)"},
    "building_year": {"db": "SMALLINT(1)"},
    "fit_out": {"db": "varchar(50)"},
    "ready_from": {"db": "DATETIME"},
    "type_of_ownership": {"db": "varchar(50)"},
    "rental_for_students": {"db": 'BOOLEAN'},
    "type_of_room": {"db": "varchar(50)"},
    "preferred_locator": {"db": "varchar(50)"},
    "non_smokers_only": {"db": "BOOLEAN"},
    "internet": {"db": "BOOLEAN"},
    "cable_tv": {"db": "BOOLEAN"},
    "closed_terrain": {"db": "BOOLEAN"},
    "monitoring_or_security": {"db": "BOOLEAN"},
    "entry_phone": {"db": "BOOLEAN"},
    "antibulglar_doors_windows": {"db": "BOOLEAN"},
    "alarm_system": {"db": "BOOLEAN"},
    "antibulglar_blinds": {"db": "BOOLEAN"},
    "dishwasher": {"db": "BOOLEAN"},
    "cooker": {"db": "BOOLEAN"},
    "fridge": {"db": "BOOLEAN"},
    "oven": {"db": "BOOLEAN"},
    "washing_machine": {"db": "BOOLEAN"},
    "tv": {"db": "BOOLEAN"},
    "elevator": {"db": "BOOLEAN"},
    "phone": {"db": "BOOLEAN"},
    "AC": {"db": "BOOLEAN"},
    "garden": {"db": "BOOLEAN"},
    "utility_room": {"db": "BOOLEAN"},
    "parking_space": {"db": "BOOLEAN"},
    "terrace": {"db": "BOOLEAN"},
    "balcony": {"db": "BOOLEAN"},
    "separate_kitchen": {"db": "BOOLEAN"},
    "basement": {"db": "BOOLEAN"},
    "virtual_walk": {"db": "BOOLEAN"},
    "two_level_apartment": {"db": "BOOLEAN"},
    "connecting_room": {"db": "BOOLEAN"},
    "pet_friendly": {"db": "BOOLEAN"},
}

db_utility_scheme = {
    "offer_url": {"db": "varchar(700) NOT NULL"},
    "offer_name": {"db": "varchar(200)"},
    "street": {"db": "varchar(50)"},
    "offer_text": {"db": "LONGTEXT"},
}

conversations_scheme = {
    "conversation_no": {"db": "int(1) NOT NULL AUTO_INCREMENT"},
    "is_echo": {"db": "BOOLEAN"},
    "messaging": {"db": "varchar(5000)"},
    "time": {"db": "date"},
    "timestamp": {"db": "date"},
    "facebook_id": {"db": "char(100)"},
    "type": {"db": "char(100)"},
    "mid": {"db": "varchar(1000)"},
    "NLP": {"db": "BOOLEAN"},
    "stickerID": {"db": "varchar(999)"},
    "sticker_name": {"db": "varchar(999)"},
    "latitude": {"db": "FLOAT"},
    "longitude": {"db": "FLOAT"},
    "url": {"db": "BLOB"},
    "text": {"db": "varchar(999)"},
    "NLP_entities": {"db": "varchar(999)"},
    "NLP_language": {"db": "varchar(999)"},
    "NLP_intent": {"db": "varchar(999)"},
}

ratings_scheme = {
    "offer_url": {"db": "varchar(700) NOT NULL"},
    "static_rating": {"db": "float(6,2)"},
    "offer_name": {"db": "float(4,3)"},
    "offer_thumbnail_url": {"db": "float(4,3)"},
    "price": {"db": "float(4,3)"},
    "street": {"db": "float(4,3)"},
    "district": {"db": "float(4,3)"},
    "date_of_the_offer": {"db": "float(4,3)"},
    "offer_id": {"db": "float(4,3)"},
    "offer_text": {"db": "float(4,3)"},
    "offer_from": {"db": "float(4,3)"},
    "apartment_level": {"db": "float(4,3)"},
    "furniture": {"db": "float(4,3)"},
    "type_of_building": {"db": "float(4,3)"},
    "area": {"db": "float(4,3)"},
    "amount_of_rooms": {"db": "float(4,3)"},
    "additional_rent": {"db": "float(4,3)"},
    "price_per_m2": {"db": "float(4,3)"},
    "type_of_market": {"db": "float(4,3)"},
    "security_deposit": {"db": "float(4,3)"},
    "building_material": {"db": "float(4,3)"},
    "windows": {"db": "float(4,3)"},
    "heating": {"db": "float(4,3)"},
    "building_year": {"db": "float(4,3)"},
    "fit_out": {"db": "float(4,3)"},
    "ready_from": {"db": "float(4,3)"},
    "type_of_ownership": {"db": "float(4,3)"},
    "rental_for_students": {"db": "float(4,3)"},
    "location_latitude": {"db": "float(4,3)"},
    "location_longitude": {"db": "float(4,3)"},
    "type_of_room": {"db": "float(4,3)"},
    "preferred_locator": {"db": "float(4,3)"},
    "internet": {"db": "BOOLEAN"},
    "cable_tv": {"db": "BOOLEAN"},
    "closed_terrain": {"db": "BOOLEAN"},
    "monitoring_or_security": {"db": "BOOLEAN"},
    "entry_phone": {"db": "BOOLEAN"},
    "antibulglar_doors_windows": {"db": "BOOLEAN"},
    "alarm_system": {"db": "BOOLEAN"},
    "antibulglar_blinds": {"db": "BOOLEAN"},
    "dishwasher": {"db": "BOOLEAN"},
    "cooker": {"db": "BOOLEAN"},
    "fridge": {"db": "BOOLEAN"},
    "oven": {"db": "BOOLEAN"},
    "washing_machine": {"db": "BOOLEAN"},
    "tv": {"db": "BOOLEAN"},
    "elevator": {"db": "BOOLEAN"},
    "phone": {"db": "BOOLEAN"},
    "AC": {"db": "BOOLEAN"},
    "garden": {"db": "BOOLEAN"},
    "utility_room": {"db": "BOOLEAN"},
    "parking_space": {"db": "BOOLEAN"},
    "terrace": {"db": "BOOLEAN"},
    "balcony": {"db": "BOOLEAN"},
    "non_smokers_only": {"db": "BOOLEAN"},
    "separate_kitchen": {"db": "BOOLEAN"},
    "basement": {"db": "BOOLEAN"},
    "virtual_walk": {"db": "BOOLEAN"},
    "two_level_apartment": {"db": "BOOLEAN"},
    "connecting_room": {"db": "BOOLEAN"},
    "pet": {"db": "BOOLEAN"},
}

regex_scheme = {
    # "offer_url": {'regex': []},
    # "city": {'regex': []},
    # "housing_type": {'regex': []},
    # "business_type": {'regex': []},
    # "offer_name": {'regex': []},
    # "offer_thumbnail_url": {'regex': []},
    # "price": {'regex': []},
    "street": {'street': [r'(ul\.\s{,1})(.{,25})', r'(al\.\s{,1})(.{,25})', r'(ulic[ay]\s{,1})(.{,25})',
                          r'(ale[ja]\s{,1})(.{,25})', r'(alei\s{,1})(.{,25})']},
    "district": {'Center': ['centrum']},
    # "date_of_the_offer": {'regex': []},
    # "offer_id": {'regex': []},
    "offer_from": {'regex': []},
    "apartment_level": {0: ['parterze'],
                        1: ['pierwszym piętrze', r'1(.*)pi[eę]trze'],
                        2: ['drugim piętrze', r'2(.*)pi[eę]trze'],
                        3: ['trzecim piętrze', r'3(.*)pi[eę]trze'],
                        4: ['czwartym piętrze', r'4(.*)pi[eę]trze'],
                        5: ['piątym piętrze', r'5(.*)pi[eę]trze']},
    "furniture": {True: ['[^nie]umeblowane', 'z umeblowan(.{,10) '],
                  False: ['nieumeblowane', 'do umeblowania']},
    "type_of_building": {'regex': []},
    "area": {'m2': [r'(\d{1,})(.{,1})m(.{,2})2']},
    "amount_of_rooms": {'regex': []},
    "additional_rent": {'regex': []},
    "price_per_m2": {'regex': []},
    "type_of_market": {'regex': []},
    "security_deposit": {'regex': []},
    "building_material": {'regex': []},
    "windows": {'regex': []},
    "heating": {'regex': []},
    "building_year": {'regex': []},
    "fit_out": {'do wykończenia': ['do wyko(.*)czenia', 'stan deweloperski'], 'do zamieszkania': ['do zamieszkania']},
    "ready_from": {datetime.date.today(): ['od zaraz', 'od dzisiaj', 'od ju[zż]'],
                   datetime.date.today().replace(month=1, day=1): ['od(.{,15})stycz(.{,15})'],  # TODO
                   datetime.date.today().replace(month=2, day=1): ['od(.{,15})lut(.{,15})'],
                   datetime.date.today().replace(month=3, day=1): ['od(.{,15})mar(.{,15})'],
                   datetime.date.today().replace(month=4, day=1): ['od(.{,15})kwie(.{,15})'],
                   datetime.date.today().replace(month=5, day=1): ['od(.{,15})maj(.{,15})'],
                   datetime.date.today().replace(month=6, day=1): ['od(.{,15})czer(.{,15})'],
                   datetime.date.today().replace(month=7, day=1): ['od(.{,15})lip(.{,15})'],
                   datetime.date.today().replace(month=8, day=1): ['od(.{,15})sier(.{,15})'],
                   datetime.date.today().replace(month=9, day=1): ['od(.{,15})wrze(.{,15})'],
                   datetime.date.today().replace(month=10, day=1): ['od(.{,15})paźdz(.{,15})'],
                   datetime.date.today().replace(month=11, day=1): ['od(.{,15})listop(.{,15})'],
                   datetime.date.today().replace(month=12, day=1): ['od(.{,15})grud(.{,15})']},
    "type_of_ownership": {'regex': []},
    "rental_for_students": {
        True: [r'(.*) studencki', r'dla(.{,15})student(.*)', 'Wynajmę(.{,50})studentom', 'studenci']},
    "location_latitude": {'regex': []},
    "location_longitude": {'regex': []},
    "type_of_room": {'one-person': [r'jedno(.?)osobowy', r'1(.*)osobowy', r'jedynk(.*)'],
                     'two-person': [r'dwu(.?)osobowy', r'2(.*)osobowy'],
                     'three-person': [r'trzy(.?)osobowy', r'3(.*)osobowy']},
    "preferred_locator": {'regex': []},
    "scraped_ranking": {'regex': []},
    "internet": {'regex': []},
    "cable_tv": {True: ['kabl[oó]wka', 'tv(.*)kablowa', 'telewiz(.*)kablowa']},
    "closed_terrain": {True: ['(.{,30})zamkni[eę]ty', '(.{,30})ogrodzony', '(.{,30})wydzielony']},
    "monitoring_or_security": {True: ['monitoring', 'ochrona.{,10}']},
    "entry_phone": {True: ['domofon', '[vw]ideofon']},
    "antibulglar_doors_windows": {True: ['drzwi anty.{,3}wlamaniowe', 'okna anty.{,3}wlamaniowe']},
    "alarm_system": {True: ['alarm']},
    "antibulglar_blinds": {True: ['[zż]aluzje anty.{,3}wlamaniowe']},
    "dishwasher": {True: ['zmywark[aąę]']},
    "cooker": {True: ['kuchenk[aąę]']},
    "fridge": {True: ['lod[oó]wk[ęaą]']},
    "oven": {True: ['piekarnik', 'piekarnikiem']},
    "washing_machine": {True: ['pralk[aąę]']},
    "tv": {True: ['telewizor', 'tv']},
    "elevator": {True: ['wind[ęaą]']},
    "phone": {True: ['telefon']},
    "AC": {True: ['klimatyzacj[aąę]']},
    "garden": {True: [r'z(.{,20)ogr[oó]d(.{,10})', r'/+(.{,20)ogr[oó]d(.{,10})'],
               False: ['brak ogr[oó]d(.{,10})']},
    "utility_room": {'regex': []},
    "parking_space": {True: [r'miejsce w gara(.*)', r'gara(.*) podziem(.*)']},
    "terrace": {True: ['z tarasem'],
                False: ['brak tarasu']},
    "balcony": {'regex': []},
    "non_smokers_only": {True: [r'dla nie\s{,1}paląc(.*)', r'tylko nie\s{,1}paląc(.*)', r'osoby nie\s{,1}paląc(.*)',
                                'nie jest dla.{,10}pal[aą]cy', 'zakaz palenia', 'nie\s{,1}pal[aą]cy'],
                         False: [r'także paląc(.*)']},
    "separate_kitchen": {True: [r'osobn[aą] kuchni[aą]']},
    "basement": {True: ['piwnic[aąę]']},
    "virtual_walk": {'regex': []},
    "two_level_apartment": {'regex': []},
    "connecting_room": {True: ['\sprzechodni'],
                        False: ['nie(\s*)przechodni']},
    "pet_friendly": {True: ['w przypadku posiadania zwierz', 'mo[zż]liwo[sś][cć].{,12}zwierz', 'przyjazne zwierz'],
                     False: ['nie wyra[zż]am zgody na zwierz[eę]', 'zwierz[eę].{0,15}wykluczone',
                             'zwierz[eę].{0,15}zabronione', 'zwierz[eę].{0,15}niedozwolone',
                             'zwierz[eę].{0,5}nie s[aą] akceptowane', 'nie jest dla.{,25}zwierz',
                             'zakaz.{,25}zwierz', 'bez.{,15}zwierz[ąa]t', 'nie.{,2}akceptowane.{,10}zwierz',
                             'nie wyra[zż]am(.){,2} zgody na.{,15}zwierz', 'Zwierz.{,15}NIE', 'nie akceptuj.{,6}zwierz',
                             'zabrania si[eę].{,12}zwierz', 'nieposiadaj[aą]c.{,6}zwierz', 'nie mog[aą].{,15}zwierz']},
}
