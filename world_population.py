import json
from pygal_maps_world.maps import World
from country_codes import get_country_code
from pygal.style import RotateStyle,LightColorizedStyle

# 将数据加载到一个列表中
filename = 'data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 按人口数量分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'World Population in 2010,by Country'
wm.add('0-10M', cc_pops_1)
wm.add('10M-1BN', cc_pops_2)
wm.add('> 1BN', cc_pops_3)

wm.render_to_file('world_populations.svg')
