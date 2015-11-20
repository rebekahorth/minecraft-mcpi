from mcpi.minecraft import Minecraft
from time import sleep
import server
mc = Minecraft.create(server.address)

flower = 38

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)