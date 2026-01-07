#Find words longer than 5 letters in a sentence.
sentence=input("Enter the sentence: ").split()
count=0
for i in sentence:
    if len(i)>5:
        count+=1
        print(i)
print(f"There are total {count} words longer than 5 letters in this sentence")