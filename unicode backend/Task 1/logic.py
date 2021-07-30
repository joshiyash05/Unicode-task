n_ish = int(input("Enter the total number of inputs = "))
counter_dict = {}
words_list = []

for i in range(n_ish):
  word = input()
  words_list.append(word)
  if word in counter_dict:
    counter_dict[word] += 1
  else:
    counter_dict[word] = 1
    
print(len(counter_dict))
print(' '.join([str(counter_dict[word]) for word in counter_dict]))
#bonus
print("bonus task occurnes of word in descending order = ")
for y in counter_dict:
  print(y)
for key in counter_dict: 
  if counter_dict[key]>1: 
    print("The most repeated word is = ",key)
  else:
    print("The least repeated word is = ",key) 
