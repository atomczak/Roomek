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
    # Artur, co to person_type? Zaloze chwilowo jako string i dodaje
    "price_limit": {"init": None, "db": "int(1)"},
    "since": {"init": None, "db": "datetime default current_timestamp"},
    # Artur, co to since? -> zakladam, ze nowe i dodaje
    "features": {"init": None, "db": "varchar(1000)"},
    # address:
    "country": {"init": None, "db": "varchar(100)"},
    "city": {"init": None, "db": "varchar(100)"},
    "street": {"init": None, "db": "varchar(100)"},
    "latitude": {"init": 0, "db": "FLOAT"},
    "longitude": {"init": 0, "db": "FLOAT"},
    # dialogue parameters:
    "context": {"init": None, "db": "varchar(100)"},
    "interactions": {"init": 0, "db": "int(1)"},
    "shown_input": {"init": False, "db": "BOOLEAN"},
    "wants_more_features": {"init": True, "db": "BOOLEAN"},
    "wants_more_locations": {"init": True, "db": "BOOLEAN"},
    "asked_for_restart": {"init": False, "db": "BOOLEAN"},
    "wants_restart": {"init": False, "db": "BOOLEAN"},  # Artur, zakłądam, ze nowe -> dodaje
    "confirmed_data": {"init": False, "db": "BOOLEAN"},
    "add_more": {"init": False, "db": "BOOLEAN"}
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
    "rental_for_students": {"db": "varchar(25)", 'item_loaders': [], 'scraping_path_olx': '',
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
    "scraped_ranking": {"db": "FLOAT", 'item_loaders': [], 'scraping_path_olx': '', 'misc': [],
                        'scraping_path_otodom': '', 'scraping_path_olxroom': ''}
}

db_utility_scheme = {
    "offer_url": {"db": "varchar(700) NOT NULL"},
    "offer_name": {"db": "varchar(200)"},
    "street": {"db": "varchar(50)"},
    "offer_text": {"db": "LONGTEXT"},
}

offer_features_scheme = {
    "offer_url": {"db": "varchar(700) NOT NULL"},
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
}
