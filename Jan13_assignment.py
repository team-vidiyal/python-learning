def longest_even_length_word(user_sentence):
    # Split the sentence into words
    global word_length
    words = user_sentence.split()

    # Initialize the longest even length word as an empty string
    longest_word = ""

    # Iterate over each word
    for word in words:
        # Check if the word's length is even and longer than the current longest
        if len(word) % 2 == 0 and len(word) > len(longest_word):
            longest_word = word
            word_length=len(longest_word)


   # Return the longest even length word or "00" if not found
    return print(f"longest word is : {longest_word}"),  print(f"length of the word is: {word_length}")  if longest_word else "00"



# Test the function

user_sentence= input("sentence:")

print(longest_even_length_word(user_sentence))  # Output: seashore


