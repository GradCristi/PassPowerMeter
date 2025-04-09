


class pwdChecker:
    def __init__(self):
        #tier list thing for actual grading and acceptance of password
        self.ratingElements={
            "Very Weak": 20,
            "Weak": 40,
            "Adaquate": 60,
            "Strong": 80,
            "Very Strong":100
        }
    @staticmethod
    def _rateLength(password):
        """Check Length requirements of password"""
        prints=[]

        if len(password)<12:
            prints.append("Passwords need to be at least 12 characters long")
            return 10, prints #we want this to be impassible, no password should be accepted without 12 chars
            #i think we should modulo against this somehow later
        else:
            #generally, the longer the better, but this shouldnt be the sole determining factor
            return len(password)*12, prints #i want to be able to reach adaquate if 16 chars exist and all other preconditions are met.



    #Length, special characters, numbers, dictionary patterns.
    def analysys(self, string):
        lengthScore, lengthFeedback=self._rateLength(password)

