'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Classe permettant de se connecter au NAO
               (en local par defaut)
'''

from naoqi import ALProxy

class Connexion(object):


    '''
    @contructor
    '''
    def __init__(self, robot):
        
        # choix du robot
        if robot == None:
            self.__ip = "laptopnono.local"
        else:
            if robot == "astro":
                self.__ip = "10.194.70.11"
            else:
                self.__ip = "10.194.70.12"
                
        # port par defaut
        self.__port        = 9559
        
        # declaration des proxy
        self.__loggerProxy = None
        self.__proxy       = None


    '''
    Connexion au robot defini dans le contructor
    '''
    def connect(self):
        self.__loggerProxy = ALProxy("ALLogger", self.__ip, self.__port)
        self.__proxy       = ALProxy("ALMotion", self.__ip, self.__port)
        return self.__proxy

    '''
    @group: Setters
    '''
    def setIP(self, ip):
        self.__ip = ip
        
    def setPort(self, port):
        self.__port = port
        
    '''
    @group: Getters
    '''
    def getIP(self):
        return self.__ip
        
    def getPort(self):
        return self.__port
    
    def getLoggerProxy(self):
        return self.__loggerProxy
    
    def getProxy(self):
        return self.__proxy
    
    ip          = property(setIP  , getIP         , None, None)
    port        = property(setPort, getPort       , None, None)
    loggerProxy = property(None   , getLoggerProxy, None, None)
    proxy       = property(None   , getProxy      , None, None) 
    
    
        