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






    print(s1)
    print(s2)
    print(s3)
    descriptions.writelines([s1, s2, s3])
    descriptions.close

    print("--------------------")

