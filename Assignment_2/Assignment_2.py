import matplotlib.pyplot as plt
Sub =[0,15,30,45,60]
S1=[0,0,15,30,45]
S2=[15,30,45,60,60]
plt.plot(Sub,S1,label="When A arrives first")
plt.plot(Sub,S2,label="When B arrives first")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
