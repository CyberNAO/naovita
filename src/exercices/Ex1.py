'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Definition du premier exercice du parcours
               Vita, consiste a balancer les bras d'avant 
               en arriere, de maniere alternee (bras gauche
               en avant, bras droit en arriere et inversement)
'''

from tools import Zero, Init_Pose

class Ex1(object):
    '''
    classdocs
    '''

    def __init__(self, p):
        '''
        Constructor
        '''
        self.__proxy = p
    
    # ordonne au nao de faire l'exercice nbFois fois
    def do(self, nbFois):
        
        if nbFois > 0:
        
            # initialisation
            self.initialisation()
            
            # exercice
            self.repeatExercice(nbFois)
            
            # terminaison
            self.finalise()
    
    '''
    Initialisation de la position du robot
    '''
    def initialisation(self):
        # mets le nao en position Zero
        zero = Zero.Zero(self.__proxy)
        zero.do()
        
        # initialise la position des bras
        self.initPos()
    
    '''
    Repete l'exercice nbFois fois
    '''    
    def repeatExercice(self, nbFois):
        if nbFois > 1:
            for i in range(nbFois):
                self.doExercice()
        else:
            self.doExercice()
            
    '''
    Termine l'exercice en revenant en position initiale
    '''
    def finalise(self):
        # mets le robot en position Init_Pose
        initPose = Init_Pose.Init_Pose(self.__proxy)
        initPose.do()
        
        
    '''
    Decrit les mouvements pour un balancement des bras
    '''
    def doExercice(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("LShoulderPitch")
        times.append([ 1.00000, 2.00000, 3.00000])
        keys.append([ [ 2.07694, [ 2, -0.33333, 0.00000], [ 2, 0.33333, 0.00000]], [ 1.48353, [ 2, -0.33333, 0.49160], [ 2, 0.33333, -0.49160]], [ -0.87266, [ 2, -0.33333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 1.00000, 2.00000, 3.00000])
        keys.append([ [ -0.87266, [ 2, -0.33333, 0.00000], [ 2, 0.33333, 0.00000]], [ 1.48353, [ 2, -0.33333, -0.49304], [ 2, 0.33333, 0.49304]], [ 2.08560, [ 2, -0.33333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.angleInterpolationBezier(names, times, keys);
        except BaseException, err:
            print str(err)
        
    '''
    Decrit les mouvements pour aller depuis la position Zero
    jusqu'a la position choisie pour le debut de l'exercice
    '''
    def initPos(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("HeadPitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderPitch")
        times.append([ 0.10000, 1.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.30000, 0.00000]], [ 1.57080, [ 2, -0.30000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.10000, 1.00000])
        keys.append([ [ 0.00870, [ 2, -0.03333, 0.00000], [ 2, 0.30000, 0.00000]], [ 0.17453, [ 2, -0.30000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.10000, 1.00000])
        keys.append([ [ -0.00870, [ 2, -0.03333, 0.00000], [ 2, 0.30000, 0.00000]], [ -0.00873, [ 2, -0.30000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.10000, 1.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.30000, 0.00000]], [ 1.57080, [ 2, -0.30000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.10000, 1.00000])
        keys.append([ [ -0.00870, [ 2, -0.03333, 0.00000], [ 2, 0.30000, 0.00000]], [ -0.17453, [ 2, -0.30000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00870, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.angleInterpolationBezier(names, times, keys);
        except BaseException, err:
            print str(err)

        
        
        
        