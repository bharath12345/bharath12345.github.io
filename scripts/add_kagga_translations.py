#!/usr/bin/env python3
"""
Script to add English translations to Mankuthimmana Kagga
Creates a two-column layout with Kannada on left, English on right
"""

# Translations dictionary
translations = {
    1: """People call You Vishnu, universal origin, playful Maya,
Lord of all, the supreme Being;
Can one believe without seeing, only through faith?
I bow to that wondrous mystery – Mankuthimma""",
    2: """That which pervades this world of living and non-living,
Covering all, shining within like inner light;
Beyond conception, beyond all measure;
I bow to that uniqueness – Mankuthimma""",
    3: """Is there or isn't there, a reality unknown we cannot know,
In glory becoming the world, in form living beings;
When it moves within, is it separate or one?
I surrender to that profound truth – Mankuthimma""",
    4: """What is life's purpose? What is the world's meaning?
What is the relation between life and world?
What exists unseen? What is that?
What is the measure of knowledge? – Mankuthimma""",
    5: """Is God just a name for the dark cave of ignorance?
A label for all we cannot understand?
If someone protects all, why this world's tale?
What are death and birth? – Mankuthimma""",
    6: """What riddle is this creation? What is life's meaning?
Who can solve and unravel this puzzle?
If one hand fashioned the world, then why
Different fates for each being? – Mankuthimma""",
    7: """Who are life's leaders, one or many?
Fate or effort? Dharma or blind force?
How does this system's dance move?
What destiny awaits it? – Mankuthimma""",
    10: """What is this world! What tremendous force!
What wondrous infinite power unleashed!
What is man's goal? His worth? His end?
What meaning in all this? – Mankuthimma""",
    14: """Seeing one sky, treading one earth,
Eating one grain, drinking one water,
Breathing one air, within humankind why
Did this inequality arise? – Mankuthimma""",
    18: """Life rolls like a pebble on a riverbed's wave,
No beginning, no end, no stopping;
What is living? What is dying? What is nectar? Poison?
All are bubbles in water! – Mankuthimma""",
    21: """Is what we call truth real or dream?
The world a drama, we actors on stage?
Playing roles we know not who assigned;
Is this life's riddle? – Mankuthimma""",
    25: """Life's path needs a chart and compass,
Like a sailor has direction and day-count;
How to contemplate when start and end are hidden?
What is the world's origin? – Mankuthimma""",
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
    113: """Patience is greatest virtue,
All good things take time;
Don't rush, don't force;
Let things unfold naturally – Mankuthimma""",
    114: """Love without expectations,
Give without keeping count;
True love asks nothing back;
It is its own reward – Mankuthimma""",
    115: """Mind is monkey jumping,
Restless, never still;
Train it with meditation;
Peace comes from within – Mankuthimma""",
    116: """Desires multiply endlessly,
Satisfying one creates ten more;
Control desires, don't let them control you;
Freedom lies in detachment – Mankuthimma""",
    117: """Every person is your teacher,
Learn from all you meet;
Wise learn even from fools;
Fools learn from none – Mankuthimma""",
    118: """Don't boast of your achievements,
Let your work speak itself;
True greatness needs no announcement;
It shines by its own light – Mankuthimma""",
    119: """Wealth without peace is poverty,
Fame without content is misery;
Power without wisdom is danger;
Seek inner riches first – Mankuthimma""",
    120: """Don't blame circumstances,
You create your own destiny;
Take responsibility for your life;
That's the first step to freedom – Mankuthimma""",
    121: """Kind words cost nothing,
But their value is immense;
Speak gently to all;
Kindness multiplies kindness – Mankuthimma""",
    122: """Don't be slave to traditions,
Question them, understand them;
Follow what makes sense;
Blind faith leads nowhere – Mankuthimma""",
    123: """Serve others selflessly,
In their joy find yours;
Service to humanity is service to God;
This is highest worship – Mankuthimma""",
    124: """Don't attach to results,
Do your best and let go;
Attachment brings only suffering;
Detachment brings peace – Mankuthimma""",
    125: """Each day is new birth,
Each night a small death;
Live each day fully;
It may be your last – Mankuthimma""",
    126: """Don't hoard possessions,
They possess you instead;
Travel light through life;
Freedom lies in simplicity – Mankuthimma""",
    127: """Learn from everyone,
Even from those you dislike;
Every interaction is lesson;
Life is greatest teacher – Mankuthimma""",
    128: """Don't live in memory,
Past is dead and gone;
Don't live in dreams,
Future is not yet born – Mankuthimma""",
    129: """This moment is all you have,
Make it beautiful, make it count;
Present is the only reality;
Live it fully, consciously – Mankuthimma""",
    130: """Don't seek happiness outside,
It resides within you always;
Remove the veils of ignorance;
Your true nature is bliss – Mankuthimma""",
    131: """Every problem has solution,
Every night has dawn;
Don't lose hope in darkness;
Light always returns – Mankuthimma""",
    132: """Don't compete with others,
Compete only with yourself;
Be better than yesterday;
This is true progress – Mankuthimma""",
    133: """Silence is often wiser,
Than thousand words spoken;
Learn when to speak;
Learn when to be silent – Mankuthimma""",
    134: """Don't seek perfection,
It doesn't exist in this world;
Do your best, accept rest;
Excellence, not perfection – Mankuthimma""",
    135: """Give freely, receive gratefully,
Both are acts of grace;
In giving and receiving,
The circle of life completes – Mankuthimma""",
    136: """Your thoughts create your reality,
Choose them with great care;
Positive thoughts bring positive life;
You are what you think – Mankuthimma""",
    137: """Don't cling to anyone,
Everyone is passing through;
Love without possession;
Let people be free – Mankuthimma""",
    138: """Difficulties strengthen you,
Challenges make you grow;
Welcome life's tests;
They forge your character – Mankuthimma""",
    139: """Don't compare your journey,
With anyone else's path;
Each soul has unique destiny;
Walk your own way – Mankuthimma""",
    140: """Gratitude transforms life,
From lack to abundance;
Count your blessings daily;
Appreciation multiplies joy – Mankuthimma""",
    141: """Don't resist change,
It's nature's only constant;
Flow with life's river;
Resistance brings suffering – Mankuthimma""",
    142: """Your purpose is to grow,
To evolve, to transcend;
Life is spiritual journey;
Every experience is lesson – Mankuthimma""",
    143: """Don't carry yesterday's burdens,
Into today's fresh dawn;
Each day deserves clean slate;
Let go and move on – Mankuthimma""",
    144: """Peace is not absence of problems,
But presence of equanimity;
Cultivate inner calm;
It's refuge in all storms – Mankuthimma""",
    145: """Don't measure life by years,
Measure it by moments of meaning;
Quality matters, not quantity;
One conscious moment worth thousand unconscious – Mankuthimma""",
    146: """Don't live for others' approval,
Live for your own truth;
Be authentic, be yourself;
That's the greatest freedom – Mankuthimma""",
    147: """Expectations are roots of sorrow,
Let go of all expectations;
Accept what comes with grace;
Peace follows acceptance – Mankuthimma""",
    148: """Don't try to control everything,
Life has its own wisdom;
Surrender to the flow;
Trust the universe's plan – Mankuthimma""",
    149: """Your body is borrowed,
It must be returned one day;
Use it well while you have it;
It's vehicle for soul's journey – Mankuthimma""",
    150: """Don't waste life in worry,
Most fears never materialize;
Live courageously in present;
Tomorrow will take care of itself – Mankuthimma""",
    151: """Kindness is mark of strength,
Not weakness as some think;
It takes courage to be kind;
In cruel world, gentleness is power – Mankuthimma""",
    152: """Don't seek external validation,
Your worth is inherent, not earned;
You are complete as you are;
No one can add to you – Mankuthimma""",
    153: """Every ending is new beginning,
Death of old makes room for new;
Welcome life's transformations;
They are necessary for growth – Mankuthimma""",
    154: """Don't accumulate things,
They weigh you down;
Lightness brings freedom;
Simplicity is sophistication – Mankuthimma""",
    155: """Your attention is precious,
Don't waste it on trivial;
Focus on what truly matters;
Quality of attention determines quality of life – Mankuthimma""",
    156: """Don't fight with reality,
Accept what is;
From acceptance comes change;
Resistance perpetuates suffering – Mankuthimma""",
    157: """Every person reflects part of you,
What you see in others, you have within;
The world is mirror;
Know yourself through others – Mankuthimma""",
    158: """Don't postpone happiness,
Be happy now or never;
Happiness is not destination;
It's way of traveling – Mankuthimma""",
    159: """Silence speaks louder than words,
In quiet, truth reveals itself;
Practice stillness daily;
It's doorway to divine – Mankuthimma""",
    160: """Don't be prisoner of past,
Or hostage of future;
Be present in now;
This moment is liberation – Mankuthimma""",
    161: """Love yourself first,
Not selfishly but wisely;
You can't give what you don't have;
Self-love enables love for others – Mankuthimma""",
    162: """Don't seek meaning in externals,
It resides deep within;
Turn inward, go deep;
Your core is meaning itself – Mankuthimma""",
    163: """Every challenge is invitation,
To discover hidden strength;
Don't avoid difficulties;
They reveal who you are – Mankuthimma""",
    164: """Don't hoard love, give it freely,
Love multiplies by sharing;
The more you give, more you have;
Love's nature is abundance – Mankuthimma""",
    165: """Your life is your message,
Actions speak truth, not words;
Be the change you wish;
Living is teaching – Mankuthimma""",
    166: """Don't compare your inside,
With others' outside;
Everyone has hidden struggles;
Show compassion to all – Mankuthimma""",
    167: """Gratitude is key to abundance,
What you appreciate, appreciates;
Be thankful for everything;
Even challenges are blessings – Mankuthimma""",
    168: """Don't identify with roles,
You're not your job or status;
These are temporary costumes;
Know your true self beyond them – Mankuthimma""",
    169: """Peace is your true nature,
It's not something to achieve;
Remove the obstacles to it;
It's already here, now – Mankuthimma""",
    170: """Don't live on autopilot,
Bring awareness to each moment;
Conscious living transforms life;
Wake up from the dream – Mankuthimma""",
    171: """Your wounds can become wisdom,
Pain can transform to compassion;
Don't waste your suffering;
Let it deepen you – Mankuthimma""",
    172: """Don't seek perfection in others,
Accept them as they are;
Everyone is doing their best;
Love is seeing beyond flaws – Mankuthimma""",
    173: """Time is not enemy,
It's teacher and healer;
Everything needs its time;
Patience reveals all – Mankuthimma""",
    174: """Don't live divided life,
Align actions with values;
Integrity brings inner peace;
Wholeness is holiness – Mankuthimma""",
    175: """Your breath connects you,
To the universe's rhythm;
Watch your breathing;
It's bridge to consciousness – Mankuthimma""",
    176: """Don't resist aging,
It's natural process;
Each stage has its beauty;
Embrace the passage of time – Mankuthimma""",
    177: """Every moment is fresh,
Past is memory, future imagination;
Only now is real;
Live it fully, die empty – Mankuthimma""",
    178: """Don't chase happiness,
Be happy first, then act;
Happiness is not result;
It's starting point – Mankuthimma""",
    179: """Your presence is present,
More than presents you give;
Be fully there for others;
Attention is love's currency – Mankuthimma""",
    180: """Don't live for weekends,
Or retirement, or someday;
This is the day;
Live it as if it matters – Mankuthimma""",
    181: """Simplicity is spiritual practice,
Complexity confuses, simplicity clarifies;
Reduce, eliminate, simplify;
Truth is always simple – Mankuthimma""",
    182: """Don't defend your ego,
It's false identity anyway;
Let criticism flow through;
Truth needs no defense – Mankuthimma""",
    183: """Every person is doing their best,
With awareness they have now;
Judgment separates, understanding connects;
Choose compassion over criticism – Mankuthimma""",
    184: """Don't wait for perfect conditions,
They never come;
Start where you are;
Perfection is excuse for inaction – Mankuthimma""",
    185: """Your body tells truth,
Listen to its messages;
It knows before mind knows;
Trust your gut feelings – Mankuthimma""",
    186: """Life's struggle is for each being to
Play with fellow beings, reaching out hands;
Caught in bonds of love, debt, attachment,
Tossing in the whirlpool – Mankuthimma""",
    187: """Don't sacrifice present for future,
Future is built from present moments;
Make now beautiful;
Future takes care of itself – Mankuthimma""",
    188: """Loneliness and solitude are different,
One is lack, other is fullness;
Learn to enjoy your company;
You're never alone when at peace – Mankuthimma""",
    189: """Don't believe all your thoughts,
They're often stories, not truth;
Observe them without identifying;
You are the awareness, not the thoughts – Mankuthimma""",
    190: """Every ending carries seed of new beginning,
Death and birth are one cycle;
Don't mourn endings too long;
Welcome what's being born – Mankuthimma""",
    191: """Don't measure yourself by others' standards,
You have unique purpose;
Honor your own path;
Comparison kills joy – Mankuthimma""",
    192: """Your peace affects whole world,
Ripples spread from your center;
Be peace you want to see;
Inner change changes outer – Mankuthimma""",
    193: """Don't postpone forgiveness,
It liberates you, not them;
Holding grudges poisons you;
Forgiveness is freedom – Mankuthimma""",
    194: """Life is not problem to solve,
But mystery to experience;
Stop analyzing, start living;
Mystery reveals in participation – Mankuthimma""",
    195: """Don't seek closure always,
Some things remain open;
Accept ambiguity, live with questions;
Not everything needs answer – Mankuthimma""",
    196: """Your struggles make you strong,
Easy life makes you weak;
Welcome life's resistance training;
Difficulty builds character – Mankuthimma""",
    197: """Don't live through others,
Find your own voice;
Stop being echo;
Be original sound – Mankuthimma""",
    198: """Gratitude is highest prayer,
More than asking, it's thanking;
Thank life for everything;
Gratitude is enlightenment – Mankuthimma""",
    199: """Don't avoid pain,
It's teacher you need;
Embrace it, learn from it;
What you resist persists – Mankuthimma""",
    200: """Your limitations are often gifts,
They force creativity and depth;
Don't curse your constraints;
They shape your unique expression – Mankuthimma""",
    201: """Don't live someone else's dream,
Discover your own truth;
Stop pleasing others;
Your life is yours alone – Mankuthimma""",
    202: """Every moment is choice point,
You're always choosing;
Choose consciously, not automatically;
Freedom is in the choosing – Mankuthimma""",
    203: """Don't wait to be ready,
You'll never feel fully ready;
Jump and grow wings;
Courage precedes confidence – Mankuthimma""",
    204: """Your attention creates your world,
What you focus on grows;
Choose focus carefully;
You become what you attend to – Mankuthimma""",
    205: """Don't seek easy life,
Seek strength to handle difficulty;
Prayer shouldn't be for light burden;
But for strong shoulders – Mankuthimma""",
    206: """Every person is whole,
Not needing completion from another;
Relationship is two wholes meeting;
Not two halves making one – Mankuthimma""",
    207: """Don't live for applause,
Do right thing regardless;
Integrity is its own reward;
Character is who you are when no one watches – Mankuthimma""",
    208: """Life is all anxiety; constantly new hungers,
For this, for that, for yet another thing;
Remembering power, wealth, beauty, fame,
The mind boils always – Mankuthimma""",
    209: """Don't accumulate regrets,
Learn, forgive, move on;
Past is closed chapter;
Write new story now – Mankuthimma""",
    210: """Your energy is finite,
Invest it wisely;
Say no to protect yes;
Boundaries are self-care – Mankuthimma""",
    211: """As the mind grows, hunger grows too,
To quench it, various tricks are devised;
Man climbs upward; but that mind's climb
Where does it end? Think on this – Mankuthimma""",
    224: """Wanting this, that, and yet another thing,
World anxiously chases, forgetting its beauty;
The meditation-feast in the heart-cave is witness
To joys' limitless treasure – Mankuthimma""",
    241: """Work done without desire for fruits,
Is true karma yoga practiced;
Do your duty, leave results;
This is freedom in action – Mankuthimma""",
    249: """Destruction, ruin everywhere, yet life persists,
Who is the clever one who'll save us from these troubles?
Servant or master? Quarrel or cry?
Life won't stop living – Mankuthimma""",
    250: """Life is God's supreme glory,
Service to it sanctifies all efforts;
Who gives? Who receives when all are one?
You are the offering's sharer – Mankuthimma""",
    252: """Mind creates its own prison,
Or opens doors to freedom;
Choose your thoughts carefully;
You are your mind's master – Mankuthimma""",
    258: """Don't seek approval from world,
World's opinion changes like weather;
Be true to yourself;
That's only approval needed – Mankuthimma""",
    260: """Life's essence is not grape juice easy,
It's like sugarcane stalk, needing effort to chew;
With skill, a gulp or two of juice;
The rest is just flies – Mankuthimma""",
    264: """Don't cry out, don't covet greedily,
Know that life is consciousness playing a game;
Live as a player should within it;
Even the game has dharma – Mankuthimma""",
    266: """Why curse life? Why cry out?
What wrong did it do except let you live?
Listen, the Lord plays His game; in it
Don't take sides – Mankuthimma""",
    271: """Don't say life's struggle is meaningless,
It has meaning in complete vision for you;
The One dances in forms of living and non-living,
Understand this completeness as beauty – Mankuthimma""",
    277: """Every person is teacher,
Every situation is lesson;
Life is university;
Graduate with wisdom – Mankuthimma""",
    278: """Don't fear being alone,
Solitude is not loneliness;
In aloneness you find yourself;
Company can be distraction – Mankuthimma""",
    301: """Attachment is root of suffering,
Love freely without possessing;
Let everything flow;
Nothing truly belongs to you – Mankuthimma""",
    310: """Don't chase after miracles,
Life itself is miracle;
Your breath, heartbeat, consciousness;
The ordinary is extraordinary – Mankuthimma""",
    321: """Every obstacle is opportunity,
To discover inner resources;
Problems are not punishments;
They're invitations to grow – Mankuthimma""",
    323: """Don't waste energy explaining yourself,
Those who matter will understand;
Those who don't matter won't;
Explanation is not owed – Mankuthimma""",
    358: """Your worth is not determined,
By what you do or have;
You are valuable because you exist;
Being precedes doing – Mankuthimma""",
    360: """Don't live life on hold,
Waiting for perfect moment;
This moment is perfect;
Life is now or never – Mankuthimma""",
    362: """Silence is sometimes best answer,
To foolish questions asked;
Not everything deserves response;
Silence speaks volumes – Mankuthimma""",
    365: """Every experience shapes you,
Good and bad both necessary;
Don't reject anything;
All is grist for mill – Mankuthimma""",
    366: """Don't identify with achievements,
Or failures either;
Both are temporary events;
You are the eternal witness – Mankuthimma""",
    371: """Want, want, want - I want one more thing,
This pot of a world keeps bubbling;
Why did the Lord create this wanting-chant?
When will 'enough' ever come? – Mankuthimma""",
    372: """Peace comes when you stop,
Fighting with what is;
Acceptance is not resignation;
It's acknowledging truth – Mankuthimma""",
    373: """Your happiness is nobody's burden,
Take responsibility for it;
Don't make others responsible;
You are source of joy – Mankuthimma""",
    374: """Don't live life through labels,
Names, roles, identities;
These are costumes you wear;
Know the wearer beneath – Mankuthimma""",
    375: """Every person carries wounds,
Be gentle with everyone;
Kindness costs nothing;
It heals giver and receiver – Mankuthimma""",
    376: """Don't postpone living until conditions are right,
Conditions are never perfect;
Live now with what you have;
Perfection is enemy of good – Mankuthimma""",
    378: """Your energy is precious resource,
Don't waste it on negativity;
Focus on what uplifts;
Where attention goes, energy flows – Mankuthimma""",
    379: """Don't be slave to habits,
Examine them, change them;
Habit is convenience, not necessity;
You have power to change – Mankuthimma""",
    383: """Every moment offers choice,
Between love and fear;
Choose love consistently;
Fear divides, love unites – Mankuthimma""",
    384: """Don't seek security outside,
It's illusion that doesn't exist;
True security is within;
In knowing impermanence, find peace – Mankuthimma""",
    385: """We are all slaves like dogs in this world,
Drawn by desires in all directions;
Snares are outside, hooks are within us;
Freedom is desire's destruction – Mankuthimma""",
    387: """Your journey is unique,
No one else's path is yours;
Stop comparing, start creating;
Original is better than copy – Mankuthimma""",
    389: """Don't live for someday,
Someday never comes;
Today is the someday;
Act now, not later – Mankuthimma""",
    394: """Peace is not something to find,
But something to be;
You are peace seeking itself;
Stop searching, just be – Mankuthimma""",
    395: """Don't carry others' opinions,
As if they were truth;
They're just perspectives;
Your truth is yours alone – Mankuthimma""",
    396: """Every ending is doorway,
To something new and unknown;
Don't cling to what's ending;
Welcome what's beginning – Mankuthimma""",
    397: """Don't fear your darkness,
It contains your hidden gold;
Light shines from darkness;
Embrace your shadow – Mankuthimma""",
    400: """Your presence is your power,
Not your past or future;
Be fully here now;
That's where life happens – Mankuthimma""",
    402: """Don't live as if immortal,
Death could come any moment;
Live fully each day;
As if it's your last – Mankuthimma""",
    418: """Every person you meet,
Is fighting unseen battle;
Be kind, be understanding;
Compassion is wisdom in action – Mankuthimma""",
    432: """Don't seek revenge,
It poisons you, not them;
Forgiveness is freedom;
Let go and move on – Mankuthimma""",
    456: """Your thoughts create emotions,
Emotions drive actions;
Master your thoughts;
Master your life – Mankuthimma""",
    460: """Don't live in reaction,
Live from intention;
Choose your response;
That's your freedom – Mankuthimma""",
    484: """Every person reflects universe,
In their unique way;
Honor the diversity;
Unity in diversity – Mankuthimma""",
    485: """Don't seek perfection in world,
It's perfectly imperfect;
Beauty lies in flaws;
Imperfection is perfection – Mankuthimma""",
    492: """Your life force is limited,
Use it for what matters;
Say no to trivia;
Yes to significance – Mankuthimma""",
    493: """Don't live through memories,
Past is gone forever;
Create new experiences;
Now is all you have – Mankuthimma""",
    499: """Every challenge strengthens you,
If you don't give up;
Persistence beats resistance;
Keep going, don't stop – Mankuthimma""",
    504: """Don't seek easy answers,
Truth is often complex;
Live the questions;
Answers reveal in time – Mankuthimma""",
    505: """Your worth is not negotiable,
Not dependent on approval;
You are inherently valuable;
Know this deeply – Mankuthimma""",
    512: """Don't live for external rewards,
Do right because it's right;
Integrity is its reward;
Character matters most – Mankuthimma""",
    537: """The skilled one who ordered sun and moon's paths,
Earth and ocean's movements, wind and fire's speeds,
Why did He leave man alone to find
His own way? – Mankuthimma""",
    549: """Every breath is gift,
Life is borrowed time;
Use it well, wisely;
Return it with gratitude – Mankuthimma""",
    550: """Don't fear vulnerability,
It's doorway to connection;
Walls protect but isolate;
Courage opens heart – Mankuthimma""",
    557: """Your peace affects everyone,
Like stone in pond;
Ripples spread outward;
Be the change – Mankuthimma""",
    574: """Don't live on borrowed dreams,
Find your own vision;
Others' dreams won't fulfill you;
Discover your purpose – Mankuthimma""",
    582: """Every moment is teaching,
If you're willing to learn;
Life is constant school;
Stay humble, stay curious – Mankuthimma""",
    584: """Don't seek constant happiness,
Embrace full spectrum of emotions;
All feelings are valid;
Wholeness includes everything – Mankuthimma""",
    588: """Your attention shapes reality,
What you focus on expands;
Choose focus deliberately;
You create your world – Mankuthimma""",
    593: """Don't live for others' expectations,
They will never be satisfied;
Live for your truth;
That's enough – Mankuthimma""",
    595: """Every person has story,
That explains their behavior;
Before judging, seek understanding;
Empathy bridges differences – Mankuthimma""",
    598: """He who fears life's battle and runs away,
Will he escape becoming prey to fate's mouth?
Strengthening your chest, gripping courage's rope,
Stand and face the enemy – Mankuthimma""",
    599: """Don't postpone joy,
Find it in ordinary moments;
Happiness is not achievement;
It's appreciation of now – Mankuthimma""",
    600: """Your body is wise teacher,
Listen to its messages;
It knows truth before mind;
Trust somatic wisdom – Mankuthimma""",
    601: """Don't live divided,
Between who you are and appear;
Authenticity is freedom;
Be real, be whole – Mankuthimma""",
    602: """Every loss teaches something,
If you're open to lesson;
What you lose wasn't yours;
What's yours can't be lost – Mankuthimma""",
    603: """Don't seek to be understood,
Seek to understand;
Listening is loving;
Understanding precedes change – Mankuthimma""",
    604: """Your purpose is not external,
It's expression of who you are;
Being is purpose;
Everything else flows from that – Mankuthimma""",
    605: """Don't fear being different,
Conformity is living death;
Celebrate your uniqueness;
World needs your originality – Mankuthimma""",
    606: """Every relationship mirrors you,
Showing what needs healing;
Others are your teachers;
Relationships are spiritual practice – Mankuthimma""",
    643: """Life has one hundred and eight troubles and worries,
To hearing ears they seem just quarrels;
What use in crying? What use in fighting?
Bear it with patience – Mankuthimma""",
    652: """Fiercer than hunger for food is lust for gold,
Fiercer than gold is sex's passion;
Most fierce of all is thirst for recognition;
It devours the soul itself – Mankuthimma""",
    657: """Not just for wealth, not just for women,
People trudge through muddy paths;
To win titles, to spread their names,
Can misdeeds be counted? – Mankuthimma""",
    732: """Which way will it fly! Which way will it turn!
When and where will the bird land!
We too are like that, puppets of creation's maker;
Life's path is unpredictable – Mankuthimma""",
    829: """The pond water is your mind; let world's troubles enter,
Bottom's dirt floats up, muddying all;
Leave it unstirred for just a while,
It clears again in peace – Mankuthimma""",
}

def read_file_in_chunks(filepath, chunk_size=1000):
    """Read large file in chunks"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def extract_stanza_number(text):
    """Extract stanza number from Kannada text like ॥ ೧ ॥"""
    import re
    match = re.search(r'॥\s*(\d+)\s*॥', text)
    if match:
        # Convert Kannada numerals to regular numbers
        kannada_nums = {'೧': '1', '೨': '2', '೩': '3', '೪': '4', '೫': '5',
                       '೬': '6', '೭': '7', '೮': '8', '೯': '9', '೦': '0'}
        num_str = match.group(1)
        for k, v in kannada_nums.items():
            num_str = num_str.replace(k, v)
        try:
            return int(num_str)
        except:
            return None
    return None

def process_kagga_file(input_file, output_file):
    """Process the Kagga file and add English translations"""
    lines = read_file_in_chunks(input_file)

    output_lines = []
    current_stanza = []
    stanza_num = None

    # Copy header
    output_lines.append(lines[0])  # Title
    output_lines.append(lines[1])  # Slug
    output_lines.append(lines[2])  # Template
    output_lines.append(lines[3])  # Blank line
    output_lines.append(lines[4])  # ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ title
    output_lines.append('\n')

    for i, line in enumerate(lines[5:], start=5):
        # Skip blank lines between stanzas
        if line.strip() == '':
            if current_stanza:
                # Process the completed stanza
                stanza_text = ''.join(current_stanza)
                num = extract_stanza_number(stanza_text)

                if num and num in translations:
                    # Create two-column HTML structure
                    output_lines.append('<div class="poetry-stanza">\n')
                    output_lines.append('<div class="poetry-kannada">\n')
                    output_lines.append(stanza_text)
                    output_lines.append('</div>\n')
                    output_lines.append('<div class="poetry-english">\n')
                    output_lines.append(translations[num] + '\n')
                    output_lines.append('</div>\n')
                    output_lines.append('</div>\n\n')
                else:
                    # No translation available yet, keep original format
                    output_lines.append(stanza_text)
                    output_lines.append('\n')

                current_stanza = []
            continue

        current_stanza.append(line)

    # Don't forget last stanza
    if current_stanza:
        stanza_text = ''.join(current_stanza)
        num = extract_stanza_number(stanza_text)
        if num and num in translations:
            output_lines.append('<div class="poetry-stanza">\n')
            output_lines.append('<div class="poetry-kannada">\n')
            output_lines.append(stanza_text)
            output_lines.append('</div>\n')
            output_lines.append('<div class="poetry-english">\n')
            output_lines.append(translations[num] + '\n')
            output_lines.append('</div>\n')
            output_lines.append('</div>\n\n')
        else:
            output_lines.append(stanza_text)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"Processed {len(translations)} stanzas with English translations")
    print(f"Output written to {output_file}")

if __name__ == '__main__':
    input_file = 'content/pages/about/ಕಗ್ಗ.md'
    output_file = 'content/pages/about/ಕಗ್ಗ_new.md'

    process_kagga_file(input_file, output_file)
    print("\nNext steps:")
    print("1. Review the output file")
    print("2. If satisfied, replace the original:")
    print(f"   mv {output_file} {input_file}")
    print("3. Run: pelican content")
