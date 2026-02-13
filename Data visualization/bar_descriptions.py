import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart._title = 'Python projects'
chart.x_labels = ['public-apis','free-programming-books','system-design-primer']

plot_dicts = [
    {'value':398048,'label':'Description of public-apis'},
    {'value':382493,'label':'Description of free-programming-books'},
    {'value':335167,'label':'Description of system-design-primer'}
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')