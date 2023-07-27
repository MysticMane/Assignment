def most_frequent(input_string):
    letter_freq = {}
    for letter in input_string:
        if letter.isalpha():
            letter = letter.lower()  
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
    sorted_freq = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)
    for letter, freq in sorted_freq:
        print(f"{letter}: {freq}")


#Main
string=input("Enter the string ")
most_frequent(string)

'''
Output
Enter the string hello world
l: 3
o: 2
h: 1
e: 1
w: 1
r: 1
d: 1
'''

