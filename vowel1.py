n=input()
while n.isalpha()==True:
  if n=='a' or n=='A'or n=='e' or n=='E' or n=='i' or n=='I' or n=='o' or n=='O' or n=='u' or n=='U':
    print("Vowel")
    break
  else:
    print("Consonant")  
    break
if n.isalpha()==False:
  print("invalid")    
