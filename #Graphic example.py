#Graphic example
import matplotlib.pyplot as plt
x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]
z = [0,2,4,6,8,10]
plt.plot(x,y,'b*-',label='f(x)=x^2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Big Title')
plt.grid()
plt.plot(x,z,'b--',label="f'(x)=2x",c='0.6')
plt.legend()
plt.show()