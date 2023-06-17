
def index_2_claas(df):
    
    # List of animal names corresponding to their indices
    animals_name = ['Bear', 'Brown-bear', 'Bull', 'Butterfly', 'Camel', 'Canary', 'Caterpillar', 'Cattle', 'Centipede', 'Cheetah', 
                    'Chicken', 'Crab', 'Crocodile', 'Deer', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Fox', 'Frog', 
                    'Giraffe', 'Goat', 'Goldfish', 'Goose', 'Hamster', 'Harbor-seal', 'Hedgehog', 'Hippopotamus', 'Horse', 
                    'Jaguar', 'Jellyfish', 'Kangaroo', 'Koala', 'Ladybug', 'Leopard', 'Lion', 'Lizard', 'Lynx', 'Magpie', 
                    'Monkey', 'Moths-and-butterflies', 'Mouse', 'Mule', 'Ostrich', 'Otter', 'Owl', 'Panda', 'Parrot', 'Penguin',
                    'Pig', 'Polar-bear', 'Rabbit', 'Raccoon', 'Raven', 'Red-panda', 'Rhinoceros', 'Scorpion', 'Sea-lion', 'Sea-turtle', 
                    'Seahorse', 'Shark', 'Sheep', 'Shrimp', 'Snail', 'Snake', 'Sparrow', 'Spider', 'Squid', 'Squirrel', 'Starfish', 'Swan',
                    'Tick', 'Tiger', 'Tortoise', 'Turkey', 'Turtle', 'Whale', 'Woodpecker', 'Worm', 'Zebra']
    
    # Dictionary to map class indices to animal names
    animal_dict = {}

    # Iterate through unique class indices in the DataFrame
    for i in df.class_index.unique():
        
        # Enumerate through the animal names list
        for index, name  in enumerate(animals_name):
            
            # Check if the index matches the class index
            if i == index:
                
                # Assign key as class index and value as animal name
                key = i
                value = name
                
                # Add the key-value pair to the animal dictionary
                animal_dict[key] = value
    
    # Create a new column 'class_name' in the DataFrame and map class_index to animal names using animal_dict
    df['class_name'] = df['class_index'].map(animal_dict)
 
