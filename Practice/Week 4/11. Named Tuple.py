color = (55,110,24)
print(color[0])

color = {'red':55, 'green': 110, 'blue':24}
print(color['red'])

from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(blue=55, red=24, green=132)

print(color[0])
print(color.blue)