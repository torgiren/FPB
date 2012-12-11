#!/usr/bin/env python
#-*- coding: utf-8 -*-
#from graph import *
#from block import *
#print "a"
#graph=GraphEngine()
#block=Block(-5,-5,-10)
#graph.add_obj(block)
#while True:
#	graph.render()
#	pygame.time.delay(100)
from engine import *
import profile
engine=GameEngine()
engine.mainLoop()
#profile.run("engine.mainLoop()")
