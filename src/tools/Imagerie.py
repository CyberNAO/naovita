'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Classe contenant les methodes d'imagerie
'''

from vision_definitions import*
import Image

class Imagerie(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    '''
    example
    '''
    def getImage(self, camProxy):
        
        ####
        # Register a Generic Video Module
        
        resolution = kQVGA
        colorSpace = kRGBColorSpace
        fps = 30
        
        nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
        print nameId
        
        resolution = kQQVGA
        camProxy.setResolution(nameId, resolution)
        
        print 'getting image in remote'
        
        # getImageRemote(nameId) retourne un tableau
        # results[0] : width 
        # results[1] : height
        # results[2] : number of layers
        # results[3] : ColorSpace
        # results[4] : time stamp (highest 32 bits) 
        # results[5] : time stamp (lowest 32 bits)
        # results[6] : array of size height*width*nblayers containing image data
        results = camProxy.getImageRemote(nameId)
            
        camProxy.unsubscribe(nameId)
        
        print 'taille : ' + str(results[0]) + 'x' + str(results[1])
        print 'nombre de couche : ' + str(results[2])
        print 'espace des couleurs : ' + str(results[3])
        
        taille = []
        taille.append(results[0])
        taille.append(results[1])
        
        imgData = results[6]
        
        im = Image.fromstring("RGB", taille, imgData)
        im.show()
        
        print 'end of gvm_getImageLocal python script'
        
    ''' 
    TO DO
    ''' 
    def detectePanneau(self):
        print 'detection d\'un panneau...'
        return 0 
        
    ''' 
    TO DO
    '''
    def detecteExercice(self):
        print 'detection de l\'exercice...'
        return 0
        