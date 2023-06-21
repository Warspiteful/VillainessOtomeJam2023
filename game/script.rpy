# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show cg1

    "The hit manhwa 'My Magical Kindness Made the Cold Prince Fall in Love!!' is the newest craze among manhwa readers."
    "Honestly…it's not the greatest out there. I've definitely read better. The plot is repetitive and the characters are the most basic tropes."
    "However…there's one thing that keeps me reading: the food."
    y "Ahh! I just love how the desserts look so realistic!"
    y "I know Otillia and Lewis are having a moment, but…"
    "I sigh, scrolling down my phone screen."
    y "That strawberry shortcake… I want to reach through the screen and grab it."
    "My stomach growls and I sigh once again."
    "It's late at night, as it usually is when I do my daily reading of manhwa."
    y "Maybe I should get a snack."
    y "Just a few more chapters. Then I will."
    "As I read, I can feel myself getting drowsy."
    "The pale blue light makes my eyes tired. I try to keep myself awake, but my body feels weird."
    y "Ugh…"
    "I lay back on my bed, phone in hand. My body feels light and tingly."
    y "(Did I eat today? I'm sure I did.)"
    y "(So why…do I feel this way?)"
    "My eyes drift close. I decide not to fight the feeling and fall asleep. I'll just eat a big breakfast tomorrow."
    scene black with fade
    call screen custom_input_modal("What was the villainess's name?", 'mcname')
    scene bg mcroom base with fade
    "The next morning, I could hear the sounds of birds chirping. My nose twitches as a sweet scent slowly wafts through the room."
    "With a groan, I sit up, my eyes still closed. My muscles are sore and it feels as if I ran a marathon."
    "The smell of food is enough to make me crack open my eyes. Immediately, I notice a silver tray on my bedside."
    show d oh with dissolve
    mc "What's this?"
    "I pick it up and set it on my lap. With a thick swallow, I take off the lid."
    show d fc
    mc "Oh. My. God."
    "On the tray is a delectable looking breakfast spread. Two scones, a tiny container of jam, a croissant, and even a bagel with cream cheese spread across it… My mouth is already watering."
    mc "Don't mind if I do!"
    "Without a second thought, I start digging in."

    scene white #WIP: CG
    "I let out a satisfied groan as I eat."
    mc "This is delicious!!"
    "Whoever made this deserves the world. It's absolutely perfect."
    "My thoughts are interrupted by a lady bursting into my room. I pause mid bite."
    scene bg mcroom base
    show d oh at left
    show maid at right
    "She stares at me."
    "I stare back."
    "She keeps staring."
    m "My lady?"
    nvl show
    narr "It’s not until that moment when my surroundings finally start coming into view."
    narr "An expensive wardrobe with a mirror gilded in gold. Expensive white trim detailing the entire room. Floral wallpaper. Thick and soft down comforter."
    narr "I am not in my bedroom."
    nvl hide
    nvl clear
    "I take another bite of my croissant, my eyebrows furrowing. The lady in front of me, who I now recognize as a maid, looks at me in concern."
    show d neu
    mc "Hmmm…"
    "I keep looking around. An odd sense of familiarity settles in my stomach."
    "Something about this room…I know it."
    "I finish my croissant and then look over at the maid."
    mc "Can you hand me a mirror?"
    "She bows her head."
    m "Yes, my lady."
    "She seems nervous as she grabs a handheld mirror off the dressing table. She hands it to me, not making eye contact."
    "Clue number one."
    "I look in the mirror. I'm met with rosy and plump cheeks. My hair is short, brown, and curly."
    "Clue number two."
    show d oh
    mc "Ah. So it does happen."
    "Isekai: A genre where the main character gets transported to another world, usually through death."
    show d neu
    mc "(I don't remember dying. I only remember falling asleep.)"
    mc "Perhaps…"
    show d a
    "I mutter to myself. I frown. There is a hint of disappointment. If I was going to be isekai'd…"
    mc "(I wanted to be hit by a truck.)"
    "Well, you can't pick and choose."
    show d neu
    "I set the mirror down next to me and pick up one of the scones. I slather a healthy amount of jelly on it and start to eat."
    "It would seem that I am now living in the world of 'My Magical Kindness Made the Cold Prince Fall in Love!!' Not my first choice."
    "I'm in the role of villainess. Also not ideal. In the many, many manhwa I've consumed, the villainess never gets the happy ending."
    show d pout sad
    "I pout, taking another bite of my food. I look over at the maid."
    mc "Where are we?"
    m "Excuse me?"
    show d neu
    "I speak again."
    mc "Where are we?"
    "The maid tries and fails to not look too concerned."
    m "The castle…"
    show d oh
    mc "Oh!"
    "My eyes widen as I pinpoint where in the story I was transported to."
    "My character, the villainess, is engaged to the love interest, Lewis. The heroine of the story, Otillia, has just started to study at the castle."
    show d pout sad
    "I sigh to myself, finishing my food."
    show d neu
    m "Are… Are you ready to be dressed, my lady?"
    "I nod and set the tray on the bed. I get up and get dressed with the maid's help."
    m "My lady…are you all right?"
    mc "Hmmm?"
    "I look over at her."
    mc "Oh, yes. I suppose breakfast has me feeling sluggish."
    m "The food wasn't to your liking again? I can inform–"
    show d ss
    mc "That's not it."
    "I wave her off, giving her a smile."
    mc "I guess I'm left wanting more."
    scene
    "I decide not to dwell on it. After I'm dressed, the maid leads me out into the common room."
    "She says nothing more, but it's obvious that she doesn't trust my word."
    scene bg tearoom day with fade
    "The common room is just as elaborate as my bedroom, if not more." #WIP: [mcname]
    "The first thing I notice is a large bookshelf sprawling the length of one wall. A heavy dark oak table is surrounded by velvet couches and chairs. Behind it are windows with thick red curtains that have been opened to let in the morning light."
    "A man sits in the padded chair at the head of the table. There's food laid out in front of him. All of it untouched."
    show white with fade #WIP: Lewis CG
    nvl show
    narr "Lewis, the love interest of the manhwa."
    narr "He was popular among readers due to his older age. And I have to say that he is much more handsome in real life."
    narr "A soft complexion, long hair with gray streaks, glasses that rest gently on his nose, and tied together with a stern expression…"
    narr "Megane: A character with glasses. Oftentimes, male megane are seen as stoic and aloof."
    nvl hide
    nvl clear
    l "Oh, you're awake. Good morning."
    scene bg tearoom day
    show d n b at left with dissolve
    show l neu at right with dissolve
    "I just stare at him. It takes me a minute to realize he's talking to me."
    show d sb
    mc "G-good morning…"
    "Wait, how do I address him?"
    "Sir? My lord? Prince?"
    "I try to remember how the villainess addressed him in the manhwa."
    show d neu
    mc "Lewis."
    show l nerve
    l "All right then…"
    "He clears his throat awkwardly."
    show l neu
    l "Do sit."
    mc "Right."
    "I sit across from him. My eyes keep flickering from him to the food in front of me."
    show d fc
    "There is even more delicious looking food than what I got this morning. I\’m practically drooling once again."
    "Lewis picks up a newspaper and starts reading. He only stops to drink coffee from his cup."
    show d fbb
    "All that food…untouched."
    "I can’t hold back anymore."
    show d n b
    mc "Are you hungry?"
    "Lewis lowers his paper, his eyebrow raised."
    show l nerve
    l "Hmm?"
    mc "You’re not eating."
    "Lewis gives me an odd look before clearing his throat."
    show l neu
    l "I am not hungry."
    menu:
        "Then can I eat?":
            jump choice1_eat
        "You need to eat breakfast. It's the most important meal of the day.":
            jump choice1_important


label choice1_eat:
    show l shock
    "Lewis gives me an even weirder look."
    "It's as if I’d grown two heads."
    show d sb
    mc "What is it? Why are you looking at me like that?"
    l "Because you never cared for food before."
    show d oh
    "I blink."
    "That’s right. I’m not me anymore. I’m the villainess."
    "But food is food."
    show d ss
    "I shrug and give him a smile."
    mc "I've simply had a change of heart."
    show l an
    "Lewis sighs, going back to his newspaper."
    l "Go ahead. I do not mind."
    show d ls
    mc "Yay!!"
    "I take a croissant, nibbling happily on it."
    jump choice1_done


label choice1_important:
    show l nerve
    l "And…why do you care?"
    show d oh
    "The question catches me off guard. It’s not said in a rude way–it's more genuine confusion."
    show d ss
    mc "We’re engaged, aren’t we? As your fiance, I need to make sure you’re taking care of yourself."
    "Lewis stares at me. And he keeps staring."
    "I stare back."
    show l neu
    "After a moment, he just shakes his head and sighs."
    show d pout upset
    mc "I’m guessing that’s a no?"
    l "You’d guess right."
    "I pout slightly and lean forward, taking a croissant in my hand."
    mc "Suit yourself."
    jump choice1_done


label choice1_done:
    scene bg tearoom day
    nvl show
    narr "Lewis sips on his coffee, not paying me any attention. I use the time to think about how I should go about this whole villainess thing."
    narr "The manhwa was fairly new and I had read all available episodes."
    narr "When [mcname] showed up in the story, she was cruel from the get go. Stubborn, violent, and selfish, she was hated in the fandom."
    narr "I don't want that. And I don't want whatever death flags the author had planned."
    narr "Death flags: An element in a story used to foreshadow a character's imminent death or downfall."
    narr "Was this even worth it?"
    narr "I think back on my past life. It wasn't anything special."
    narr "Though, I suppose the criteria for being isekai'd is being unremarkable and then starting a new life."
    narr "I am…was a normal office worker. Not a manager, just someone who stayed mediocre."
    narr "Despite that, I was overworked. I found myself eating mediocre instant ramen from the convenience store."
    narr "At night, I would get my fill of delicious food while reading manhwa and manga."
    narr "Now that I think back on it, my life was kind of pathetic. Sure, I enjoyed the nights I had, but my life as a whole wasn't fulfilling."
    nvl hide
    nvl clear
    "I look down at the table, the plates cleared of food and my stomach happy."
    show d ls at center with dissolve
    mc "(Yeah. This is way better.)"
    l "[mcname]."
    show d fbb
    "Here, I can live for myself. I can eat all the delicious food and not be tied down by anything."
    "Not even the title of villainess. Although it would be a shame if I die again because of it."
    "I sigh happily and pick up a cream puff."
    show l neu at right with dissolve
    show d oh at left with move

    l "[mcname]!"
    "I'm knocked out of my thoughts as I look up at Lewis."
    mc "Sorry, sorry. What is it?"
    show l nerve
    "His eyebrows furrow once again as he leans forward."
    l "You've been acting odd."
    mc "Odd?"
    l "The [mcname] I know would currently be talking about the gossip she’s been hearing around the castle."
    "I shake my head slightly and wave my hand dismissively."
    show d ss
    mc "I'm not interested in petty gossip."
    show d sb
    show l shock
    "The room is filled with gasps. I look around, confused."
    "The castle staff and Lewis are all staring at me in shock."
    show d oh
    mc "Did I… Did I say something wrong?"
    show maid at offscreenright
    show maid at center with move #Maid Sprite
    show l shock
    "The maid shakily points at me, her face filled with fear."
    m "Who are you and what have you done with [mcname]?"
    show d gloom
    "Oh, right."
    "[mcname] loved gossip and spreading rumors. It eventually made a rift between her and Lewis."
    show d neu
    "I quickly try to cover my words."
    "Before I can speak, the maid talks once again."
    m "My lord, she's been acting odd since she woke up. She's been eating food she normally doesn't and has been acting more…"
    "She looks over at me, as if fearful of my reaction."
    m "More docile."
    show l an
    "Lewis sighs and pinches the bridge of his nose."
    l "I do not have time for this."
    show l a
    "He scowls at me."
    l "Otillia is visiting soon. Be ready by then."
    show l at offscreenright with move
    show maid at right with move #WIP: Maid Sprite
    "Without another word, he gets up and exits the room."
    "I turn towards the maid, the uneaten cream puff in my hand."
    show d fbb
    mc "Could you possibly ask the chef if there are any more croissants? They were delicious."
    m "Yes, my lady."
    hide maid with dissolve
    show d neu at center with move
    "She stares at me one last time before making her way to the kitchen. I start eating the cream puff, letting my thoughts come together."
    "In the manhwa, Otillia and [mcname]'s meeting was basically the start of the main plotline."
    "The original [mcname] was rude towards Otillia, despite her prowess in magic and being personally trained by the head mage."
    "She laughed in Otillia's face and made fun of her aspirations."
    show d gloom
    mc "(Classic villainess.)"
    "Lewis ended up defending Otillia. She was touched and that's when they started to get closer."
    mc "If I can just avoid this first flag…I should be in the clear."
    "It's not like I don't want them to end up together. I just want to live and not suffer the fate of every manhwa villainess."
    show d neu
    "When I'm about to formulate a plan, I hear hushed whispering from the corner."
    scene cg cenric #WIP: Cenric CG
    "I look towards the source of the noise and see the maid and a man in a chef's uniform conversing with each other."
    "The man is tall and big, with fluffy blonde hair and a slightly chubby face."
    "Cute."
    "With a confused and slightly concerned smile, I nod in their direction."
    "Both of them walk over to me. The chef bows deeply, not making eye contact."
    scene bg tearoom day
    show d neu at left
    show c puppy lookDown at right
    c "My lady… I'm Cenric. The head chef."
    menu:
        "Your food is absolutely delicious!":
            jump choice2_delicious
        "It's a pleasure to meet you, Cenric!":
            jump choice2_pleasure


label choice2_delicious:
    show c smile lookDown:
    "Cenric straightens, his face lit up in a smile. His cheeks are a dark red."
    c "Th-thank you, my lady."
    mc "(He looks like a cute golden retriever.)"
    "Golden Retriever: A character that highly resembles a golden retriever. Often kind, blond, and a bit stupid."
    c "I w-wanted to personally see what else you would like to eat."
    c "I know you said you wanted croissants but…I can make you anything if you please."
    "My eyes immediately shine at the thought. As soon as I open my mouth, a flood of requests starts pouring out."
    mc "Anything? Can you make doughnuts? Crepes? Curry? Hamburg steak? Stew? Parfaits? Oooh! There's so many options!!"
    "Cenric looks surprised but smiles happily."
    c "Anything you wish, my lady."
    "I take a second to think."
    "This is a big decision. The ultimate power: the ability to have any type of food made for me."
    "Well, mostly any type. I doubt I could get something like tteokbokki here."
    "I gasp as I suddenly think of one of my favorite comfort foods."
    mc "Since Otillia is visiting, can you make some tea and foods to go along with it? And be sure to include strawberry shortcake."
    c "As you wish, my lady."
    hide c with dissolve
    show d neu at center with move
    "Cenric bows his head, that same goofy grin on his face. He turns and makes his way back to the kitchen."
    "I smile and mutter to myself."
    mc "So adorable."
    jump choice2_done

label choice2_pleasure:
    c "It's rare for someone to come back for more food."
    "He still avoids eye contact, bowing deeply."
    "I give him a gentle smile."
    mc "It was quite delicious. I wanted you to make some more so I can share with Lewis when he gets back."
    c "Do you have anything in mind?"
    "I think for a second. If Otillia will also be visiting, it would be wise to set an inviting atmosphere."
    "This could work."
    mc "Well, since Otillia is also visiting, could you please prepare tea and some finger foods for us?"
    c "Any specifics?"
    mc "Hmmm…"
    "For some reason, the sight of Lewis not eating fills my mind."
    mc "Something that Lewis would like."
    c "Of course, my lady."
    hide c with dissolve
    show c neu at center with move
    "With another bow, he makes his way back to the kitchen."


label choice2_done:
    "Since I'm alone–"
    "I look over to the maid standing in the corner."
    "Well, relatively alone, I'll take this time to look around."
    "It's so odd and very surreal being in a place that was fictional before."
    "I walk around the tea room, taking in every bit of detail. Fantasy manhwa tend to have a lot of detail and 'My Magical Kindness Made the Cold Prince Fall in Love!!' was no exception."
    "Everything is elegant and just screams royalty. Not to mention…glittery. Why is everything so glittery?"
    mc "It's like I'll be blinded."
    "I touch a vase with gold accents, watching as it glints in the sunlight."
    "To think I would ever end up in a place like this. It makes me wonder about my old life."
    "Did people even know that I died? Would they even care? What about–"
    mc "What about the food in my fridge? It'll spoil. Such a waste."
    scene cg otilla
    "I can hear more voices getting closer to the room. I turn and see Lewis, Otillia, and the grand mage."
    mc "Woah."
    "Otillia is even more gorgeous in person. Golden locks fall across her shoulders, looking as smooth as silk. She has a rosy complexion, her blue eyes crystal clear."
    "She's the typical heroine, except her beauty puts her above others. This is when it sets in that I truly am inside a manhwa."
    scene bg tearoom day
    show o neu at right
    show d neu at left
    "I grin, walking over to them. I curtsy, my eyes meeting hers."
    mc "It's a pleasure to meet you, Miss Otillia. I am Lady [mcname], but please, call me [mcname]."
    o "O-oh!"
    "Otillia's eyes widen. Just for a second, she hesitates before returning the curtsy."
    "It must be a surprise. [mcname]'s reputation was already less than ideal from the get go. Besides the rumors she spread, she was known to be mean-spirited."
    "What's supposed to happen at this point is that [mcname]…or I am supposed to scoff and make fun of her background. I call her a wannabe noble that has no true talent and will only end up as trash."
    "Lewis would then immediately come to Otillia's aid and scold [mcname], calling her bitter and jealous."
    mc "(Yikes.)"
    "Since I don't want to see my doom, I take the obvious route."
    mc "Thank you so much for coming over!! I've heard all about your gift, Miss Otillia."
    "Otillia smiles, albeit awkwardly."
    o "It's a pleasure to meet you as well, Lady [mcname]."
    mc "Oh, please. Call me [mcname]. It's fine, I promise."
    mc "Come, sit."
    "I guide her over to the couch. We both sit as the grand mage and Lewis sit across from us. I take a deep breath. Doing good so far."
    mc "Please, tell me about your studies so far. I have never met someone with powerful magic before."
    "Otillia smiles, looking a bit cautious. It's best if I'm not too enthusiastic or it would seem like I'm scheming up a plan."
    o "Oh, it's not much. It's just light magic. Healing… I'm not special."
    "The grand mage shakes her head."
    hide d
    show o neu at left with move
    show l neu at right
    show noble at center
    gm "Light magic is the rarest form of magic. Not to mention your healing powers are quite exceptional. You are like a gift from the gods."
    "Despite looking uncomfortable, Otillia blushes, looking down into her lap."
    o "I wouldn't say that much."
    l "Healing magic, you say?"
    "I look over at Lewis. In the story, he had Otillia attempt to heal his brother. Unfortunately, the disease he had was already too far along, and Lewis ended up taking the throne."
    o "I've been practicing, but it still drains a lot out of me. I won't be useful for a while."
    hide noble
    show d neu at center with dissolve
    "I shake my head, laughing slightly."
    mc "That's all right. I don't think anyone is in a rush to have you go out and do some healing."
    "She seems to finally relax as she nods."
    o "Thank you for saying that, my lady."
    l "By the way, I wanted to ask about–"
    hide o
    show c conf at left with dissolve
    "Lewis's words are interrupted by Cenric entering the room. He's rolling a cart filled with tea and snacks. My eyes immediately light up."
    "Lewis looks surprised before sighing and glancing over at me."
    l "[mcname], what is this?"
    mc "I asked Cenric to make us some snacks!"
    "I squeal, standing up as Cenric positions the cart near the table. Lewis' expression turns into a scowl."
    l "Good lord, [mcname]. This is practically enough for a party! Why did you do this?"
    menu:
        "Because I wanted to eat more of Cenric's cooking.":
            jump choice3_eatmore
        "You need to appreciate Cenric's cooking more.":
            jump choice3_appreciate

label choice3_eatmore:
    "Cenric blushes and then bows his head."
    c "You're too kind, my lady."
    mc "It's true!"
    "I then motion towards Otillia."
    mc "Come! You must taste his cooking. It's absolutely divine."
    l "I don't think it's entirely appropriate–"
    mc "Oh, shush. We have guests. We can't have them hungry."
    hide l with dissolve
    show o flust at right with dissolve
    "Otillia walks over, her eyes scanning all the options."
    mc "Pick whatever you'd like."
    "She settles on a pink macaron filled with some type of jelly. She takes a small bite. Then she takes a bigger one, popping the whole thing in her mouth."
    o "This is delicious!"
    "Cenric chuckles, rubbing the back of his head sheepishly."
    c "It's not my best, but I appreciate your words."
    "I click my tongue, giving him a mock stern look."
    mc "You need to have more confidence in yourself. Anyone would be lucky to have your food."
    "Cenric doesn't say anything and looks away. His face is almost completely red."
    "I bite back a giggle and then turn to the food, grabbing some for myself. Lewis sighs and rolls his eyes."
    l "Anyway, back to the topic at hand."
    jump choice3_done

label choice3_appreciate: #WIP: Set transforms to show all 4 sprites on-screen at once
    "Lewis scoffs, rolling his eyes. I walk over to him and tug on his sleeve."
    mc "Come on."
    l "[mcname]…"
    "I don't listen and drag him over to the cart. I point towards the food."
    mc "Go on. Choose one."
    l "I don't want to."
    mc "As your fiance, I command you."
    "He snorts and raises an eyebrow, crossing his arms."
    l "There's the [mcname] I'm used to."
    l "Fine, I'll do it."
    "He looks over the food for a moment. He seems uninterested and grabs a small tart. He bites into it and then shrugs."
    l "It's all right. Nothing special."
    "I turn towards Cenric and see his face fall. I turn back towards Lewis and frown. Can someone really be this apathetic towards food?"
    hide c with dissolve
    show o neu at left with move
    mc "Don't be rude. Cenric worked hard."
    l "Food isn't necessarily something I need to worry about. We're here for a meeting, not your hunger."
    "The words almost make me angry. I roll my eyes. This would be an issue to solve later."
    mc "Suit yourself."
    "I smile towards Otillia and the grand mage."
    mc "Please, come eat."
    "Everyone shuffles in to get food. Lewis tries to keep the conversation on track."
    jump choice3_done

label choice3_done:
    "We all sit with our plates, the conversation flowing easily between one another. The attention is on Otillia and her upbringing."
    "I never thought I'd be in a position like this. It seems so surreal that I'm in a pretty and glittering dress while talking to the two most important people in the kingdom."
    "At first, I was worried I would feel out of place. But I am genuinely having a good time. I feel like I have settled in, if only for now."
    "I just need to avoid becoming a villainess."
    o "Well, I'm no one to celebrate."
    mc "What? Of course you are! You faced a hard childhood and look at you now. Studying directly under the grand mage. That deserves a party."
    "Otillia giggles, covering her face."
    o "Oh, please. You and Prince Lewis have been the talk of the town since your engagement."
    "Lewis's face turns red, and I smirk slightly."
    mc "(Right. Engaged.)"
    o "You know, it would be great to have a ball!"
    "Lewis looks at her curiously."
    l "A ball?"
    "She nods, a sudden glint in her eye."
    o "You two haven't had an engagement party, correct?"
    "I nod before glancing over at my fiance."
    mc "He isn't one for parties."
    l "I'm too busy."
    mc "(And introverted.)"
    "Like I'm one to talk. I spent my nights reading manhwa. Not exactly party animal material."
    o "How can you expect to be king if you can't organize balls?"
    "Lewis opens his mouth then shuts it. Otillia's smile is bright as if she just won a prize."
    o "It's settled! I'll leave the planning to you two!"
    "There isn't much room for discussion. Otillia quickly changes the subject and refuses to let it circle back to the party. After a while, both her and the grand mage depart."
    "I sit back in my chair, sipping on some tea. I think that went well. Well enough to form a good relationship with Otillia and not be blasted away by light magic."
    mc "(Victory!)"
    l "[mcname]?"
    mc "Hmm?"
    "I look over at Lewis. He's staring straight at me as if he's studying a painting."
    l "I am truly concerned for you. You aren't acting like your normal self."
    mc "Would you rather I be cruel and rude?"
    l "No, but–"
    mc "Then there is no problem."
    "That shuts him up. He exhales, rubbing the bridge of his nose."
    l "You do know I have no time to be throwing parties. I am to be crowned king soon. I need to spend more time focusing on that."
    return
