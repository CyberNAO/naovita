'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Definition du sixieme exercice du parcours
               Vita, consiste a etirer l'interieur des cuisses
'''

from tools import Init_Pose

class Ex6(object):
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
            
            # exercice
            self.repeatExercice(nbFois)
            
            self.finalise()
        
    '''
    Repete l'exercice nbFois fois
    '''
    def repeatExercice(self, nbFois):
        self.init4ExerciceGauche()
        if nbFois > 1:
            for i in range(nbFois):
                self.doExerciceGauche()
            self.finalise()
            self.init4ExerciceDroite()
            for i in range(nbFois):
                self.doExerciceDroite()
        else:
            self.doExerciceGauche()
            self.finalise()
            self.init4ExerciceDroite()
            self.doExerciceDroite()
        
    '''
    Termine l'exercice en revenant en position initiale
    '''
    def finalise(self):
        # mets le robot en position Init_Pose
        initPose = Init_Pose.Init_Pose(self.__proxy)
        initPose.do()
        
    def init4ExerciceGauche(self):
        # mets le robot en position Init_Pose
        initPose = Init_Pose.Init_Pose(self.__proxy)
        initPose.do()
        
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
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 1.39626, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.10000, 1.50000, 3.00000])
        keys.append([ [ 0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 0.87266, [ 2, -0.46667, -0.04887], [ 2, 0.50000, 0.05236]], [ 0.92502, [ 2, -0.50000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ -1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 0.17453, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ -1.04720, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ -1.56207, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 1.39626, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.10000, 1.50000, 3.00000])
        keys.append([ [ -0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ -0.87266, [ 2, -0.46667, 0.04887], [ 2, 0.50000, -0.05236]], [ -0.92502, [ 2, -0.50000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ -0.17453, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.04720, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 1.56207, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.69813, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.10472, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.43633, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.40143, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.69813, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 1.13446, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.29671, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.73832, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.43633, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.26180, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.69813, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.08727, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.36652, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.57596, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.angleInterpolationBezier(names, times, keys);
        except BaseException, err:
            print str(err)

        
    def init4ExerciceDroite(self):
        # mets le robot en position Init_Pose
        initPose = Init_Pose.Init_Pose(self.__proxy)
        initPose.do()
        
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
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 1.39626, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.10000, 1.50000, 3.00000])
        keys.append([ [ 0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 0.87266, [ 2, -0.46667, -0.04887], [ 2, 0.50000, 0.05236]], [ 0.92502, [ 2, -0.50000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ -1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 0.17453, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ -1.04720, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ -1.56207, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 1.39626, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.10000, 1.50000, 3.00000])
        keys.append([ [ -0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ -0.87266, [ 2, -0.46667, 0.04887], [ 2, 0.50000, -0.05236]], [ -0.92502, [ 2, -0.50000, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ -0.17453, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.10000, 1.50000])
        keys.append([ [ 1.04720, [ 2, -0.03333, 0.00000], [ 2, 0.46667, 0.00000]], [ 1.56207, [ 2, -0.46667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.69813, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.73832, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.43633, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.26180, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.69813, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.08727, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 0.36652, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.57596, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.10472, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.43633, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.40143, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ 0.69813, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ 1.13446, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.10000, 3.00000])
        keys.append([ [ -0.34907, [ 2, -0.03333, 0.00000], [ 2, 0.96667, 0.00000]], [ -0.29671, [ 2, -0.96667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.10000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.angleInterpolationBezier(names, times, keys);
        except BaseException, err:
            print str(err)
        
    '''
    Decrit les mouvements de l'exercice pour le cote gauche
    '''
    def doExerciceGauche(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("HeadPitch")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderPitch")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.39626, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.92502, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.92502, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.17453, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.17453, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ -1.56207, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -1.56207, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.39626, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.92502, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.92502, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ -0.17453, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.17453, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 1.56207, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.56207, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.69813, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.69813, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.69813, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.69813, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.10472, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.10472, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.10472, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.10472, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.40143, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.40143, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.40143, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.40143, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 1.13446, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.62316, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 1.62316, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 1.13446, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.29671, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.87266, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.87266, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.29671, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.10000, 2.00000, 4.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.73832, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.73827, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.73832, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.73832, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.26180, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.10472, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.10472, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.26180, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.08727, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.08727, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.08727, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.08727, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.36652, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.69813, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.69813, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.36652, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.57596, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.57596, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.57596, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.57596, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.angleInterpolationBezier(names, times, keys);
        except BaseException, err:
            print str(err)
        
    '''
    Decrit les mouvements de l'exercice pour le cote droit
    '''
    def doExerciceDroite(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("HeadPitch")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderPitch")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.39626, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LShoulderRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.92502, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.92502, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.17453, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.17453, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LElbowRoll")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ -1.56207, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -1.56207, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LWristYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHand")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderPitch")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 1.39626, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.39626, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RShoulderRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.92502, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.92502, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.92502, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ -0.17453, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.17453, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RElbowRoll")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 1.56207, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.56207, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RWristYaw")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHand")
        times.append([ 0.10000, 2.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipYawPitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.69813, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.69813, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.69813, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.69813, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.73832, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.73827, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.73832, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.73832, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LHipPitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.26180, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.10472, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.10472, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.26180, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LKneePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.08727, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.08727, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.08727, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.08727, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnklePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 0.36652, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.69813, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.69813, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.36652, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("LAnkleRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.57596, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.57596, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.57596, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.57596, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipRoll")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.10472, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.10472, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.10472, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.10472, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RHipPitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.40143, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.40143, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.40143, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.40143, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RKneePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ 1.13446, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 1.62316, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 1.62316, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ 1.13446, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnklePitch")
        times.append([ 0.10000, 2.00000, 4.00000, 6.00000])
        keys.append([ [ -0.29671, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ -0.87266, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.87266, [ 2, -0.66667, 0.00000], [ 2, 0.66667, 0.00000]], [ -0.29671, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        names.append("RAnkleRoll")
        times.append([ 0.10000, 2.00000, 4.00000])
        keys.append([ [ 0.00000, [ 2, -0.03333, 0.00000], [ 2, 0.63333, 0.00000]], [ 0.00000, [ 2, -0.63333, 0.00000], [ 2, 0.66667, 0.00000]], [ 0.00000, [ 2, -0.66667, 0.00000], [ 2, 0.00000, 0.00000]]])
        
        try:
            self.__proxy.angleInterpolationBezier(names, times, keys);
        except BaseException, err:
            print str(err)