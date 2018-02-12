# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:10:09 2018

@author: clawford
"""

def write_to_scrol(inst):
    print('hi from Queue', inst)
    for idx in range(10):
        inst.gui_queue.put('Message from a queue: ' + str(idx))
    inst.create_thread()