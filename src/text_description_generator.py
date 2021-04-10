import pandas as pd



filename = r'data\plants_usda_selected_features.txt'
read_file = pd.read_csv(filename, error_bad_lines=False)

def get_attributes(feature):
    return pd.Series.tolist(read_file[feature])

def isify(s, o=["yes","no"],r=["is, isn't"]):
    for i in range(len(o)):
        if(o[i]==s):
            return r[i]
        return ""


names = get_attributes("Accepted Symbol")
areas = get_attributes("PLANTS Floristic Area")
categories = get_attributes("Category")
kingdoms = get_attributes("Kingdom")
durations = get_attributes("Duration")
habits = get_attributes("Growth Habit")
growth_periods = get_attributes("Active Growth Period")
regrowth_rates = get_attributes("After Harvest Regrowth Rate")
fall_conspicuouses = get_attributes("Fall Conspicuous")
fire_resistances = get_attributes("Fire Resistance")
flower_colors = get_attributes("Flower Color")
flower_conspicuouses = get_attributes("Flower Conspicuous")
foliage_colors = get_attributes("Foliage Color")
foliage_porosities_summer = get_attributes("Foliage Porosity Summer")
foliage_porosities_winter = get_attributes("Foliage Porosity Winter")
foliage_texture = get_attributes("Foliage Porosity Summer")
fruit_colors = get_attributes("Fruit Color")
fruit_conspicuouses = get_attributes("Fruit Conspicuous")
growth_forms = get_attributes("Growth Form")
growth_rates = get_attributes("Growth Rate")
start_heights = get_attributes("Height at Base Age, Maximum (feet)")
mature_heights = get_attributes("Height, Mature (feet)")
leaf_retentions = get_attributes("Leaf Retention")
lifespans = get_attributes("Lifespan")
low_growing_grasses = get_attributes("Low Growing Grass")
shape_and_orientations = get_attributes("Shape and Orientation")
toxicities = get_attributes("Toxicity")



for i in range(3, 10): #len(names)
    name = names[i]
    filename = f'data\{name}_{0}.txt'
    descriptions = open(filename, 'w+')  # change w+ mode later (overriding every time for now)

    import numpy as np
    prefix = "A plant "
    if str(areas[i]) == 'nan':
        print()
    area = f"that lives in {areas[i]}."
    s1 = (prefix + area + '\n') if str(areas[i]) != 'nan' else ""

    category = f"A plant categorized as {categories[i]} "
    kingdom = f"and is a {kingdoms[i]}." # fungus, plantae
    s2 = category + kingdom + '\n'

    duration = f"A {durations[i]} plant that grows as "
    habit = f"{habits[i]} during the "
    growth_period = f"{growth_periods[i]}, and "
    fall_conspicuous = f"{isify(fall_conspicuouses[i])} conspicuous during the fall \n"
    s3 = duration + habit + growth_period + fall_conspicuous + '\n'

    fruit_color = f"A plant that has {fruit_color[i]} colored fruit and "
    fruit_conspicuous = f"its' fruit {isify(fruit_conspicuouses[i])} conspicuous \n"
    fruit = fruit_color + fruit_conspicuous + '\n'

    growth_form = f"A plant that grows in {growth_forms[i]} form and "
    growth_rate = f"at a {growth_rate[i]} rate \n"
    growth = growth_form + growth_rate + '\n'

    start_height = f"A plant that starts at {start_heights[i]} feet tall "
    mature_height = f"and its' mature height is {mature_height[i]} feet tall \n"
    height = start_height + mature_height + '\n'

    if isify(leaf_retention[i]) == "":
        leaf_retention = f"A plant that does not retain leaves "
    else:
        leaf_retention = f"A plant that retains leaves "
    lifespan = f"and has a {lifespans[i]} lifespan "
    toxicity = f"is {toxicities[i]} toxic "
    if isify(low_growing_grasses[i]) == "":
        low_growing_grass = f"and does not have low growing grass "
    else:
        low_growing_grass = f"and has low growing grass "
    shape_and_orientation = f"with a {shape_and_orientations[i]} orientation \n"
    leaves_life_shape = leaf_retention + lifespan + toxicity + low_growing_grass + shape_and_orientation
    







    print(s1)
    print(s2)
    print(s3)
    print (fruit)
    print (growth)
    print (height)
    print (leaves_life_shape)
    descriptions.writelines([s1, s2, s3, fruit, growth, height, leaves_life_shape])
    descriptions.close

    print("--------------------")

