from elo import rate_1vs1, quality_1vs1, adjust_1vs1

import elo

user_Rating = elo.Rating(1200)
course_rating = elo.Rating(800)


for i in range(28):
    course_rating,user_Rating = elo.rate_1vs1(course_rating,user_Rating)

print(course_rating,user_Rating)


user_Rating,course_rating = elo.rate_1vs1(user_Rating,course_rating)

print(course_rating,user_Rating)

