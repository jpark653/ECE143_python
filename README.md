# ECE143_python
UCSD ECE143-Python

ECE 143 Individual Project, 

Function : drawcanvas() : 
         : drawRec(canvasX,canvasY,canvas)
         : saveRecinfo(x,y,width,height,listRec)
         : trimRec(listRec,canvas)
         : gettotalsurface(listRec)
         : main(canvasX,canvasY)
Libraries used:
         
In this project, user input, number of the trials, width and height of the canvas, program draw several number of 
rectangles on the top of canvas. and it will draw the rectangle untill it covers the maximum area of the initial surface
of area. Since the 



Algorithm of Trimming: 
 Everytime program draw the rectangle, it save the infomation of the rectangle in to the list called "listRec", 
 trimRec(listRec,canvas) function reads the list of the rectangle on the canvas and compare the latest rectangle 
 and every previous rectangle on the canvas. There are total 15 cases of rectangle positioning, and each positioning
 program compare with n th tower rectangle and find out the new rectangle is either corrupted or not. 
 and also it finds out the max area size of rectangle that is not corrupted. Then we add that new trimmed rectangle 
 in to the list instead of the latest rectagle.



Discussion Quesitons: 
  Result : 
 Number of trial  |    1    |    10     |    100    |    200    |   300    |    400   |    500   |
__________________|_________|___________|___________|___________|__________|__________|__________|
  Avg number Rec  |
__________________|
  Avg surf cover  |
__________________|
  
Technical limitations:
  
  remove of previous rectangle:
  
  github:
