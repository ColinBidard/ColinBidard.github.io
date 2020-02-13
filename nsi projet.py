from random import*
import sys
color = sys.stdout.shell

##################################################################################
    ##################################################################################
vie=15
chance= 0

d={'slot1' : 0, 'slot2' : 0, 'slot3' : 0}
Hasard=['Pomme','Epée', 'bouclier', 'crotte']
inventaire = 0
k=0
def inventair():
    global inventaire
    global Hasard
    if inventaire==1:
        d['slot1']=Hasard[0]
    elif inventaire==2:
        d['slot2']=Hasard[0]
    elif inventaire==3:
        d['slot3']=Hasard[0]
    elif inventaire>=4:
        print("votre inventaire est plein")
        
    
def prendre():
    global inventaire
    shuffle(Hasard)
    print("l'ennemie à laissé tomber un objet souhaiter vous prendre", Hasard[0],)
    choix=input()
    if choix=='oui':
        inventaire= inventaire + 1
        inventair()
        print(d)
    if choix == 'non':
        print("Vous ne la ramassez pas")
def pause(): # fonction de pause
    color.write("\nAppuyer sur Entrée pour continuer\n", "KEYWORD")
    input()

def gameover():# Mort du personnage
    print(" ")   
    color.write("\nVous êtes mort dommage n'hesite pas à réssayer\n" ,"COMMENT")
    print("pour réssayer appuyez sur espace")
    pause()

from random import*
import sys
color = sys.stdout.shell

vie= 15
ration=0
faim=0


def d20(): # dé de 20 aléatoire
    return randint(1,20)

def d6(): # dé de 6 aléatoire
    return randint(1,6)

def d4(): # dé de 4 aléatoire
    return randint(1,4)
             
def faim():
    global faim # gestion de la faim
    if faim==2:
        vie= vie - 3
        print("Vous avez très faim vous perdez 3 vie")
        print("Vous avez", vie,"vie")
        
def enigme():# énigme de l'homme masqué
    for i in range(3):
        choix=input()
        global chance
        if choix=='prenom':
            break 
        else:
            print("non recommence")
            chance -=1
    if chance== -3:
        print(" ")
        print("perdu tu vas mourir")
        gameover()
    else:
        print(" ")
        print("bravo tu a reussi, je vais te libérer, te  donner de la nourriture et aussi un conseil ")
        
def bandit():# atribut du Bandit
    global vieb
    color.write("\nc'est a ton tour !\n", "STRING")
    print("lance un d20 pour voir si tu le touche")
    toucher=input()

    if toucher=='d20':
            bandit2()
    else:
        print("Tu dois écrire d20")
        return bandit()
       
def bandit2():# dégat envers le Bandit
    res = d20()+3
    print("Résultat du lancé :", res)
    if res==20:
        print("Houa tu vien de faire un coup critique")
        bandit4()
    elif res>=12:
        bandit3()
    else:
      print("dommage il a esquivé réessaye")
      print("                          ")
      return banditattaque()

def bandit3():# dégats normaux
    global vieb
    print("lance un d6 pour voir les dégats que le monstre prend")
    touche=input()

    if touche=='d6':
        res1=d6()
        if vieb<=res1:
            print("Il prend:", res1,"dégats et il meurt")
            banditdead()
        else:
            print("Le Brigant prend:", res1,"dégats, mais il n'est pas mort")
            print("                                                     ")
            vieb = vieb - res1
            return banditattaque()
    
    else:
        print("Tu dois ecrire d6")
        return bandit3()

def bandit4():# coup critique
    print("lance un d6 pour voir les dégats que le Brigant prend")
    touchee=input()
      
    if touchee=='d6':
      global vieb
      rescrit=d6()*2

      if vieb<=rescrit:
            print("Il prend:", rescrit,"dégats et il meurt")
            banditdead()
      else:
            print("Le Brigant prend:", rescrit,"dégats, mais il n'est pas mort")
            vieb = vieb - rescrit
            return banditattaque()
    else:
        print("Tu dois ecrire d6")
        return bandit4(vieb)

def banditdead():# mort du bandit
    color.write("\nLe bandit est mort\n", "STRING")
    print("il vous reste", vie,"vie")

def banditattaque():# mauvais il faut changer
    global vie
    color.write("\nC'est au tour de ton enemie\n", "COMMENT")
    resm= d20()
    print("Résultat du lancé :",resm)
    if resm>=14:
        print("Vous êtes touché")
        deg= d4()
        print("vous perdez",deg," vie")
        vie = vie - deg

        if vie<=deg:
            print("vous prennez:", deg,"dégats et vous mourrez")
            print(" ")
            gameover()
        else:
            print(" il vous reste",vie," vie")
            print("                       ")
            return bandit()
    else:
        print("bien joué vous avez esquivé")
        print("                        ")
        return bandit()# bloquer car vieb is not defined

def gobelin():# atribut du gobelin
    global vieg
    color.write("\nc'est a ton tour !\n", "STRING")
    print("lance un d20 pour voir si tu le touche")
    toucher=input()

    if toucher=='d20':
            gobelin2()
    else:
        print("Tu dois écrire d20")
        return gobelin()

def gobelin2():# dégat envers le Gobelin
    res = d20()+3
    print("Résultat du lancé :", res)
    if res>=10:
        gobelin3()
    elif res==20:
        print("Houa tu vien de faire un coup critique")
        gobelin4()
    else:
        print("dommage il a esquivé réessaye")
        print("                             ")
        return gobelinattaque()

def gobelin3():# dégats normaux
    print("lance un d6 pour voir les dégats que le monstre prend")
    touche=input()
    global vieg

    if touche=='d6':
        res1=d6()
        if vieg<=res1:
            print("Il prend:", res1,"dégats et il meurt")
            return gobelindead()
        else:
            print("Le Gobelin prend:", res1,"dégats, mais il n'est pas mort")
            vieg = vieg - res1
            return gobelinattaque()
    else:
        print("Tu dois ecrire d6")
        return gobelin3()

def gobelin4():# coup critique
    print("lance un d6 pour voir les dégats que le monstre prend")
    touchee=input()
    global vieg

    if touchee=='d6':
        rescrit=d6()*2
        if vieg<=rescrit:
            print("Il prend:", rescrit,"dégats et il meurt")
            gobelindead()
        else:
            print("Le Gobelin prend:", rescrit,"dégats, mais il n'est pas mort")
            vieg = vieg - rescrit
            return gobelinattaque()
    else:
        print("Tu dois ecrire d6")
        return gobelin3()
    
def gobelindead():# mort du Gobelin
    color.write("\nLe gobelin est mort\n", "STRING")
    print("il vous reste", vie,"vie")

def gobelinattaque():# mauvais il faut changer
    global vie
    color.write("\nC'est au tour de ton enemie\n", "COMMENT")
    resm= d20()
    print("Résultat du lancé :",resm)
    if resm>=14:
        print("Vous êtes touché")
        deg= d4()
        print("vous perdez",deg," vie")
        vie = vie - deg

        if vie<=deg:
            print("vous prennez:", deg,"dégats et vous mourrez")
            print(" ")
            gameover()
        else:
            print(" il vous reste",vie," vie")
            print("                       ")
            return gobelin()
    else:
        print("bien joué vous avez esquivé")
        print("                        ")
        return gobelin()

def choix2():
    print("Vous pouvez (accepter) ou (refuser)")
    choix1=input()
    if choix1=='accepter':
        print("« Merci Heros, cet lettre doit etre livrée a mon fils il est forgeron et s'appelle James.")
        pause()
    else:
        color.write("\nJe t'es dis d'accepter tu ne veux pas avoir t'a premiere quête ou quoi\n", "STRING")
        return choix2()
    
#########################################################################################
    ########################################################################################


while vie>=0:
    print("Bienvenue, aventurier ou aventurière dans le doux monde d’Esperya.")
    print("Avant de te lancer dans ce monde, je dois t’expliquer quelque règles:")
    color.write("\n-Tout d'abord je me nomme Yo je suis le maître de ce monde, tu pourra avoir affaire moi de temps à autre, je t'indiquerai le chemin à prendre si tu semble perdu\n", "STRING")
    print("-Dans ce monde tu devra prendre des décisions qui changeront ton destin, alors choisi bien.")
    print("-Tu rencontrera des monstres ou des personnes qui te voudront du mal, tu devra donc tuer ou être tuer.")
    print("-Tu utilisera souvent des dés: soit de 20 (d20), ou de 6 (d6).")
    print("Voila tous est claire maintenant, je te souhaite de ne pas mourir en chemin, bonne chance aventurier.")
    pause()
    
    print("Yo- Bonjour Héros, comment te nomme tu ?")
    noms=input()
    a="bien le bonjour mon cher "+noms+ " !"
    b="Ha tu te nommes "+noms+" c'est moche, mais ca ira"
    rep=[a,b]
    print(choice(rep))
    print("",noms,", tu vas maintenant arrivé dans le monde d'Esperya, prepare toi.")
    pause()
    
    print("                                                                        ")
    print("Le Soleil était deja haut dans le ciel lorque que vous vous reveilliez, vous sentiez la chaleur du Soleil sur votre peau.")
    print(" ")
    print("Apres avoir reprit vos espris vous remarquez que vous êtes dans le lit d'une maison en pierre, soudainement la porte de la chaumière s'ouvrit.")
    print(" ")
    print("Une femme agée vous regarda et vous lança « Ha étranger vous vous reveillez enfin, vous dormez depuis deux jour. je vous est trouvée sur le bord d'une route il y a 2 jour. »")
    print(" ")
    print("« Vous devez surement avoir des questions mais pour l'instant vous devez vous enfuir, des brigants me poursuive. »")
    print("                                                                                                                  ")
    pause()
    
    color.write("\nYo- Voila tu dois maintenant faire ton premier choix: soit (aider) soir s'(enfuir) choisi bien\n", "STRING")
    choix=input()
    if choix=='aider':
        print("                                                                                      ")
        print("Vous dites a la femme que vous allez l'aider, elle vous remerci et vas se cacher.")
        print(" ")
        print("Vous prener votre épée et sortez.")
        print("Dehors le Soleil vous éblouissa dabord mais vous vous habituiez vite.")
        print(" ")
        print(" vous remarquer que des silhouettes se tiennent à quelque metres devant vous, vous reconnaisez 3 bandits.")
        print("L'un d'eux vous attaque !")
        print("                                             ")
        vieb=6
        bandit() #Probleme
        pause()
        prendre()
        pause()
        print(" Vous vous relevez apres cette dur epreuve, la femme vous rejoint en courant et vous remercie pour l'avoir sauvée.")
        print(" ")
        print("« Merci, vous êtes mon Héros, si vous avez réussi a battre ces bandit pouvez vous allez remettre une lettre au village de Bri. »")
        print(" ")
        print("« Vous devrez passer par la forêt des mensonges, ne faites confiance a personne dans cette forêt. »")
        print(" ")
        color.write("Yo- Wow regarde t'a premiere quête accepte la\n", "STRING")
        
        choix2()
        print("« Je vais tous dabord vous soigner »")
        print(" ")
        vie = 15
        print("Vous avez", vie,"vie")
        print(" ")
        print("« Puisque vous m'avez aidée je vais vous donner un conseil, lorsque vous serez dans la forêt prennez tous de suite à gauche au premier croisement. »")
        print(" ")
        print("« Je vous donne aussi 2 rations pour la route. »")
        ration = ration + 2
        print(" ")
        print("Apres un aurevoir vous vous dirigez vers la forêt")
        pause()
        print("Après quelques minutes de marche vous arrivez devant la Forêt des Mensonges, elle est d'une noirceur effrayante.")
        print(" ")
        print("Vous prenez votre souffle, regardez en arrière et pénétrez dans la forêt.")
        pause()
        print("dans la forêt il fait très sombre, vous n'entendez presque aucun bruit seulement le bruit du vent sur les branches.")
        print(" ")
        print("Quelque dizaines de mètres plus loin vous arrivez à un croisement.")
        print(" ")
        color.write("\nVous pouvez aller soit à (gauche) soit à (droite)\n", "STRING")
        choix=input()
        if choix=='gauche':
            print("Vous décidez de prendre à gauche.")
            pause()
            print("Au fur et à mesure que vous marcher vous sentez que l’on vous observe, vous décidez donc de presser le pas.")
            print(" ")
            print("comme vous marcher trop vite vous ne remarquez pas la racine sur le bord du chemin.")
            print(" ")
            color.write("\ntentez votre chance, lancé un d20 si vous faites entre 10 et 20 vous êtes chanceux sinon vous êtes malchanceux.\n", "KEYWORD")
            choix=input()
            if choix=='d20':
                reschan=d20()
                print("Vous avez fait", reschan,"")
                if reschan>=10:
                    print(" vous réussissez à vous rattraper à temps, vous avez esquiver un buisson de ronce.")
                else:
                    print("vous tombez dans un buisson de ronce vous perdez 2 vie")
                    vie= vie - 2
            pause()
            print("Vous entendez maintenant clairement une personne, qui court dans la forêt.")
            print(" ")
            print("Vous sortez votre arme et attendez qu'il se montre, quelque seconde plus tard quelque chose sort des brousailles.")
            print("")
            print("Devant vous se dresse un petit homme vert avec une dague dans sa main, il s'agit d'un gobelin.")
            print(" ")
            print("Il vous fonce dessus, il attaque !")
            pause()
            vieg=6
            gobelin()
            pause()
            prendre()
            pause()
            print("Vous reprenez votre souffle, c'est la premiere fois que vous rencontrez une créature comme celle la.")
            print(" ")
            print("Vous imaginez tous les danger que vous pourriez rencontrer dans cette forêt mais vous n'avez pas peur au contraire vous etes exité.")
            print(" ")
            print("Vous reprenez la route.")
            pause()
            print("Apres quelques minutes de marche vous revoyez le cadavre du gobelin")
            print(" ")
            print("Apres plusieur passage devant le gobelin vous comprenez que vous tournez en rond")
            print(" ")
            print("Vous remarquez aussi qu'il fait presque nuit")
            pause()
            print("que décidez vous (camper) ou (continuer) de marcher")
            choix=input()
            if choix=='camper':
                print("Vous décidez de vous installer pour la nuit.")
                print(" ")
                print("Une fois le campement installé vous allumez un feu")
                print(" ")
                print("si vous avez une ration vous pouvez en manger")
                print(" ")
                print("Souhaitez vous manger une ration (oui) ou (non)")
                choix=input()
                if choix=='oui':
                    if ration>=1:
                        ration = - 1
                        print("Vous mangez une ration vous regagnez 3 vie")
                        vie = vie + 3
                        print("Vous avez", vie,"vie")
                    else:
                        print("Vous ne pouvez pas manger de ration vous n'en avez plus")
                        faim =  + 1
                elif choix=='non':
                    print("vous décidez de ne pas manger, attention a bien manger tous les deux jours")
                    faim = + 1
                pause()
                print("Soudainement, une vague d'énergie vous assomme sans que vous puissiez l'esquiver")
                print(" ")
                print("Vous tombez dans un cauchemar qui semble semble sans fin ou vous voyez sans arrêt votre prénom")
                pause()
                print("lorsque vous vous reveillez, vous remarquez que vous êtes dans une hutte en peau.")
                print(" ")
                print("Un homme est assis juste devant l'entrée, il porte un masque qui vous met mal a l'aise")
                print(" ")
                print("Il vous regarde et vous lance.")
                print(" ")
                print("Bonjour voyageur, j'espere que vous ne souffrez pas trop")
                print(" ")
                print("Je me nomme Zed et ici c'est chez moi, normalement les gens savent qu'il ne faut pas aller a gauche au chemin.")
                print(" ")
                print("Mais vous y etes allé.")
                print(" ")
                print("je vous propose donc un jeu si vous gagnez, je vous laisse filer sinon je vous tue.")
                print(" ")
                print("Cool vous avez l'air d'accord.")
                pause()
                print("Je vais donc vous proposer une énigme.")
                print(" ")
                print("Qu’est-ce qui t’appartient mais que les gens utilisent beaucoup plus que toi ?")
                print(" ")
                print("je te laisse trois chance")
                print(" ")
                enigme()
                pause()
                print("Mon conseil et de ne pas prendre le chemin qui te semble être le plus facile.")
                print(" ")
                print("Voila également 2 ration.")
                print(" ")
                print("Et je vais également soigner vos blessure.")
                vie = 15
                print("Il vous reste",vie,"vie")
                print(" ")
                print("Maintenant tu dois partir")
                print(" ")
                print("Vous sortez de la hutte et remarquez que vous étiez dans une prairie entouré de piege a loup.")
                print(" ")
                print("Vous suivez le chemin qui méne vers la forêt.")
                print(" ")
                print("apres quelque minute de marche vous retrouvez le gobelin que vous aviez tué.")
                print(" ")
                print("Vous continuez donc sur le même chemin.")
                pause()
                print("Au bout de une heure de marche vous arrivez a un croisement deux chemin s'offre a vous.")
                print(" ")
                print("Le chemin de gauche est parsemé de fleurs, vous sentez leur bonnes odeur.")
                print(" ")
                print("Le chemin de droite est lui plein de piques surmonter de têtes avec des panneaux interdisant d'aller plus loin.")
                print(" ")
                color.write("\n salut c'est Yo je te conseil de bien choisir, car l'un d'eu envoie a une mort certaines.\n", "STRING")
                pause()
                print("Vous pouvez choisir d'aller soit à (gauche), soit à (droite).")
                choix=input()
                if choix=='gauche':
                    print("Vous decidez de prendre le chemin de gauche.")
                    print(" ")
                    print("Les fleurs qui vous entoure sentent tellement bon, sans vous rendre compte vous arrivez jusqu'a une clairière.")
                    print(" ")
                    print("Vous remarquez que cette clairière est parsemé de tache rouge.")
                    print(" ")
                    print("Soudainement, vous voyez que ce sont des cadavre et non des taches.")
                    print(" ")
                    print("Vous vous trouvez dans le champs de la mort, les fleurs qui le compose ont une odeur mortelle.")
                    print(" ")
                    print("Malheuresement vous n'avez pas le temps de courir, votre corps s'éffondre et votre chemin s'arrête en même temps")
                    vie=0
                if choix=='droite':
                    print("Vous décidez de prendre a droite.")
                    print(" ")
                    print("Le chemin est tres sinueu et très mal entretenue vous pourriez vous casser la cheville à tous moment.")
                    print(" ")
                    print("Apres plusieur minute vous arrivez à une autre clairière.")
                    print(" ")
                    print("Vous voyez des tentes et des hommes en armure de cuir.")
                    print(" ")
                    print("Soudaint dérièrre vous un homme sort des broussailles, il est immense et porte une grosse épée.")
                    print(" ")
                    print("Il vous regarde en souriant et vous frappe")
                    print(" ")
                    color.write("\ntentez votre chance, lancez un d20 si vous faites entre 10 et 20 vous êtes chanceux sinon vous êtes malchanceux.\n", "KEYWORD")
                    choix=input()
                    if choix=='d20':
                        reschan=d20()
                        print("Vous avez fait", reschan,"")
                        if reschan>=10:
                            print(" vous réussissez à esquivez à temps, mais il vous attaque.")
                        else:
                            print("vous prenez le coup de plein fouet vous prennez 4 dégats, il vous attaque.")
                            vie= vie - 4
                    vieb=8
                    bandit()
                    pause()
                    prendre()
                    print("Vous vous relevez et respirez un coup.")
                    print(" ")
                    print("c'était un adversaire d'un autre trempe.")
                    print(" ")
                    print("Vous avez deux options soit vous (traversez) la clairière soit vous la (contournez)")
                    choix=input()
                    if choix=='traversez':
                        print("Vous décidez de traversez mais lorsque vous êtes a la moitiez du trajet une pluit de fléche vous transperce.")
                        print(" ")
                        print("Qu'elle idée de traversez un camps de bandit, votre aventure s'arrête ici.")
                        gameover()
                    if choix=='contournez':
                        print("Vous décidez de contourner.")
                        print(" ")
                        print("Au bout de quelque minutes, un curieux personnage vous aborde.")
                        print(" ")
                    
                    
                
                
            elif choix=='continuer':
                print("Vous décidez de continuer.")
                print(" ")
                print("Au fur et a mesure que vous avancez, vous fatiguez de plus en plus.")
                print(" ")
                print("si vous avez une ration vous pouvez en manger")
                print(" ")
                print("Souhaitez vous manger une ration (oui) ou (non)")
                choix=input()
                if choix=='oui':
                    if ration>=1:
                        ration = - 1
                        print("Vous mangez une ration vous regagnez 3 vie")
                        vie = vie + 3
                        print("Vous avez", vie,"vie")
                    else:
                        print("Vous ne pouvez pas manger de ration vous n'en avez plus")
                        faim = + 1
                elif choix=='non':
                    print("vous décidez de ne pas manger, attention a bien manger tous les deux jours")
                    faim = + 1
                pause()
                print("Soudainement, une vague d'énergie vous assomme sans que vous puissiez l'esquiver")
                print(" ")
                print("Vous tombez dans un cauchemar qui semble semble sans fin ou vous voyez sans arrêt votre prénom")
                pause()
                print("lorsque vous vous reveillez, vous remarquez que vous êtes dans une hutte en peau.")
                print(" ")
                print("Un homme est assis juste devant l'entrée, il porte un masque qui vous met mal a l'aise")
                print(" ")
                print("Il vous regarde et vous lance.")
                print(" ")
                print("Bonjour voyageur, j'espere que vous ne souffrez pas trop")
                print(" ")
                print("Je me nomme Zed et ici c'est chez moi, normalement les gens savent qu'il ne faut pas aller a gauche au chemin.")
                print(" ")
                print("Mais vous y etes allé.")
                print(" ")
                print("je vous propose donc un jeu si vous gagnez, je vous laisse filer sinon je vous tue.")
                print(" ")
                print("Cool vous avez l'air d'accord.")
                pause()
                print("Je vais donc vous proposer une énigme.")
                print(" ")
                print("Qu’est-ce qui t’appartient mais que les gens utilisent beaucoup plus que toi ?")
                print(" ")
                print("je te laisse trois chance")
                print(" ")
                enigme()
                pause()
                print("Mon conseil et de ne pas prendre le chemin qui te semble être le plus facile.")
                print(" ")
                print("Voila également 2 ration.")
                print(" ")
                print("Et je vais également soigner vos blessure.")
                vie = 15
                print("Il vous reste",vie,"vie")
                print(" ")
                print("Maintenant tu dois partir")
                print(" ")
                print("Vous sortez de la hutte et remarquez que vous étiez dans une prairie entouré de piége a loup.")
                print(" ")
                print("Vous suivez le chemin qui méne vers la forêt.")
                print(" ")
                print("apres quelque minute de marche vous retrouvez le gobelin que vous aviez tué.")
                print(" ")
                print("Vous continuez donc sur le même chemin.")
                pause()
                print("Au bout de une heure de marche vous arrivez a un croisement deux chemin s'offre a vous.")
                print(" ")
                print("Le chemin de gauche est parsemé de fleurs, vous sentez leur bonnes odeur.")
                print(" ")
                print("Le chemin de droite est lui plein de piques surmonter de têtes avec des panneaux interdisant d'aller plus loin.")
                print(" ")
                color.write("\n salut c'est Yo je te conseil de bien choisir, car l'un d'eu envoie a une mort certaines.\n", "STRING")
                pause()
                print("Vous pouvez choisir d'aller soit à (gauche), soit à (droite).")
                choix=input()
                if choix=='gauche':
                    print("Vous decidez de prendre le chemin de gauche.")
                    print(" ")
                    print("Les fleurs qui vous entoure sentent tellement bon, sans vous rendre compte vous arrivez jusqu'a une clairière.")
                    print(" ")
                    print("Vous remarquez que cette clairière est parsemé de tache rouge.")
                    print(" ")
                    print("Soudainement, vous voyez que ce sont des cadavre et non des taches.")
                    print(" ")
                    print("Vous vous trouvez dans le champs de la mort, les fleurs qui le compose ont une odeur mortelle.")
                    print(" ")
                    print("Malheuresement vous n'avez pas le temps de courir, votre corps s'éffondre et votre chemin s'arrête en même temps")
                    vie=0
                if choix=='droite':
                    print("Vous décidez de prendre a droite.")
                    print(" ")
                    print("Le chemin est tres sinueu et très mal entretenue vous pourriez vous casser la cheville à tous moment.")
                    print(" ")
                    print("Apres plusieur minute vous arrivez à une autre clairière.")
                    print(" ")
                    print("Vous voyez des tentes et des hommes en armure de cuir.")
                    print(" ")
                    print("Soudaint dérièrre vous un homme sort des broussailles, il est immense et porte une grosse épée.")
                    print(" ")
                    print("Il vous regarde en souriant et vous frappe")
                    print(" ")
                    color.write("\ntentez votre chance, lancez un d20 si vous faites entre 10 et 20 vous êtes chanceux sinon vous êtes malchanceux.\n", "KEYWORD")
                    choix=input()
                    if choix=='d20':
                        reschan=d20()
                        print("Vous avez fait", reschan,"")
                        if reschan>=10:
                            print(" vous réussissez à esquivez à temps, mais il vous attaque.")
                        else:
                            print("vous prenez le coup de plein fouet vous prennez 4 dégats, il vous attaque.")
                            vie= vie - 4
                    vieb=8
                    bandit()
                    pause()
                    prendre()
                    print("Vous vous relevez et respirez un coup.")
                    print(" ")
                    print("c'était un adversaire d'un autre trempe.")
                    pause()
                    print("Vous avez deux options soit vous (traversez) la clairière soit vous la (contournez)")
                    choix=input()
                    if choix=='traversez':
                        print("Vous décidez de traversez mais lorsque vous êtes a la moitiez du trajet une pluit de fléche vous transperce.")
                        print(" ")
                        print("Qu'elle idée de traversez un camps de bandit, votre aventure s'arrête ici.")
                        vie=0
                    if choix=='contournez':
                        print("Vous décidez de contourner.")
                        print(" ")
                        print("Au bout de quelque minutes, un curieux personnage vous aborde.")
                        print(" ")
                        color.write("\nMerci d'avoir jouer a la démo, des mises à jour seront apportées régulierement.\n", "KEYBORD")
                        pause()
                        
        if choix=='droite':
            print("Vous décidez d'aller a droite")
            print(" ")
            print("Vous avancez et au bout d'un moment vous tombez sur un homme qui semble vieux.")
            print(" ")
            print("Il vous regarde et vous demande de l'aide, car il n'arrive pas a atteindre une pomme dans un arbre.")
            print(" ")
            print("Vous pouvez soit l'(aider) soit (partir)")
            choix=input()
            if choix=='aider':
                print("Vous décidez de l'aider.")
                print(" ")
                print("Vous lui proposez votre aide et vous prenez la pomme.")
                print(" ")
                print("Au moment ou vous attraper la pomme vous sentez un eclair vous traversez.")
                print(" ")
                print("En quelque seconde vous vous transformez en lapin.")
                print(" ")
                print("L'homme vous regarde et dit en souriant.")
                print(" ")
                print("Il ne faut faire confiance à personne ici.")
                vie=0
            if choix=='partir':
                print("Vous décidez de passer votre chemin.")
                print(" ")
                print("L'homme se retourne et vous dit d'un ton agressive.")
                print(" ")
                print("On aide pas les vielles personnes alors.")
                print(" ")
                print("Il leve les main vers vous et un éclair vous transperce.")
                print(" ")
                print("He bas on ne vous a pas apris les bonnes manieres")
                print(" ")
                print("Votre aventure s'arrête ici")
                gameover()
                    

                


            
    elif choix=='enfuir':
        print(" ")
        print("La femme vous regarde et se met a pleurer, elle vous demande au moins de porter une lettre a son fils.")
        print(" ")
        print("Il habite a Bri, traversez la forêt et vous y serez.")
        print(" ")
        print("Vous prenez la lettre et vous partez direction la forêt.")
        pause()
        print("Après quelques minutes de marche vous arrivez devant la Forêt des Mensonges, elle est d'une noirceur effrayante.")
        print(" ")
        print("Vous prenez votre souffle, regardez en arrière et pénétrez dans la forêt.")
        pause()
        print("dans la forêt il fait très sombre, vous n'entendez presque aucun bruit seulement le bruit du vent sur les branches.")
        print(" ")
        print("Quelque dizaines de mètres plus loin vous arrivez à un croisement.")
        print(" ")
        color.write("\nVous pouvez aller soit à (gauche) soit à (droite)\n", "STRING")
        choix=input()
        if choix=='gauche':
            print("Vous décidez de prendre à gauche.")
            pause()
            print("Au fur et à mesure que vous marcher vous sentez que l’on vous observe, vous décidez donc de presser le pas.")
            print(" ")
            print("comme vous marcher trop vite vous ne remarquez pas la racine sur le bord du chemin.")
            print(" ")
            color.write("\ntentez votre chance, lancé un d20 si vous faites entre 10 et 20 vous êtes chanceux sinon vous êtes malchanceux.\n", "KEYWORD")
            choix=input()
            if choix=='d20':
                reschan=d20()
                print("Vous avez fait", reschan,"")
                if reschan>=10:
                    print(" vous réussissez à vous rattraper à temps, vous avez esquiver un buisson de ronce.")
                else:
                    print("vous tombez dans un buisson de ronce vous perdez 2 vie")
                    vie= vie - 2
            pause()
            print("Vous entendez maintenant clairement une personne, qui court dans la forêt.")
            print(" ")
            print("Vous sortez votre arme et attendez qu'il se montre, quelque seconde plus tard quelque chose sort des brousailles.")
            print("")
            print("Devant vous se dresse un petit homme vert avec une dague dans sa main, il s'agit d'un gobelin.")
            print(" ")
            print("Il vous fonce dessus, il attaque !")
            pause()
            vieg=6
            gobelin()
            pause()
            prendre()
            pause()
            print("Vous reprenez votre souffle, c'est la premiere fois que vous rencontrez une créature comme celle la.")
            print(" ")
            print("Vous imaginez tous les danger que vous pourriez rencontrer dans cette forêt mais vous n'avez pas peur au contraire vous etes exité.")
            print(" ")
            print("Vous reprenez la route.")
            pause()
            print("Apres quelques minutes de marche vous revoyez le cadavre du gobelin")
            print(" ")
            print("Apres plusieur passage devant le gobelin vous comprenez que vous tournez en rond")
            print(" ")
            print("Vous remarquez aussi qu'il fait presque nuit")
            pause()
            print("que décidez vous (camper) ou (continuer) de marcher")
            choix=input()
            if choix=='camper':
                print("Vous décidez de vous installer pour la nuit.")
                print(" ")
                print("Une fois le campement installé vous allumez un feu")
                print(" ")
                print("si vous avez une ration vous pouvez en manger")
                print(" ")
                print("Souhaitez vous manger une ration (oui) ou (non)")
                choix=input()
                if choix=='oui':
                    if ration>=1:
                        ration = - 1
                        print("Vous mangez une ration vous regagnez 3 vie")
                        vie = vie + 3
                        print("Vous avez", vie,"vie")
                    else:
                        print("Vous ne pouvez pas manger de ration vous n'en avez plus")
                        faim = + 1
                elif choix=='non':
                    print("vous décidez de ne pas manger, attention a bien manger tous les deux jours")
                    faim = + 1
                pause()
                print("Soudainement, une vague d'énergie vous assomme sans que vous puissiez l'esquiver")
                print(" ")
                print("Vous tombez dans un cauchemar qui semble semble sans fin ou vous voyez sans arrêt votre prénom")
                pause()
                print("lorsque vous vous reveillez, vous remarquez que vous êtes dans une hutte en peau.")
                print(" ")
                print("Un homme est assis juste devant l'entrée, il porte un masque qui vous met mal a l'aise")
                print(" ")
                print("Il vous regarde et vous lance.")
                print(" ")
                print("Bonjour voyageur, j'espere que vous ne souffrez pas trop")
                print(" ")
                print("Je me nomme Zed et ici c'est chez moi, normalement les gens savent qu'il ne faut pas aller a gauche au chemin.")
                print(" ")
                print("Mais vous y etes allé.")
                print(" ")
                print("je vous propose donc un jeu si vous gagnez, je vous laisse filer sinon je vous tue.")
                print(" ")
                print("Cool vous avez l'air d'accord.")
                pause()
                print("Je vais donc vous proposer une énigme.")
                print(" ")
                print("Qu’est-ce qui t’appartient mais que les gens utilisent beaucoup plus que toi ?")
                print(" ")
                print("je te laisse trois chance")
                print(" ")
                enigme()
                pause()
                print("Mon conseil et de ne pas prendre le chemin qui te semble être le plus facile.")
                print(" ")
                print("Voila également 2 ration.")
                print(" ")
                print("Et je vais également soigner vos blessure.")
                vie = 15
                print("Il vous reste",vie,"vie")
                print(" ")
                print("Maintenant tu dois partir")
                print(" ")
                print("Vous sortez de la hutte et remarquez que vous étiez dans une prairie entouré de piége a loup.")
                print(" ")
                print("Vous suivez le chemin qui méne vers la forêt.")
                print(" ")
                print("apres quelque minute de marche vous retrouvez le gobelin que vous aviez tué.")
                print(" ")
                print("Vous continuez donc sur le même chemin.")
                pause()
                print("Au bout de une heure de marche vous arrivez a un croisement deux chemin s'offre a vous.")
                print(" ")
                print("Le chemin de gauche est parsemé de fleurs, vous sentez leur bonnes odeur.")
                print(" ")
                print("Le chemin de droite est lui plein de piques surmonter de têtes avec des panneaux interdisant d'aller plus loin.")
                print(" ")
                color.write("\nSalut c'est Yo je te conseil de bien choisir, car l'un d'eu envoie a une mort certaines.\n", "STRING")
                pause()
                print("Vous pouvez choisir d'aller soit à (gauche), soit à (droite).")
                choix=input()
                if choix=='gauche':
                    print("Vous decidez de prendre le chemin de gauche.")
                    print(" ")
                    print("Les fleurs qui vous entoure sentent tellement bon, sans vous rendre compte vous arrivez jusqu'a une clairière.")
                    print(" ")
                    print("Vous remarquez que cette clairière est parsemé de tache rouge.")
                    print(" ")
                    print("Soudainement, vous voyez que ce sont des cadavre et non des taches.")
                    print(" ")
                    print("Vous vous trouvez dans le champs de la mort, les fleurs qui le compose ont une odeur mortelle.")
                    print(" ")
                    print("Malheuresement vous n'avez pas le temps de courir, votre corps s'éffondre et votre chemin s'arrête en même temps")
                    vie=0
                if choix=='droite':
                    print("Vous décidez de prendre a droite.")
                    print(" ")
                    print("Le chemin est tres sinueu et très mal entretenue vous pourriez vous casser la cheville à tous moment.")
                    print(" ")
                    print("Apres plusieur minute vous arrivez à une autre clairière.")
                    print(" ")
                    print("Vous voyez des tentes et des hommes en armure de cuir.")
                    print(" ")
                    print("Soudaint dérièrre vous un homme sort des broussailles, il est immense et porte une grosse épée.")
                    print(" ")
                    print("Il vous regarde en souriant et vous frappe")
                    print(" ")
                    color.write("\ntentez votre chance, lancez un d20 si vous faites entre 10 et 20 vous êtes chanceux sinon vous êtes malchanceux.\n", "KEYWORD")
                    choix=input()
                    if choix=='d20':
                        reschan=d20()
                        print("Vous avez fait", reschan,"")
                        if reschan>=10:
                            print(" vous réussissez à esquivez à temps, mais il vous attaque.")
                        else:
                            print("vous prenez le coup de plein fouet vous prennez 4 dégats, il vous attaque.")
                            vie= vie - 4
                    vieb=8
                    bandit()
                    pause()
                    prendre()
                    print("Vous vous relevez et respirez un coup.")
                    print(" ")
                    print("c'était un adversaire d'un autre trempe.")
                    pause()
                    print("Vous avez deux options soit vous (traversez) la clairière soit vous la (contournez)")
                    choix=input()
                    if choix=='traversez':
                        print("Vous décidez de traversez mais lorsque vous êtes a la moitiez du trajet une pluit de fléche vous transperce.")
                        print(" ")
                        print("Qu'elle idée de traversez un camps de bandit, votre aventure s'arrête ici.")
                        gameover()
                    if choix=='contournez':
                        print("Vous décidez de contourner.")
                        print(" ")
                        print("Au bout de quelque minutes, un curieux personnage vous aborde.")
                        print(" ")
                        color.write("\nMerci d'avoir jouer a la démo, des mises à jour seront apportées régulierement.\n", "KEYBORD")
                        pause()
                    
                
            elif choix=='continuer':
                print("Vous décidez de continuer.")
                print(" ")
                print("Au fur et a mesure que vous avancez, vous fatiguez de plus en plus.")
                print(" ")
                print("si vous avez une ration vous pouvez en manger")
                print(" ")
                print("Souhaitez vous manger une ration (oui) ou (non)")
                choix=input()
                if choix=='oui':
                    if ration>=1:
                        ration = - 1
                        print("Vous mangez une ration vous regagnez 3 vie")
                        vie = vie + 3
                        print("Vous avez", vie,"vie")
                    else:
                        print("Vous ne pouvez pas manger de ration vous n'en avez plus")
                        faim = + 1
                elif choix=='non':
                    print("vous décidez de ne pas manger, attention a bien manger tous les deux jours")
                    faim = + 1
                pause()
                print("Soudainement, une vague d'énergie vous assomme sans que vous puissiez l'esquiver")
                print(" ")
                print("Vous tombez dans un cauchemar qui semble semble sans fin ou vous voyez sans arrêt votre prénom")
                pause()
                print("lorsque vous vous reveillez, vous remarquez que vous êtes dans une hutte en peau.")
                print(" ")
                print("Un homme est assis juste devant l'entrée, il porte un masque qui vous met mal a l'aise")
                print(" ")
                print("Il vous regarde et vous lance.")
                print(" ")
                print("Bonjour voyageur, j'espere que vous ne souffrez pas trop")
                print(" ")
                print("Je me nomme Zed et ici c'est chez moi, normalement les gens savent qu'il ne faut pas aller a gauche au chemin.")
                print(" ")
                print("Mais vous y etes allé.")
                print(" ")
                print("je vous propose donc un jeu si vous gagnez, je vous laisse filer sinon je vous tue.")
                print(" ")
                print("Cool vous avez l'air d'accord.")
                pause()
                print("Je vais donc vous proposer une énigme.")
                print(" ")
                print("Qu’est-ce qui t’appartient mais que les gens utilisent beaucoup plus que toi ?")
                print(" ")
                print("je te laisse trois chance")
                print(" ")
                enigme()
                pause()
                print("Mon conseil et de ne pas prendre le chemin qui te semble être le plus facile.")
                print(" ")
                print("Voila également 2 ration.")
                print(" ")
                print("Et je vais également soigner vos blessure.")
                vie = 15
                print("Il vous reste",vie,"vie")
                print(" ")
                print("Maintenant tu dois partir")
                print(" ")
                print("Vous sortez de la hutte et remarquez que vous étiez dans une prairie entouré de piége a loup.")
                print(" ")
                print("Vous suivez le chemin qui méne vers la forêt.")
                print(" ")
                print("apres quelque minute de marche vous retrouvez le gobelin que vous aviez tué.")
                print(" ")
                print("Vous continuez donc sur le même chemin.")
                pause()
                print("Au bout de une heure de marche vous arrivez a un croisement deux chemin s'offre a vous.")
                print(" ")
                print("Le chemin de gauche est parsemé de fleurs, vous sentez leur bonnes odeur.")
                print(" ")
                print("Le chemin de droite est lui plein de piques surmonter de têtes avec des panneaux interdisant d'aller plus loin.")
                print(" ")
                color.write("\nSalut c'est Yo je te conseil de bien choisir, car l'un d'eu envoie a une mort certaines.\n", "STRING")
                pause()
                print("Vous pouvez choisir d'aller soit à (gauche), soit à (droite).")
                choix=input()
                if choix=='gauche':
                    print("Vous decidez de prendre le chemin de gauche.")
                    print(" ")
                    print("Les fleurs qui vous entoure sentent tellement bon, sans vous rendre compte vous arrivez jusqu'a une clairière.")
                    print(" ")
                    print("Vous remarquez que cette clairière est parsemé de tache rouge.")
                    print(" ")
                    print("Soudainement, vous voyez que ce sont des cadavre et non des taches.")
                    print(" ")
                    print("Vous vous trouvez dans le champs de la mort, les fleurs qui le compose ont une odeur mortelle.")
                    print(" ")
                    print("Malheuresement vous n'avez pas le temps de courir, votre corps s'éffondre et votre chemin s'arrête en même temps")
                    vie=0
                if choix=='droite':
                    print("Vous décidez de prendre a droite.")
                    print(" ")
                    print("Le chemin est tres sinueu et très mal entretenue vous pourriez vous casser la cheville à tous moment.")
                    print(" ")
                    print("Apres plusieur minute vous arrivez à une autre clairière.")
                    print(" ")
                    print("Vous voyez des tentes et des hommes en armure de cuir.")
                    print(" ")
                    print("Soudaint dérièrre vous un homme sort des broussailles, il est immense et porte une grosse épée.")
                    print(" ")
                    print("Il vous regarde en souriant et vous frappe")
                    print(" ")
                    color.write("\ntentez votre chance, lancez un d20 si vous faites entre 10 et 20 vous êtes chanceux sinon vous êtes malchanceux.\n", "KEYWORD")
                    choix=input()
                    if choix=='d20':
                        reschan=d20()
                        print("Vous avez fait", reschan,"")
                        if reschan>=10:
                            print(" vous réussissez à esquivez à temps, mais il vous attaque.")
                        else:
                            print("vous prenez le coup de plein fouet vous prennez 4 dégats, il vous attaque.")
                            vie= vie - 4
                    vieb=8
                    bandit()
                    pause()
                    prendre()
                    print("Vous vous relevez et respirez un coup.")
                    print(" ")
                    print("c'était un adversaire d'un autre trempe.")
                    pause()
                    print("Vous avez deux options soit vous (traversez) la clairière soit vous la (contournez)")
                    choix=input()
                    if choix=='traversez':
                        print("Vous décidez de traversez mais lorsque vous êtes a la moitiez du trajet une pluit de fléche vous transperce.")
                        print(" ")
                        print("Qu'elle idée de traversez un camps de bandit, votre aventure s'arrête ici.")
                        gameover()
                    if choix=='contournez':
                        print("Vous décidez de contourner.")
                        print(" ")
                        print("Au bout de quelque minutes, un curieux personnage vous aborde.")
                        print(" ")
                        color.write("\nMerci d'avoir jouer a la démo, des mises à jour seront apportées régulierement.\n", "KEYBORD")
                        pause()
    
        if choix=='droite':
            print("Vous décidez d'aller a droite")
            print(" ")
            print("Vous avancez et au bout d'un moment vous tombez sur un homme qui semble vieux.")
            print(" ")
            print("Il vous regarde et vous demande de l'aide, car il n'arrive pas a atteindre une pomme dans un arbre.")
            print(" ")
            print("Vous pouvez soit l'(aider) soit (partir)")
            choix=input()
            if choix=='aider':
                print("Vous décidez de l'aider.")
                print(" ")
                print("Vous lui proposez votre aide et vous prenez la pomme.")
                print(" ")
                print("Au moment ou vous attraper la pomme vous sentez un eclair vous traversez.")
                print(" ")
                print("En quelque seconde vous vous transformez en lapin.")
                print(" ")
                print("L'homme vous regarde et dit en souriant.")
                print(" ")
                print("Il ne faut faire confiance à personne ici.")
                gameover()
            if choix=='partir':
                print("Vous décidez de passer votre chemin.")
                print(" ")
                print("L'homme se retourne et vous dit d'un ton agressive.")
                print(" ")
                print("On aide pas les vielles personnes alors.")
                print(" ")
                print("Il leve les main vers vous et un éclair vous transperce.")
                print(" ")
                print("He bas on ne vous a pas apris les bonnes manieres")
                print(" ")
                print("Votre aventure s'arrête ici")
                gameover()
                
        
        

print(" ")   
print("Vous êtes mort dommage n'hesite pas à réssayer")

############################



