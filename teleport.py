import mcpi.minecraft as minecraft
import time
import server
mc = minecraft.Minecraft.create(server.address)
x = 6
y = 5
z = 2
currentpos = mc.player.getPos()
blockType = 103
mc.player.setTilePos(0,0,0)
mc.setBlock(x,y,z,blockType)
y+=1
mc.setBlock(x,y,z,blockType)
