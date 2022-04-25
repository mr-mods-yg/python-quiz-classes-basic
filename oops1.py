from cgi import print_directory


class Trivia:
    def __init__(self,zques,zopt,zans):
        self.ques = zques
        self.opt = zopt
        self.ans = zans

    def print_details(self):
        print(self.__dict__)

q1 = Trivia('who is Pm of india',['modi','rk badra','kohli','ifran'],'modi')
print(q1.ques)
print(q1.opt)
a = int(input('enter which is correct :'))
ans_index = q1.opt.index(q1.ans) + 1
if a == ans_index:
    print('YOOOOOOoooooo !!! correct')
else:
    print('NOOOOOOoooooo !!!')
   