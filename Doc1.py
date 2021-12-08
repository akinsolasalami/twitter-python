# Function for finding "good enough" word matches?
# From the 'difflib' library and it's called 'get_close_matches() 
# Source - @driscollis

import difflib
words = ["apple", "ape", "appeal", "par", "parade"]
difflib.get_close_matches("appel", words)
difflib.get_close_matches("pa", words)
difflib.get_close_matches("par", words)



