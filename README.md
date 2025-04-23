# PassPowerMeter
A password strength analyzer tool written in Python that takes into account common password good-practice rules in order to assess if the password is easily broken into. 

##How-To
Running the program is done in the usual Python way, and it will prompt the user for a simple string. Upon entering the string the program will return a set of instructions to strenghten the password, and also provide an overall score.

##Categories
The program assess the following criteria:
  - password length (over 12 characters is recommended)
  - presence of numeric characters (at least one)
  - presence of special characters (at least one)
  - presence of more than 2 words linked to a common english word dictionary (3 or more such words are recommended if you want to go the sentence route)


##Scoring 
The program provides scoring, anything over 60 is considered acceptable, but the user may implement thresholds for password acceptance/rejection based on their personal preferrences.
