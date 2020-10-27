# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles =convert_distance(55)

my_trip_km = convert_distance(55)

print("The distance in kilometers is " + str(my_trip_miles))

print("The round-trip in kilometers is " +str( my_trip_km*2))
