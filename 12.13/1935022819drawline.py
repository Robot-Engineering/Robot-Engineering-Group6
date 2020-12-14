import turtle as t

class DrawLine:
    def __init__(self,xRect,lengthLine,widthLine): 
        self.xLine=xLine
        self.lengthLine=lengthLine
        self.widthLine=widthLine

    def showRect(self):
        t.penup()
        t.goto(self.xLine)
        t.pendown() 
        for _ in range(0,1):
            t.forword(self.lengthLine)
            t.right(90)
            t.forword(self.widthLine)
            t.right(90)
