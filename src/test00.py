'''
                    CYBERNETIQUE APPLIQUEE
                PROJET DE SEMESTRE PRINTEMPS 2011
                    PARCOURS VITA POUR NAO

@author      : Arnaud BEGUIN
@description : Procedure de test des exercices
'''
from tools import Connexion, Stiffness, Init_Pose
from exercices import Ex1, Ex2, Ex3, Ex4, Ex5

def main():
    
    nomRobot = "astro"
    
    print '##############################################################'
    print '                    CYBERNETIQUE APPLIQUEE                    '
    print '                PROJET DE SEMESTRE PRINTEMPS 2011             '
    print '                    PARCOURS VITA POUR NAO                    '
    print '##############################################################'
    print ''
    print ''
    
    
    # objet de connexion au nao
    print 'connexion au robot ' + str(nomRobot) + '...'
    print '' 
    c         = Connexion.Connexion(nomRobot) # parametres possibles : None (localhost), astro, robby
    # connexion au nao
    proxy     = c.connect()
    
    # objet permettant d'asservir / desasservir les moteurs du robot
    asservir = Stiffness.Stiffness(proxy)
    asservir.asservir()
    
    # initialisation de la position du robot
#    init = Init_Pose.Init_Pose(proxy)
#    init.do()
    
    exercices = []                           # liste qui contiendra les exercices a tester
    
    # ajout des exercices a la liste
#    exercices.append(Ex1.Ex1(proxy))
#    exercices.append(Ex2.Ex2(proxy))
#    exercices.append(Ex3.Ex3(proxy))
#    exercices.append(Ex4.Ex4(proxy))
    exercices.append(Ex5.Ex5(proxy))

    print 'test des exercices...'
    print ''
    if len(exercices) > 1:
        for i in range(len(exercices)):
            print 'exercice ' + str(i+1) + '...'
            exercices[i].do(1)
    elif len(exercices) > 0:
        exercices[0].do(2)
    else:
        print "aucun exercice n'est defini!"
    

if __name__ == '__main__':
    main()