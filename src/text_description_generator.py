import pandas as pd



filename = r'data\plants_usda_selected_features.txt'
read_file = pd.read_csv(filename, error_bad_lines=False)

def get_attributes(feature):
   return pd.Series.tolist(read_file[feature])

def isify(s, o=["yes","no"],r=["is, isn't"]):
    if(s==None):
        return ""
    for i in range(len(o)):
        if(o[i]==s):
            return before+" "+r[i]+" "+after
    return ""


def isnan(input):
   if str(input) == 'nan':
       return True
   return False


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
drought  =  pd.Series.tolist(read_file["Drought Tolerance"]) 
fertility =  pd.Series.tolist(read_file["Fertility Requirement"]) 
fire_tolerance  =  pd.Series.tolist(read_file["Fire Tolerance"])
precipitation1  =  pd.Series.tolist(read_file["Precipitation (Minimum)"])
precipitation1  =  pd.Series.tolist(read_file["Precipitation (Maximum)"])

shade =  pd.Series.tolist(read_file["Shade Tolerance"])
tempature = pd.Series.tolist(read_file["Temperature, Minimum (°F)"])
period = pd.Series.tolist(read_file["Bloom Period"])
bulb = pd.Series.tolist(read_file["Propogated by Bulbs"])

#product =  pd.Series.tolist(read_file["Berry/Nut/Seed Product"])
palatable = pd.Series.tolist(read_file["Palatable Human"])



for i in range(3, 10): #len(names)
    name = names[i]
    filename = f'data\{name}_{0}.txt'
    descriptions = open(filename, 'w+')  # change w+ mode later (overriding every time for now)

    prefix = "A plant "

    area = f"that lives in {areas[i]} " if not isnan(str(areas[i])) else ""
    category = f"categorized as {categories[i]} " if not isnan(str(categories[i])) else ""
    kingdom = f"in the {kingdoms[i]} kingdom" if not isnan(str(kingdoms[i])) else "" # fungus, plantae
    s_category = prefix + area + category + kingdom + '.\n'

    duration = f"{durations[i]}ly " if not isnan(str(durations[i])) else ""
    habit = f"as {habits[i]} " if not isnan(str(habits[i])) else ""
    growth_period = f"in the {growth_periods[i]} " if not isnan(str(growth_periods[i])) else ""
    fall_conspicuous = f",{isify(fall_conspicuouses[i])} conspicuous during the fall"
    s_growth = prefix + "that grows " + duration + habit + growth_period + fall_conspicuous + '.\n'

    fire_resistance = f"{isify(fire_resistances[i])} resistant to fire " if not isnan(str(fire_resistances[i])) else ""
    flower_color = f"with {flower_colors[i]} flower color " if not isnan(str(flower_colors[i])) else ""
    flower_conspicuous = f"with flower that {isify(flower_conspicuouses[i])} resistant to fire " if not isnan(str(flower_conspicuouses[i])) else ""
    s_flower = prefix + fire_resistance + flower_color + flower_conspicuous + '.\n'

    foliage_color = f"that is {foliage_colors[i]}, " if not isnan(str(foliage_colors[i])) else ""
    foliage_texture = f"that is {foliage_textures[i]}" if not isnan(str(foliage_textures[i])) else ""
    foliage_porosity_summer = f"{foliage_porosities_summer[i]} over the summer " if not isnan(str(foliage_porosities_summer[i])) else ""
    foliage_porosity_winter = f"and {foliage_porosities_winter[i]} over the winter" if not isnan(str(foliage_porosities_summer[i])) else ""
    s_foliage = prefix + "with foliage " + foliage_color + foliage_texture + foliage_porosity_summer + foliage_porosity_winter + '.\n'

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

    drought="that is "+ isify(drought[i],s=["low","medium","high"],r=["not","somewhat","very"] +" tolorant of drought")
    fertility = "that "+isify(fire_tolerance[i],s=["low","medium","high"],r=["doesn't require fertle","requires normal","requires fertle"])+" soil to grow"
    fire_tolerance = "that is "+isify(fire_tolerance[i],s=["med","low","high"],r=["somewhat","isn't","is"])+" tolerant to fire"
    precipitation = "needs between "+precipitation1[i]+" and "+precipitation2[i]+" precipitation "
    shade = "that is "+shade[i]+"of shade"
    tempature = "that survives at "+"Temperature, Minimum (°F)"
    period = "that blooms in "+period[i]
    bulb = "that "+isify(bulb[i],r=["has",""])+ "bulbs"
    palatable = "that "+isify(palatable[i])+" edible"


    L = [s1, s2, s3, fruit, growth, height, leaves_life_shape]
    print(L)
    descriptions.writelines(L)
    descriptions.close

    print("--------------------")

