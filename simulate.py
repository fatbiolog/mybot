import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for z in range(1000):
    
    p.stepSimulation()
    time.sleep( 1/60 )
    print(z)


p.disconnect() 
