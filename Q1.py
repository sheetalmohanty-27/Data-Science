import statistics

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

less_than_two = []
between_two_and_five = []
more_than_five = []

for salary, tenure in salaries_and_tenures:
    if tenure < 2:
        less_than_two.append(salary)
    elif tenure >= 2 and tenure <= 5:
        between_two_and_five.append(salary)
    else:
        more_than_five.append(salary)

avg_less_than_two = statistics.mean(less_than_two)
avg_between_two_and_five = statistics.mean(between_two_and_five)
avg_more_than_five = statistics.mean(more_than_five)

print(f"Average salary for less than two years of tenure: ${avg_less_than_two:.2f}")
print(f"Average salary for two to five years of tenure: ${avg_between_two_and_five:.2f}")
print(f"Average salary for more than five years of tenure: ${avg_more_than_five:.2f}")
