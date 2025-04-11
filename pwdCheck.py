import sys

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
            return 0, prints #we want this to be impassible, no password should be accepted without 12 chars
            #i think we should modulo against this somehow later
        else:
            #generally, the longer the better, but this shouldnt be the sole determining factor
            return len(password)*3.75, prints #i want to be able to reach adaquate if 16 chars exist and all other preconditions are met.

    @staticmethod
    def _rateSpecNumeric(password):
        containsNumber=False
        containsSpecial=False
        prints =[]
        """Check for presence of numbers and special characters"""
        for letter in password:
            if 48 <= ord(letter) <= 57:
                containsNumber=True
            elif letter.isprintable() and not letter.isspace() and not letter.isalnum():
                containsSpecial=True
        if not containsNumber:
            prints.append("Passwords must contain numbers")
            return 0, prints
        if not containsSpecial:
            prints.append("Passwords must contain special characters")
            return 0, prints
        return 10, prints
    
    
    #we would need to establish how much percetntage-wise a password is a single dictionary word+numbers. 
    #three longer dictionary words+ some numbers should be enough to constitute a secure password.
    @staticmethod
    def _isDictionaryVulnerable(password):
        dictionary = []
        min_word_length=3
        count=0
        try:
            with open('/usr/share/dict/words', 'r') as file:
                #size was measured at 1.96MB which I consider to be low enough to not warrant additional processing
                dictionary = [word.strip().lower() for word in file if len(word.strip()) >= min_word_length]
        except FileNotFoundError:
            # Fallback to a smaller common word list
            print("Dictionary file not found. Please provide a path to a dictionary file.")
            return False
        passwordLower=password.lower()
        for word in dictionary:
            if word in passwordLower:
                count+=1
        return 0

    #Length, special characters, numbers, dictionary patterns.
    def analysis(self, string):
        #checking the overall length of the password
        lengthScore, lengthFeedback=self._rateLength(string)
        if len(lengthFeedback)>0:
            return lengthScore, lengthFeedback
        #checking special characters and numbers in one single go
        specNumericScore, specNumericFeedback= self._rateSpecNumeric(string)
        random=self._isDictionaryVulnerable(string)
        ##we also need a total aggregate feedback and score.
        if len(specNumericFeedback)>0:
            return lengthScore+specNumericScore, specNumericFeedback
        return lengthScore+specNumericScore, specNumericFeedback

# Create an instance of the class
checker = pwdChecker()

# Get input from the user
user_password = input("Enter a password to check: ")

# Call the analysis method
score, feedback = checker.analysis(user_password)

# Print the results
print(f"Password score: {score}")
print("Feedback:")
for item in feedback:
    print(f"- {item}")
