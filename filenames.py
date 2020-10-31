filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for name in filenames:
  if name.endswith(".hpp"):
    newfilenames.append(name[0:-2])
  if name.endswith(".out"):
    newfilenames.append(name)
  if name.endswith(".c"):
    newfilenames.append(name)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
