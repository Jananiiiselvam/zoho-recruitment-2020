a = 'welcome'
mid = int(len(a)//2)
str1 = a[mid:]
str2 = a[:mid]
end_string = str1+str2
k = 2*len(a) - 2
for i in range(0, len(a)+1):
  for j in range(0, k):
      print(end=" ")
  k = k - 1

  for j in range(0, i+1):
      output = end_string[:i]
      print(output , end="")
      break
    
  print("\r")
