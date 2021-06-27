# EngHack 2021 - Intro to Python
# Example code
# Written by Eric Chen (@the_ricetech)

some_str = "hello world"
some_num = 26.5

# Using commas (automatic spaces & type casting)
print(some_str, some_num, (2 + 2))

# Using plus signs (no spaces or type casting)
print(some_str + str(some_num) + str(2 + 2))
# Add spaces manually
print(some_str + " " + str(some_num) + " " + str(2 + 2))

# Using formatted strings (best/cleanest way)
# Anything in curly braces is treated as an expression
print(f"asdf {some_str} {some_num} {2 + 2}")  # Spaces inserted manually