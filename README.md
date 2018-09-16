# botvfxpython
1. In Python write loop code to print the following output?
```python
##########
#..#..#..#
#..#..#..#
##########
#..#..#..#
#..#..#..#
##########
#..#..#..#
#..#..#..#
##########
```

2. In Python write code loop to print a circle output similar to the following?
```python
#########################################
#########################################
##############.............##############
############.................############
##########..........#..........##########
#########......###########......#########
########.....###############.....########
#######....###################....#######
######....#####################....######
#####....#######################....#####
####....#########################....####
####...###########################...####
###....###########################....###
###...#############################...###
##....#############################....##
##...###############################...##
##...###############################...##
##...###############################...##
##...###############################...##
##...###############################...##
##..#################################..##
##...###############################...##
##...###############################...##
##...###############################...##
##...###############################...##
##...###############################...##
##....#############################....##
###...#############################...###
###....###########################....###
####...###########################...####
####....#########################....####
#####....#######################....#####
######....#####################....######
#######....###################....#######
########.....###############.....########
#########......###########......#########
##########..........#..........##########
############.................############
##############.............##############
#########################################
#########################################
```

3. In Python refactor the code from question 1 and question 2 into classes?

4. Depth first traversal

![alt text](https://github.com/muthukaruppanp/botvfxpython/blob/master/sample/images/folder_structure.jpg)

Given the above folder structure in Python implement depth first traversal to print
everything under the `episodes` directory. This must be implemented without
using any tools or libraries specifically intended for traversing sub folders (eg.
os.walk). You may use a directory lister such as os.listdir(). Be sure to list every file
and directory.
Format the output so that it is clearly readable, preferably a format such as the tree
command.

5. Do the same search above, but using a **Breadth** first search

6. Rewrite the classes from question 4 and 5 in JavaScript / Coffee Script / Babel

7. Using tables in appendix A, write the SQL command which returns a table of all the
shots in CMP002 ordered by the BidPds

8. Using tables in appendix A, write the SQL command which returns all artists who have
worked on CMP002

9. Using the tables in appendix A, write the SQL command which returns a table with the
columns shown below, return all records from all tables (i.e some of the columns might
be null):

| CompanyName | ShowCode | ShotID | ShotName | BidPDS | Artist | AssignedHours | HoursWorked |
| ----------- |:--------:|:------:|:--------:|:------:|:------:|:-------------:|:-----------:|

10. Using the tables in appendix A, write the SQL command returning **distinct Artists** and
their **Efficiency** using the formula given below:

**ArtistEfficiency** = Total hours worked divided by Total assigned hours

11. Using the tables in appendix A, write the SQL command returning distinct shots
by show while calculating the **Efficiency** using the formula given below:

**ShotEfficiency** = Total hours spend for a shot divided by Total hours assigned to that shot
