from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""
while x==4:
    print("True")
while x==5:
    print("False")

while True:
        x,y,z=mc.player.getTilePos()
        mc.postToChat("你在X； "+str(x)+"Y: "+str(y)+"Z: "+str(z) )
"""
x,y,z =mc.player.getTilePos()
mc.setBlock()