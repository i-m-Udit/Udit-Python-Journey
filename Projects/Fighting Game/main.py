import random
import time

bosses = ["The Skeleton Pirate" , "Chicken Jockey" , "The Ender Dragon"]

print ("Welcome to the FIGHT or GOOD NIGHT game!!")
time.sleep(1)
print("In this game you can become 3 fighters each has its own pros and cons.") 
time.sleep(1)
print(f"What do you want to become? \n1.The Warrior ( He has high hp (hitpoints) but low damage) \n2. The Ninja (He has low hp (hitpoints) but high damage) \n3.The Titan ( He has perfect balance between hp (hitpoints) and damage)")
time.sleep(1)

warrior_hp = 200
warrior_attack1 = 15
warrior_attack2 = 20
warrior_heal = 10

ninja_hp = 100
ninja_attack1=25
ninja_attack2 = 30
ninja_heal = 20

titan_hp = 150
titan_attack1 = 20
titan_attack2 = 20
titan_heal = 15

boss_name = random.choice(bosses)
boss_hp = 175
boss_attack1 = 25
boss_attack2 = 30
boss_heal = 5

boss_tasks = [boss_attack1 , boss_attack2 , boss_heal]

def bossTasks_w():
    global boss_hp
    global warrior_hp

    boss_t = random.choice(boss_tasks)

    if boss_t == boss_attack1:
        print(f"Boss dealt {boss_attack1} damage")
        warrior_hp = warrior_hp - boss_attack1

    elif boss_t == boss_attack2:
        print(f"Boss dealt {boss_attack2} damage")
        warrior_hp = warrior_hp - boss_attack2

    elif boss_t == boss_heal:
        print(f"Boss healed {boss_heal} hp")
        boss_hp = boss_hp + boss_heal

    print(f"You : {warrior_hp} Boss : {boss_hp}")
    time.sleep(0.75)

def bossTasks_n():
    global boss_hp
    global ninja_hp
    boss_t = random.choice(boss_tasks)
    if boss_t == boss_attack1:
        print(f"Boss dealt {boss_attack1} damage")
        ninja_hp = ninja_hp - boss_attack1
    elif boss_t == boss_attack2:
        print(f"Boss dealt {boss_attack2} damage")
        ninja_hp = ninja_hp - boss_attack2
    elif boss_t == boss_heal:
        print(f"Boss healed {boss_heal} hp")
        boss_hp = boss_hp + boss_heal
    print(f"You : {ninja_hp} Boss : {boss_hp}")
    time.sleep(0.75)

def bossTasks_t():
    global boss_hp
    global titan_hp
    boss_t = random.choice(boss_tasks)
    if boss_t == boss_attack1:
        print(f"Boss dealt {boss_attack1} damage")
        titan_hp = titan_hp - boss_attack1
    elif boss_t == boss_attack2:
        print(f"Boss dealt {boss_attack2} damage")
        titan_hp = titan_hp - boss_attack2
    elif boss_t == boss_heal:
        print(f"Boss healed {boss_heal} hp")
        boss_hp = boss_hp + boss_heal
    print(f"You : {titan_hp} Boss : {boss_hp}")
    time.sleep(0.75)

try:
    choice = int(input(">  "))
    time.sleep(1)

    if choice == 1:
        print('''🔥 You walk the path of strength...

🛡️ **The Warrior** — forged in battle, fueled by will.

He has no magic, no tricks, no fancy robes.  
Only scars... and the discipline of a thousand fights.

When others flee, he stands.  
When others fall, he rises.  
When war calls — he answers.

His blade is heavy.  
His heart, heavier.

You are the Warrior.  
⚔️ And this arena... is your proving ground.
  
                ''')
        print(f"You are fighting {boss_name}")

        time.sleep(1)

        while True:
            warrior_fight = int(input("What do you want to do? \n1.Punch \n2.Sword attack \n3.Heal \n > (1 / 2 / 3)   >  "))
            time.sleep(1)

            if warrior_fight == 1:
                print (f"You dealt {warrior_attack1} damage")
                boss_hp= boss_hp - warrior_attack1
                print(f"Boss : {boss_hp}")
                time.sleep (1)

                bossTasks_w()

            if warrior_fight == 2:
                print (f"You dealt {warrior_attack2} damage")
                boss_hp= boss_hp - warrior_attack2
                print(f"Boss : {boss_hp}")
                bossTasks_w()

            if warrior_fight == 3:
                print(f"You healed up {warrior_heal} health")
                warrior_hp = warrior_hp+ warrior_heal
                
                bossTasks_w()
            if boss_hp<=0 and warrior_hp<=0:
                print(""" 🤝 It's a draw...

Both fighters fall to the ground — weapons shattered, spirits unbroken.

⚔️ This was not victory.  
💀 This was not defeat.

It was a battle worthy of legends.

But legends don't end here...  
They rise again — stronger than before.
""")

            if warrior_hp <= 0:
                print("""You lost , 💀 You have fallen today...

But remember:  
🛡️ **A true warrior learns more from defeat than from victory.**

Rise again. Fight smarter. Come back stronger.
""")
                time.sleep(1)
                break
            if boss_hp<=0:
                print("""You won , 🏆 Victory is yours!

The enemy lies broken — not just by your strength,
but by your will to never give up.

⚔️ **You fought. You endured. You conquered.**

Remember this moment — for it was forged by fire.
""")
                time.sleep(1)
                break
    if choice == 2:
        time.sleep(1)

        print("""🌑 You have chosen the path of shadows...

⚔️ **The Ninja** — swift, silent, and deadly.

Trained in forgotten temples,  
Master of the blade, smoke, and silence,  
They strike before they're seen...  
...and vanish before they`re remembered.

No brute force. No mercy.  
Only precision — and purpose.

🩸 One mistake from the enemy… and it`s over.

You are the Ninja.  
🕶️ Let the shadows guide your bla
""")
        print(f"You are fighting {boss_name}")
        time.sleep(1)

        while True:
            ninja_fight = int(input("What do you want to do? \n1.Punch \n2.Sword attack \n3.Heal \n > (1 / 2 / 3)   >  "))
            time.sleep(1)

            if ninja_fight == 1:
                print (f"You dealt {ninja_attack1} damage")
                boss_hp= boss_hp - ninja_attack1
                print(f"Boss : {boss_hp}")
                time.sleep (1)
                bossTasks_n()

            if ninja_fight == 2:
                print (f"You dealt {ninja_attack2} damage")
                boss_hp= boss_hp - ninja_attack2
                print(f"Boss : {boss_hp}")
                time.sleep (1)
                bossTasks_n()

            if ninja_fight == 3:
                print(f"You healed up {ninja_heal} health")
                ninja_hp = ninja_hp+ ninja_heal
                bossTasks_n()
            
            if boss_hp<=0 and ninja_hp<=0:
                    print(""" 🤝 It's a draw...

Both fighters fall to the ground — weapons shattered, spirits unbroken.

⚔️ This was not victory.  
💀 This was not defeat.

It was a battle worthy of legends.

But legends don't end here...  
They rise again — stronger than before.
""")
                    break
                
            if ninja_hp <= 0:
                print("""You lost , 💀 You have fallen today...

But remember:  
🛡️ **A true ninja learns more from defeat than from victory.**

Rise again. Fight smarter. Come back stronger.
""")
                break
            if boss_hp<=0:
                print("""You won , 🏆 Victory is yours!

The enemy lies broken — not just by your strength,
but by your will to never give up.

⚔️ **You fought. You endured. You conquered.**

Remember this moment — for it was forged by fire.
""")
            time.sleep(1)
            break
    if choice == 3:
        time.sleep(1)

        print("""🌩️ The ground trembles... the skies grow silent...

From the edge of forgotten realms rises the unstoppable force —  
💀 **The Titan.**

Born of chaos.  
Built for destruction.  
Feared by gods... and hunted by none.

He doesn`t dodge.  
He doesn`t kneel.  
He only crushes.

Every swing is an earthquake.  
Every step, a warning.

You face the Titan now...  
⚠️ Pray your courage lasts longer than your breath.

""")
        print(f"You are fighting {boss_name}")
        time.sleep(1)

        while True:
            titan_fight = int(input("What do you want to do? \n1.Punch \n2.Sword attack \n3.Heal \n > (1 / 2 / 3)   >  "))
            time.sleep(1)

            if titan_fight == 1:
                print (f"You dealt {titan_attack1} damage")
                boss_hp= boss_hp - titan_attack1
                print(f"Boss : {boss_hp}")
                time.sleep (1)
                bossTasks_t()

            if titan_fight == 2:
                print (f"You dealt {titan_attack2} damage")
                boss_hp= boss_hp - titan_attack2
                print(f"Boss : {boss_hp}")
                time.sleep (1)
                bossTasks_t()

            if titan_fight == 3:
                print(f"You healed up {titan_heal} health")
                titan_hp = titan_hp+ titan_heal
                time.sleep(0.75)
                bossTasks_t()

            if boss_hp<=0 and titan_hp<=0:
                    print(""" 🤝 It's a draw...

Both fighters fall to the ground — weapons shattered, spirits unbroken.

⚔️ This was not victory.  
💀 This was not defeat.

It was a battle worthy of legends.

But legends don't end here...  
They rise again — stronger than before.
""")
                    break
            
            if titan_hp <= 0:
                print("""You lost , 💀 You have fallen today...

But remember:  
🛡️ **A true ninja learns more from defeat than from victory.**

Rise again. Fight smarter. Come back stronger.
""")
                break
            if boss_hp<=0:
                print("""You won , 🏆 Victory is yours!

The enemy lies broken — not just by your strength,
but by your will to never give up.

⚔️ **You fought. You endured. You conquered.**

Remember this moment — for it was forged by fire.
""")
                time.sleep(1)
                break

except ValueError :
    print("Enter a valid value!!!")
    
except Exception as e :
    print(e)
