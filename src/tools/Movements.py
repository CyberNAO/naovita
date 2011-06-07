'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Classe permettant de definir des mouvements

'''

from naoqi import ALProxy

class Movements(object):
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
        
    def move(self):
        try:
            self.__proxy.post.angleInterpolationBezier(self.names, self.times, self.keys);
        except BaseException, err:
            print str(err)
        
    '''
    @group : Setters
    '''
    def addName(self, name):
        self.names.append(name)
        
    def addTime(self, time):
        self.times.append(time)
        
    def addKey(self, key):
        self.keys.append(key)
        
    '''
    @group : Getters
    '''
    def getNames(self):
        return self.names
        
    def getTimes(self):
        return self.times
        
    def getKeys(self):
        return self.keys
    
    names = property(addName, getNames, None, None)
    times = property(addTime, getTimes, None, None)
    keys  = property(addKey,  getKeys,  None, None)
        
            