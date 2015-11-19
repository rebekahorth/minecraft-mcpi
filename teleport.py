import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
x = 6
y = 5
z = 2
currentpos = mc.player.getPos()
blockType = 103
mc.player.setTilePos(0,0,0)
mc.setBlock(x,y,z,blockType)

y+=1
mc.setBlock(x,y,z,blockType)
