import elo
import math

elo_lesson = 1000
elo_user = 1200

test_case_factor = 9/10

normal_elo = elo.rate_1vs1(elo_lesson,elo_user)

difference = math.fabs(elo_lesson - normal_elo[0])

print(elo_lesson,elo_user)
print()
print(normal_elo)

print(elo_lesson + difference - (difference*test_case_factor))
print(elo_user - difference + (difference*test_case_factor))