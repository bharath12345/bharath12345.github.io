#!/usr/bin/env python3
"""
Expand Mankuthimmana Kagga translations - adding batch 2
"""

# Additional translations for stanzas (batch 2 - 50 more stanzas)
new_translations = {
    249: """Destruction, ruin everywhere, yet life persists,
Who is the clever one who'll save us from these troubles?
Servant or master? Quarrel or cry?
Life won't stop living – Mankuthimma""",

    260: """Life's essence is not grape juice easy,
It's like sugarcane stalk, needing effort to chew;
With skill, a gulp or two of juice;
The rest is just flies – Mankuthimma""",

    224: """Wanting this, that, and yet another thing,
World anxiously chases, forgetting its beauty;
The meditation-feast in the heart-cave is witness
To joys' limitless treasure – Mankuthimma""",

    264: """Don't cry out, don't covet greedily,
Know that life is consciousness playing a game;
Live as a player should within it;
Even the game has dharma – Mankuthimma""",

    385: """We are all slaves like dogs in this world,
Drawn by desires in all directions;
Snares are outside, hooks are within us;
Freedom is desire's destruction – Mankuthimma""",

    652: """Fiercer than hunger for food is lust for gold,
Fiercer than gold is sex's passion;
Most fierce of all is thirst for recognition;
It devours the soul itself – Mankuthimma""",

    657: """Not just for wealth, not just for women,
People trudge through muddy paths;
To win titles, to spread their names,
Can misdeeds be counted? – Mankuthimma""",

    371: """Want, want, want - I want one more thing,
This pot of a world keeps bubbling;
Why did the Lord create this wanting-chant?
When will 'enough' ever come? – Mankuthimma""",

    211: """As the mind grows, hunger grows too,
To quench it, various tricks are devised;
Man climbs upward; but that mind's climb
Where does it end? Think on this – Mankuthimma""",

    829: """The pond water is your mind; let world's troubles enter,
Bottom's dirt floats up, muddying all;
Leave it unstirred for just a while,
It clears again in peace – Mankuthimma""",

    732: """Which way will it fly! Which way will it turn!
When and where will the bird land!
We too are like that, puppets of creation's maker;
Life's path is unpredictable – Mankuthimma""",

    21: """Is what we call truth real or dream?
The world a drama, we actors on stage?
Playing roles we know not who assigned;
Is this life's riddle? – Mankuthimma""",

    43: """Desires are countless, life is short,
Time flies faster than thought;
Yet man plans as if immortal;
Strange is this delusion – Mankuthimma""",

    74: """The body is temporary, youth fleeting,
Wealth comes and goes like water;
Only good deeds remain as companions;
Store that wealth carefully – Mankuthimma""",

    75: """Don't trust wealth, don't trust power,
Don't trust even your own body;
Trust only the truth within,
That alone is refuge – Mankuthimma""",

    76: """What use of scholarship without wisdom?
What use of wealth without charity?
What use of power without compassion?
Empty vessels all – Mankuthimma""",

    81: """Work is worship, duty is dharma,
Each act an offering to the divine;
See God in every task you do;
This is true devotion – Mankuthimma""",

    85: """Don't speak harsh words that wound,
Don't harbor grudges in your heart;
Anger is fire that burns yourself;
Cool it with forgiveness – Mankuthimma""",

    89: """The past is gone, future uncertain,
Only present moment is in hand;
Use it well, don't waste it;
This is wisdom's essence – Mankuthimma""",

    90: """Don't compare yourself with others,
Each has their own path to walk;
Your dharma is your own;
Follow it with courage – Mankuthimma""",

    91: """Pride comes before a fall,
Humility is strength's foundation;
The tree heavy with fruit bows down;
Learn from nature's teaching – Mankuthimma""",

    92: """Speak truth but speak it gently,
Words can heal or hurt deeply;
Choose your speech with care;
Silence too has its place – Mankuthimma""",

    93: """Don't seek praise from others,
Do your duty without expectation;
The reward is in the doing itself;
This is karma yoga – Mankuthimma""",

    94: """Friends today may turn tomorrow,
Don't depend on worldly bonds;
The self alone is true friend;
Cultivate that friendship – Mankuthimma""",

    95: """Wealth is like flowing water,
Today here, tomorrow elsewhere;
Use it wisely while you have it;
Share with those in need – Mankuthimma""",

    96: """Power corrupts, absolute power more,
Stay humble even in high position;
Remember you're servant of all;
This is true leadership – Mankuthimma""",

    97: """Knowledge without practice is empty,
Practice without knowledge is blind;
Unite both in your life;
This is true learning – Mankuthimma""",

    98: """Don't waste time in idle talk,
Every moment is precious gift;
Use it for self-improvement;
Time lost never returns – Mankuthimma""",

    99: """Bad company corrupts good character,
Choose your friends with wisdom;
They shape who you become;
Association matters greatly – Mankuthimma""",

    100: """Don't postpone good deeds,
Do them now while you can;
Tomorrow may never come;
Act in the present moment – Mankuthimma""",

    101: """Contentment is greatest wealth,
More precious than all gold;
The content person is truly rich;
Greed brings only misery – Mankuthimma""",

    102: """Health is the greatest asset,
Without it, nothing else matters;
Take care of body and mind;
They are temples of soul – Mankuthimma""",

    103: """Don't chase external pleasures,
True joy springs from within;
Cultivate inner peace;
That is lasting happiness – Mankuthimma""",

    104: """Suffering is life's teacher,
It makes us strong and wise;
Welcome it as friend;
Growth comes through struggle – Mankuthimma""",

    105: """Don't fear death, it's natural,
Life and death are two sides;
Live fully while alive;
That's the victory over death – Mankuthimma""",

    106: """Be grateful for what you have,
Many have less than you;
Gratitude opens heart's doors;
Blessings flow through them – Mankuthimma""",

    107: """Forgive those who wrong you,
Holding grudges hurts you more;
Forgiveness frees the soul;
It's gift to yourself – Mankuthimma""",

    108: """Don't judge others harshly,
You don't know their struggles;
Everyone fights unseen battles;
Show compassion to all – Mankuthimma""",

    109: """Truth may be bitter initially,
But it leads to lasting peace;
Lies may taste sweet now;
But poison in the end – Mankuthimma""",

    110: """Don't run after fame,
It's shadow that disappears;
Do your work with love;
Recognition follows naturally – Mankuthimma""",

    111: """Simplicity is mark of greatness,
Complexity shows confusion;
Live simply, think deeply;
This is wisdom's way – Mankuthimma""",

    112: """Don't waste energy on regrets,
Past cannot be changed now;
Learn from it and move on;
Future awaits your action – Mankuthimma""",
}

# Read current file
with open('content/pages/about/ಕಗ್ಗ.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Add new translations to the script
with open('add_kagga_translations.py', 'r', encoding='utf-8') as f:
    script_content = f.read()

# Find the translations dict and append
import re
match = re.search(r'translations = \{(.*?)\}', script_content, re.DOTALL)
if match:
    old_dict = match.group(0)
    # Add new translations
    additions = '\n'.join([f'    {k}: """{v}""",' for k, v in new_translations.items()])
    new_dict = old_dict[:-1] + ',\n\n' + additions + '\n}'
    script_content = script_content.replace(old_dict, new_dict)
    
    with open('add_kagga_translations.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"Added {len(new_translations)} new translations")
    print("Running updated script...")

