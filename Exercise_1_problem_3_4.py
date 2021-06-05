#!/usr/bin/env python
# coding: utf-8

# # Problems 3-4 
# 
# ## Problem 3: Reading coordinates from a file and creating geometries.
# 
# 1: Read the [data/travelTimes_2015_Helsinki.txt](data/travelTimes_2015_Helsinki.txt) file into a variable **`data`** using  pandas.
# 

# YOUR CODE HERE 1 to read the file
#raise NotImplementedError()
import pandas as pd 

# Define the file path
fp = r'data/travelTimes_2015_Helsinki.txt'
# Read the CSV
# The text file was separated by ;
data = pd.read_csv(fp, header = 0, sep = ';')

#Check how many rows and columns there are:
print(data.shape)

# CODE FOR TESTING YOUR SOLUTION

# This test print should print first five rows in the data (if not, something is incorrect):
print(data.head())


# 2: Select the 4 columns that contain coordinate information (**'from_x'**, **'from_y'**, **'to_x'**, **'to_y'**) and store them in variable **`data`** (i.e. update the data -variable  to contain only these four columns).
# 

# YOUR CODE HERE 2 to set `data`
# Update data to have the selected 4 cols
data = data[['from_x', 'from_y', 'to_x', 'to_y']]

# CODE FOR TESTING YOUR SOLUTION
print(list(data.columns))


# 3: Create two empty lists called **`orig_points`** and **`dest_points`**. We will store the shapely points in these lists in the next step.
# 

# YOUR CODE HERE 3 to define empty lists orig_points and dest_points
orig_points = []
dest_points = []

# CODE FOR TESTING YOUR SOLUTION

# List length should be zero at this point:
print('orig_points length:', len(orig_points))
print('dest_points length:', len(dest_points))


# 4: Create shapely points for each origin and destination and add origin points to `orig_points` list and destination points to `dest_points` list.
# 
# - Create origin points based on columns `from_x` and `from_y`
# - Create destination points based on columns `to_x` and `to_y`
# 
# **HOW?**
# 
# **Approach A:** 
# 
# - Create a for-loop and iterate over the rows of your dataframe
# - For each row, create Shapely Point -objects based on the coordinate columns (columns `from_x` and `from_y` for the origins and columns `to_x` and `to_y` for the destinations)
# - Append the point objects into the **`orig_points`** -list and **`dest_point`** -list.
# 
# 
# **Approach B (advanced):**
# - Apply the Shapely point constructor on each row all at once. 
#     - Define your own function and apply it on the dataframe (in practice, the function is applied on each row). 
#     - Alternatively, you can apply the Polygon constructor directly using a lambda function, See hints e.g. [in here](https://towardsdatascience.com/apply-and-lambda-usage-in-pandas-b13a1ea037f7).
#     - You can store the outputs either to new columns in the dataframe, or separate variables (Pandas Series objects)
# - Convert outputs into lists and assign as values for `orign_points` and `dest_points` lists (data type needs to be a list for the next steps!).
# 
# 
# 

# YOUR CODE HERE 4 to append points in orig_points and dest_points
from shapely.geometry import Point
# For the length of data
for i in range(len(data)):
  # Create orig_point to store the coordinate of the ith start point
  orig_point = Point(data['from_x'][i], data['from_y'][i])
  # Create dest_point to store the coordinate of the ith end point
  dest_point = Point(data['to_x'][i], data['to_y'][i])
  # Append them to the lists
  orig_points.append(orig_point)
  dest_points.append(dest_point)

# CODE FOR TESTING YOUR SOLUTION

# This test print should print out the first origin and destination coordinates in the two lists:
print("ORIGIN X Y:", orig_points[0].x, orig_points[0].y)
print("DESTINATION X Y:", dest_points[0].x, dest_points[0].y)

#Check that you created a correct amount of points:
assert len(orig_points) == len(data), "Number of origin points must be the same as number of rows in the original file"
assert len(dest_points) == len(data), "Number of destination points must be the same as number of rows in the original file"


# Remember to commit your code using git after each major change (for example, after solving each problem).
# 
# ## Done!
# 
# That's it. Now you are ready to continue for the final Problem 4.

# ## Problem 4: Creating LineStrings that represent the movements:
# 
# This task continuous where we left in Problem 3. In this problem, the goal is to create lines (Shapely LineString objects) between each origin-destination pair.
#    
# 1: Create a list called `lines`
# 

# YOUR CODE HERE 5
lines = []

# CODE FOR TESTING YOUR SOLUTION

# Lines length should be zero at this stage:
print('lines length:', len(lines))


# 2a: Create a Shapely LineString -object for each origin and destination pair
# 
#   - Alternative 1: You can take advantage of `range()` function and index values to access the values from two lists at the same time inside a for-loop.
#      
#   - Alternative 2: You can use `zip()` function to iterate over many lists at the same time. [See hints for this week](https://autogis-site.readthedocs.io/en/latest/lessons/L1/exercise-1.html#iterating-multiple-lists-simultaneously)
#   
# 2b: Add each LineString object into the `lines` -list you created before.
# 

# YOUR CODE HERE 6 to append LineString to lines
#raise NotImplementedError()
from shapely.geometry import LineString
# For the length of data
# The length of data, orig_points, and dest_points are same
for i in range(len(data)):
  # Create a list to store each start and end points
  line = [orig_points[i], dest_points[i]]
  # Append it in the form of LineString
  lines.append(LineString(line))

# CODE FOR TESTING YOUR SOLUTION

#Test that the list has correct number of LineStrings
assert len(lines) == len(data), "There should be as many lines as there are rows in the original data"


# 3: Create a variable called **`total_length`**, and store the total (Euclidian) distance of all the origin-destination LineStrings that we just created into that variable.
# 
#   - Hint: You might want to iterate over the lines and update the total lenght on each iteration.
# 

# YOUR CODE HERE 7 to find total length
# Create total_length with default value, 0
total_length = 0

# For each element
# The length of lines is same as data's
for i in range(len(data)):
  # Add the length of ith line to total_length 
  total_length += lines[i].length

# CODE FOR TESTING YOUR SOLUTION

# This test print should print the total length of all lines
print("Total length of all lines is", round(total_length, 2))


# 4: write the previous parts, i.e. the creation of the LineString and calculating the total distance, into dedicated functions:  
# 
# - `create_od_lines()`: Takes two lists of Shapely Point -objects as input and returns a list of LineStrings
# - `calculate_total_distance()`: Takes a list of LineString geometries as input and returs their total length
# 
# You can copy and paste the codes you have written earlier into the functions. Below, you can find a code cell for testing your functions (you should get the same result as earler).
# 
# **Note: avoid using the same variable names as earlier inside your functions!** Functions are often defined at the top of the script file (or jupyter notebook), and now that we have them here at the very end you might accidentally alter an existing variable inside your functions. To avoid this, alter the variable names inside your own functions if you re-use code from this notebook. 

# YOUR CODE HERE 8 to define create_od_lines() and calculate_total_distance()
def create_od_lines(list1, list2):
  """
  Function to create a list of LineStrings.
  Just in case, I checked the argument type by using assert.

  Parameters
  ----------
  list1, list2: <list>
    The list of points.

  Returns
  -------
  <LineStrings>
    The LineStrings of the points.
  """
  # Assert the inputs type
  assert type(list1) == list and type(list2) == list, "Inputs should be lists!"
  # Same as above codes
  lines = []
  for i in range(len(list1)):
    line = [list1[i], list2[i]]
    lines.append(LineString(line))
  return lines

def calculate_total_distance(line):
  """
  Function to calculate the length of the line.
  Just in case, I checked the argument type by using assert.

  Parameters
  ----------
  line: <LineString>
    The LineString with points.

  Returns
  -------
  <float>
    The length of the LineString.
  """
  # Assert the inputs type
  assert type(line) == list, "Input should be a list of LineString!"
  # Same as above codes
  total_length = 0
  for i in range(len(data)):
    total_length += lines[i].length
  return total_length


# CODE FOR TESTING YOUR SOLUTION

# Use the functions
# -----------------

# Create origin-destination lines
od_lines = create_od_lines(orig_points, dest_points)

# Calculate the total distance
tot_dist = calculate_total_distance(od_lines)

print("Total distance", round(tot_dist,2))


# 
# ## All done!
# 
# Awesome, now you have successfully practiced how geometries can be created in Python. Next week we will start using them actively.



