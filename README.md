# ECE143_python
UCSD ECE143-Python

ECE 143 Individual Project, 

Function : drawcanvas() : 
         : drawRec(canvasX,canvasY,canvas)
         : saveRecinfo(x,y,width,height,listRec)
         : trimRec(listRec,canvas)
         : gettotalsurface(listRec)
         : main(canvasX,canvasY)
         >> specific docstrings of the functions are under program file
         
Libraries used: matplotlib, random, math, numpy,time

         
        In this project, user input, number of the trials, width and height of the canvas, program draw several number of 
rectangles on the top of canvas. and it will draw the rectangle untill it covers the maximum area of the initial surface
of area. Since drawing rectangle is all random. So, program needs to create random position inside the canvas and 
also have to create random number of width and height which should fit inside the fixed canvas size.



Algorithm of Trimming: 
          Everytime program draw the rectangle, it save the infomation of the rectangle in to the list called "listRec", 
 trimRec(listRec,canvas) function reads the list of the rectangle on the canvas and compare the latest rectangle 
 and every previous rectangle on the canvas. There are total 15 cases of rectangle positioning, and each positioning
 program compare with n th tower rectangle and find out the new rectangle is either corrupted or not. 
 and also it finds out the max area size of rectangle that is not corrupted. Then we add that new trimmed rectangle 
 in to the list instead of the latest rectagle.
 Every drawing and trimming part of the programs are runned at main function(also visualization) and based on the result of the main 
 program runs several times to calculate the average number and surfaced covered 
 
 I commented the plt.show() line for the faster run of the program. 
 

Discussion Quesitons: 
  Result : 
         Program read the number of trial(cycle) of program at the beginning of the program
  So I tested the 1 10 50 100 200 300 400  trials under given width and height of the canvas 10x10 sized window
  these are the result of average number of rectangle and average surface covered percent from each number or trial
  (Number of trials/ Avg number of rectangle / Avg surface covered percent)
  (1   / 5 / 92.0% )
  (10  / 7 / 86.0% )
  (50  / 6 / 83.0% )
  (100 / 6 / 87.0% )
  (200 / 6 / 85.0% )
  (300 / 6 / 86.0% )
  (400 / 6 / 86.0% )
  As, we can see on the result, it creates average 5~7 rectangle with over 80% surface covered. 
  When I run the program with small trial numbers sometimes it shows more number of rectangle with more surface covered, 
  but over 50 + number of trials it shows average 6 with ~85% area covered.
  
  
Technical limitations:
  
 1. remove of previous rectangle:
         couldn't figure out how to remove and redraw the trimmed rectangle. so on my program. It just add
  all the untrimmed rectangle and trimmed rectangle on the canvas.
  However, my listofRec only includes trimmed rectanlge. 
  
 2. Visualization : 
         couldn't figure out how to run the code with stepping .I tried to put time function and sleep. or try to use 
   animation libraries to show all the step of drawing rectangle and trimming However, couldn't figure out till the end. 
   time.sleep() funciton only holds the programming for certain times 
   and animation librraies. I tired to figure out animationing but couldn't find out. 
   So I erase all the part. 
   
 3. github: 
         This is my first time using github repository. so I struggleed using the github. and also I keep failed to push the file in to    my repository . 
