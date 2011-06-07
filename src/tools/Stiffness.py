'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Asservissement/desasservissement des moteurs

'''


class Stiffness(object):
    '''
    classdocs
    '''


    def __init__(self, p):
        '''
        Constructor
        '''
        self.__proxy    = p
        self.corps      = "Body"  # Body = collection de tous les joints du robots
        self.stiffness  = 0.0     # moteur desasservis par defaut
        self.temps      = 1.0     # effectue l'ordre tout de suite
        
    
    '''
    Asservissement des moteurs
    '''
    def asservir(self):
        self.stiffness = 1.0
        self.__proxy.stiffnessInterpolation(self.corps, self.stiffness, self.temps)
        
    '''
    De-asservissement des moteurs
    '''
    def desasservir(self):
        self.stiffness = 0.0
        self.__proxy.stiffnessInterpolation(self.corps, self.stiffness, self.temps)
    
        