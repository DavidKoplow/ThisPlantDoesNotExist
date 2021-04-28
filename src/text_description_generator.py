import pandas as pd
import random
import os

filename = r'data\plants_usda_selected_features.txt'
read_file = pd.read_csv(filename, error_bad_lines=False)

def get_attributes(feature):
   return pd.Series.tolist(read_file[feature])

def isify(s, o=["Yes","No"],r=["is, isn't"]):
    if(s==None):
        return ""
    for i in range(len(o)):
        if(o[i]==s):
            return " "+r[i]+" "
    return ""

def isify_(s, o=["Yes","No"],r=["is, isn't"]):
   for i in range(len(o)):
       if(o[i]==s):
           return r[i]
       return "is unknown if"

def isknown(s):
    if isnan(str(s)):
        return "unknown"  # not nan
    return str(s)

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
droughts = pd.Series.tolist(read_file["Drought Tolerance"])
fertilities =  pd.Series.tolist(read_file["Fertility Requirement"])
fire_tolerances  =  pd.Series.tolist(read_file["Fire Tolerance"])
precipitation1s  =  pd.Series.tolist(read_file["Precipitation (Minimum)"])
precipitation2s  =  pd.Series.tolist(read_file["Precipitation (Maximum)"])

shades =  pd.Series.tolist(read_file["Shade Tolerance"])
temperatures = pd.Series.tolist(read_file["Temperature, Minimum (°F)"])
periods = pd.Series.tolist(read_file["Bloom Period"])
bulbs = pd.Series.tolist(read_file["Propogated by Bulbs"])

#product =  pd.Series.tolist(read_file["Berry/Nut/Seed Product"])
palatables = pd.Series.tolist(read_file["Palatable Human"])


for i in range(3, len(names)):
#for i in range(3, 10):
    prefix = "A plant "

    area = f"that lives in {areas[i]} " if not isnan(str(areas[i])) else "" # change this to unabbreviated place names
    category = f"categorized as {categories[i]} " if not isnan(str(categories[i])) else ""
    kingdom = f"in the {kingdoms[i]} kingdom" if not isnan(str(kingdoms[i])) else "" # fungus, plantae
    s_category = prefix + area + category + kingdom + '.\n'

    duration = prefix + f"that grows {durations[i]}ly \n" if not isnan(str(durations[i])) else ""
    habit = prefix + f"that grows as {habits[i]} \n" if not isnan(str(habits[i])) else ""
    growth_period = prefix + f"that grows in the {growth_periods[i]} \n" if not isnan(str(growth_periods[i])) else "\n"
    fall_conspicuous = prefix + f"that is {isify_(fall_conspicuouses[i])} conspicuous during the fall \n"

    flower_color = prefix + f"with {isknown(flower_colors[i])} flower color. \n"
    flower_conspicuous = prefix + f"with flower that {isify_(flower_conspicuouses[i])} conspicuous.\n"
    foliage_color = prefix + f"with {isknown(foliage_colors[i])} foliage color. \n"
    foliage_texture = prefix + f"with {isknown(foliage_textures[i])} foliage texture. \n"
    foliage_porosity = prefix + f"with {isknown(foliage_porosities_summer[i])} foliage porosity over the summer and {isknown(foliage_porosities_summer[i])} foliage porosity over the winter. \n"
    #s_foliage = prefix + "with foliage " + foliage_color + foliage_texture + foliage_porosity_summer + foliage_porosity_winter + '.\n'

    fruit_color = f"A plant that has {isknown(fruit_colors[i])} colored fruit. \n"
    fruit_conspicuous = f"A plant with fruit that {isify_(fruit_conspicuouses[i])} conspicuous. \n"

    growth_form = prefix + f"that grows in {isknown(growth_forms[i])} form." + '\n'
    growth_rate = prefix + f"that grows at a {isknown(growth_rates[i])} rate. \n"

    start_height = prefix + f"that starts at {isknown(start_heights[i])} feet tall. \n"
    mature_height = f"that has mature height {mature_heights[i]} feet tall. \n"
    height = start_height + "and" + mature_height

    leaf_retention = prefix + "that " + isify_(leaf_retentions[i], o=["Yes", "No"],
                                    r=["does", "does not"]) + " retaining leaves" + '.\n'
    lifespan = prefix + f"that has a {isknown(lifespans[i])} lifespan.\n"
    toxicity = prefix + f"that {isify_(toxicities[i])} toxic.\n"
    low_growing_grass = prefix + f"that {isify_(low_growing_grasses[i])} low growing grass. \n"
    shape_and_orientation = prefix + f"that has a {isknown(shape_and_orientations[i])} orientation." + "\n"
    #leaves_life_shape = prefix + leaf_retention + lifespan + toxicity + low_growing_grass + shape_and_orientation + '.\n'

    drought = prefix + "that " + isify_(droughts[i],o=["None", "Low","Medium","High"],r=["not","slightly", "moderately","very"]) +" tolerant of drought" + '.\n'
    fertility = prefix + "that "+ isify_(fertilities[i])+" requiring fertile soil to grow" + '.\n'
    fire_tolerance = prefix + "that "+ isify_(fire_tolerances[i],o=["None", "Low","Medium","High"],r=["not","slightly", "moderately","very"])+" tolerant of fire" + '.\n'
    precipitation = prefix + "that needs between "+ str(precipitation1s[i]) +" and "+str(precipitation2s[i])+" precipitation " + '.\n'
    shade = prefix + "that "+ isify_(str(shades[i])) +" providing of shade" + '.\n'
    temperature = prefix + "that survives at "+ isknown(temperatures[i]) + " degrees, minimum (°F)" + '.\n'
    bulb = prefix + "that" + isify_(bulbs[i],r=["has","does not have"])+ "bulbs" + '.\n'
    palatable = prefix + "that "+isify_(palatables[i])+ " edible" + '.\n'


    L = [s_category] + [duration, habit, growth_period, fall_conspicuous] + [flower_color, flower_conspicuous] + \
        [foliage_color, foliage_texture, foliage_porosity] +\
        [fruit_color, fruit_conspicuous] + \
        [growth_form, growth_rate, height] + \
        [leaf_retention, lifespan, toxicity, shape_and_orientation] + \
        [low_growing_grass, drought, fertility] + \
        [growth_form, growth_rate, fire_tolerance, precipitation, shade, temperature, bulb, palatable]

    # for now, we choose to ignore the sparse entries
    L = [l for l in L if 'unknown' not in l and ' nan ' not in l and l != '']
    # rng time
    feats = len(L)

    name = names[i]
    for copy in range(20): # 20 descriptions per images (is that enough?)
        if not os.path.exists(f'data\{name}'):
            os.makedirs(f'data\{name}')
        filename = f'data\{name}\{name}_{copy}.txt'
        descriptions = open(filename, 'w+')  # change w+ mode later (overriding every time for now)
        L = random.sample(L, 3 * len(L) // 4)  # include 3/4 of the features into each file
        descriptions.writelines(L)
        descriptions.close


