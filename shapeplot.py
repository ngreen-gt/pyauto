import matplotlib.pyplot as plt
from shapely.geometry import Point

points = [Point(1, 1), 
          Point(2, 1),
          Point(2, 1)]
xs = [point.x for point in points]
ys = [point.y for point in points]
# plt.scatter(xs, ys)
plt.plot(xs, ys)
plt.show()