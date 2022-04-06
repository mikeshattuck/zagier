# zagier
Source code for generating "windmills" for set S in Zagier's one sentence proof that a 4k+1 prime can be written as the sum of two integer squares.
This was written and tested with Python 3.10.4

To use this program, from the command line enter: python zagier.py <number>
  
Example input & output:
  
(Note please look at the raw file to see proper formatting!)
  
> python zagier.py 997  
  
  Solution Set S for 997 = x^2 + 4yz contains 61 windmills  
(x,y,z)             Fixed by I          Fixed by G          Solution  
(1,1,249)           Yes                 No  
(1,3,83)            No                  No  
(5,3,81)            No                  No  
(1,83,3)            No                  No  
(7,3,79)            No                  No  
(3,1,247)           No                  No  
(1,249,1)           No                  No  
(3,13,19)           No                  No  
(23,13,9)           No                  No  
(3,19,13)           No                  No  
(29,13,3)           No                  No  
(5,1,243)           No                  No  
(3,247,1)           No                  No  
(5,9,27)            No                  No  
(13,9,23)           No                  No  
(5,27,9)            No                  No  
(23,9,13)           No                  No  
(5,81,3)            No                  No  
(11,3,73)           No                  No  
(7,1,237)           No                  No  
(5,243,1)           No                  No  
(7,79,3)            No                  No  
(13,3,69)           No                  No  
(9,1,229)           No                  No  
(7,237,1)           No                  No  
(11,1,219)          No                  No  
(9,229,1)           No                  No  
(11,73,3)           No                  No  
(17,3,59)           No                  No  
(13,1,207)          No                  No  
(11,219,1)          No                  No  
(13,23,9)           No                  No  
(31,9,1)            No                  No  
(13,69,3)           No                  No  
(19,3,53)           No                  No  
(15,1,193)          No                  No  
(13,207,1)          No                  No  
(17,1,177)          No                  No  
(15,193,1)          No                  No  
(17,59,3)           No                  No  
(23,3,39)           No                  No  
(19,1,159)          No                  No  
(17,177,1)          No                  No  
(19,53,3)           No                  No  
(25,3,31)           No                  No  
(21,1,139)          No                  No  
(19,159,1)          No                  No  
(23,1,117)          No                  No  
(21,139,1)          No                  No  
(23,39,3)           No                  No  
(29,3,13)           No                  No  
(25,1,93)           No                  No  
(23,117,1)          No                  No  
(25,31,3)           No                  No  
(31,3,3)            No                  Yes                 31^2 + 6^2  
(27,1,67)           No                  No  
(25,93,1)           No                  No  
(29,1,39)           No                  No  
(27,67,1)           No                  No  
(31,1,9)            No                  No  
(29,39,1)           No                  No  
  
