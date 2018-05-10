from elo import rate_1vs1, quality_1vs1, adjust_1vs1

import elo

user_Rating = elo.Rating()
course_rating = elo.Rating(600)

# draw probability
q = quality_1vs1(user_Rating, course_rating)

# rate_1vs1(r1,r2) => if r1 beats r2
# rate_1vs1(r1,r2) => if r2 beats r1


user_Rating, course_rating = elo.rate_1vs1(user_Rating, course_rating)

print(user_Rating)

print(course_rating)
