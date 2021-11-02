# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Brady Bender bmb6369@psu.edu
# Collaborator: Kenleigh Leonard kml6565@psu.edu
# Collaborator: Yu Hsiang Huang ykh5222@psu.edu
# Section: 4
# Breakout: 4

def is_palindrome1(s):
  """
  This function returns True if s is a palindrome, i.e.,
  if s reads the same backward as forward, returns False otherwise.
  You must implement this with a while loop that compares
  characters in s one by one going forward vs. going backward
  """
  i = 0
  while i < len(s):
      if s[i] != s[-i - 1]:
          return False
      i += 1
  return True

def is_palindrome2(s):
  """
  This function returns True if s is a palindrome, i.e.,
  if s reads the same backward as forward, returns False otherwise.
  You must implement this function with recursion. A string is a
  palindrome only if its first character and its last
  character are the same AND the middle (smaller) part is a palindrome.
  Use negative index to get the last character and use
  slicing to get the middle of the string.
  """
  if len(s) <= 0:
    return True
  else:
    if(s[0] == s[-1]):
      return is_palindrome2(s[1:-1])
    else:
      return False

def is_palindrome3(s):
  """
  This function returns True if s is a palindrome, i.e.,
  if s reads the same backward as forward, returns False otherwise.
  You must implement this function with a one-liner.
  Use slicing (with step being -1) to get the reverse of a
  string, and a string is a palindrome if it is equivalent to its reverse.
  """
  return s == s[::-1]

def run():
  s = input("Enter a string: ")
  print(is_palindrome1(s))
  print(is_palindrome2(s))
  print(is_palindrome3(s))

if __name__ == "__main__":
  run()
