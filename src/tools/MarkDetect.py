'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Alex Bulla
@description : Classe contenant les methodes de detection
                des naoMarks
'''

import time
import motion
from vision_definitions import *

class MarkDetect(object):
    
    def __init__(self, connection):
        '''
            Constructor
        '''        
        # Needs both proxies to move and detect nao marks
        self.__motionProxy = connection.getProxy('ALMotion')
        
        # Subscribe to the ALLandMarkDetection proxy
        # This means that the module will write in ALMemory with
        # the given period below (period = 500)
        self.__landMarkProxy = connection.getProxy('ALLandMarkDetection')
        self.__landMarkProxy.subscribe("MarkDetect", 500, 0.0 )
        
        # ALMemory variable where the ALLandMarkdetection modules
        # outputs its results
        self.__memoryProxy = connection.getProxy('ALMemory')
        self.__memValue = "LandmarkDetected"
        
        # Get camera proxy
        self.__cameraProxy = connection.getProxy('ALVideoDevice')
        

    def walkUntilDetection(self):
        '''
            Walk until a nao mark is seen on the floor
        '''
        
        #select the lower camera
        #self.__switchCam('low')
        
        ids = {}
        # A simple loop that reads the memValue and checks whether landmarks are detected.
        for i in range(0, 20):
            time.sleep(0.5)
            #id = self.getMarkId()
            
            if id != None :
                if id not in ids.keys() :
                    ids[id] = 1
                else :        
                    ids[id] += 1
            
        #maxDected = max(ids.values())
        #for id in ids.keys() :
        #    if ids[id] == maxDected :
        #        detectedId = ids[id]
        
        maxDected = max(ids, key=ids.get)
        
        print "Detected mark id is " + str(maxDected)

        
        # unsubscribe proxies
        self.__unsubscribe()
    
    
    def getMarkId(self):
        val = self.__memoryProxy.getData(self.__memValue)
        print ""
        print "*****"
        print ""
        
        # Check whether we got a valid output: a list with two fields.
        if(val and isinstance(val, list) and len(val) == 2):
    
            # We detected naomarks !
            # For each mark, we can read its shape info and ID.
            # First Field = TimeStamp.
            timeStamp = val[0]
            # Second Field = array of Mark_Info's.
            markInfoArray = val[1]
            
            try:
                # Browse the markInfoArray to get info on each detected mark.
                for markInfo in markInfoArray:    
                    # First Field = Shape info.
                    markShapeInfo = markInfo[0]
        
                    # Second Field = Extra info (ie, mark ID).
                    markExtraInfo = markInfo[1]
                    id = markExtraInfo[0]
                    print "mark  ID: %d" % (markExtraInfo[0])
                    print "  alpha %.3f - beta %.3f" % (markShapeInfo[1], markShapeInfo[2])
                    print "  width %.3f - height %.3f" % (markShapeInfo[3], markShapeInfo[4])
                    return id

            except Exception, e:
                print "Naomarks detected, but it seems getData is invalid. ALValue ="
                print val
                print "Error msg %s" % (str(e))
        
        else:
            print "No landmark detected"
            return None
    
    
    def __switchCam(self, camId):
        '''
            high is 1, low is 0 
        '''
        if camId == 'low':
            camId = 1
        else:
            camId = 0
        
        self.__cameraProxy.subscribe("MarkDetect", kQVGA, kRGBColorSpace, 30)
        self.__cameraProxy.setParam(kCameraSelectID, camId)
        
        self.__cameraProxy.unsubscribe(self.__cameraProxy)
    
    def __unsubscribe(self):
        '''
            Destroy method
        '''
        self.__landMarkProxy.unsubscribe("MarkDetect")
        
                        
                        
                        