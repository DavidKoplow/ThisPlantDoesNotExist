import pandas as pd

def plant_info_generator(filename):
    read_file = pd.read_csv (filename)
    features = read_file.columns

    # optionally print feature list
    # print('\n'.join([str(i) + "\t" + e for (i, e) in enumerate(features)]))

    # process all plant names as a list
    symbol = features[0]
    data = read_file["Accepted Symbol"]
    all_plant_symbols = pd.Series.tolist(data)
    print('\n'.join(all_plant_symbols))
    return all_plant_symbols


    # can repeat process for other features; (ex) Fruit color
    # data = read_file["Fruit Color"]
    # all_fruit_colors = pd.Series.tolist(data)  # a lot of NaN's


# plant_info_generator(r'data\plants_usda_selected_features.txt')