'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Classe contenant les methodes de deplacements
               jusqu'aux exercices
'''

import time
import motion
class Deplacements(object):
    '''
    classdocs
    '''

    def __init__(self, connection):
        '''
        Constructor
        '''
        self.__distanceAcceptable = 50
        self.__motionProxy = connection.getProxy('Motion')
        

    def walk(self):
        #####################
        ## Enable arms control by Walk algorithm
        #####################
        self.__motionProxy.setWalkArmsEnable(True, True)
        #~ motionProxy.setWalkArmsEnable(False, False)
        
        #####################
        ## FOOT CONTACT PROTECTION
        #####################
        #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",False]])
        self.__motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])
        
        #TARGET VELOCITY
        X = 1.0  #backward
        Y = 0.0
        Theta = 0.0
        Frequency =1.0 #low speed
        self.__motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
        
        time.sleep(4.0)
        
        #TARGET VELOCITY
        X = 0.8
        Y = 0.0
        Theta = 0.0
        Frequency =1.0 #Max speed
        self.__motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
        
        time.sleep(4.0)
        
        #####################
        ## Arms User Motion
        #####################
        
        # desactivate Left Arm
        self.__motionProxy.setWalkArmsEnable(False, True)
        
        JointNames = ["LShoulderPitch", "LShoulderRoll","LElbowYaw","LElbowRoll"]
        Arm1 = [-40,  25, 0, -40]
        Arm1 = [ x * motion.TO_RAD for x in Arm1]
        
        Arm2 = [-40,  50, 0, -80]
        Arm2 = [ x * motion.TO_RAD for x in Arm2]
        
        self.__motionProxy.angleInterpolationWithSpeed(JointNames,Arm1, 0.6)
        self.__motionProxy.angleInterpolationWithSpeed(JointNames,Arm2, 0.6)
        self.__motionProxy.angleInterpolationWithSpeed(JointNames,Arm1, 0.6)
        
        # reactivate Left Arm
        self.__motionProxy.setWalkArmsEnable(True, True)
        
        time.sleep(2.0)
        
        #####################
        ## End Walk
        #####################
        #TARGET VELOCITY
        X = 0.0
        Y = 0.0
        Theta = 0.0
        self.__motionProxy.setWalkTargetVelocity(  X, Y, Theta, Frequency)


    def step(self):
        '''
        Step To
        Make Nao one Step
        '''
        # send robot to Pose Init
        self.poseInit()
        
        #####################
        ## Enable arms control by Walk algorithm
        #####################
        self.__motionProxy.setWalkArmsEnable(False, False)
        
        #STEPTO
        Leg = "RLeg"
        X = 0.04
        Y = -0.02
        Theta = -0.3
        self.__motionProxy.stepTo(Leg, X, Y, Theta)
        self.__motionProxy.waitUntilWalkIsFinished()
        
        #~ #STEPTO
        Leg = "RLeg"
        X = 0.00
        Y = 0.00
        Theta = 0.00
        self.__motionProxy.stepTo(Leg, X, Y, Theta)



    def poseInit(self):
        # Feel free to experiment with these values
        kneeAngle  = 40
        torsoAngle =  0
        wideAngle  =  0
        #----------------------------- prepare the angles ----------------------------
        #Get the Number of Joints
        NumJoints = len( self.__motionProxy.getJointNames("Body"))
    
        # Define The Initial Position
        Head     = [0, 0]
        LeftArm  = [120,  15, -90, -80]
        LeftLeg  = [0,  wideAngle, -kneeAngle/2-torsoAngle, kneeAngle, -kneeAngle/2, -wideAngle]
        RightLeg = [0, -wideAngle, -kneeAngle/2-torsoAngle, kneeAngle, -kneeAngle/2,  wideAngle]
        RightArm = [120, -15,  90,  80]
        
        # If we have hands, we need to add angles for wrist and open/close hand
        if (NumJoints == 26):
            LeftArm  += [0, 0]
            RightArm += [0, 0]
        
        # Gather the joints together
        pTargetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm
        
        # Convert to radians
        pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
        
        #------------------------------ send the commands -----------------------------
        #We use the "Body" name to signify the collection of all joints
        pNames = "Body"
        #We set the fraction of max speed
        pMaxSpeedFraction = 0.2
        #Ask motion to do this with a blocking call
        self.__motionProxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

    '''
    TO DO
    '''
    def goTo(self, position):
        print 'je vais jusqu\'a la position ' + str(position) + '...'
        
        distanceRestante = self.testDistance()
        
        while  distanceRestante > self.__distanceAcceptable:
            
            distanceRestante = self.testDistance()
            
    
    '''
    TO DO
    '''
    def testDistance(self):
        print 'test de la distance restante entre le panneau et le nao...'
        
        return 0