import matplotlib.pyplot as plt

field = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

grid_spot = 'C1'
# alpha is 0, number is 1

alpha_num = ord(grid_spot[0]) - 64

field[alpha_num-1][int(grid_spot[1])-1] = 1

plt.imshow(field)
plt.show()
