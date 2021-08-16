"""from replit import clear


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()"""

"""student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
        score = student_scores[student]
        if score < 70:
            student_grades[student] = "Fail"
        elif score > 71 and score < 80:
            student_grades[student] = "Acceptable"
        elif score > 81 and score < 90:
            student_grades[student] = "Exceeds expectation"
        else:
            "Outstanding"



print(student_grades)"""

"""travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name, visit_count, cities_visited):
    new_country ={}
    new_country["country"] = name  
    new_country["visits"] = visit_count
    new_country["cities"] = cities_visited
    travel_log.append(new_country)   
        

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
"""

