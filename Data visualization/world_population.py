import json 

import pygal_maps_world.maps
from pygal.style import RotateStyle

from country_codes import get_country_code

#Load the data in to a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

#Group the countries into three population levels
cc_pop_1,cc_pop_2,cc_pop_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop 
    elif pop < 1000000000:
        cc_pop_2[cc] = pop 
    else:
        cc_pop_3[cc] = pop 

#See how many countries are in each level
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))


wm_style = RotateStyle('#333699')
wm = pygal_maps_world.maps.World() 
wm.title = 'World population in 2010, by country'
wm.add('0-10m',cc_pop_1)
wm.add('10m-1b',cc_pop_2)
wm.add('>1b',cc_pop_3)

wm.render_to_file('world_population.svg')