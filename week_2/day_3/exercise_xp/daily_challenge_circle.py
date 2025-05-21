import math

class Circle:
    def __init__(self, radius=0, diameter=None):
        if diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    # Print the circle nicely
    def __str__(self):
        return f"Circle with radius {self.radius:.2f}, diameter {self.diameter:.2f}, and area {self.area():.2f}"

    # Add two circles (new radius is sum of both)
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # Compare which circle is bigger
    def __gt__(self, other):
        return self.radius > other.radius

    # Compare if two circles are equal
    def __eq__(self, other):
        return self.radius == other.radius

    # Sorting uses this
    def __lt__(self, other):
        return self.radius < other.radius

# -----------------------------
# Example usage:

c1 = Circle(radius=3)
c2 = Circle(diameter=10)

print(c1)
print(c2)

# Add two circles
c3 = c1 + c2
print("Added circle:", c3)

# Compare sizes
print("Is c1 bigger than c2?", c1 > c2)
print("Are c1 and c2 equal?", c1 == c2)

# Sort a list of circles
circles = [c1, c2, c3]
circles.sort()

print("\nSorted circles:")
for c in circles:
    print(c)