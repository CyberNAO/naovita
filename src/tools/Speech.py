'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Alex Bulla
@description : Classe contenant les methodes de deplacements
               jusqu'aux exercices
'''


class Speech(object):
    '''
    classdocs
    '''

    def __init__(self, connection):
        '''
        Constructor
        '''
        #self.__distanceAcceptable = 50
        self.__tts = connection.getProxy('ALTextToSpeech')
        self.__tts.setVolume(0.8)
        
    def say(self, text):
        self.__tts.post.say(text)

    #Volume (between 0.0 and 1.0).
    def setVolume(self, volume):
        self.__tts.setVolume(volume)