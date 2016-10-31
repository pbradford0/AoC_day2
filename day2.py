#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/2

import sys

def calc_paper(filename):
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
    #do the math that is always the same first,
    subtotal = 2*l*w + 2*w*h + 2*h*l
    #then do the one that can change
    subtotal = subtotal + min(l*w, w*h, h*l)
    total = total + subtotal
  f.close()
  return total

def calc_ribbon(filename):
  #literally just steal the first method until the maths
  l = 0
  w = 0
  h = 0
  total = 0
  f = open(filename, 'rU')
  for line in f:
    line = line.strip()
    line_split = line.split("x")
    if len(line_split) > 3:
      print "Error: Input must be in the form LxHxW"
      sys.exit(0)
    l = int(line_split[0])
    w = int(line_split[1])
    h = int(line_split[2])
    #new math goes here: do the static formula first...
    subtotal = l*w*h
    #then the variable one
    subtotal = subtotal + min((l+l+w+w), (w+w+h+h), (h+h+l+l))
    total = total + subtotal
  f.close()
  return total

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)
  
  paper = calc_paper(sys.argv[1])
  print "Santa's elves must order " + str(paper) + " sq.ft. of paper."

  ribbon = calc_ribbon(sys.argv[1])
  print "Santa's elves must order " + str(ribbon) + " ft. of ribbon."

if __name__ == '__main__':
  main()