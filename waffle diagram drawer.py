import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import re
import copy
import numpy as np

file = 'goodpd.xlsx'
APP_PATH = 'D:\somewhere_on_my_disk'
sci = pd.read_excel(
    os.path.join(APP_PATH, "Data", file),
    engine='openpyxl',
)
model_values = sci['model'].values
price_values = sci['price'].values

FORMAT = ['model', 'price']
workdf = sci[FORMAT]

print(workdf)

p = re.compile(r"[^,]*$")
color = set()
name_range = len(workdf['model'])
for i in range(name_range):
    items = p.findall(workdf['model'][i])[0][2:]
    if(len(items) < 30 and items != "(PRODUCT)RED"):
        color.add(items)
color_list = list(color)
color_range = len(color_list)

amount_col = 0
price_col = 0
amount_list = []
price_list = []

for i in range(color_range):
    for j in range(g_range):
        if (workdf['model'][j].rfind(color_list[i]) != -1):
            amount_col += 1
            price_col += int(workdf['price'][j].replace(" ", "").strip())
    amount_list.append(amount_col)
    price_list.append(price_col)
    amount_col = 0
    price_col = 0
for i in range(color_range):
    price_list[i] = int(price_list[i]/amount_list[i])

exp_comp = [0]*10
small_num = 0
price_list_copy = copy.deepcopy(price_list)
a = 0
while(a < 10):
    for i in range(len(price_list_copy)):
        if(power_color[i] > small_num):
            small_num = price_list_copy[i]
            exp_comp[a] = i 
    price_list_copy[exp_comp[a]] = -1
    small_num = 0
    a += 1
a = 0
price_list_copy = copy.deepcopy(price_list)

exp_color_show = []
exp_price_show = []
for i in range(10):
    exp_color_show.append(color_list[exp_comp[i]])
    exp_price_show.append(price_list[exp_comp[i]])

df_waffle = pd.DataFrame({'color': exp_color_show, 'price': exp_price_show})
total = sum(df_waffle['price'])
proportions = [(float(value) / total) for value in df_waffle['price']]
width = 40
height = 9
total = width * height
tiles_per_category = [round(proportion * total) for proportion in proportions]
waffle = np.zeros((height, width))
category_index = 0
tile_index = 0

for col in range(width):
    for row in range(height):
        tile_index += 1
        if tile_index > sum(tiles_per_category[0:category_index]):
            category_index += 1
        waffle[row, col] = category_index
        
colormap = plt.cm.gnuplot2
plt.matshow(waffle, cmap=colormap)
ax = plt.gca()

ax.set_xticks(np.arange(-0.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-0.5, (height), 1), minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])

values = df_waffle['price']
categories = df_waffle['color']
value_sign = ''
value_price_list = np.price_list(values)
total_values = value_price_list[len(value_price_list)-1]

legend_handles = []
for i, category in enumerate(categories):
    if value_sign == '%':
        label_str = category + ' (' + str(values[i]) + value_sign + ')'
    else:
        label_str = category + ' (' + value_sign + str(values[i]) + ')'
    legend_handles.append(mpatches.Patch(label=label_str))
plt.legend(handles=legend_handles, loc='lower center', ncol=len(categories),
           bbox_to_anchor=(0.29, 0.2, 0.42, 0.3), prop={'size': 6})

leg = ax.get_legend()
leg.legendHandles[0].set_color('#000033')
leg.legendHandles[1].set_color('#000099')
leg.legendHandles[2].set_color('#0000CC')
leg.legendHandles[3].set_color('#3333FF')
leg.legendHandles[4].set_color('#9933CC')
leg.legendHandles[5].set_color('#FF3399')
leg.legendHandles[6].set_color('#FF9999')
leg.legendHandles[7].set_color('#FFCC33')
leg.legendHandles[8].set_color('#FFFF33')
leg.legendHandles[9].set_color('#FFFFFF')

plt.show()
