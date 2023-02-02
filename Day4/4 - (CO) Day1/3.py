#3. Solution

#start
liste = list()
liste = []
type(liste)

#index
liste = [0,5,6,8,10,15,22,26]
liste[0] = -1
print(liste)

#method
liste.append(20) # Append
liste.count(0) # Count
liste.clear() # Clear
liste.extend([5,10,18,99]) #Extends
liste.insert(3,44) # 3. -> 44
liste.index(44) # Index
liste.pop() # Pop
liste.remove(44) #Remove 3
liste.sort() #Sorted

#functions
sorted(liste)
min(liste)
max(liste)