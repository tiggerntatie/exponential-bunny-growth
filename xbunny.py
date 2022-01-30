from ggame import ImageAsset, Sprite, MouseEvent
from random import random, randint
from ggame.timer import Timer
from ggame.mathapp import MathApp


bunnylist = []
AVERAGEOFFSPRING = 5


class Bunny(Sprite):

    asset = ImageAsset("bunny.png")

    @classmethod
    def randomBunny(cls, width, height):
        return cls((randint(-50,width),randint(-50,height)))

    def __init__(self, position):
        super().__init__(Bunny.asset, position)


    def step(self):
        pass
    
    



class DemoApp(MathApp):

    def __init__(self):
        super().__init__()
        for i in range(2):
            bunnylist.append(Bunny.randomBunny(self.width, self.height))
        self.TIMER = Timer()
        # Execute timercallback every 1 seconds
        self.TIMER.callEvery(1, self.timercallback)
        
    def timercallback(self, t):
        """
        Callback function to receive notification of timer expiration.
        """
        for i in range(len(bunnylist)//2*AVERAGEOFFSPRING):
            bunnylist.append(Bunny.randomBunny(self.width, self.height))



# Create the app
app = DemoApp()
# Run the app
app.run()
