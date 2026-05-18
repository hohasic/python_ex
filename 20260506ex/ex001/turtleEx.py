import turtle

t = turtle.Turtle()     # 그림 그리기 준비 완료!
t.shape('turtle')       # 아이콘 설정

angle = 120

t.right(angle)          # 오른쪽으로 120도 회전
t.forward(100)          # 100픽셀 실선 그리기

t.left(angle)           # 왼쪽으로 120도 회전
t.forward(100)          # 100픽셀 실선 그리기

t.left(angle)           # 왼쪽으로 120도 회전
t.forward(100)          # 100픽셀 실선 그리기