import pandas as pd

read_file = pd.read_csv (r'data\plants_usda_selected_features.txt')
features = read_file.columns
names = pd.Series.tolist(read_file["Accepted Symbol"])
area = pd.Series.tolist(read_file["PLANTS Floristic Area"])

for i in range(len(names)):
    name = name[i]
    flower = "A flower"
    area = f"that flowers in {area[i]}"
#
# 1. Distribution
# PLANTS Floristic Area  - that flowers in "{area}" - NA (L48) -- skip for now
# State and Province - that flowers in "{}" - USA or CAN (check if in) --- skip state names for now
#
#
# 2. Taxonomy
# Category - categorized as a "{category}"
# Scientific Name - also called "scientific name"
#
# Kingdom  - "a {plant / fungus} that..." fungus, plantae
# 3. Ecology
# Duration - "perennial, annual, biennial"
# Growth Habit - that grows as - "just copy for now"
# 5. Additional Information in PLANTS
# Image Gallery
# Items Selected for Part B: Characteristics Data
# 1. Morphology/Physiology
# Active Growth Period
# After Harvest Regrowth Rate
# Fall Conspicuous - yes/no
# Fire Resistance -yes / no
# Flower Color
# Flower Conspicuous - yes/no
# Foliage Color
# Foliage Porosity Summer - dense/moderate/porous
# Foliage Porosity Winter
# Foliage Texture - coarse / fine / medium
# Fruit Color
# Fruit Conspicuous
# Growth Form - grows in "" form
# Growth Rate - slow moderate rapid
# Height at Base Age, Maximum (feet) - starts at "_" feet tall
# Height, Mature (feet) - ends at "_ feet tall"
# Leaf Retention - yes/no does retain leaf
# Lifespan - long/short/moderate lifespan
# Low Growing Grass - yes/no
# Shape and Orientation - "orientation" orientation
# Toxicity - moderate/none/severe/slight
# 2. Growth Requirements
# Adapted to Coarse Textured Soils - yes/no
# Adapted to Medium Textured Soils - yes/no
# Adapted to Fine Textured Soils - yes/no
# Drought Tolerance - low/medium/high
# Fertility Requirement - low/medium/high
# Fire Tolerance - med/low/high
# Moisture Use - med/low/high
# Precipitation (Minimum) - in numbers
# Precipitation (Maximum)
# Shade Tolerance - tolerant/intermediate
# Temperature, Minimum (°F) - integer
# 3. Reproduction
# Bloom Period - blooms in ""
# Propogated by Bulbs - yes/no
# 4. Suitability/Use
# Berry/Nut/Seed Product - no/yes
# Palatable Human - no/yes
