import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for z in range(1000):
    
    p.stepSimulation()
    time.sleep( 1/60 )
    print(z)


p.disconnect() 
