'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Classe contenant les methodes d'imagerie
'''

from vision_definitions import*
#from PIL import Image
import Image

class Imagerie(object):
    '''
    classdocs
    '''


    def __init__(self, connection):
        '''
        Constructor
        '''
        self.__camProxy = connection.getProxy('ALVideoDevice')
        
    '''
    example
    '''
    def getImage(self):
        
        ####
        # Register a Generic Video Module
    
        resolution = kQQVGA
        colorSpace = kRGBColorSpace
        fps = 30
        nameId = self.__camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
        print nameId
        
        #resolution = kQQVGA
        #camProxy.setResolution(nameId, resolution)
        
        self.__camProxy.setParam(kCameraSelectID, 0)
        
        print 'getting image in remote'
        
        # getImageRemote(nameId) retourne un tableau
        # results[0] : width 
        # results[1] : height
        # results[2] : number of layers
        # results[3] : ColorSpace
        # results[4] : time stamp (highest 32 bits) 
        # results[5] : time stamp (lowest 32 bits)
        # results[6] : array of size height*width*nblayers containing image data
        results = self.__camProxy.getImageRemote(nameId)
            
        self.__camProxy.unsubscribe(nameId)
        
        print 'taille : ' + str(results[0]) + 'x' + str(results[1])
        print 'nombre de couche : ' + str(results[2])
        print 'espace des couleurs : ' + str(results[3])
        
        taille = []
        taille.append(results[0])
        taille.append(results[1])
        
        imgData = results[6]
        
        im = Image.fromstring("RGB", taille, imgData)
        #im.show()
        print 'end of gvm_getImageLocal python script'
        return im
    
        