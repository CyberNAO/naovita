'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Canevas de l'algorithme globale du projet
'''

from tools import Connexion, Stiffness, Deplacements, Imagerie, SquareFinder,\
    MarkDetect, Init_Pose
from exercices import Ex1, Ex2, Ex3, Ex4, Ex5
import time



'''
Connexion au robot Nao
'''
def connexion():
    nomRobot = "astro"
    #nomRobot = "robby"

    # objet de connexion au nao
    print 'connexion au robot ' + str(nomRobot) + '...'
    print '' 
    c         = Connexion.Connexion(nomRobot) # parametres possibles : None (localhost), astro, robby
    # connexion au nao
    #c.connect()
    return c

def doExercice(ex, proxy):
    
    # creation de l'objet correspondant a l'exercice a faire
    exercice = {
      1 : Ex1.Ex1(proxy),
      2 : Ex2.Ex2(proxy),
      3 : Ex3.Ex3(proxy),
      4 : Ex4.Ex4(proxy),
      5 : Ex5.Ex5(proxy)
    }[ex]()
    
    # lancement de l'exercice
    exercice.do(1)
        
    
'''
Condition d'arret de l'algorithme : tous les exercices ont ete fait
'''
def parcoursTermine(exercices):
    termine = True
    for ex in exercices:
        if not ex:
            termine = False
    return termine


def joinTheTotem(img, sf, deplacements):
    
    #loop until the totem
    turnCount = 0
    while turnCount < 5 :
        #get blue cube
        img.switchCam("low")
        deplacements.bendHead()
        dir = sf.orient('blue')
        deplacements.raiseHead()
        img.switchCam("high")
        
        
        if dir['blue'] != None :
            print "!!!!!!Found the blue cube!"
            turnCount = 0
            break
            
        else :
            dir = sf.orient('red')
            if dir['red'] != None :
                turnCount = 0
                #go to the red totem
                print "Go to the red totem"
                if dir['red'] != 0:
                    print "Turn " + str(dir['red'])
                    deplacements.turn(dir['red'] * 0.1963) #pi/16
            
                else :
                    #go straight
                    print "Go straight"
                    deplacements.walk(3.0) #adapt dist
            else :
                print("I am lost !")
                deplacements.turn(-0.7853) #pi/4
                turnCount += 1
                
    #end loop
    #####
    if turnCount > 4 :
        print("I am REEALLY lost !")
    
    
    ################3old school

            #distRapport = 4 - (area-200)/100.0 * 0.35 
            #if (distRapport < 0.5) distRapport = 0.5
            #elif (distRapport > 6) distRapport = 6
            
        ############################

def doExercice(ex, proxy, nbFois):
    
    # creation de l'objet correspondant a l'exercice a faire
    if ex == 2:
        exercice = Ex2.Ex2(proxy)
    elif ex == 3:
        exercice = Ex3.Ex3(proxy)
        nbFois = nbFois - 1
    elif ex == 4:
        exercice = Ex4.Ex4(proxy)
    elif ex == 5:
        exercice = Ex5.Ex5(proxy)
    elif ex == 6:
        exercice = Ex6.Ex6(proxy)
    else:
        exercice = Ex1.Ex1(proxy)
    
    # lancement de l'exercice
    exercice.do(nbFois)
    

def main():
    
    exercices = [False, False, False, False, False]
    
    print '##############################################################'
    print '                    CYBERNETIQUE APPLIQUEE                    '
    print '                PROJET DE SEMESTRE PRINTEMPS 2011             '
    print '                    PARCOURS VITA POUR NAO                    '
    print '##############################################################'
    print ''
    print ''
    
    # connexion au robot Nao
    c = connexion()
    
    # objet permettant d'asservir / desasservir les moteurs du robot
    stiffness = Stiffness.Stiffness(c.getProxy("ALMotion"))
    stiffness.asservir()
    
    # objet pour l'analyse d'image
    #img = Imagerie.Imagerie()
    #img.getImage(c.getProxy("ALVideoDevice"))
    
    # objet controlant les deplacements du Nao d'un exercice a l'autre
    deplacements = Deplacements.Deplacements(c)        
    img = Imagerie.Imagerie(c)
    sf = SquareFinder.SquareFinder(c)
    
    deplacements.poseInit()
    #deplacements.standUp()
    #deplacements.turn()
    #deplacements.bendHead()
    #deplacements.raiseHead()
    
    
    joinTheTotem(img, sf, deplacements)
    #il detecte une marque 
    
    deplacements.poseInit()
    deplacements.turn(3.14)
    
    
    # objet permettant d'initialiser la position du robo
    ALMotionProxy = c.getProxy("ALMotion")
    init = Init_Pose.Init_Pose(ALMotionProxy)
    
    ###################################
    #: faire un exo
    init.do()
    doExercice(1, ALMotionProxy, 1)
    time.sleep(0.5)
    
    #walk to 1
    deplacements.poseInit()   
    deplacements.walkToCenter()
    deplacements.poseInit()
    
    joinTheTotem(img, sf, deplacements)
    #il detecte une marque 
    
    deplacements.poseInit()
    deplacements.turn(3.14)
    
    
    ###################################
    #: faire un exo
    init.do()
    doExercice(2, ALMotionProxy, 1)
    time.sleep(0.5)
    
    #walk to 2
    deplacements.poseInit()
    deplacements.walkToCenter()
    deplacements.poseInit()
    
    
    ########### Vertig
    deplacements.kneel()
    stiffness.desasservir()
    
        
if __name__ == '__main__':
    main()
    
    
    