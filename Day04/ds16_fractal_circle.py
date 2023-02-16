# 프랙탈 원 그리기
import turtle

t = turtle.Turtle() # 거북이 만들기
t = turtle.Turtle() # 거북이 만들기
t.shape('turtle')

c = t.clone() # 거북이 복제
c.color('red')
c.circle(30)

for i in range(4,10):
    c.circle(i *10)

turtle.mainloop()
