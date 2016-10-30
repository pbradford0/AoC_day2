#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/2

import sys

def calc_order(filename):
  #loop through the file, separate each int
  l = 0
  w = 0
  h = 0
  total = 0
  #load file
  f = open(filename, 'rU')
  for line in f:
    #remove \n
    line = line.strip()
    #split each input line into a list
    line_split = line.split("x")
    
    #if input is formatted incorrectly, exit program
    if len(line_split) > 3:
      print "Error: Input must be in the form LxHxW"
      sys.exit(0)
    
    #store each int to calculate
    l = int(line_split[0])
    w = int(line_split[1])
    h = int(line_split[2])
    #find out the largest side to determine what 2 sides make up smallest area
    subtotal = 0
    if l > w and l > h:
      subtotal = 2*l*w + 2*w*h + 2*h*l + w*h
    elif w > l and w > h:
      subtotal = 2*l*w + 2*w*h + 2*h*l + l*h
    else:
      subtotal = 2*l*w + 2*w*h + 2*h*l + l*w
    total = total + subtotal
  return total

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)
  
  total = calc_order(sys.argv[1])
  print "Santa's elves must order " + str(total) + " sq.ft. of paper."

if __name__ == '__main__':
  main()