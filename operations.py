#performing operations on n*n matrix
import numpy as np
x=np.array(input("enter n*n matrix"))
y=np.array(input("enter  another n*n matrix"))
print "the matrix x\n", x
print "the matrix y\n",y
add=np.add(x,y)
print "addition of two matrices\n",add
sub=np.subtract(x,y)
print"subtraction of two matrices\n",sub
div=np.divide(x,y)
print "division of two matrices\n",div
mul=np.multiply(x,y)
print"multipilcation of two matrices\n",mul
dot=np.dot(x,y)
print"dot product of two matrices\n",dot
sqrt=np.sqrt(x)
print "sqrt of matrix x\n",sqrt
trans=x.T
print" transpose of matrix y \n",trans
summ=np.sum(y)
print"sum of elements of y\n",summ
sqr=np.square(y)
print" square of matrix y \n",sqr
trac=np.trace(x)
print "trace of matrix x\n",trac
dia=np.diagonal(x)
print "diagonal elements of matrix x\n",trac
rank=np.linalg.matrix_rank(x)
print"rank of matrix x\n",rank
det=np.linalg.det(x)
print"determinant of the matrix\n",det
inverse=np.linalg.inv(x)
print"inverse of matrix x\n",inverse
eig=np.linalg.eig(x)
print "eigen vectors of x \n",eig
eigval=np.linalg.eigvals(x)
print "eigen values of x \n",eigval
power=np.linalg.matrix_power(x,3)
print"power of matrix x\n",power

