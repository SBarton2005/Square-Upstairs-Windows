import turtle
h = turtle.Turtle()
h.up()
h.backward(245)
h.right(90)
h.forward(100)
h.left(90)
def house():
  number = int(input("# of Houses: "))
  i = 0
  while i < number:
    length = int(input("Length: "))
    height = int(input("Height: "))
    hc = input("House Color: ")
    dh = int(input("Door Height: "))
    dw = int(input("Door Width: "))
    dc = input("Door Color: ")
    distance = (length / 2) - (dw /2)
    chimney = input("Is there a chimeny (y/n): ")
    if chimney == "y":
      ch = int(input("Chimney Height: "))
      cw = int(input("Chimney Width: "))
      cd = ch - (cw * (3 ** .5))
      cc = input("Chimeny Color: ")
    aw = input("Is there an attic window (y/n): " )
    if aw == "y":
      radius = int(input("Radius: "))
      center = (length / 6) * (3 ** .5)
      wc = input("Circle Window Color: ")
    lp = input("Is there a plot of land in front (y/n): ")
    if lp == "y":
      print("Length of land is length of house")
      width = int(input("Width of Land Plot: "))
      lpc = input("Color of Land: ")
    uw = input("Are there two upstairs sqare windows (y/n): ")
    if uw == "y":
      side = int(input("Side Length: "))
      swd = (length - side - side) / 3
      dwd = (height - dh - side) / 2
      wc = input("Window Color: ")
    h.down()
    h.fillcolor(hc)
    h.begin_fill()
    h.forward(length)
    h.left(90)
    h.forward(height)
    h.left(30)
    h.forward(length)
    h.left(120)
    h.forward(length)
    h.left(120)
    h.forward(length)
    h.left(180)
    h.forward(length)
    h.left(90)
    h.forward(height)
    h.left(90)
    h.end_fill()
    h.forward(distance)
    h.left(90)
    h.fillcolor(dc)
    h.begin_fill()
    h.forward(dh)
    h.right(90)
    h.forward(dw)
    h.right(90)
    h.forward(dh)
    h.right(90)
    h.forward(dw)
    h.end_fill()
    h.right(180)
    h.forward(dw)
    if chimney == "y":
      h.fillcolor(cc)
      h.right(180)
      h.forward(dw)
      h.forward(distance)
      h.right(90)
      h.forward(height)
      h.begin_fill()
      h.forward(ch)
      h.right(90)
      h.forward(cw)
      h.right(90)
      h.forward(cd)
      h.right(30)
      h.forward(2*cw)
      h.left(30)
      h.end_fill()
      h.forward(height)
      h.left(90)
      h.forward(distance)
      h.forward(dw)
    if aw == "y":
      h.up()
      h.backward(dw/2)
      h.left(90)
      h.forward(height)
      h.forward(center)
      h.backward(radius)
      h.right(90)
      h.down()
      h.fillcolor(wc)
      h.begin_fill()
      h.circle(radius)
      h.end_fill()
      h.left(90)
      h.forward(radius*2)
      h.backward(radius)
      h.right(90)
      h.forward(radius)
      h.backward(radius*2)
      h.forward(radius)
      h.right(90)
      h.up()
      h.forward(center)
      h.forward(height)
      h.left(90)
      h.forward(dw/2)
    if lp == "y":
      h.forward(distance)
      h.down()
      h.fillcolor(lpc)
      h.right(90)
      h.begin_fill()
      h.forward(width)
      h.right(90)
      h.forward(length)
      h.right(90)
      h.forward(width)
      h.right(90)
      h.forward(length)
      h.end_fill()
      h.backward(distance)
    if uw == "y":
      h.up()
      h.backward(dw)
      h.backward(distance)
      h.left(90)
      h.forward(dh)
      h.forward(dwd)
      h.right(90)
      h.forward(swd)
      h.fillcolor(wc)
      h.begin_fill()
      h.down()
      h.forward(side)
      h.left(90)
      h.forward(side)
      h.left(90)
      h.forward(side)
      h.left(90)
      h.forward(side)
      h.left(90)
      h.end_fill()
      h.forward(side/2)
      h.left(90)
      h.forward(side)
      h.backward(side/2)
      h.right(90)
      h.forward(side/2)
      h.backward(side)
      h.forward(side/2)
      h.right(90)
      h.forward(side/2)
      h.left(90)
      h.backward(side/2)
      h.up()
      h.forward(side)
      h.forward(swd)
      h.begin_fill()
      h.down()
      h.forward(side)
      h.left(90)
      h.forward(side)
      h.left(90)
      h.forward(side)
      h.left(90)
      h.forward(side)
      h.left(90)
      h.end_fill()
      h.forward(side/2)
      h.left(90)
      h.forward(side)
      h.backward(side/2)
      h.right(90)
      h.forward(side/2)
      h.backward(side)
      h.forward(side/2)
      h.right(90)
      h.forward(side/2)
      h.left(90)
      h.backward(side/2)
      h.up()
      h.forward(side)
      h.forward(swd)
      h.right(90)
      h.forward(dwd)
      h.forward(dh)
      h.right(90)
      h.forward(distance)
      h.left(180)
    h.forward(distance)
    h.up()
    h.forward(20)
    i += 1
house()