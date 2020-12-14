
import turtle as t

class DrawRect:
    def __init__(self,xRect,yRect,lengthRect,widthRect): #设置起始点和长宽
        self.xRect=xRect
        self.yRect=yRect
        self.lengthRect=lengthRect
        self.widthRect=widthRect

    def showRect(self):      #画矩形
        t.penup()
        t.goto(self.xRect,self.yRect)
        t.pendown() 
        for _ in range(0,1):
            t.forword(self.lengthRect)
            t.right(90)
            t.forword(self.widthRect)
            t.right(90)
        

    
