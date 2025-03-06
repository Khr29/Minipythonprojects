#1-reading the story from a file
with open("story.txt", "r") as f:
    story = f.read()

#2-initialize variables to store placeholders and track positions
words = set()
start_of_word = -1
start_of_target = "<"
ends_of_target = ">"

#3-extract placeholders (words inside < >) from the story 
for i, char in enumerate(story):
    if char == start_of_target:
        start_of_word = i

    if char == ends_of_target and start_of_word != -1:
        word = story[start_of_word: i + 1] 
        words.add(word)
        start_of_word = -1  #resets to prepare for the next placeholder
#4-ask the user for replacement words
answers = {}   
for word in words:
    answer = input("Enter a word for " + word +": ")
    answers[word] = answer

#5-replace placeholders with user-provided words
for word in words:
    story = story.replace(word , answers[word])

#6-print the final story 
print(story)
