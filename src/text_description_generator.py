import pandas as pd



filename = r'data\plants_usda_selected_features.txt'
read_file = pd.read_csv(filename, error_bad_lines=False)

names = pd.Series.tolist(read_file["Accepted Symbol"])
areas = pd.Series.tolist(read_file["PLANTS Floristic Area"])
categories = pd.Series.tolist(read_file["Category"])
kingdoms = pd.Series.tolist(read_file["Kingdom"])
durations = pd.Series.tolist(read_file["Duration"])
habits = pd.Series.tolist(read_file["Growth Habit"])
growth_periods = pd.Series.tolist(read_file["Active Growth Period"])
regrowth_rates = pd.Series.tolist(read_file["After Harvest Regrowth Rate"])
fall_conspicuouses = pd.Series.tolist(read_file["Fall Conspicuous"])


for i in range(1, 10): #len(names)
    name = names[i]
    filename = f'data\{name}_{0}.txt'
    descriptions = open(filename, 'w+')  # change w+ mode later (overriding every time for now)


    prefix = "A plant "
    area = f"that lives in {areas[i]}."
    s1 = prefix + area + '\n'

    category = f"A plant categorized as {categories[i]} "
    kingdom = f"and is a {kingdoms[i]}." # fungus, plantae
    s2 = category + kingdom + '\n'

    duration = f"A {durations[i]} plant that grows as "
    habit = f"{habits[i]} during the "
    growth_period = f"{growth_periods[i]}, and is "
    if fall_conspicuouses[i] == 'Yes':
        fall_conspicuous = f"conspicuous during the fall."
    else:
        fall_conspicuous = f"not conspicuous during the fall."
    s3 = duration + habit + growth_period + fall_conspicuous + '\n'

    print(s1)
    print(s2)
    print(s3)
    descriptions.writelines([s1, s2, s3])
    descriptions.close

    print("--------------------")

