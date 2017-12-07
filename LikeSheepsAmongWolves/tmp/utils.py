# Get column values
cols_attr = ["statuses_count", "followers_count", "followees_count", "favorites_count", "listed_count", "median_int",
             "average_int", "betweenness", "eigenvector", "in_degree", "out_degree", "sentiment",
             "number hashtags", "tweet number", "retweet number", "quote number", "status length",
             "number urls", "baddies",
             "mentions"]
cols_empath = [
    "traveling_empath", "fashion_empath", "sadness_empath", "fun_empath",
    "noise_empath", "phone_empath", "cold_empath", "driving_empath", "love_empath", "weather_empath",
    "magic_empath", "messaging_empath", "appearance_empath", "cooking_empath", "contentment_empath",
    "business_empath", "art_empath", "politics_empath", "pain_empath", "ocean_empath", "economics_empath",
    "lust_empath", "philosophy_empath", "communication_empath", "giving_empath", "kill_empath", "sleep_empath",
    "sound_empath", "leisure_empath", "body_empath", "law_empath", "pet_empath", "fear_empath", "affection_empath",
    "stealing_empath", "vacation_empath", "children_empath", "swearing_terms_empath", "independence_empath",
    "leader_empath", "toy_empath", "animal_empath", "monster_empath", "masculine_empath", "crime_empath",
    "health_empath", "valuable_empath", "legend_empath", "rage_empath", "writing_empath", "beauty_empath",
    "hipster_empath", "irritability_empath", "negotiate_empath", "work_empath", "meeting_empath", "worship_empath",
    "reading_empath", "neglect_empath", "youth_empath", "swimming_empath", "medical_emergency_empath",
    "white_collar_job_empath", "banking_empath", "zest_empath", "sports_empath", "social_media_empath",
    "morning_empath", "positive_emotion_empath", "breaking_empath", "hygiene_empath", "dance_empath",
    "aggression_empath", "computer_empath", "night_empath", "horror_empath", "military_empath", "optimism_empath",
    "exasperation_empath", "exercise_empath", "emotional_empath", "celebration_empath", "dispute_empath",
    "music_empath", "torment_empath", "nervousness_empath", "ridicule_empath", "warmth_empath", "royalty_empath",
    "speaking_empath", "prison_empath", "heroic_empath", "disgust_empath", "shape_and_size_empath",
    "movement_empath", "ancient_empath", "wedding_empath", "terrorism_empath", "envy_empath", "achievement_empath",
    "surprise_empath", "anticipation_empath", "real_estate_empath", "cheerfulness_empath", "furniture_empath",
    "domestic_work_empath", "play_empath", "deception_empath", "liquid_empath", "suffering_empath",
    "restaurant_empath", "competing_empath", "programming_empath", "negative_emotion_empath", "exotic_empath",
    "party_empath", "fabric_empath", "dominant_heirarchical_empath", "wealthy_empath", "timidity_empath",
    "childish_empath", "healing_empath", "listen_empath", "school_empath", "order_empath", "eating_empath",
    "water_empath", "war_empath", "joy_empath", "cleaning_empath", "government_empath", "clothing_empath",
    "help_empath", "vehicle_empath", "money_empath", "air_travel_empath", "science_empath", "beach_empath",
    "urban_empath", "sexual_empath", "tool_empath", "payment_empath", "superhero_empath", "ugliness_empath",
    "occupation_empath", "politeness_empath", "attractive_empath", "college_empath", "family_empath",
    "friends_empath", "anger_empath", "fire_empath", "weakness_empath", "strength_empath", "home_empath",
    "poor_empath", "gain_empath", "injury_empath", "office_empath", "divine_empath", "sailing_empath",
    "musical_empath", "dominant_personality_empath", "hearing_empath", "confusion_empath", "rural_empath",
    "weapon_empath", "internet_empath", "hate_empath", "technology_empath", "sympathy_empath", "fight_empath",
    "car_empath", "hiking_empath", "pride_empath", "disappointment_empath", "anonymity_empath", "shame_empath",
    "violence_empath", "trust_empath", "alcohol_empath", "smell_empath", "blue_collar_job_empath", "death_empath",
    "feminine_empath", "medieval_empath", "journalism_empath", "farming_empath", "plant_empath", "shopping_empath",
    "ship_empath", "religion_empath", "tourism_empath", "power_empath"]
cols_glove = ["{0}_glove".format(v) for v in range(300)]

# Get neighborhood column values
cols_attr_c = ["c_" + v for v in cols_attr]
cols_glove_c = ["c_" + v for v in cols_glove]
cols_empath_c = ["c_" + v for v in cols_empath]