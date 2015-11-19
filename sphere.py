import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create("54.175.169.202")

mc.postToChat("Here is your sphere")

radius = 6
playerPos = mc.player.getPos()

for x in range(radius*-1,radius):
	for y in range(radius*-1,radius):
		for z in range(radius*-1,radius):
			if x**2 + y**2 + z**2 < radius**2:
				mc.setBlock(playerPos.x+x,playerPos.y+y+radius,playerPos.z-z-10, block.GOLD_BLOCK)
time.sleep(5)

mc.postToChat("Too Late!")
for x in range(radius*-1,radius):
	for y in range(radius*-1,radius):
		for z in range(radius*-1,radius):
			if x**2 + y**2 + z**2 < radius**2:
				mc.setBlock(playerPos.x+x,playerPos.y+y+radius,playerPos.z-z-10, 0)
