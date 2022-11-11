import pandas as pd
import numpy as np 

def main():
    # name, radius in cm, height in cm, cost_per_can
    cans = ["1-Picnic	6.83	10.16	$0.28", 
        "1-Tall	7.78	11.91	$0.43",
        "2	8.73	11.59	$0.45",
        "2.5	10.32	11.91	$0.61",
        "3-Cylinder	10.79	17.78	$0.86",
        "5	13.02	14.29	$0.83",
        "6Z	5.40	8.89	$0.22",
        "8Z-short	6.83	7.62	$0.26",
        "10	15.72	17.78	$1.53",
        "211	6.83	12.38	$0.34",
        "300	7.62	11.27	$0.38",
        "303	8.10	11.11	$0.42"]

    x = 0
    new_cans = []
    for line in cans:
        result = line.split()
        new_cans.insert(x, result)
        x += 1

    x = 0
    calc_volume = []
    for y in new_cans:
        v = volume(float(new_cans[x][1]), float(new_cans[x][2]))
        calc_volume.insert(x,v)
        x += 1

    x = 0
    calc_surface_area = []
    for y in new_cans:
        s = surface_area(float(new_cans[x][1]), float(new_cans[x][2]))
        calc_surface_area.insert(x,s)
        x += 1

    df = pd.DataFrame(new_cans, columns=['name', 'radius_cm', 'height_cm', 'cost_per_can'])
    df["volume_cm_cube"] = calc_volume
    df["surface_area_cm_squared"] = calc_surface_area
    df["efficency"] = round(df["volume_cm_cube"]/df["surface_area_cm_squared"],2)

    print(df)

def volume(radius, height):
    volume = round(np.pi*radius*radius*height, 2)
    return volume

def surface_area(radius, height):
    surface_area = round(2*np.pi*radius*(radius + height),2)
    return surface_area

main()