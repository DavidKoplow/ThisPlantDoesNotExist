import pandas as pd
import random

filename = r'data\plants_usda_selected_features.txt'
read_file = pd.read_csv(filename, error_bad_lines=False)

def get_attributes(feature):
   return pd.Series.tolist(read_file[feature])

def isify(s, o=["yes","no"],r=["is, isn't"]):
    if(s==None):
        return ""
    for i in range(len(o)):
        if(o[i]==s):
            return " "+r[i]+" "
    return ""

def isify_(s, o=["yes","no"],r=["is, isn't"]):
   for i in range(len(o)):
       if(o[i]==s):
           return r[i]
       return "is unknown if"

def isknown(s):
    if isnan(str(s)):
        return "unknown"  # not nan
    return s

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
foliage_textures = get_attributes("Foliage Porosity Summer")
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
fertilities =  pd.Series.tolist(read_file["Fertility Requirement"])
fire_tolerance  =  pd.Series.tolist(read_file["Fire Tolerance"])
precipitation1  =  pd.Series.tolist(read_file["Precipitation (Minimum)"])
precipitation2  =  pd.Series.tolist(read_file["Precipitation (Maximum)"])

shades =  pd.Series.tolist(read_file["Shade Tolerance"])
temperatures = pd.Series.tolist(read_file["Temperature, Minimum (°F)"])
periods = pd.Series.tolist(read_file["Bloom Period"])
bulbs = pd.Series.tolist(read_file["Propogated by Bulbs"])

#product =  pd.Series.tolist(read_file["Berry/Nut/Seed Product"])
palatables = pd.Series.tolist(read_file["Palatable Human"])



for i in range(3, 10):
# change to for i in range(len(names)):
    name = names[i]
    filename = f'data\{name}_{0}.txt'
    descriptions = open(filename, 'w+')  # change w+ mode later (overriding every time for now)

    prefix = "A plant "

    area = f"that lives in {areas[i]} " if not isnan(str(areas[i])) else "" # change this to unabbreviated place names
    category = f"categorized as {categories[i]} " if not isnan(str(categories[i])) else ""
    kingdom = f"in the {kingdoms[i]} kingdom" if not isnan(str(kingdoms[i])) else "" # fungus, plantae
    s_category = prefix + area + category + kingdom + '.\n'

    duration = f"{durations[i]}ly " if not isnan(str(durations[i])) else ""
    habit = f"as {habits[i]} " if not isnan(str(habits[i])) else ""
    growth_period = f"in the {growth_periods[i]} " if not isnan(str(growth_periods[i])) else ""
    fall_conspicuous = f",{isify_(fall_conspicuouses[i])} conspicuous during the fall"
    s_growth = prefix + "that grows " + duration + habit + growth_period + fall_conspicuous + '.\n'

    flower_color = prefix +f"with {isknown(flower_colors[i])} flower color "
    flower_conspicuous = prefix + f"with flower that {isify_(flower_conspicuouses[i])} conspicuous"

    foliage_color = f"that is {foliage_colors[i]}, " if not isnan(str(foliage_colors[i])) else ""
    foliage_texture = f"that is {foliage_textures[i]}" if not isnan(str(foliage_textures[i])) else ""
    foliage_porosity_summer = f"{foliage_porosities_summer[i]} over the summer " if not isnan(str(foliage_porosities_summer[i])) else ""
    foliage_porosity_winter = f"and {foliage_porosities_winter[i]} over the winter" if not isnan(str(foliage_porosities_summer[i])) else ""
    s_foliage = prefix + "with foliage " + foliage_color + foliage_texture + foliage_porosity_summer + foliage_porosity_winter + '.\n'

    fruit_color = f"A plant that has {isknown(fruit_colors[i])} colored fruit. \n"
    fruit_conspicuous = f"A fruit with fruit that {isify_(isify_(fruit_conspicuouses[i]))} conspicuous \n"

    growth_form = prefix + f"that grows in {isknown(growth_forms[i])} form." + '\n'
    growth_rate = prefix + f"that grows at a {isknown(growth_rates[i])} rate. \n"

    start_height = prefix + f"that starts at {start_heights[i]} feet tall. "
    mature_height = f"and has mature height {mature_heights[i]} feet tall. \n"
    height = start_height + mature_height

    if isify(leaf_retentions[i]) == "":
        leaf_retention = prefix + f"that does not retain leaves.\n"
    else:
        leaf_retention = prefix + f"that retains leaves.\n"
    lifespan = prefix + f"that has a {lifespans[i]} lifespan.\n"
    toxicity = prefix + f"that {isify_(toxicities[i])} toxic.\n"
    if isify(low_growing_grasses[i]) == "":
        low_growing_grass = prefix + f"that does not have low growing grass " + "\n"
    else:
        low_growing_grass = prefix + f"that has low growing grass " + "\n"
    shape_and_orientation = prefix + f"that has a {isknown(shape_and_orientations[i])} orientation" + "\n"
    #leaves_life_shape = prefix + leaf_retention + lifespan + toxicity + low_growing_grass + shape_and_orientation + '.\n'

    drought= prefix + "that " + isify_(drought[i],o=["low","medium","high"],r=["not","somewhat","very"]) +" tolerant of drought" + '.\n'
    fertility = prefix + "that requires "+ isknown(fertilities[i])+" fertile soil to grow" + '.\n'
    fire_tolerance = prefix + "that "+ isify_(fire_tolerance[i],o=["med","low","high"],r=["somewhat","isn't","is"])+" tolerant to fire" + '.\n'
    precipitation = prefix + "that needs between "+ str(precipitation1[i]) +" and "+str(precipitation2[i])+" precipitation " + '.\n'
    shade = prefix + "that "+ isify_(str(shades[i])) +" providing of shade" + '.\n'
    temperature = prefix + "that survives at "+ str(temperatures[i]) + " degrees, minimum (°F)" + '.\n'
    bulb = prefix + "that "+isify(bulbs[i],r=["has",""])+ "bulbs" + '.\n' if not isnan(str(bulbs[i])) else prefix+"that does not have bulbs"+".\n"
    palatable = prefix + "that "+isify_(palatables[i])+ " edible" + '.\n'


    L = [s_category, s_growth, flower_color, flower_conspicuous, fruit_color, fruit_conspicuous, growth_form, growth_rate, height, leaf_retention, lifespan, toxicity, shape_and_orientation, low_growing_grass, drought, fertility, growth_form, growth_rate, fire_tolerance, precipitation, shade, temperature, bulb, palatable]
    print(L)

    # rng time
    feats = len(L)
    L = random.choices(L, k=3*feats//4)  # include 3/4 of the features into each file


    descriptions.writelines(L)
    descriptions.close

    print("--------------------")

