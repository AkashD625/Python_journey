#what this enumarator does?
#---> This is used to add or include index for the for loop . 
#it has ability to start the index from 0 by default and increament it self.
#example code
marks = [20,30,65,98,54,21,65,98]
for index,ma in enumerate(marks):
      print(ma)
      if(index==5):
            print("Entered the index.") 


#if we want to start the index from some where else ,  then we can use 1 more parator as the start index.
# Example code
marks = [20,30,65,98,54,21,65,98]
for index,ma in enumerate(marks,start=2):
      print(ma)
      if(index==5):
            print("Entered the index.")             