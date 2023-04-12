# que 1
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex((self.real+no.real), self.imaginary+no.imaginary)
        
    def __sub__(self, no):
         return Complex((self.real-no.real), (self.imaginary-no.imaginary))
        
    def __mul__(self, no):
        r = (self.real*no.real)-(self.imaginary*no.imaginary)
        i = (self.real*no.imaginary+no.real*self.imaginary)
        return Complex(r, i)

    def __truediv__(self, no):
        conjugate = Complex(no.real, (-no.imaginary))
        num = self*conjugate
        denom = no*conjugate
        try:
            return Complex((num.real/denom.real), (num.imaginary/denom.real))
        except Exception as e:
            print(e)

    def mod(self):
        m = math.sqrt(self.real**2+self.imaginary**2)
        return Complex(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

# que 2
import math

class Point:
  """docstring for Point"""
  def __init__(self, x, y, z):
    # super(Point, self).__init__()
    self.x = x
    self.y = y
    self.z = z

  def minus(self, other):
    return Point(self.x - other.x, self.y - other.y, self.z - other.z)

  def cross(self, other):
    return Point( self.y * other.z - self.z * other.y
                 , self.z * other.x - self.x * other.z
                 , self.x * other.y - self.y * other.x)

  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z

  def abs(self):
    return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

  def str(self):
    return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

def get_Point():
  lst = map(float, raw_input().strip().split())
  return Point(lst[0], lst[1], lst[2])

a = get_Point()
b = get_Point()
c = get_Point()
d = get_Point()

ab = a.minus(b)
bc = b.minus(c)
cd = c.minus(d)

x = ab.cross(bc)
y = bc.cross(cd)

v = x.dot(y) / (x.abs() * y.abs())


print "%.2f" % (math.acos(v) / math.acos(0) * 90,)