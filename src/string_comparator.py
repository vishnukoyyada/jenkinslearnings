def compare_strings(string1, string2):
  """Compares two strings and prints if they are equal or not."""
  if string1 == string2:
    print("The strings are equal.")
  else:
    print("The strings are not equal.")

# Get the two strings from Jenkins job parameters
string1 = os.getenv("input_1")
string2 = os.getenv("input_2")

# Check if both parameters are defined
if string1 is None or string2 is None:
  print("Error: Both STRING_1 and STRING_2 parameters are required.")
else:
  compare_strings(string1, string2)
