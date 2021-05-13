class CompanyA:
    def employee(self):
        print('Need a programmer')
        print('Level C')

class CompanyB:
    def employee(self):
        print('Need a hacker')
        print('Level B')
        
class CompanyC:
    def employee(self):
        print('Need a data scientist')
        print('Level A')

class Resume:
    def fun(self, obj):
        obj.employee()

comA = CompanyA()
comB = CompanyB()
comC = CompanyC()
comList = [comA, comB, comC]
resume = Resume() 
# resume.fun(comA)
for obj in comList:
    resume.fun(obj)

