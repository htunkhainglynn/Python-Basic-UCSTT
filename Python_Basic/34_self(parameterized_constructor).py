class Vote:
    def __init__(self, eligible_age=18):
        self.eligible_age = eligible_age

    def is_eligible(self, user_age):
        if self.eligible_age <= user_age:
            print('You are eligible to vote')
        else:
            print('You are not eligible to vote')


voter1 = Vote()
voter1.is_eligible(20)

voter2 = Vote()
voter2.is_eligible(16)
