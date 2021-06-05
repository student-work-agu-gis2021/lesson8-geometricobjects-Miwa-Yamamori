#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Creating basic geometries 
# 
# In this problem you will create custom-made functions for creating geometries. We start with a very simple function, and proceed to creating functions that can handle invalid input values. 
# 
# 1: Create a function called `create_point_geom()` that has two parameters (x_coord, y_coord). Function should create a shapely `Point` geometry object and return that. 
#    


from shapely.geometry import Point, LineString, Polygon
#YOUR CODE HERE 1 to define create_point_geom()
# Define create_point_geom() function which returns the point of the arguments
def create_point_geom(x_coord, y_coord):
  """
  Function to return the point.

  Parameters
  ----------
  x_coord : <numerical>
    x coordinate.

  y_coord : <numerical>
    y coordinate.

  Returns
  -------
  <Point>
    The point.
  """
  return Point(x_coord, y_coord)

# Test your function by running these code cells:

# CODE FOR TESTING YOUR SOLUTION
point1 = create_point_geom(0.0, 1.1)

# CODE FOR TESTING YOUR SOLUTION
print(point1)

# CODE FOR TESTING YOUR SOLUTION
print(point1.geom_type)

# 2: Create a function called **`create_line_geom()`** that takes a list of Shapely Point objects as parameter called **`points`** and returns a LineString object of those input points. In addition, you should take care that the function is used as it should:
# 

# YOUR CODE HERE 2 to define create_line_geom()
def create_line_geom(points):
  """
  Function for checking the input type and taking a list of Shapely Point objects as parameter.

  Parameters
  ----------
  points: <list>
    A list of Shapely Point objects.

  Returns
  -------
  <LineString>
    The LineString with points.
  """
  # Assert whether the 'points' type is list
  assert type(points) == list, "Input should be a list!"
  # Assert whether the length of points is equal to or more than two
  assert len(points) >= 2, "LineString object requires at least two Points!"
  
  # For each element, check whether the points type is correct
  for i in range(len(points)):
    assert type(points[i]) == Point, "All list values should be Shapely Point objects!"
  
  # Return the LineString
  return LineString(points)

# Demonstrate the usage of your function; For example, create a line object with two points: `Point(45.2, 22.34)` & `Point(100.22, -3.20)` and store the result in a variable called `line1`:

line1 = None
# YOUR CODE HERE 3 to define two points and store the result in line1
# Create two points
point1 = Point(45.2, 22.34)
point2 = Point(100.22, -3.20)

# Store the points to line1 by uisng the function
line1 = create_line_geom([point1, point2])

# CODE FOR TESTING YOUR SOLUTION
print(line1)

# CODE FOR TESTING YOUR SOLUTION
print(line1.geom_type)


# Check if your function checks the input correctly by running this code cell:

# CODE FOR TESTING YOUR SOLUTION
try:
    # Pass something else than a list
    create_line_geom("Give me a line!")
except AssertionError:
    print("Found an assertion error. List check works correctly.")
except Exception as e:
    raise e


# 3: Create a function called **`create_poly_geom()`** that has one parameter called **`coords`**. `coords` parameter should containt **a list of coordinate tuples**. The function should create and return a Polygon object based on these coordinates.  
# 
#   - Inside the function, you should first check with `assert` -functionality that the input is a **list** (see [lesson 6](https://geo-python.github.io/site/lessons/L6/interpreting-errors.html#assertions) and [hints](https://automating-gis-processes.github.io/site/develop/lessons/L1/exercise-1.html#hints)). If something else than a list is passed for the function, you should return an Error message: `"Input should be a list!"`
#   - You should also check with `assert` that the input list contains **at least** three values. If not, return an Error message: `"Polygon object requires at least three Points!"`
#   - Check the data type of the objects in the input list. All values in the input list should be tuples. If not, return an error message: "All list values should be coordinate tuples!" using assert.
#   - **Optional:** Allow also an input containing a list of Shapely Point objects. If `coords` contains a list of Shapely Point objects, return a polygon based on these points. If the input is neither a list of tuples, nor a list of Points, return an appropriate error message using assert.
#   


# YOUR CODE HERE 4 to define create_poly_geom()
def create_poly_geom(coords):
  """
  Function to check the input type, and create and return a Polygon object based on the coordinates.

  Parameters
  ----------
  coords: <list>
    The coordinates.

  Returns
  -------
  <Polygon>
    The Polygon object based on coordinates.
  """
  # Assert the coords type
  assert type(coords) == list, "Input should be a list!"
  # Assert the length of coords
  assert len(coords) >= 3, "Polygon object requires at least three Points!"
  # For each element, assert whether the type is correct
  for i in range(len(coords)):
    assert type(coords[i]) == tuple, "All list values should be coordinate tuples!"

  # Return the polygon of coords
  return Polygon(coords)

# Demonstrate the usage of the function. For example, create a Polygon with three points: `(45.2, 22.34)`, `(100.22, -3.20)` & `(70.0, 10.20)`.

# YOUR CODE HERE 5 to define poly1 with three points
# Create a polygon with three given points
poly1 = create_poly_geom([(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)])

# CODE FOR TESTING YOUR SOLUTION
print(poly1)

# CODE FOR TESTING YOUR SOLUTION
print(poly1.geom_type)

# Check if your function checks the length of the input correctly by running this code cell:

# CODE FOR TESTING YOUR SOLUTION
try:
    # Pass something else than a list
    create_poly_geom("Give me a polygon")
except AssertionError:
    print("List check works")
except Exception as e:
    raise e

# ## Done!
# 
# That's it. Now you are ready to continue with Problem 2. 

# ## Problem 2: Attributes of geometries (*5 points*)
# 
# 1: Create a function called `get_centroid()` that has one parameter called `geom`. The function should take any kind of Shapely's geometric -object as an input, and return a centroid of that geometry. In addition, you should take care that the function is used as it should:
# 
#   - Inside the function, you should first check with `assert` -functionality that the input is a Shapely Point, LineString or Polygon geometry (see [lesson 6](https://autogis-site.readthedocs.io/en/latest/lessons/L1/exercise-1.html#hints) from the Geo-Python couurse and [hints](https://autogis-site.readthedocs.io/en/latest/lessons/L1/exercise-1.html#hints) for help). If something else than a list is passed for the function, you should return an Error message: `"Input should be a Shapely geometry!"`
# 

#  YOUR CODE HERE 6 to define get_centroid()
def get_centroid(geom):
  """
  Function for checking the input type and creating a centroid of the input geometry.

  Parameters
  ----------
  geom: <Point, LineString, or Polygon>
    A geometry.

  Returns
  -------
  <Point>
    The centroid of geom.
  """
  # Assert whether the geom type is shapely geometry
  assert type(geom) == Point or type(geom) == LineString or type(geom) == Polygon, "Input should be a Shapely geometry!"
  # Return the centroid
  return geom.centroid

# Test and demonstrate the usage of the function. You can, for example, create shapely objects using the functions you created in problem 1 and print out information about their centroids:
# 

#  YOUR CODE HERE 7 to define some objects
# Create a polygon with three given points
poly1 = create_poly_geom([(45.2, 22.34), (100.22, -3.20), (70.0, 10.20)])

# CODE FOR TESTING YOUR SOLUTION
centroid = get_centroid(poly1)
print(centroid)
###print("centroid type: ", centroid.geom_type)

# Check that the assertion error works correctly:
# CODE CELL FOR TESTING YOUR SOLUTION
try:
    # Pass something else than a Shapely geometry
    get_centroid("Give me a centroid!")
except AssertionError:
    print("Found and assertion error. Geometry -check works correctly.")
except Exception as e:
    raise e


# 2: Create a function called `get_area()` with one parameter called `polygon`. Function should take a Shapely's Polygon -object as input and returns the area of that geometry. 
#    
#    - Inside the function, you should first check with `assert` -functionality that the input is a Shapely Polygon geometry (see [lesson 6](https://geo-python.github.io/site/lessons/L6/interpreting-errors.html#assertions) and [hints](https://automating-gis-processes.github.io/site/develop/lessons/L1/exercise-1.html#hints)). If something else than a list is passed for the function, you should return an Error message: `"Input should be a Shapely Polygon -object!"`

# YOUR CODE HERE 8 to define get_area()
def get_area(polygon):
  """
  Function to check the input type and return the length of the line (if input is LineString) and length of the exterior ring (if input is Polygon). 

  Parameters
  ----------
  polygon: <Polygon>
    The Polygon.

  Returns
  -------
  <float>
    The area of the polygon.
  """
  assert type(polygon) == Polygon, "Input should be a Shapely Polygon -object!"
  return polygon.area

# Test and demonstrate the usage of the function:
get_area(poly1)

# CODE FOR TESTING YOUR SOLUTION
area = get_area(poly1)
print(round(area, 2))

# Check that the assertion works:

# CODE FOR TESTING YOUR SOLUTION
try:
    # Pass something else than a Shapely geometry
    get_area("Give me an area!")
except AssertionError:
    print("Geometry -check works")
except Exception as e:
    raise e

# 3: Create a function called `get_length()` with parameter called `geom`. The function should accept either a Shapely LineString or Polygon -object as input. Function should check the type of the input and returns the length of 
# the line if input is LineString and length of the exterior ring if input is Polygon. If something else is passed to the function, you should return an `Error` `"'geom' should be either LineString or Polygon!"`. (Use assert functionality). 
# 


#  YOUR CODE HERE 9 to define get_length()
def get_length(geom):
  """
  Function to check the input type and return the length of the line (if input is LineString) and length of the exterior ring (if input is Polygon).

  Parameters
  ----------
  geom: <LineString or Polygon>
    The LineString or Polygon.

  Returns
  -------
  <float>
    The length of the polygon.
  """
  # Assert the geom type
  assert type(geom) == LineString or type(geom) == Polygon, "'geom' should be either LineString or Polygon!"
  return geom.length

# Test and demonstrate the usage of the function:

get_length(poly1)


# CODE FOR TESTING YOUR SOLUTION
line_length = get_length(line1)
print("Line length:", round(line_length,2))



# CODE FOR TESTING YOUR SOLUTION
poly_exterior_length = get_length(poly1)
print("Polygon exterior length:", round(poly_exterior_length,2))


# CODE CELL FOR TESTING YOUR SOLUTION
try:
    # Pass something else than a Shapely LineString or Polygon
    get_length(Point(1,2))
except AssertionError:
    print("Geometry -check works")
except Exception as e:
    raise e

# ## Docstrings
# 
# Did you add a docstring to all the functions you defined? If not, add them now :) A short one-line docstring is enough in this exercise.

# YOUR ANSWER HERE

# In addition, you can run the code cell below to check all the docstrings!

# CODE FOR TESTING YOUR SOLUTION

# List all functions we created
functions = [create_point_geom, create_line_geom, create_poly_geom, 
             get_centroid, get_area, get_length]

print("My funcitions:\n")

for function in functions:
    #Print function name and docstring:
    print("-", function.__name__ +":", function.__doc__)


# ## Done!
# 
# That's it. Now you are ready to continue with Problem 3. 




