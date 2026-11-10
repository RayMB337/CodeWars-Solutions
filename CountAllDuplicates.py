# ============================================
# CHALLENGE: Count Distinct Duplicates
# ============================================
#
# GOAL
# [ ] Return the count of distinct characters that occur MORE THAN ONCE
#     (count each such character only once, no matter its frequency)
# [ ] Matching must be case-insensitive ('b' and 'B' are the same)
# [ ] Input contains only letters and digits — no validation needed
#
# PLAN (dictionary approach)
# [ ] 1. Normalize: lowercase the input string            -> text.lower()
# [ ] 2. Tally: build a frequency dict char -> count
#        - use counts.get(char, 0) + 1   (avoids KeyError)
#        - OR use collections.Counter
# [ ] 3. Answer: count dict values that are > 1
#        - sum(1 for c in counts.values() if c > 1)
#
# TEST CASES
# [ ] "abcde"            -> 0   (no repeats at all)
# [ ] "aabbcde"          -> 2   ('a', 'b')
# [ ] "aabBcde"          -> 2   (case-insensitive 'b')
# [ ] "indivisibility"   -> 1   ('i' x6 counts as ONE duplicate)
# [ ] "Indivisibilities" -> 2   ('i' x7, 's' x2)
# [ ] "aA11"             -> 2   ('a', '1')
# [ ] "ABBA"             -> 2   ('A', 'B')
#
# EDGE CASES / GOTCHAS
# [ ] Empty string ""    -> should return 0 (empty dict -> sum of nothing)
# [ ] Single char "a"    -> should return 0
# [ ] ALL caps "AAAA"    -> should return 1, not 4 (distinct chars!)
# [ ] Forgot .lower()?   -> "aabBcde" would wrongly give 1 instead of 2
# [ ] Used >= 1?         -> wrong: EVERY counted char has count >= 1,
#                           you need > 1 (strictly more than once)
#
# CLEANUP
# [ ] All tests pass
# [ ] Removed debug prints
# [ ] Function has a clear name + docstring
# ============================================

def duplicate_count(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return sum(1 for n in counts.values() if n > 1)

