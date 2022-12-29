from sympy import *

x=Symbol('x')

def tanLine(y,t):
    dy=diff(y,x)
    m=dy.subs(x,t)
    return sympify(m*(x-t)+y.subs(x,t))

def newtonMathod(f,val):
    tl=tanLine(f,val)
    slv=solve(Eq(tl,0),x)

    plot_1 = plot(f, xlim=[0,10], ylim=[0,10], show=False)
    plot_2 = plot(tl, xlim=[0,10], ylim=[0,10], show=False)
    plot_1.extend(plot_2)

    plot_1.show()
    print(N(slv[0]))
    if(abs(slv[0]-val)<=0.00000001):
        return slv[0]
    else:
        return newtonMathod(f,slv[0])    

eq=input("방정식을 입력하세요.:")

x0=int(input("초깃값을 입력하세요.:"))

leq=sympify(eq.split('=')[0])
req=sympify(eq.split('=')[1])
y=sympify(leq-req)

newtonMathod(y,x0)
