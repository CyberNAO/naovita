'''
Created on 7 juin 2011

@author: baggins
'''

from tools import Connexion, Stiffness, Deplacements, Init_Pose
from exercices import Ex1, Ex2, Ex3, Ex4, Ex5, Ex6
import time
import motion

'''
Connexion au robot Nao
'''
def connexion():
    nomRobot = "robby"
    
    # objet de connexion au nao
    print 'connexion au robot ' + str(nomRobot) + '...'
    print '' 
    c         = Connexion.Connexion(nomRobot) # parametres possibles : None (localhost), astro, robby
    # connexion au nao
    return c

def step(motionProxy, X, Y, Theta, Frequency):
    #####################
    ## Enable arms control by Walk algorithm
    #####################
    motionProxy.setWalkArmsEnable(True, True)
    
    #####################
    ## FOOT CONTACT PROTECTION
    #####################
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])
    
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    
    time.sleep(5.0)
        
    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    motionProxy.setWalkTargetVelocity( 0, 0, 0, Frequency)

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
    
def doEnchainement(init, deplacements, ALMotionProxy, crtEx):
    #######################################################
    # Se deplace vers un panneau
    print "Se deplace vers un panneau..."
    deplacements.poseInit()
    X         = 1.0
    Y         = 0.0
    Theta     = 0.0
    Frequency = 1.0
    step(ALMotionProxy, X, Y, Theta, Frequency)
    deplacements.poseInit()
    #######################################################
    # Fais l'exercice deux fois
    print "Fais l'exercice..."
    init.do()
    doExercice(crtEx, ALMotionProxy, 2)
    time.sleep(0.5)
    #######################################################
    # Pivote de 180 degres
    print "Pivote..."
    deplacements.poseInit()
    X     = 0.0
    Y     = 0.1
    Theta = 1.0
    step(ALMotionProxy, X, Y, Theta, Frequency)
    #######################################################
    # Retourne vers le point de depart
    print "Se deplace vers le point de depart..."
    deplacements.poseInit()
    time.sleep(1.0)
    X         = 1.0
    Y         = 0.0
    Theta     = 0.0
    step(ALMotionProxy, X, Y, Theta, Frequency)
    #######################################################
    # S'oriente vers le prochain panneau
    print "Pivote..."
    deplacements.poseInit()
    time.sleep(1.0)
    X     = 0.0
    Y     = 0.1
    Theta = -0.75
    step(ALMotionProxy, X, Y, Theta, Frequency)
    

def main():
    exercices = [1, 2, 4, 5, 6]
    print '##############################################################'
    print '                    CYBERNETIQUE APPLIQUEE                    '
    print '                PROJET DE SEMESTRE PRINTEMPS 2011             '
    print '                    PARCOURS VITA POUR NAO                    '
    print '            -----------------------------------------         '
    print ' Parcours predefini pour tester l\'enchainement des exercices '
    print '##############################################################'
    print ''
    print ''
    
    # connexion au robot Nao
    c             = connexion()
    ALMotionProxy = c.getProxy('ALMotion')
    
    # objet permettant d'asservir / desasservir les moteurs du robot
    asservir = Stiffness.Stiffness(ALMotionProxy)
    asservir.asservir()
    
    # objet permettant d'initialiser la position du robo
    init = Init_Pose.Init_Pose(ALMotionProxy)
    
    # objet controlant les deplacements du Nao d'un exercice a l'autre
    deplacements = Deplacements.Deplacements(c)
    
    #######################################################
    # Suite d'enchainements du parcours predefini
    for crtEx in exercices:
        doEnchainement(init, deplacements, ALMotionProxy, crtEx)
    
    ALFrameProxy = c.getProxy("ALFrameManager")
##    
##    #behaviorID = ALFrameProxy.newBehaviorFromFile("/home/nao/behaviors/standup.xar", "")
##    
    behaviorID = ALFrameProxy.newBehaviorFromFile("/home/nao/behaviors/behavior.xar", "")
    ALFrameProxy.completeBehavior(behaviorID)
    #######################################################
    # FIN
    asservir.desasservir()

if __name__ == '__main__':
    main()