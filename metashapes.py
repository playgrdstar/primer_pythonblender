import bpy
import math
import random 
import numpy as np

# Functions to compute grid points for a sphere, pyramid and square 

def sphere(n,r):
    theta =(math.pi)/n
    phi = (2*math.pi)/n

    vertices = []

    for stack in range(n):
        stackRadius = math.sin(theta*stack) * r
        for slice in range(n):
            x = math.cos(phi*slice) * stackRadius
            y = math.sin(phi*slice) * stackRadius
            z = math.cos(theta*stack) * r
            vertices.append([x,y,z])

    return vertices


s_pts = sphere(20,5)


def pyramid(n, scale):
    vertices = []
    for z in np.arange(-n,n,2):
        for y in np.arange(-z,z,2):
            for x in np.arange(-z,z,2):
                vertices.append([x/scale,y/scale,z/scale])

    return vertices

p_pts = pyramid(40,5)


def square(n, scale):
    vertices = []
    for z in np.arange(-n,n,2):
        for y in np.arange(-n,n,2):
            for x in np.arange(-n,n,2):
                vertices.append([x/scale,y/scale,z/scale])

    return vertices

sq_pts = square(20,5)

# Function to sample from the grid of points created in the functions above
# I do this as I want a fixed number of locations for each shape

def shapePts(array):

    locations = []

    for i in range(400):
        index = random.randint(0,len(array)-1)
        locations.append(array[index])
        
    return locations

# Seelecting the scene and creating metaballs

scene = bpy.context.scene

mball  = bpy.data.metaballs.new('MetaBall')
obj = bpy.data.objects.new('MetaBallObj', mball)
scene.objects.link(obj)

mball.resolution = 0.2
mball.render_resolution = 0.02


locations = shapePts(s_pts)

for i in range(len(locations)):
    # print(locations[i][0])
    coordinate = (locations[i][0], locations[i][1], locations[i][2])
    element = mball.elements.new()
    element.co = coordinate
    element.radius = 0.5


# Animating the metaball elements as they move from location to location for each grid shape
# Should be fairly self explanatory

currframe = bpy.context.scene.frame_start

bpy.context.scene.frame_set(currframe)

locations = shapePts(p_pts)

for i in range(len(mball.elements)):
    coordinate = (locations[i][0], locations[i][1], locations[i][2])
    mball.elements[i].co = coordinate
    mball.elements[i].keyframe_insert(data_path='co')

bpy.context.scene.frame_set(currframe+60)

locations = shapePts(s_pts)

for i in range(len(mball.elements)):
    coordinate = (locations[i][0], locations[i][1], locations[i][2])
    mball.elements[i].co = coordinate
    mball.elements[i].keyframe_insert(data_path='co')

bpy.context.scene.frame_set(currframe+120)

locations = shapePts(sq_pts)

for i in range(len(mball.elements)):
    coordinate = (locations[i][0], locations[i][1], locations[i][2])
    mball.elements[i].co = coordinate
    mball.elements[i].keyframe_insert(data_path='co')


bpy.context.scene.frame_set(currframe+180)

locations = shapePts(s_pts)

for i in range(len(mball.elements)):
    coordinate = (locations[i][0], locations[i][1], locations[i][2])
    mball.elements[i].co = coordinate
    mball.elements[i].keyframe_insert(data_path='co')

bpy.context.scene.frame_set(currframe+240)

locations = shapePts(p_pts)

for i in range(len(mball.elements)):
    coordinate = (locations[i][0], locations[i][1], locations[i][2])
    mball.elements[i].co = coordinate
    mball.elements[i].keyframe_insert(data_path='co')
