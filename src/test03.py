'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Canevas de l'algorithme globale du projet
'''

from tools import Connexion, Stiffness, Deplacements, Imagerie, SquareFinder,\
    MarkDetect, Init_Pose, Speech
from exercices import Ex1, Ex2, Ex3, Ex4, Ex5, Ex6
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
    
#returns nb blue cubes
def joinTheTotem(img, sf, deplacements, speech):
    
    #loop until the totem
    turnCount = 0
    while turnCount < 5 :
        #get blue cube
        img.switchCam("low")
        deplacements.bendHead()
        dir = sf.recon('blue')
        deplacements.raiseHead()
        img.switchCam("high")
        
        
        if dir['blue'][0] != None :
            print "###### Found the blue cube! ######"
            nbCubes = dir['blue'][1]
            print "###### " + str(nbCubes) + " cube(s) ######"
            if nbCubes == 1: cubeWord = "one treasure"
            else:           cubeWord = "many treasures"
            speech.say("Oh Ho! I found " + cubeWord)
            turnCount = 0
            return nbCubes
            
        else :
            dir = sf.recon('red')
            if dir['red'][0] != None :
                turnCount = 0
                #go to the red totem
                print "Go to the red totem"
                if dir['red'][0] != 0:
                    print "Turn " + str(dir['red'][0])
                    deplacements.turn(dir['red'][0] * 0.1963) #pi/16
            
                else :
                    #go straight
                    print "Go straight"
                    speech.say("I see the red to taim.")
                    range = dir['red'][2]
                    deplacements.walk(range)   #3.0) #adapt dist
            else :
                print("I am lost !")
                speech.say("I am lo-ost !")
                deplacements.turn(-0.7853) #pi/4
                turnCount += 1
                
    #end loop
    #####
    if turnCount >= 5 :
        print("Help, I am REEALLY lost !")
        speech.say("Help, I am REEALLY lost !")
        return None
    ################3old school

            #distRapport = 4 - (area-200)/100.0 * 0.35 
            #if (distRapport < 0.5) distRapport = 0.5
            #elif (distRapport > 6) distRapport = 6
            
        ############################

def doDance(id, c):
    frameProxy = c.getProxy("ALFrameManager")
    if id == 1 :
        behaviorID = frameProxy.newBehaviorFromFile("/home/nao/behaviors/dance/behavior.xar", "")
    elif id == 2 :
        behaviorID = frameProxy.newBehaviorFromFile("/home/nao/behaviors/dance/behavior.xar", "")
    else :
        behaviorID = frameProxy.newBehaviorFromFile("/home/nao/behaviors/dance/behavior.xar", "")
    
    print "Danse"
    frameProxy.completeBehavior(behaviorID)
    


def doExercice(ex, c, nbFois):
    
    proxy = c.getProxy("ALMotion")
    
    # creation de l'objet correspondant a l'exercice a faire
    if ex == 2:
        exercice = Ex2.Ex2(proxy)
    elif ex == 3:
        frameProxy = c.getProxy("ALFrameManager")
        behaviorID = frameProxy.newBehaviorFromFile("/home/nao/behaviors/dance/behavior.xar", "")
        print "Danse"
        frameProxy.completeBehavior(behaviorID)
    elif ex == 4:
        exercice = Ex4.Ex4(proxy)
    elif ex == 5:
        exercice = Ex5.Ex5(proxy)
    elif ex == 6:
        exercice = Ex6.Ex6(proxy)
    elif ex == 1:
        exercice = Ex1.Ex1(proxy)
    
    # lancement de l'exercice
    if ex != 3 :
        exercice.do(nbFois)
    

def main():
    
    #exercices = [False, False, False, False, False]
    
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
    stiffness = Stiffness.Stiffness(c)
    stiffness.asservir()
    # objet controlant les deplacements du Nao d'un exercice a l'autre
    deplacements = Deplacements.Deplacements(c)
    # objet permettant d'initialiser la position du robo
    init = Init_Pose.Init_Pose(c.getProxy("ALMotion"))
    # objets pour l'analyse d'image
    img = Imagerie.Imagerie(c)
    sf = SquareFinder.SquareFinder(c)
    # objets pour la gestion de la parole
    speech = Speech.Speech(c)
    
    
    #deplacements.standUp()
    ############          Do exercises            #############    
    for i in range(1, 3) :
        if i == 1 :
            speech.say("Rock'n'roll!")
        else :
            #walk to the center again 
            deplacements.poseInit()   
            deplacements.walkToCenter()
        
        # walk to the next totem
        deplacements.poseInit()
        exoId = joinTheTotem(img, sf, deplacements, speech)
        if exoId == None :
            init.do()
            break
        
        #TODO : NAO mark detection
        
        deplacements.poseInit()
        deplacements.turn(3.14)
        
        # do the exercise
        init.do()
        doExercice(exoId, c, 2)
        #doDanse(exoId, c)
        time.sleep(4)
    
    
    ########### Vertig
    if exoId == None :
        speech.say("Being a scavenger is really exhausting!")
    else :
        speech.say("Pa Pa nA da taaa")
    
    deplacements.kneel()
    stiffness.desasservir()
    
        
if __name__ == '__main__':
    main()
    
    
    