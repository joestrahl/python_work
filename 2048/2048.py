import random
myArray = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
inducerlist = [0,1,2,3]
myArray[random.choice(inducerlist)][random.choice(inducerlist)]=2
def users_choice(myArray,user_input):
    
if user_input == "u":
        
i=0
        
for j in range(0,4):
            
if myArray[i][j]!=0 or myArray[i+1][j]!=0 or myArray[i+2][j]!=0 or myArray[i+3][j]!=0:
                
if myArray[i][j]==0:
                    
while myArray[i][j]==0:
                        
myArray[i][j]=myArray[i+1][j]
                        
myArray[i+1][j]=myArray[i+2][j]
                        
myArray[i+2][j] = myArray[i+3][j]
                        
myArray[i+3][j]=0
                
if myArray[i+1][j]==0 and (myArray[i+2][j]!=0 or myArray[i+3][j]!=0):
                    
while myArray[i+1][j]==0:
                        
 
                        
myArray[i+1][j]=myArray[i+2][j]
                        
myArray[i+2][j]=myArray[i+3][j]
                        
myArray[i+3][j]=0
                
if myArray[i+2][j]==0 and (myArray[i+3][j]!=0):
                    
while myArray[i+2][j]==0:
                        
myArray[i+2][j]=myArray[i+3][j]
                        
myArray[i+3][j]=0
        
i=0
        
for j in range(0,4):
            
if myArray[i][j]==myArray[i+1][j]:
                
myArray[i][j]=myArray[i][j]+myArray[i+1][j]
                
myArray[i+1][j]=myArray[i+2][j]
                
myArray[i+2][j]=myArray[i+3][j]
                
myArray[i+3][j]=0
            
if myArray[i+1][j]==myArray[i+2][j]:
                
myArray[i+1][j]=myArray[i+1][j]+myArray[i+2][j]
                
myArray[i+2][j]=myArray[i+3][j]
                
myArray[i+3][j]=0
            
if myArray[i+2][j]==myArray[i+3][j]:
                
myArray[i+2][j]=myArray[i+2][j]+myArray[i+3][j]
                
myArray[i+3][j]=0
                        
 
                        
 
          
 
    
elif user_input == "d":
        
i=0
        
for j in range(0,4):
            
if myArray[i][j]!=0 or myArray[i+1][j]!=0 or myArray[i+2][j]!=0 or myArray[i+3][j]!=0:
                
if myArray[i+3][j]==0:
                    
while myArray[i+3][j]==0:
                        
myArray[i+3][j]=myArray[i+2][j]
                        
myArray[i+2][j]=myArray[i+1][j]
                        
myArray[i+1][j]=myArray[i][j]
                        
myArray[i][j]=0
                
if myArray[i+2][j]==0 and (myArray[i+1][j]!=0 or myArray[i][j]!=0):
                    
while myArray[i+2][j]==0:
                        
myArray[i+2][j]=myArray[i+1][j]
                        
myArray[i+1][j]=myArray[i][j]
                        
myArray[i][j]=0
 
                
if myArray[i+1][j]==0 and myArray[i][j]!=0:
                    
while myArray[i+1][j]==0:
                        
myArray[i+1][j]=myArray[i][j]
                        
myArray[i][j]=0
        
i=0
        
for j in range(0,4):
            
if myArray[i+3][j]==myArray[i+2][j]:
                
myArray[i+3][j]=myArray[i+3][j] + myArray[i+2][j]
                
myArray[i+2][j]=myArray[i+1][j]
                
myArray[i+1][j]=myArray[i][j]
                
myArray[i][j]=0
            
if myArray[i+2][j]==myArray[i+1][j]:
                
myArray[i+2][j]=myArray[i+2][j]+myArray[i+1][j]
                
myArray[i+1][j]=myArray[i][j]
                
myArray[i][j]=0
            
if myArray[i+1][j]==myArray[i][j]:
                
myArray[i+1][j]=myArray[i+1][j]+myArray[i][j]
                
myArray[i][j]=0
            
 
    
elif user_input == "l":
        
j=0
        
for i in range(0,4):
 
            
if myArray[i][j]!=0 or myArray[i][j+1]!=0 or myArray[i][j+2]!=0 or myArray[i][j+3]!=0:
                
if myArray[i][j]==0:
                    
while myArray[i][j]==0:
                        
myArray[i][j]=myArray[i][j+1]
                        
myArray[i][j+1]=myArray[i][j+2]
                        
myArray[i][j+2] = myArray[i][j+3]
                        
myArray[i][j+3]=0
                
if myArray[i][j+1]==0 and (myArray[i][j+2]!=0 or myArray[i][j+3]!=0):
                    
while myArray[i][j+1]==0:
                        
myArray[i][j+1]=myArray[i][j+2]
                        
myArray[i][j+2]=myArray[i][j+3]
                        
myArray[i][j+3]=0
                
if myArray[i][j+2]==0 and (myArray[i][j+3]!=0):
                    
while myArray[i][j+2]==0:
                        
myArray[i][j+2]=myArray[i][j+3]
                        
myArray[i][j+3]=0
        
j=0
        
for i in range(0,4):
            
if myArray[i][j]==myArray[i][j+1]:
                
myArray[i][j]=myArray[i][j]+myArray[i][j+1]
                
myArray[i][j+1]=myArray[i][j+2]
                
myArray[i][j+2]=myArray[i][j+3]
                
myArray[i][j+3]=0
            
if myArray[i][j+1]==myArray[i][j+2]:
                
myArray[i][j+1]=myArray[i][j+1]+myArray[i][j+2]
                
myArray[i][j+2]=myArray[i][j+3]
                
myArray[i][j+3]=0
            
if myArray[i][j+2]==myArray[i][j+3]:
                
myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+3]
                
myArray[i][j+3]=0
    
elif user_input == "r":
        
j=0
        
for i in range(0,4):
            
if myArray[i][j]!=0 or myArray[i][j+1]!=0 or myArray[i][j+2]!=0 or myArray[i][j+3]!=0:
                
if myArray[i][j+3]==0:
                    
while myArray[i][j+3]==0:
                        
myArray[i][j+3]=myArray[i][j+2]
                        
myArray[i][j+2]=myArray[i][j+1]
                        
myArray[i][j+1]=myArray[i][j]
                        
myArray[i][j]=0
                
if myArray[i][j+2]==0 and (myArray[i][j+1]!=0 or myArray[i][j]!=0):
                    
while myArray[i][j+2]==0:
                        
myArray[i][j+2]=myArray[i][j+1]
                        
myArray[i][j+1]=myArray[i][j]
                        
myArray[i][j]=0
 
                
if myArray[i][j+1]==0 and myArray[i][j]!=0:
                    
while myArray[i][j+1]==0:
                        
myArray[i][j+1]=myArray[i][j]
                        
myArray[i][j]=0
        
j=0
        
for i in range(0,4):
            
if myArray[i][j+3]==myArray[i][j+2]:
                
myArray[i][j+3]=myArray[i][j+3] + myArray[i][j+2]
                
myArray[i][j+2]=myArray[i][j+1]
                
myArray[i][j+1]=myArray[i][j]
                
myArray[i][j]=0
            
if myArray[i][j+2]==myArray[i][j+1]:
                
myArray[i][j+2]=myArray[i][j+2]+myArray[i][j+1]
                
myArray[i][j+1]=myArray[i][j]
                
myArray[i][j]=0
            
if myArray[i][j+1]==myArray[i][j]:
                
myArray[i][j+1]=myArray[i][j+1]+myArray[i][j]
                
myArray[i][j]=0
                
 
                
 
while True:
    
print myArray[0][0],"\t",myArray[0][1],"\t",myArray[0][2],"\t",myArray[0][3],"\n"
    
print myArray[1][0],"\t",myArray[1][1],"\t",myArray[1][2],"\t",myArray[1][3],"\n"
    
print myArray[2][0],"\t",myArray[2][1],"\t",myArray[2][2],"\t",myArray[2][3],"\n"
    
print myArray[3][0],"\t",myArray[3][1],"\t",myArray[3][2],"\t",myArray[3][3],"\n"
    
user_input = raw_input("u for upward direction, d for downwards, l for left and r for Right")
    
users_choice(myArray,user_input)
    
listfori = []
    
listforj = []
    
count = 0
    
for i in range(0,4):
        
for j in range(0,4):
            
if myArray[i][j]==0:
                
count+=1
                
listfori.append(i)
                
listforj.append(j)
    
if count > 0:
        
if count > 1:
            
randomindex = listfori.index(random.choice(listfori))
            
myArray[listfori[randomindex]][listforj[randomindex]]=2
        
else:
            
myArray[listfori[0]][listforj[0]]=2
    
else:
        
break
print "Game over"
