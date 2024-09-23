## Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

def tile_cost(width, height, cost):
    total_cost = width*height*cost  #width and height in meters, cost in euros per square meter
    return print(total_cost,'€')

tile_cost(10,10,200)