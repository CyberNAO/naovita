'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Canevas de l'algorithme globale du projet
'''

from tools import Connexion, Stiffness, Deplacements, Imagerie, SquareFinder
from exercices import Ex1, Ex2, Ex3, Ex4, Ex5




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
    exercice.do(3)
        
    
'''
Condition d'arret de l'algorithme : tous les exercices ont ete fait
'''
def parcoursTermine(exercices):
    termine = True
    for ex in exercices:
        if not ex:
            termine = False
    return termine

   

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
    #deplacements.poseInit()
    deplacements.standUp()
    #deplacements.turn()
    #deplacements.bendHead()
    #deplacements.raiseHead()
    
    
    sf = SquareFinder.SquareFinder(c)
    sf.orient()
    
    deplacements.kneel()
    stiffness.desasservir()
    
    # Temps que tous les exercices n'ont pas ete fait
    #while not parcoursTermine(exercices):
        
        #print 'En developpement...'
        
        ##############################################################
        #                        DEPLACEMENTS                        #
        ##############################################################
        # Recherche d'un panneau d'un exercice pas encore effectue 
        #panneau = analyseImage.detectePanneau()
        # ...
        # Tant que le nao n'est pas devant le panneau trouve
    #deplacements.poseInit()
    #deplacements.step()
    #asservir.desasservir()
            # ...
            # Estimer la distance et la direction
            # ...
            # Se deplacer
            # ...
            # Verifier que le deplacement est bon
        
        ##############################################################
        #                 RECONNAISSANCE D'IMAGES                    #
        ##############################################################
        # Une fois bien positionner, reconnaitre l'exercice a faire
        #ex           = analyseImage.detecteExercice()
        # ...
        
        
        ##############################################################
        #                          EXERCICES                         #
        ##############################################################
        # Faire l'exercice
        #doExercice(ex, proxy)
        # ...
        # Marquer l'exercice comme fait
        #exercices[ex] = True
        # ...
            

if __name__ == '__main__':
    main()