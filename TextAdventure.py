# Update this text to match your story.
start = '''
You wake up one day in the middle of a forrest. Standing up, you look around, scanning the area.
After a fruitless search to find something familiar, you realize the awful truth.
You're lost.
What do you do?
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left. The more you wander, the scarier it looks. You begin to move faster. And faster. And faster. Suddenly, you run into a giant monster. He roars. What do you do?")
    print("Type 'run away' to escape or type 'befriend' to befriend the monster. (Don't pick run away- not quite done yet.)")
    user_input = input()# Update to match your story.
    if user_input == "run away":
        print("You escape the terrifying beast within an inch of your life, and finally slow to a walk. Suddenly, a glimmering figure appears in the corner of your eye. As it grows closer, you can discern that it's a fairy. Although her voice is extremely high and soft, you can tell she's offering help. Do you accept?")
        print()
    elif user_input == "befriend":
        print("The monster is extremely grateful that you didn't run away in fear like everyone else. He tells you his name is Frank. You tell him about your issue, and he offers assistance out of the woods? Do you take his help?")
        print("Type 'yes' to accept and 'no' to decline.")
        if user_input == 'yes':
            print("You follow Frank for a while, as the sun sinks slowly into the sky. You see two similarly shaped and colored rocks. Then a third. And a fourth. The trees look sort of familiar. And is that the same rabbit hole you woke up next to? Suddenly, Frank turns to you, and says, 'You know, I am really sorry, but now I think I am lost as you are.'")
        elif user_input == 'no':
            print("Frank shakes his head sadly. 'You know, you're a pretty nice person. I hope you find your way out.")
            print("Frank has really seemed to have taken a shine to you, and now that you think about it, you've never quite met anybody like Frank. Do you want to keep going or hang out with Frank?")
            print("Type 'keep going' to travel on or 'hang out with Frank' to stay.")
            if user_input == 'keep going':
                print("You say goodbye to Frank, and keep walking on ahead. As you walk, you notice the grass beneath your feet slowly shift into a beaten dirt path. The more you walk, the more familiar it seems. The tree cover begins to thin out. You can just make out the buildings on the outskirts of town. You're home!")
            elif user_input == 'hang out with Frank':
                print("You and Frank become best friends, and stay that way, until your entire town burns down the forrest looking for you. Frank refueses to speeak to you anymore, thinking that you orchestrated the incinceration of his home. You do end up getting home, but at what cost?")
    # iContinue code to finish story.

elif user_input == "right":
    print("You choose to go right. The longer you walk, the denser the forrest becomes. All of the sudden you run into a giant tree, completely blocking your path, but you remember you have your machete. What now?" )
    print("Type 'climb' to climb the tree or type 'attack' to hack at the tree with your machete.")
    user_input = input()
    if user_input == "attack":
        print("You hear a sudden screech of pain. It startles you so badly you drop your machete. You hear a booming voice say, 'You're lucky that was only a scratch.' You see the bark of the trunk morph into a face. What do you do?")
        print("Type 'run' to escape or 'reply' to strike up a conversation.")
        if user_input == 'run':
            print("You sprint away, mind spinning. There is no way that trees can talk. That's not possible. That's not right. You run so fast, in fact, you don't look where you're going, and trip over a tree root headlong into a ravine. You smack head pretty hard on those pointy rocks, and your world goes dark.")
        elif user_input == 'reply':
            print("After apologizing, the tree introduces itself as 'Quercus rubra', nothing more and nothing less. Having grown here for over a thousand years, it has seen lots of lost people like you, and in a partially bored tone, informs you that you need to take right, then another right, and then a left before you get out. Floored, you remember your manners and thank the tree before following its directions. So focused on following the path, you don't even notice that you walk straight into your best friend, Betsy. You made it home!") # Update to match your story.
    elif user_input == "climb":
        print("You hear a groan of complaint as the tree informs you 'You know, you could've just told me to move.' You freeze. You are possibly crazy, and definetely far from home. Do you talk to the tree or continue to climb?")
        print("Type 'talk' to have a conversation with the tree, or type 'climb' to continue climbing.")
        if user_input == 'talk':
            print("The tree is very happy to have someone to talk to. When you inform the 'Quercus rubra' (as it insists to be called) that you're lost, it allows to climb its branches (its pride and joy) and take a look. From it's massive height, you can clearly see the end of the woods. You set out on your way.")
        elif user_input == 'climb':
            print("The tree shakes you off, and you plummet to the ground, but not nearly, as you land on the cart of a passing farmer. Hold on, wait second.. that's Tom Smith, John's brother! What's he doing so far out of town? He can't be...he wouldn't be...Your town grows barely enough to sustain itself. It can't take someone selling their food for cash. He's as confused as you are, but offers you a ride back home anyway. Neither of you speak of this ever again.")

    # Continue code to finish story.
