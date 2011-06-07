'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Exportation de la position Zero definie 
               par defaut dans Choregraphe
'''

from naoqi import ALProxy

class Zero(object):
    '''
    classdocs
    '''


    def __init__(self, p):
        '''
        Constructor
        '''
        self.__proxy = p
        self.names   = list()
        self.times   = list()
        self.keys    = list()
        
    def do(self):
        self.names.append("LShoulderPitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LShoulderRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00870, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LElbowYaw")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LElbowRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ -0.00870, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RShoulderPitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RShoulderRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ -0.00870, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RElbowYaw")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RElbowRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00870, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LHipYawPitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LHipRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LHipPitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LKneePitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LAnklePitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("LAnkleRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RHipRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RHipPitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RKneePitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RAnklePitch")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        self.names.append("RAnkleRoll")
        self.times.append([ 2.00000])
        self.keys.append([ [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.post.angleInterpolationBezier(self.names, self.times, self.keys);
        except BaseException, err:
            print str(err)