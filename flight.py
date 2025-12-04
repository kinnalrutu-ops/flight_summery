import sys
if sys.argv==5:
  flight_no=sys.argv[1]
  passenger_name=sys.argv[2]
  source=sys.argv[3]
  destination=sys.argv[4]
else:
  flight_no=1234
  passenger_name="rutu"
  source="hubli"
  destination="bengalore"
print("SUMMERY")
print("flight number:",flight_no)
print("passenger name:",passenger_name)
print("source:",source)
print("destination:",destination)
