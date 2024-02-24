def pair_chars(string):
  """
  Pairs the characters in a string, adding a star to the last pair if the string has an odd number of characters.

  Args:
    string: The string to be paired.

  Returns:
    A list of two-character pairs.
  """

  pairs = []
  for i in range(0, len(string), 2):
    if i + 1 < len(string):
      pairs.append(string[i:i+2])
    else:
      pairs.append(string[i] + "*")
  return pairs

# Example usage
string = "Hello, world!"
pairs = pair_chars(string)
print(pairs)  # Output: [('He', 'll'), ('o,', ' w'), ('or', 'ld!')]

string = "Gomathi"
pairs = pair_chars(string)
print(pairs)