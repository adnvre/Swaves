"""
The function for the Runge Kutta method

"""

# The Runge Kutta method
def RK4(diffEQ,xStart,vStart,tStart,dt):
	a1 = diffEQ(xStart,vStart,tStart)
	v1 = vStart

	xHalf1 = xStart + v1 * dt/2.0
	vHalf1 = vStart + a1 * dt/2.0

	a2 = diffEQ(xHalf1,vHalf1,tStart+dt/2.0)
	v2 = vHalf1

	xHalf2 = xStart + v2 * dt/2.0
	vHalf2 = vStart + a2 * dt/2.0

	a3 = diffEQ(xHalf2,vHalf2,tStart+dt)
	v3 = vHalf2

	xEnd = xStart + v3 * dt
	vEnd = vStart + a3 * dt

	a4 = diffEQ(xEnd,vEnd,tStart+dt)
	v4 = vEnd

	aMiddle = 1.0/6.0 * (a1+2*a2+2*a3+a4)
	vMiddle = 1.0/6.0 * (v1+2*v2+2*v3+v4)

	xEnd = xStart + vMiddle*dt
	vEnd = vStart + aMiddle*dt

	return xEnd, vEnd
