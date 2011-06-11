'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Classe permettant de se connecter au NAO
               (en local par defaut)
'''

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
            elif robot == "astro-local":
                self.__ip = "10.194.70.1"
            elif robot == "robby":
                self.__ip = "10.194.70.12"
            elif robot == "robby-local":
                self.__ip = "10.194.70.2"
            else :
                self.__ip = "10.194.70.11"
                
        # port par defaut
        self.__port        = 9559
        
        # declaration des proxy
        self.__AudioDeviceProxy     = None
        self.__AudioPlayerProxy     = None
        self.__BehaviorManagerProxy = None
        self.__FrameManagerProxy    = None
        self.__FsrProxy             = None
        self.__InertialProxy        = None
        self.__LedsProxy            = None
        self.__LoggerProxy          = None
        self.__LogoDetectionProxy   = None
        self.__LandMarkDetectionProxy = None
        self.__MemoryProxy          = None
        self.__MotionProxy          = None
        self.__SensorsProxy         = None
        self.__SonarProxy           = None
        self.__TextToSpeechProxy    = None
        self.__VideoDeviceProxy     = None
        self.__DCMProxy             = None
        


    '''
    Connexion au robot defini dans le contructor
    '''
#    def connect(self):        
#        try :
#            self.__AudioDeviceProxy     = ALProxy("ALAudioDevice"    , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__AudioPlayerProxy     = ALProxy("ALAudioPlayer"    , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__BehaviorManagerProxy = ALProxy("ALBehaviorManager", self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__FrameManagerProxy    = ALProxy("ALFrameManager"   , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__FsrProxy             = ALProxy("ALFsr"            , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__InertialProxy        = ALProxy("ALInertial"       , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__LedsProxy            = ALProxy("ALLeds"           , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__LoggerProxy          = ALProxy("ALLogger"         , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__LogoDetectionProxy   = ALProxy("ALLogoDetection"  , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__MemoryProxy          = ALProxy("ALMemory"         , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__MotionProxy          = ALProxy("ALMotion"         , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__SensorsProxy         = ALProxy("ALSensors"        , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__SonarProxy           = ALProxy("ALSonar"          , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__TextToSpeechProxy    = ALProxy("ALTextToSpeech"   , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__VideoDeviceProxy     = ALProxy("ALVideoDevice"    , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)
#        try :
#            self.__DCMProxy             = ALProxy("ALDCM"            , self.__ip, self.__port)
#        except RuntimeError,e:
#            print str(e)

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
    
    def getProxy(self, name):
        # ALAudioDevice
        if name == 'ALAudioDevice':
            if self.__AudioDeviceProxy == None :
                try:
                    self.__AudioDeviceProxy = ALProxy("ALAudioDevice", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__AudioDeviceProxy
        # ALAudioPlayer
        elif name == 'ALAudioPlayer':
            if self.__AudioPlayerProxy == None:
                try:
                    self.__AudioPlayerProxy = ALProxy("ALAudioPlayer", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__AudioPlayerProxy
        # ALBehaviorManager
        elif name == 'ALBehaviorManager':
            if self.__BehaviorManagerProxy == None:
                try:
                    self.__BehaviorManagerProxy = ALProxy("ALBehaviorManager", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__BehaviorManagerProxy
        # ALFrameManager
        elif name == 'ALFrameManager':
            if self.__FrameManagerProxy == None:
                try:
                    self.__FrameManagerProxy = ALProxy("ALFrameManager", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__FrameManagerProxy
        # ALFsr
        elif name == 'ALFsr':
            if self.__FsrProxy == None:
                try:
                    self.__FsrProxy = ALProxy("ALFsr", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__FsrProxy
        # ALInertial
        elif name == 'ALInertial':
            if self.__InertialProxy == None:     
                try:
                    self.__InertialProxy = ALProxy("ALInertial", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__InertialProxy
        # ALLeds
        elif name == 'ALLeds':
            if self.__LedsProxy == None:
                try:
                    self.__LedsProxy = ALProxy("ALLeds", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__LedsProxy
        # ALLogger
        elif name == 'ALLogger':
            if self.__LoggerProxy == None:
                try:
                    self.__LoggerProxy = ALProxy("ALLogger", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__LoggerProxy
        # ALLogoDetection
        elif name == 'ALLogoDetection':
            if self.__LogoDetectionProxy == None:
                try:
                    self.__LogoDetectionProxy = ALProxy("ALLogoDetection", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__LogoDetectionProxy
        # ALLandMarkDetection
        elif name == 'ALLandMarkDetection':
            if self.__LandMarkDetectionProxy == None:
                try:
                    self.__LandMarkDetectionProxy = ALProxy("ALLandMarkDetection", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__LandMarkDetectionProxy
        # ALMemory
        elif name == 'ALMemory':
            if self.__MemoryProxy == None:
                try:
                    self.__MemoryProxy = ALProxy("ALMemory", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__MemoryProxy
        # ALMotion
        elif name == 'ALMotion':
            if self.__MotionProxy == None:
                try:
                    self.__MotionProxy = ALProxy("ALMotion", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__MotionProxy
        # ALSensors
        elif name == 'ALSensors':
            if self.__SensorsProxy == None:
                try:
                    self.__SensorsProxy = ALProxy("ALSensors", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__SensorsProxy
        # ALSonar
        elif name == 'ALSonar':
            if self.__SonarProxy == None:
                try:
                    self.__SonarProxy = ALProxy("ALSonar", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__SonarProxy
        # ALTextToSpeech
        elif name == 'ALTextToSpeech':
            if self.__TextToSpeechProxy == None:
                try:
                    self.__TextToSpeechProxy = ALProxy("ALTextToSpeech", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__TextToSpeechProxy
        # ALVideoDevice
        elif name == 'ALVideoDevice':
            if self.__VideoDeviceProxy == None:
                try:
                    self.__VideoDeviceProxy = ALProxy("ALVideoDevice", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__VideoDeviceProxy
        # ALDCM
        elif name == 'ALDCM':
            if self.__DCMProxy == None:
                try:
                    self.__DCMProxy = ALProxy("ALDCM", self.__ip, self.__port)
                except RuntimeError,e:
                    print str(e)
            return self.__DCMProxy
    
    ip          = property(setIP  , getIP  , None, None)
    port        = property(setPort, getPort, None, None)
    
    
        