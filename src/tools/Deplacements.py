'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Alex Bulla
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
        #self.__distanceAcceptable = 50
        self.__motionProxy = connection.getProxy('ALMotion')
    
    
    def walkToCenter(self):
        self.walk(5.5)
        self.turn(2.231) #6pi/8
    
    def turn(self, Theta):
        #180 degrees
        self.__motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])
        
        #TARGET VELOCITY
        X = 0.0
        Y = 0.0
        #Theta = 1.5709
        Frequency = 0.4 #low speed
        self.__motionProxy.post.walkTo(X, Y, Theta)
        #self.__motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
        
        #time.sleep(4.0)
        
        self.__motionProxy.waitUntilWalkIsFinished()
        #print "turn finished"
        #####################
        ## End Walk
        #####################
        #TARGET VELOCITY
        #X = 0.0
        #Y = 0.0
        #Theta = 0.0
        #self.__motionProxy.setWalkTargetVelocity(  X, Y, Theta, Frequency)
        

    def walk(self, duration):
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
        X = 1.0
        Y = 0.0
        Theta = 0.0
        Frequency = 0.3 #low speed
        self.__motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
        
        time.sleep(duration)
        
        #TARGET VELOCITY
        #X = 0.8
        #Y = 0.0
        #Theta = 0.0
        #Frequency = 1.0 #Max speed
        #self.__motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
        
        #time.sleep(4.0)
        
        #####################
        ## Arms User Motion
        #####################
        
        # desactivate Left Arm
        '''
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
        '''
        #####################
        ## End Walk
        #####################
        #TARGET VELOCITY
        X = 0.0
        Y = 0.0
        Theta = 0.0
        self.__motionProxy.setWalkTargetVelocity(  X, Y, Theta, Frequency)



    def omniWalk(self):
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
        X = 1.0
        Y = 0.0
        Theta = 0.0
        Frequency = 0.3 #low speed
        self.__motionProxy.post.setWalkTargetVelocity(X, Y, Theta, Frequency)
        
        #time.sleep(2.0)
        

    def stopWalk(self):        
        #####################
        ## End Walk
        #####################
        #TARGET VELOCITY
        X = 0.0
        Y = 0.0
        Theta = 0.0
        Frequency = 0.3 #low speed
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
        LeftArm  = [120,  40, -80, -100]
        LeftLeg  = [0,  wideAngle, -kneeAngle/2-torsoAngle, kneeAngle, -kneeAngle/2, -wideAngle]
        RightLeg = [0, -wideAngle, -kneeAngle/2-torsoAngle, kneeAngle, -kneeAngle/2,  wideAngle]
        RightArm = [120, -40,  80,  100]
        
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


    def standUp(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadYaw")
        times.append([ 2.00000])
        keys.append([ [ 0.00303, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("HeadPitch")
        times.append([ 2.00000])
        keys.append([ [ -0.01538, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderPitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 1.41721, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 1.41891, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 0.66323, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.36658, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.25831, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -1.37451, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -1.08210, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -1.05382, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 1.14668, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 1.04720, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 2.00000])
        keys.append([ [ 0.00526, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 1.41721, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 1.41439, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.66323, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -0.36053, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 0.25831, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 1.38056, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 1.08210, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 1.05543, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -1.14668, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -1.04720, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 2.00000])
        keys.append([ [ 0.00526, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.05365, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.00004, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.02269, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.00004, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.87441, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -0.43715, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 2.11185, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.69793, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -1.18952, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -0.34826, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 0.00771, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.00004, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 0.02269, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.00004, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.87441, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -0.43723, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ 2.11185, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.69801, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -1.18645, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ -0.35278, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.13333, 2.00000])
        keys.append([ [ -0.01530, [ 2, -0.04444, 0.00000], [ 2, 0.62222, 0.00000]], [ 0.00004, [ 2, -0.62222, 0.00000], [ 2, 0.00000, 0.00000]]])

        self.__motionProxy.angleInterpolationBezier(names, times, keys);
    
    
    def kneel(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadYaw")
        times.append([ 0.06667])
        keys.append([ [ 0.00303, [ 2, -0.02222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("HeadPitch")
        times.append([ 0.06667])
        keys.append([ [ -0.01538, [ 2, -0.02222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderPitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 1.41891, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 1.41721, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.36658, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 0.66323, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -1.37451, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.25831, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -1.05382, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -1.08210, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 1.04720, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 1.14668, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 0.06667])
        keys.append([ [ 0.00526, [ 2, -0.02222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 1.41439, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 1.41721, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -0.36053, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.66323, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 1.38056, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 0.25831, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 1.05543, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 1.08210, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -1.04720, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -1.14668, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 0.06667])
        keys.append([ [ 0.00526, [ 2, -0.02222, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.00004, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.05365, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.00004, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.02269, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -0.43715, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.87441, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.69793, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 2.11185, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -0.34826, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -1.18952, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.00004, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 0.00771, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.00004, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 0.02269, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -0.43723, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.87441, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.69801, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ 2.11185, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ -0.35278, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -1.18645, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.06667, 2.00000])
        keys.append([ [ 0.00004, [ 2, -0.02222, 0.00000], [ 2, 0.64444, 0.00000]], [ -0.01530, [ 2, -0.64444, 0.00000], [ 2, 0.00000, 0.00000]]])

        self.__motionProxy.angleInterpolationBezier(names, times, keys);
        

    def kneel2(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("LHipYawPitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ -0.00149, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -0.05365, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ 0.00158, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -0.02269, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ -0.43715, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -0.87441, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ 0.69639, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ 2.11185, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ -0.34826, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -1.18952, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ 0.00004, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ 0.00771, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ 0.00004, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ 0.02269, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ -0.43723, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -0.87441, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ 0.69494, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ 2.11185, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ -0.34971, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -1.18645, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.20000, 2.73333])
        keys.append([ [ 0.00004, [ 2, -0.06667, 0.00000], [ 2, 0.84444, 0.00000]], [ -0.01530, [ 2, -0.84444, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.__motionProxy.angleInterpolationBezier(names, times, keys);


    def bendHead(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([ 0.13333, 0.46667, 0.80000, 1.13333, 1.40000])
        keys.append([ [ 0.08727, [ 2, -0.04444, 0.00000], [ 2, 0.11111, 0.00000]], [ 0.17453, [ 2, -0.11111, -0.02909], [ 2, 0.11111, 0.02909]], [ 0.26180, [ 2, -0.11111, -0.02909], [ 2, 0.11111, 0.02909]], [ 0.34907, [ 2, -0.11111, -0.03232], [ 2, 0.08889, 0.02586]], [ 0.43633, [ 2, -0.08889, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.__motionProxy.angleInterpolationBezier(names, times, keys);
        #self.__motionProxy.waitUntilWalkIsFinished()
        
        #print "bend is finished"
        

    def raiseHead(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([ 0.06667, 0.40000, 0.73333, 1.06667, 1.40000, 1.73333])
        keys.append([ [ 0.43633, [ 2, -0.02222, 0.00000], [ 2, 0.11111, 0.00000]], [ 0.34907, [ 2, -0.11111, 0.02909], [ 2, 0.11111, -0.02909]], [ 0.26180, [ 2, -0.11111, 0.02909], [ 2, 0.11111, -0.02909]], [ 0.17453, [ 2, -0.11111, 0.02909], [ 2, 0.11111, -0.02909]], [ 0.06632, [ 2, -0.11111, 0.02909], [ 2, 0.11111, -0.02909]], [ 0.00000, [ 2, -0.11111, 0.00000], [ 2, 0.00000, 0.00000]]])

        self.__motionProxy.angleInterpolationBezier(names, times, keys);
        #self.__motionProxy.waitUntilWalkIsFinished()
        #print "raise is finished"

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