#pokemon game.py
import pygame, time, sys, os
pygame.init()

class Pokemon():
    #pokemon class
    pokeHealth = 0
    pokeAttack1 = 0
    pokeAttack2 = 0
    pokeEffect = 0
    EffectNum = 0
    pokeType = 0
    pokeUsed = 0
    moves = []

    def pokemonAlive(self):
        if self.pokeHealth <= 0:
            pygame.quit()        
            sys.exit()

pikachu = Pokemon()
pikachu.pokeHealth = 10
pikachu.pokeType = 1
pikachu.pokeAttack1 = 2
pikachu.pokeAttack2 = 1 # 3 on water opponents, 0 on other opponents#'''1 on every opponent'''
pikachu.pokeEffect = "None" #'''extra 2 damage next turn''' #'''1 reverse damage if attacked next turn'''
pikachu.EffectNum = 0
pikachu.pokeUsed = 0
pikachu.pokeName = 'Pikachu'
pikachu.moves = ['Thunder Shock','Growl','Charge up','Electrify']

squirtle = Pokemon()
squirtle.pokeHealth = 12
squirtle.pokeType = 2
squirtle.pokeAttack1 = 3
squirtle.pokeAttack2 = 3 #'''2 on fire enemy'''= False #'''5 on every enemy if their health is less than 5'''
squirtle.pokeEffect = 'None' #'''2 less damage if attacked next turn'''#'''recover 1 hp'''
squirtle.EffectNum = 0
squirtle.pokeUsed = 0
squirtle.pokeName = 'Squirtle'
squirtle.moves = ['Water Splash','Finishing Blow','Shell Shock','Rest']

charmander = Pokemon()
charmander.pokeHealth = 10
charmander.pokeType = 3
charmander.pokeAttack1 = 2 #2 damage to grass types, ignores all shields, otherwise does damage to self
charmander.pokeAttack2 = 2 
charmander.pokeEffect = 'None' 
charmander.EffectNum = 0
charmander.pokeUsed = 0
charmander.pokeName = 'Charmander'
charmander.moves = ['Flamethrower','Scratch','BlazeShield','Dragon Rage']

player1Pokemon = pikachu
player2Pokemon = squirtle
playerTurn = 0












while True:
    if playerTurn == 0:
        player1Pokemon.pokeUsed = 0
        os.system('clear')
        print (player1Pokemon.pokeName,"is in battle with", player2Pokemon.pokeName)
        print ("Your health:", player1Pokemon.pokeHealth, "         Opponents health:", player2Pokemon.pokeHealth )
        print ("You can use: 1(", player1Pokemon.moves[0], "); 2(", player1Pokemon.moves[1], "); 3(", player1Pokemon.moves[2],"); 4(", player1Pokemon.moves[3], "); 5( info on moves ) " )
        MoveMade = 0
        while MoveMade == 0:
            while player1Pokemon.pokeUsed == 0:
                move = input("Choose a move: ")
                player1Pokemon.pokeUsed = 1
                os.system('clear')

            #move 1 for player 1    
            if move == '1':

                if player1Pokemon.pokeType== 1 and player2Pokemon.pokeType == 2: #check if electric and water pokemon
                    if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                        if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            if player2Pokemon.EffectNum > player1Pokemon.pokeAttack1 + player1Pokemon.EffectNum: 
                                MoveMade =1
                            else:
                                player2Pokemon.pokeHealth == player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack1 - player1Pokemon.EffectNum
                                MoveMade = 1
                        else:
                            if player2Pokemon.EffectNum > player1Pokemon.pokeAttack1 :
                                MoveMade =1
                            else:
                                player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack1
                                MoveMade = 1
                    else:
                        if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - player1Pokemon.pokeAttack1 - player1Pokemon.EffectNum
                            MoveMade = 1
                        else:
                            player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack1
                            MoveMade = 1

                if player1Pokemon.pokeType== 2: #check if water pokemon
                    if player2Pokemon.pokeType == 3: #check if fire pokemon   
                        if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                            if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                if player2Pokemon.EffectNum > player1Pokemon.pokeAttack1 + player1Pokemon.EffectNum: 
                                    MoveMade =1
                                else:
                                    player2Pokemon.pokeHealth == player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack1 - player1Pokemon.EffectNum
                                    MoveMade = 1
                            else:
                                if player2Pokemon.EffectNum > player1Pokemon.pokeAttack1 :
                                    MoveMade =1
                                else:
                                    player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack1
                                    MoveMade = 1
                        else:
                            if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - player1Pokemon.pokeAttack1 - player1Pokemon.EffectNum
                                MoveMade = 1
                            else:
                                player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack1
                                MoveMade = 1
                    else: #if not a fire pokemon
                        if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                            if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                if player2Pokemon.EffectNum > 1 + player1Pokemon.EffectNum: 
                                    MoveMade =1
                                else:
                                    player2Pokemon.pokeHealth == player2Pokemon.pokeHealth + player2Pokemon.EffectNum - 1 - player1Pokemon.EffectNum
                                    MoveMade = 1
                            else:
                                if player2Pokemon.EffectNum > 1 :
                                    MoveMade =1
                                else:
                                    player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - 1
                                    MoveMade = 1
                        else:
                            if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - 1 - player1Pokemon.EffectNum
                                MoveMade = 1
                            else:
                                player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - 1
                                MoveMade = 1

                if player1Pokemon.pokeType == 3: #check if fire pokemon
                    if player2Pokemon.pokeType == 4:
                        player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - player1Pokemon.pokeAttack1
                    else:
                        player1Pokemon.pokeHealth-=1
                    MoveMade = 1        

                else:
                    MoveMade = 1
                if player2Pokemon.pokeEffect == "Spike" :
                    player1Pokemon.pokeHealth = player1Pokemon.pokeHealth - player2Pokemon.EffectNum 
                MoveMode = 1      
                player1Pokemon.EffectNum = 0
                player1Pokemon.pokeEffect = 'None'



            #move2 for player1        
            elif move == '2':
                if player1Pokemon.pokeType == 1:
                    if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                        if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            if player2Pokemon.EffectNum > player1Pokemon.pokeAttack2 + player1Pokemon.EffectNum: 
                                MoveMade =1
                            else:
                                player2Pokemon.pokeHealth == player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack2 - player1Pokemon.EffectNum
                                MoveMade = 1
                        else:
                            if player2Pokemon.EffectNum > player1Pokemon.pokeAttack2 :
                                MoveMade =1
                            else:
                                player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack2
                                MoveMade = 1
                    else:
                        if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - player1Pokemon.pokeAttack2 - player1Pokemon.EffectNum
                            MoveMade = 1
                        else:
                            player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack2
                            MoveMade = 1
                elif player1Pokemon.pokeType == 2:
                    if player2Pokemon.pokeHealth <= 5:
                        if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                            if player1Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                if player2Pokemon.EffectNum > player1Pokemon.pokeAttack2 + player1Pokemon.EffectNum: 
                                    MoveMade =1
                                else:
                                    player2Pokemon.pokeHealth == player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack2 - player1Pokemon.EffectNum
                                    MoveMade = 1
                            else:
                                if player2Pokemon.EffectNum > player1Pokemon.pokeAttack2 :
                                    MoveMade =1
                                else:
                                    player2Pokemon.pokeHealth = player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack2
                                    MoveMade = 1
                    else:
                        MoveMade = 1
                elif player1Pokemon.pokeType == 3:
                    if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                        if player2Pokemon.EffectNum > player1Pokemon.pokeAttack2 + player1Pokemon.EffectNum: 
                            MoveMade =1
                        else:
                            player2Pokemon.pokeHealth == player2Pokemon.pokeHealth + player2Pokemon.EffectNum - player1Pokemon.pokeAttack2 - player1Pokemon.EffectNum
                            MoveMade = 1

                if player2Pokemon.pokeEffect == "Spike" :
                    player1Pokemon.pokeHealth = player1Pokemon.pokeHealth - player2Pokemon.EffectNum   
                player1Pokemon.EffectNum = 0
                player1Pokemon.pokeEffect = 'None'


            #move3 for player 1
            elif move == '3':
                if player1Pokemon.pokeType == 1:
                    player1Pokemon.pokeEffect = "Damage" 
                    player1Pokemon.EffectNum = 2
                if player1Pokemon.pokeType == 2:
                    player1Pokemon.pokeEffect = "Protect" 
                    player1Pokemon.EffectNum = 2
                MoveMade = 1
                if player1Pokemon.pokeType == 3:
                    player1Pokemon.pokeEffect = "Spike" 
                    player1Pokemon.EffectNum = 2
                MoveMade = 1  

            #move4 for player 1
            elif move == '4':
                if player1Pokemon.pokeType == 1:
                    player1Pokemon.pokeEffect = "Spike"
                    player1Pokemon.EffectNum = 1
                if player1Pokemon.pokeType == 2:
                    player1Pokemon.pokeEffect = "Heal"
                    player1Pokemon.EffectNum = 2
                    player1Pokemon.pokeHealth+=player1Pokemon.EffectNum
                if player1Pokemon.pokeType == 3:
                    player2Pokemon.pokeHealth-=4
                    player1Pokemon.pokeEffect = "Attack"
                    player1Pokemon.pokeHealth-=3
                MoveMade = 1 

            elif move == '5':
                if player1Pokemon.pokeType == 1:
                    print ("Thunder Shock: 3 damage on water opponents, 0 on other opponents")
                    print ("Growl: 1 damage on every type")
                    print ("Charge Up: 2 extra damage next turn")
                    print ("Electrify: 1 damage is reversed if you get attacked next turn")
                    player1Pokemon.pokeUsed = 0
                if player1Pokemon.pokeType == 2:
                    print ("Water Splash: 2 damage on fire opponents, 1 on other opponents")
                    print ("Finishing Blow: 3 damage if opponents health is 5 or less")
                    print ("ShellShock: 2 less damage next turn")
                    print ("Rest: Heal 2 HP")
                    player1Pokemon.pokeUsed = 0
                if player1Pokemon.pokeType == 3:
                    print ("Flamethrower: 2 damage on grass opponents, ignoring all their effects, otherwise 1 damage to self")
                    print ("Scratch: 2 damage to opponent")
                    print ("BlazeShield: 2 damage is reversed if youre attacked next turn")
                    print ("Dragon Rage: Do 4 damage to your opponent, but also take 3 yourself")
                    player1Pokemon.pokeUsed = 0
            else:
                print ("Choose a valid move")
                player1Pokemon.pokeUsed = 0

        player1Pokemon.pokemonAlive()
        player2Pokemon.pokemonAlive()
       
        blink = 0
        while blink != 3:
            print ("Move Made!")
            print ("Your health:", player1Pokemon.pokeHealth, "         Opponents health:", player2Pokemon.pokeHealth)
            if player1Pokemon.pokeType == 1:
                if player1Pokemon.pokeEffect == "Damage":
                    print("You are charged up now!")
                if player1Pokemon.pokeEffect == "Spike":
                    print("You are covered entirely with lightning bolts now!")
            if player1Pokemon.pokeType == 2:
                if player1Pokemon.pokeEffect == "Protect":
                    print("You hide in your shell!")
                if player1Pokemon.pokeEffect == "Heal":
                    print("You rest and heal 2 hp")
            if player1Pokemon.pokeType == 3:
                if player1Pokemon.pokeEffect == "Spike":
                    print("You set yourself on fire!")
                if player1Pokemon.pokeEffect == "Attack":
                    print("You go in a fit of rage")
            time.sleep(0.6)
            os.system('clear')
            time.sleep(0.3)
            blink+=1
        del move
        playerTurn = 1

















#player2 turn
    if playerTurn == 1:
        player2Pokemon.pokeUsed = 0
        os.system('clear')
        print (player2Pokemon.pokeName,"is in battle with", player1Pokemon.pokeName)
        print ("Your health:", player2Pokemon.pokeHealth, "         Opponents health:", player1Pokemon.pokeHealth )
        print ("You can use: 1(", player2Pokemon.moves[0], "); 2(", player2Pokemon.moves[1], "); 3(", player2Pokemon.moves[2],"); 4(", player2Pokemon.moves[3], "); 5( info on moves ) " )
        MoveMade = 0
        while MoveMade == 0:
            while player2Pokemon.pokeUsed == 0:
                move = input("Choose a move: ")
                player2Pokemon.pokeUsed = 1
                os.system('clear')

            #move 1 for player 2    
            if move == '1':
                if player2Pokemon.pokeType== 1 and player1Pokemon.pokeType == 2: #check if electric and water pokemon
                    if player1Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                        if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            if player1Pokemon.EffectNum > player2Pokemon.pokeAttack1 + player2Pokemon.EffectNum: 
                                MoveMade =1
                            else:
                                player1Pokemon.pokeHealth == player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack1 - player2Pokemon.EffectNum
                                MoveMade = 1
                        else:
                            if player1Pokemon.EffectNum > player2Pokemon.pokeAttack1 :
                                MoveMade =1
                            else:
                                player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack1
                                MoveMade = 1
                    else:
                        if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            player1Pokemon.pokeHealth = player1Pokemon.pokeHealth - player1Pokemon.pokeAttack1 - player2Pokemon.EffectNum
                            MoveMade = 1
                        else:
                            player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack1
                            MoveMade = 1
                if player2Pokemon.pokeType== 2: #check if water pokemon
                    if player1Pokemon.pokeType == 3: #check if fire pokemon   
                        if player2Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                            if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                if player1Pokemon.EffectNum > player2Pokemon.pokeAttack1 + player2Pokemon.EffectNum: 
                                    MoveMade =1
                                else:
                                    player1Pokemon.pokeHealth == player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack1 - player2Pokemon.EffectNum
                                    MoveMade = 1
                            else:
                                if player1Pokemon.EffectNum > player2Pokemon.pokeAttack1 :
                                    MoveMade =1
                                else:
                                    player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack1
                                    MoveMade = 1
                        else:
                            if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                player1Pokemon.pokeHealth = player1Pokemon.pokeHealth - player2Pokemon.pokeAttack1 - player2Pokemon.EffectNum
                                MoveMade = 1
                            else:
                                player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack1
                                MoveMade = 1
                    else: #if not a fire pokemon
                        if player1Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                            if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                if player1Pokemon.EffectNum > 1 + player2Pokemon.EffectNum: 
                                    MoveMade =1
                                else:
                                    player1Pokemon.pokeHealth == player1Pokemon.pokeHealth + player1Pokemon.EffectNum - 1 - player2Pokemon.EffectNum
                                    MoveMade = 1
                            else:
                                if player1Pokemon.EffectNum > 1 :
                                    MoveMade =1
                                else:
                                    player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - 1
                                    MoveMade = 1
                        else:
                            if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                player1Pokemon.pokeHealth = player1Pokemon.pokeHealth - 1 - player2Pokemon.EffectNum
                                MoveMade = 1
                            else:
                                player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - 1
                                MoveMade = 1
                else:
                    MoveMade = 1
                if player1Pokemon.pokeEffect == "Spike" :
                    player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - player1Pokemon.EffectNum   
                player2Pokemon.EffectNum = 0
                player2Pokemon.pokeEffect = 'None'

            #move2 for player1        
            elif move == '2':
                if player2Pokemon.pokeType == 1:
                    if player1Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                        if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            if player1Pokemon.EffectNum > player2Pokemon.pokeAttack2 + player2Pokemon.EffectNum: 
                                MoveMade =1
                            else:
                                player1Pokemon.pokeHealth == player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack2 - player2Pokemon.EffectNum
                                MoveMade = 1
                        else:
                            if player1Pokemon.EffectNum > player2Pokemon.pokeAttack2 :
                                MoveMade =1
                            else:
                                player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack2
                                MoveMade = 1
                    else:
                        if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                            player1Pokemon.pokeHealth = player1Pokemon.pokeHealth - player2Pokemon.pokeAttack2 - player2Pokemon.EffectNum
                            MoveMade = 1
                        else:
                            player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack2
                            MoveMade = 1
                elif player2Pokemon.pokeType == 2:
                    if player1Pokemon.pokeHealth <= 5:
                        if player1Pokemon.pokeEffect == "Protect": #checks if opponent is protected
                            if player2Pokemon.pokeEffect == "Damage": #checks if you have extra damage
                                if player1Pokemon.EffectNum > player2Pokemon.pokeAttack2 + player2Pokemon.EffectNum: 
                                    MoveMade =1
                                else:
                                    player1Pokemon.pokeHealth == player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack2 - player2Pokemon.EffectNum
                                    MoveMade = 1
                            else:
                                if player1Pokemon.EffectNum > player2Pokemon.pokeAttack2 :
                                    MoveMade =1
                                else:
                                    player1Pokemon.pokeHealth = player1Pokemon.pokeHealth + player1Pokemon.EffectNum - player2Pokemon.pokeAttack2
                                    MoveMade = 1
                    else:
                        MoveMade = 1
                if player1Pokemon.pokeEffect == "Spike" :
                    player2Pokemon.pokeHealth = player2Pokemon.pokeHealth - player1Pokemon.EffectNum   
                player2Pokemon.EffectNum = 0
                player2Pokemon.pokeEffect = 'None'

            #move3 for player 1
            elif move == '3':
                if player2Pokemon.pokeType == 1:
                    player2Pokemon.pokeEffect = "Damage" 
                    player2Pokemon.EffectNum = 2
                if player2Pokemon.pokeType == 2:
                    player2Pokemon.pokeEffect = "Protect" 
                    player2Pokemon.EffectNum = 2
                MoveMade = 1 

            #move4 for player 1
            elif move == '4':
                if player2Pokemon.pokeType == 1:
                    player2Pokemon.pokeEffect = "Spike"
                    player2Pokemon.EffectNum = 1
                if player2Pokemon.pokeType == 2:
                    player2Pokemon.pokeEffect = "Heal"
                    player2Pokemon.EffectNum = 2
                    player2Pokemon.pokeHealth+=player2Pokemon.EffectNum
                MoveMade = 1 

            elif move == '5':
                if player2Pokemon.pokeType == 1:
                    print ("Thunder Shock: 3 damage on water opponents, 0 on other opponents")
                    print ("Growl: 1 damage on every type")
                    print ("Charge Up: 2 extra damage next turn")
                    print ("Electrify: 1 damage is reversed if you get attacked next turn")
                    player2Pokemon.pokeUsed = 0
                if player2Pokemon.pokeType == 2:
                    print ("Water Splash: 2 damage on fire opponents, 1 on other opponents")
                    print ("Finishing Blow: 3 damage if opponents health is 5 or less")
                    print ("ShellShock: 2 less damage next turn")
                    print ("Rest: Heal 2 HP")
                    player2Pokemon.pokeUsed = 0
            else:
                print ("Choose a valid move")
                player2Pokemon.pokeUsed = 0

        player1Pokemon.pokemonAlive()
        player2Pokemon.pokemonAlive()
       
        blink = 0
        while blink != 3:
            print ("Move Made!")
            print ("Your health:", player2Pokemon.pokeHealth, "         Opponents health:", player1Pokemon.pokeHealth)
            if player2Pokemon.pokeType == 1:
                if player2Pokemon.pokeEffect == "Damage":
                    print("You are charged up now!")
                if player2Pokemon.pokeEffect == "Spike":
                    print("You are covered entirely with lightning bolts now!")
            if player2Pokemon.pokeType == 2:
                if player2Pokemon.pokeEffect == "Protect":
                    print("You hide in your shell!")
                if player2Pokemon.pokeEffect == "Heal":
                    print("You rest and heal 2 hp")
            time.sleep(0.6)
            os.system('clear')
            time.sleep(0.3)
            blink+=1
        del move
        playerTurn = 0