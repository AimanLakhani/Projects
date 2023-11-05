#  File: Boxes.py

#  Description:

#  Student Name: Aiman Lakhani

#  Student UT EID: al54554

#  Partner Name: Parul Gupta

#  Partner UT EID: 

#  Course Name: CS 313E

#  Unique Number: 58032

#  Date Created: 3/3/2023

#  Date Last Modified: 3/4/2023

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  nesting_lst = []
  
  for i in range(len(box_list)):
    nesting_lst.append(1)
    count = 0
    for j in range(i-1, -1, -1):
      if(does_fit(box_list[j], box_list[i])):
        if(nesting_lst[j] > count):
          count = nesting_lst[j]
    nesting_lst[i] += count

  max_nest = max(nesting_lst)
  num_sets = []
  memo_lst = memo(nesting_lst, box_list)
  nesting_combos(len(box_list) - 1, len(box_list) - 1, len(box_list) - 2, 1, max_nest, box_list, nesting_lst, num_sets, memo_lst)
  num_sets = len(num_sets)
  return max_nest, num_sets

def memo(nesting_lst, box_list):
  memo_lst = [[] for i in range(len(box_list))]
  for i in range(len(memo_lst)):
    for j in range(i - 1, -1, -1):
      if(does_fit(box_list[j], box_list[i]) and nesting_lst[i] <= len(memo_lst[j]) + 2):
        memo_lst[i].append(j)
  return memo_lst


# start is the current box we are checking against
# idx is the box we want to fit inside of start
# count is the current number we are nesting
# max_nest is how many boxes need to nest inside each other
# box_list is the list of boxes
# nesting_lst is how many boxes fit inside the one we are checking
# lst is what we are storing the boxes inside of
def nesting_combos(start, idx, count, max_nest, box_list, nesting_lst, lst, memo_lst):
  if(start <= 0 and count != max_nest):
    return
  elif(count == max_nest):
      print(memo_lst)
      lst.append(1)
  else:
    while(idx >= 0):
        if(does_fit(box_list[idx], box_list[start]) and nesting_lst[idx] + count == max_nest):
            nesting_combos(idx, idx-1, count+1, max_nest, box_list, nesting_lst, lst, memo_lst)
        idx -= 1
    nesting_combos(start-1, start-2, 1, max_nest, box_list, nesting_lst, lst, memo_lst) 

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  """print (box_list)
  print()

"""  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  """print (box_list)
  print()"""
  #print(box_list)
  #nesting_boxes (box_list)

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()
