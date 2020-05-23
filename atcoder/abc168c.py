import math

pi = math.pi
a, b, h, m = map(int, input().split())
m_theta = m*2*pi/60
h_theta = h*2*pi/12 + m*2*pi/720
theta = abs(h_theta-m_theta)
# print(math.cos(theta))
c2 = a**2 + b**2 - 2*a*b*math.cos(theta)
print(math.sqrt(c2))
