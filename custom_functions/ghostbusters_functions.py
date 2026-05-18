#!/usr/bin/env python3
"""Ghostbusters Lab | Step 1"""

def report_ghost_sighting():
    """Prints a message about a ghost sighting."""
    print("Ghost sighted! Who you gonna call?")

# WHO YOU GONNA CALL?... no one, apparently!

#!/usr/bin/env python3
"""Ghostbusters Lab | Step 2"""

def report_ghost_sighting():
    """Prints a message about a ghost sighting."""
    print("Ghost sighted! Who you gonna call?")

# Function calls
report_ghost_sighting()
report_ghost_sighting()
report_ghost_sighting()

#!/usr/bin/env python3
#"""Ghostbusters Lab | Step 3"""

#def report_ghost_sighting(ghost_name, location): # <-- these are PARAMETERS
 #   """Prints details about the ghost sighting."""
  #  print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

# Function calls
#report_ghost_sighting("Slimer", "Hotel Sedgewick")  # <-- these are ARGUMENTS
#report_ghost_sighting("Stay Puft")  # Invalid call, missing 'location'

#!/usr/bin/env python3
"""Ghostbusters Lab | Step 4"""

def report_ghost_sighting(ghost_name, location="New York City"):
    """Prints details about the ghost sighting with a default location."""
    print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

# Function calls
report_ghost_sighting("Slimer", "Hotel Sedgewick")  # Valid call
report_ghost_sighting("Stay Puft")  # Valid call, 'location' defaults to "New York City"

#!/usr/bin/env python3
"""Ghostbusters Lab | Step 5"""

def calculate_catch_rate(ghost_name):
    """Returns a catch rate based on the ghost's name."""
    return len(ghost_name) * 10
    # len() is a built-in function that counts the number of 'pieces' to an object

# Call the function and store the result
rate = calculate_catch_rate("Slimer")

# Print the result
print("The catch rate for this ghost is:", rate)

