import re
from collections import Counter

text= u'''The silver lining of being stuck at home during the coronavirus pandemic is getting to cozy up with a good book, especially one that will encourage you to think about the world from new perspectives. 

Below are some recommendations, based on what university professors and staff at Harvard, Yale and Columbia have been reading while self-isolating or quarantining at home:
1. ‘The Plague’

By Albert Camus

“The Plague” is one of the most well-known books on the topic of epidemic disease — and right now, it’s on the reading lists of many professors.

Bill Hanage, associate professor of epidemiology at the Harvard T.H. Chan School of Public Health, told The Harvard Gazette that although he hasn’t had time to start the 1947 novel yet, he’s read it before. ”[Albert] Camus has influenced my thinking ever since my best friend introduced me to his work,” he said.

“This book is very vivid in conveying what it feels like to be in a city hit by an epidemic, and what it feels like to be in quarantine,” Jenny Davidson, a professor at Columbia University said in an interview with book recommendations site FiveBooks.com. “It conveys how important it is to retain our humanity and our sense of connection to others in times when so much is at stake.”
2. ‘The Stoic Challenge’

By William B. Irvine

Laurie Santos, a psychology professor at Yale University, puts “The Stoic Challenge” high up on her Covid-19 reading list. “It’s the perfect call to arms for a tough time like we’re experiencing, but it gives you hope that a stoic outlook on life can help,” she told Yale News.

Author and philosopher William B. Irvine uses centuries-old wisdom to teach us how to turn unexpected setbacks into opportunities for a tougher, calmer and more resilient life.

“The main thesis is that we can view bad things in our life as a challenge to overcome, rather than a crisis to be endured,” Santos said.
3. ‘A Jewish Refugee in New York’

By Kadya Molodovsky (translated by Anita Norich)

Originally published in Yiddish in 1941 (but recently translated), “A Jewish Refuge in New York” is about a 20-year-old Jewish woman who arrives in New York shortly after the Nazi invasion of Poland, her home country — and must cope with a different way of life in the U.S.

″[The protagonist] is trying to survive and go on, but she’s also frequently angry at how little those around her know or apparently care about the situation in Europe,” Katie Trumpener, a professor of comparative literature at Yale, told Yale News.

“Somehow this was very comforting to read in the first strange days of the pandemic,” she added, ”[especially] as the danger moved closer, but was still largely invisible, as some people were loading up their grocery carts in anticipation, while others were still in denial that it could possibly ever affect or touch them.”
4. ‘Untamed’

By Glennon Doyle

“The braver we are, the luckier we get,” activist and speaker Glennon Doyle writes in her memoir. 

“Untamed” is an exploration of the happiness, joy and peace we find when we stop bending over backwards to meet societal expectations. “I am going slowly because I don’t want it to end, I love it so much,” Kathy Delaney-Smith, head coach of Harvard’s women’s basketball team, told The Harvard Gazette.

She plans to make her whole team read “Untamed” once practice is back in session — and recommends it to all women.

“It looks at the whole set of characteristics that are attributed to men and the very different set attributed to women,” said Delaney-Smith, “and makes the point that it’s time for women to understand they are free to be whoever they are, to find their true selves.”
5. ‘The Decameron’

By Giovanni Boccacio

Priyamvada Natarajan, a professor in the Departments of Astronomy and Physics at Yale, recently finished reading “The Decameron.” 

“It’s essentially a collection of 100 stories from 14th-century Italy, told by a group of seven women and three men who are sheltering — staying home! — in a villa outside Florence to escape the Black Death (the epidemic of 1348),” Natarajan explained to Yale News.

The stories are all “wonderful ... some comic, some tragic, some absurd, and some magical,” she said. “The original is in vernacular Florentine Italian. I read it in translation, of course.”
'''

def neutral_converter_sp(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(lambda x: '\\b' + x + '\\b', map(re.escape, substrings))))
    return regex.sub(lambda match: substitutions[match.group(0)], string) 

def neutral_converter(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.subn(lambda match: substitutions[match.group(0)], string)   #subn to count conversions



#   TO BE CONSIDERED:
#   Words such as 'woman' and 'man' as an isolated word or placed at the end of a sentence or phrase, will not be converted since the converter recognizes 'woman ' or 'man ', that is to say, with a space succeeding the word. 
#   This is to prevent conversion of words such as 'Manchester' or 'womanizer' resulting in 'Personchester' and 'personizer'.

dict_neutral_sp = {'than a man': 'than a person','than men': 'than people',
                'than a woman': 'than a person','than women': 'than people',
                ' he does': ' they do', 'He does': 'They do', 'Does he': 'Do they',
                ' she does': ' they do', 'She does': 'They do', 'Does she': 'Do they',
                ' he is': ' they are', ' he was': ' they were', 'Is he': 'Are they', 
                'Is she': 'Are they', ' he is.': ' they are.', ' he is?': ' they are?', 
                ' he has': ' they have',
                'He is ': 'They are ', 'He was ': 'They were ', '(he is': '(they are', '(he was': '(they were',
                'He has ': 'They have ',
                ' she is ': ' they are ', ' she was ': ' they were ', '(she is': '(they are', 
                '(she was': '(they were', ' she is.': ' they are.', ' she is?': ' they are?',
                ' she has ': ' they have ',
                'She is ': 'They are ', 'She was ': 'They were ',
                'She has ': 'They have ',
                'she’s read': 'they’ve read', "she's read": "they've read", 
                'She’s read': 'They’ve read', "She's read": "They've read",
                'he’s read': 'they’ve read', "he's read": "they've read", 
                'He’s read': 'They’ve read', "He's read": "They've read",
                'an actor': 'a performer', 'an actress': 'a performer',
                 " he isn’t": " they aren’t", " she isn’t": " they aren’t", 
                 " he isn't": " they aren't", " she isn't": " they aren't",
                "He isn’t": "They aren’t", "She isn’t": "They aren’t", 
                "He isn't": "They aren't", "She isn't": "They aren't",
                ' he still has ': ' they still have ', 'He still has ': 'They still have ', 
                ' she still has ': ' they still have ', 'She still has ': 'They still have ', 
                ' her over': ' them over', ' her by': ' them by',
                ' him boy': ' them kiddo', ' her girl': ' them kiddo', 
                ' her up': ' them up', 
                'takes her home': 'takes them home', 'take her home': 'take them home',
                'His are': 'Theirs are', 'His is': 'Theirs is', 
                'His was': 'Theirs was', 'His were': 'Theirs were',
                'Hers are': 'Theirs are',  'Her is': 'Theirs is', 
                'Her was': 'Theirs was','Hers were': 'Theirs were',
                ' her “that' : ' them “that', ' her that' : ' them that', ' her "that' : ' them "that',
                ' her out': ' them out',
                'from her is': 'from them is', 'From her is': 'From them is',
                'from her was': 'from them was', 'From her was': 'From them was', 
                ' her back to' : ' them back to', 
                }

dict_neutral = {'United Kingdom': 'United Kingdom', 'Staunton': 'Staunton', 'taunt' : 'taunt', 'The Sportsman': 'The Sportsman,', #first exceptions
                'THE SPORTSMAN': 'THE SPORTSMAN', 'Queens, New York' : 'Queens, New York', 'emotional intelligence': 'emotional intelligence', #first exceptions
                'Emotional inteligence': 'Emotional inteligence', #first exceptions 
                #' men.': ' people.', ' men,': ' people,', " men’": " people’", " men'": " people'",
                # '-men': '-people', "Men'": "People'", "Man'": "Person'", ' man.': ' person.', ' man,': ' person,', " man’": " person’", 
                # " man'": " person'", '-man' : '-person ', '-Man': '-Person', 'Man,': 'Person,', 'Men,': 'People,', '-Men': '-People','man' :  'person',
                #, ' woman ': ' person ', ' woman.': ' person.', ' woman,': ' person,', " woman’": " person’", " woman'": " person'", 
                #'-woman': '-person', '-Woman': '-Person', ' woman”': ' person”', ' Woman”': ' Person”', ' woman"': ' person"', ' Woman"': ' Person"',
                # ' women.': ' people.', ' women,': ' people,', 
                # " women’": " people’", " women'": " people'", '-women': '-people', '-Women': '-People', ' women”': ' people”', ' Women”': ' People”', 
                #' women"': ' people"', ' Women"': ' People"','actors': ' performers', '-actor': '-performer', 
                #'Actors': 'Performers',"he'll": "they'll", "she'll": "they'll", "he’d": "they’d", "she’d": "they’d", "he'd": "they'd", "she'd": "they'd",  
                # "He’d": "They’d", "She’d": "They’d", "He'd": "They'd", "She'd": "They'd", ' he ': ' they ', 'He ': 'They ',   "He’ll": "They’ll", 
                # '(he ': '(they ',' she ': ' they ', 'She ': 'They ', "She’ll": "They’ll", '(she ': '(they ', ' his.': ' theirs.', 'hers.': ' theirs.',                  
                # ' him,': ' them,',  ' him.': ' them.',   'female-': None, 'Female-': None,"‘feminine’ ": None, "‘Feminine’ ": None, "'feminine' ": None, 
                # "'Feminine' ": None, 'feminine, ': None, "‘masculine’ ": None, "‘Masculine’ ": None, "'masculine' ": None, "'Masculine' ": None, 
                # 'masculine, ': None, 'male-': None, 'Male-': None,
                #'King’': 'Monarch’','king’': 'monarch’','stableboys': 'kiddos', 'Stableboys': 'Kiddos',' boys': ' kiddos', 'Boys': 'Kiddos',
                # 'boyfriends': 'partners', 'Boyfriends': 'Partners',' bros ': ' siblings ',  'brothers ': 'siblings ',  ' sisters ': ' siblings ',
                # 'Brothers ': 'Siblings ',  ' Sisters ': ' Siblings ',' bro.': ' sibling.',  ' sis.': ' sibling.', ' bros.': ' siblings.',  
                # ' sistas.': ' siblings.', 'brother.': 'sibling.',  ' sister.': ' sibling.', 'brothers.': 'siblings.',  ' sisters.': ' siblings.', 'Brother.': 'Sibling.',  ' Sister.': ' Sibling.', 
                # 'Brothers.': 'Siblings.',  ' Sisters.': ' Siblings.', 
                # ' bro,': ' sibling,',  ' sis,': ' sibling,', ' bros,': ' siblings,',  ' sistas,': ' siblings,',
                # 'brother,': 'sibling,',  ' sister,': ' sibling,', 'brothers,': 'siblings,',  ' sisters,': ' siblings,', 'Brother,': 'Sibling,',  ' Sister,': ' Sibling,', 
                # 'Brothers,': 'Siblings,',  ' Sisters,': ' Siblings,', 
                #'fathers': 'parents', 'Fathers': 'Parents',' girls': ' kiddos', 'Girls': 'Kiddos',  'girlfriends': 'partners', 'Girlfriends': 'Partners',  
                #'Good-guys': 'Good folks', 'Bad-guys': 'Bad folks','good-guys': 'good folks', 'bad-guys': 'bad folks', 'mom.': 'mada.', 'dad.': 'mada.', 
                #'mommy.': 'maddy.', 'daddy.': 'maddy.',   
                #'her aunt': "their parent's sibling", ' son.': ' child.', 'Son.': 'Child.',
                # 
                # 
                # 
                # 
                #
                'men': 'people', 'Men': 'People', 'man' :  'person',  'Man': 'Person', 'MAN': 'PERSON', 'MEN': 'PEOPLE',
                'woman': 'person',  'Woman': 'Person', 'women': 'people', 'Women': 'People', 'WOMAN': 'PERSON', 'WOMEN': 'PEOPLE',
                'Mr': 'Mx', 'Ms': 'Mx', 'Sir': 'Mx', 'Lady': 'Mx', 'Lord': 'Mx', 
                'MR' : 'MX', 'MS': 'MX', 'SIR': 'MX', 'LORD': 'MX', 
                'lady': ' person', 'gentleman': 'person', 'ladies': 'people', 'gentlemen': 'people',  
                'LADY': 'PERSON', 'GENTLEMAN': 'PERSON', 'LADIES': 'PEOPLE', 'GENTLEMEN': 'PEOPLE',
                'bride': 'nearlywed', 'groom ': 'nearlywed ', 'Bride': 'Nearlywed', 'Groom': 'Nearlywed',
                'BRIDE': 'NEARLYWED', 'GROOM ': 'NEARLYWED ',
                'fiancée': 'nearlywed', 'fiance': 'nearlywed', 'fiancee': 'nearlywed', 'Fiancée': 'Nearlywed', 
                'FIANCÉE': 'NEARLYWED',
                'Fiance': 'Nearlywed', 'Fiancee': 'Nearlywed',
                'FIANCE': 'NEARLYWED', 'FIANCEE': 'NEARLYWED',
                'actor': 'performer',  'Actor': 'Performer', 
                'ACTOR': 'PERFORMER', 
                'actress': 'performer', 'actresses': 'performers', 'Actress': 'Performer', 'Actresses': 'Performers', 
                'ACTRESS': 'PERFORMER', 'ACTRESSES': 'PERFORMERS',
                'assemblyman': 'member of assembly', 'assemblyman': 'Member of assembly', 
                'ASSEMBLYMAN': 'MEMBER OF ASSEMBLY', 
                'assemblymen': 'members of assembly', 'Assemblymen': 'Members of assembly',
                'ASSEMBLYMEN': 'MEMBERS OF ASSEMBLY',
                'assemblywoman': 'member of asssembly', 'Assemblywoman': 'Member of assembly',
                'ASSEMBLYWOMAN': 'MEMBER OF ASSEMBLY',
                'assemblywomen': 'members of assembly', 'Assemblywomen': 'Members of assembly',
                'ASSEMBLYWOMEN': 'MEMBERS OF ASSEMBLY',
                'businessman': 'business executive', 'Businessman': 'Business executive', 
                'BUSINESSMAN': 'BUSINESS EXECUTIVE',
                'businessmen': 'business executives', 'Businessmen': 'Business executives', 
                'BUSINESSMEN': 'BUSINESS EXECUTIVES',
                'businesswoman': 'business executive', 'Businesswoman': 'Business executive', 
                'BUSINESSWOMAN': 'BUSINESS EXECUTIVE',
                'businesswomen': 'business executives', 'Businesswomen': 'Business executives', 
                'BUSINESSWOMEN': 'BUSINESS EXECUTIVES',
                'heroine': 'hero', 'Heroine': 'Hero',
                'HEROINE': 'HERO',
                'cameraman': 'camera operator', 'Cameraman': 'Camera operator', 
                'CAMERAMAN': 'CAMERA OPERATOR',
                'cameramen': 'camera operators', 'Cameramen': 'Camera operators', 
                'CAMERAMEN': 'CAMERA OPERATORS',
                'camerawoman': 'camera operator', 'Camerawoman': 'Camera operator', 
                'CAMERAWOMAN': 'CAMERA OPERATOR',
                'camerawomen': 'camera operators', 'Camerawomen': 'Camera operators', 
                'CAMERAWOMEN': 'CAMERA OPERATORS',
                'chairman': 'chairperson', 'Chairman': 'Chairperson', 
                'CHAIRMAN': 'CHAIRPERSON',
                'chairmen': 'chairpeople', 'Chairmen': 'Chairpeople', 
                'CHAIRMEN': 'CHAIRPEOPLE',
                'chairwoman': 'chairperson', 'Chairwoman': 'Chairperson',
                'CHAIRWOMAN': 'CHAIRPERSON', 
                'chairwomen': 'chairpeople', 'Chairwomen': 'Chairpeople', 
                'CHAIRWOMEN': 'CHAIRPEOPLE',
                'congressman': 'member of congress', 'Congressman': 'Member of congress',
                'CONGRESSMAN': 'MEMBER OF CONGRESS', 
                'congressmen': 'members of congress', 'Congressmen': 'Members of congress',
                'CONGRESSMEN': 'MEMBERS OF CONGRESS',
                'congresswoman': 'member of congress', 'Congresswoman': 'Member of congress', 
                'CONGRESSWOMAN': 'MEMBER OF CONGRESS',
                'congresswomen': 'members of congress', 'Congresswomen': 'Members of congress',
                'CONGRESSWOMEN': 'MEMBERS OF CONGRESS',
                'councilman': 'council person', 'Councilman': 'Council person', 
                'COUNCILMAN': 'COUNCIL PERSON',
                'councilwoman': 'council person', 'Councilwoman': 'Council person', 
                'COUNCILWOMAN': 'COUNCIL PERSON',
                'fireman': 'firefighter', 'Fireman': 'Firefighter', 
                'FIREMAN': 'FIREFIGHTER',
                'firemen': 'firefighters', 'Firemen': 'Firefighters', 
                'FIREMEN': 'FIREFIGHTERS',
                'freshman': 'first-year student', 'Freshman': 'First-year student', 
                'FRESHMAN': 'FIRST-YEAR STUDENT', 
                'freshmen ': 'first-year students', 'Freshmen ': 'First-year students',
                'FRESHMEN ': 'FIRST-YEAR STUDENTS',
                'milkmaid' : 'milker', 'Milkmaid': 'Milker',
                'MILKMAID': 'MILKER',
                'policeman': 'police officer', 'Policeman': 'Police officer', 
                'POLICEMAN': 'POLICE OFFICER',
                'policemen': 'police officers', 'Policemen': 'Police officers', 
                'POLICEMEN': 'POLICE OFFICERS',
                'policewoman': 'police officer', 'Policewoman': 'Police officer', 
                'policewomen': 'police officers', 'Policewomen': 'Police officers', 
                'postman': 'postal worker', 'Postman': 'Postal worker',
                'POSTMAN': 'POSTAL WORKER',
                'postmen': 'postal workers', 'Postmen': 'Postal workers',
                'POSTMEN': 'POSTAL WORKERS',
                'postwoman': 'postal worker', 'Postwoman': 'Postal worker',
                'POSTWOMAN': 'POSTAL WORKER',
                'postwomen': 'postal workers', 'Postwomen': 'Postal workers',
                'POSTWOMEN': 'POSTAL WORKERS',
                'repairman' : 'repairer', 'Repairman': 'Repairer', 
                'REPAIRMAN': 'REPAIRER',
                'repairmen' : 'repairers', 'Repairmen': 'Repairers', 
                'REPAIRMEN' : 'REPAIRERS',
                'salesman': 'salesperson', 'Salesman': 'Salesperson',
                'SALESMAN': 'SALESPERSON',
                'saleswoman': 'salesperson', 'Saleswoman': 'Salesperson',
                'SALESWOMAN': 'SALESPERSON',
                'salesmen': 'salespeople', 'Salesmen': 'Salespeople',
                'SALESMEN': 'SALESPEOPLE',
                'saleswomen': 'salespeople', 'Saleswomen': 'Salespeople',
                'SALESWOMEN': 'SALESPEOPLE',
                'spokesman': 'spokesperson', 'Spokesman': 'Spokesperson',
                'SPOKESMAN': 'SPOKESPERSON',
                'spokeswoman': 'spokesperson', 'Spokeswoman': 'Spokesperson',
                'SPOKESWOMAN': 'SPOKESPERSON',
                'spokeswomen': 'spokespeople', 'Spokeswomen': 'Spokespeople',
                'SPOKESWOMEN': 'SPOKESPEOPLE',
                'spokesmen': 'spokespeople', 'Spokesmen': 'Spokespeople',
                'SPOKESMEN': 'SPOKESPEOPLE',
                'sportsman': 'athlete', 'Sportsman': 'Athlete',
                'SPORTSMAN': 'ATHLETE',
                'sportswoman': 'athlete', 'Sportswoman': 'Athlete',
                'SPORTSWOMAN': 'ATHLETE',
                'sportswomen': 'athletes', 'Sportswomen': 'Athletes',
                'SPORTSWOMEN': 'ATHLETES',
                'sportsmen': 'athletes', 'Sportsmen': 'Athletes',
                'SPORTSMEN': 'ATHLETES',              
                'workman': 'worker', 'Workman': 'Worker',
                'WORKMAN': 'WORKER',
                'workmen': 'workers', 'Workmen': 'Workers',
                'WORKMEN': 'WORKERS',
                'workwoman': 'worker', 'Workwoman': 'Worker',
                'WORKWOMAN': 'WORKER',
                'workwomen': 'workers', 'Workwomen': 'Workers',
                'WORKWOMEN': 'WORKERS',                
                'She/he': 'They', 'she/he': 'they', 'he/she': 'they', 'He/she': 'they', 'He/She': 'They',
                'SHE/HE': 'THEY',
                'HerName': 'TheirName', 'HisName': 'TheirName',
                'HERNAME': 'THEIRNAME', 'HISNAME': 'THEIRNAME',
                'he': 'they', 'she': 'they', 
                'SHE': 'THEY',                 
                'He': 'They', 'She': 'They',
                'HE': 'THEY',                
                "he’s": "they’re", "she’s": "they’re",
                "SHE’S": "THEY’RE",
                "he's": "they're", "she's": "they're", 
                "HE'S": "THEY'RE",
                "He’s": "They’re", "She’s": "They’re", 
                "SHE’S": "THEY’RE", 
                "He's": "They're", "She's": "They're", 
                "HE'S": "THEY'RE",           
                'his': 'their', 'His': 'Their',
                'HIS': 'THEIR',
                'her': 'their',  'Her': 'Their',  
                'HER': 'THEIR',
                'her,': 'them,', 'her.': 'them.',
                'HER,': 'THEM,', 'HER.': 'THEM.',
                'him': 'them', 
                'HIM': 'THEM',
                'himself': 'themself', 'herself': 'themself',   
                'HIMSELF': 'THEMSELF', 'HERSELF': 'THEMSELF',                 
                'hers': 'them', 
                'HERS': 'THEM',
                'female': None, 'Female': None, 
                'FEMALE': None,
                'feminine': None, 'Feminine': None, 
                'FEMININE': None,
                'masculine': None, 'Masculine': None,
                'MASCULINE': None,
                'male': None, 'Male': None, 
                'MALE': None,
                'dudely': None, 'Dudely': None,
                'DUDELY': None,
                'womanly': None, 'Womanly': None,
                'WOMANLY': None,
                'boyish': None, 'Boyish': None,
                'BOYISH': None,
                'girly': None, 'Girly': None,
                'GIRLY': None,
                'manly': None, 'Manly': None,
                'MANLY': None,
                'the Rev.': None,   
                'THE REV.': None,           
                'feminist': 'gender-equality activist', 'Feminist': 'Gender-equality activist',
                'FEMINIST': 'GENDER-EQUALITY ACTIVIST',
                'misandrist': 'gender-equality activist', 'Misandrist': 'Gender-equality activist',
                'MISANDRIST': 'GENDER-EQUALITY ACTIVIST',
                'feminism': 'gender-equality activism', 'Feminism': 'Gender-equality activism', 
                'FEMINISM': 'GENDER-EQUALITY ACTIVISM',
                'misandry': 'gender-equality activism', 'Misandry': 'Gender-equality activism',
                'MISANDRY': 'GENDER-EQUALITY ACTIVISM',
                'femininity': 'humanity', 'masculinity': 'humanity', 
                'FEMININITY': 'HUMANITY',
                'Femininity': 'Humanity', 'Masculinity': 'Humanity',
                'MASCULINITY': 'HUMANITY',
                'bossy': 'assertive', 'pushy': 'assertive', 
                'BOSSY': 'ASSERTIVE', 
                'Bossy': 'Assertive', 'Pushy': 'Assertive',
                'PUSHY': 'ASSERTIVE',
                'emotional': 'empathetic', 'hormonal': 'passionate', 
                'EMOTIONAL': 'EMPATHETIC',
                'Emotional': 'Empathetic', 'Hormonal': 'Passionate',
                'HORMONAL': 'PASSIONATE',
                'ditsy': 'silly', 'frigid': 'lacking sexual responsivness', 
                'FRIGID': 'LACKING SEXUAL RESPONSIVNESS',
                'Ditsy': 'Silly', 'Frigid': 'Lacking sexual responsivness',
                'DITSY': 'SILLY',
                'frumpy': 'dowdy', 'Frumpy': 'Dowdy',
                'FRUMPY': 'DOWDY',
                'shrill': 'high pitched', 'Shrill': 'High pitched',
                'SHRILL': 'HIGH PITCHED',
                'hysterical': 'irrational', 'Hysterical': 'Irrational',
                'HYSTERICAL': 'IRRATIONAL',
                'mumsy': 'old fashioned', 'Mumsy': 'Old fashioned',
                'MUMSY': 'OLD FASHIONED',
                'virile': 'energetic', 'Virile': 'Energetic',
                'VIRILE': 'ENERGETIC',
                'emperor': 'ruler', 'empress': 'ruler', 
                'EMPRESS': 'RULER',
                'Emperor': 'Ruler', 'Empress': 'Ruler', 
                'EMPEROR': 'RULER',
                'queen': 'monarch', 'king': 'monarch', 
                'QUEEN': 'MONARCH',
                'Queen': 'Monarch', 'King': 'Monarch',
                'KING': 'MONARCH', 
                'Kingdom': 'Realm', 'kingdom': 'realm', 
                'KINGDOM': 'REALM',                
                'princess': "monarch's child", 'Princess': "Monarch's child", 
                'PRINCESS': "MONARCH'S CHILD",
                'princesses': "monarch's children", 'Princesses': "Monarch's children",
                'PRINCESSES': "MONARCH'S CHILDREN", 
                'prince': "monarch's child", 'Prince': "Monarch's child", 
                'PRINCE': "MONARCH'S CHILD",
                'princes': "monarch's children", 'Princes': "Monarch's children",
                'PRINCES': "MONARCH'S CHILDREN",
                'manliness ': 'humanness',
                'MANLINESS ': 'HUMANNESS',
                'womanliness ': 'humannness',
                'WOMANLINESS ': 'HUMANNNESS',
                'womanhood': 'humanhood', 'Womanhood': 'Humanhood',
                'WOMANHOOD': 'HUMANHOOD',
                'manhood': 'humanhood',  'Manhood': 'Humanhood',
                'MANHOOD': 'HUMANHOOD',
                'maiden' : 'kiddo', 'Maiden': 'Kiddo',
                'MAIDEN': 'KIDDO',
                'stableboy': 'kiddo', 'Stableboy': 'Kiddo', 
                'STABLEBOY': 'KIDDO',                
                'boy': 'kiddo', 'Boy': 'Kiddo', 
                'BOY': 'KIDDO',
                'boyfriend': 'partner', 'Boyfriend': 'Partner', 
                'BOYFRIEND': 'PARTNER',
                'daughter': 'child', 'Daughter': 'Child', 
                'BOYFRIEND': 'PARTNER',
                'daughters': 'children',
                'DAUGHTERS': 'CHILDREN',
                'bro': 'sibling', 'sis': 'sibling', 
                'BRO': 'SIBLING', 'SIS': 'SIBLING',
                'sistas': 'siblings', 
                'SISTAS': 'SIBLINGS',
                'brother': 'sibling ',  'sister': 'sibling',
                'SISTER': 'SIBLING',  
                'Brother': 'Sibling',  'Sister': 'Sibling', 
                'BROTHER': 'SIBLING',         
                'fraternity': 'fellowship', 'sorority': 'fellowship', 
                'FRATERNITY': 'FELLOWSHIP',
                'Fraternity': 'Fellowship', 'Sorority': 'Fellowship',
                'SORORITY': 'FELLOWSHIP',
                'brotherhood': 'fellowship', 'sisterhood': 'fellowship',
                'BROTHERHOOD': 'FELLOWSHIP', 
                'Brotherhood': 'Fellowship', 'Sisterhood': 'Fellowship',
                'SISTERHOOD': 'FELLOWSHIP',
                'girlhood': 'fellowship', 'boyhood': 'fellowship', 
                'BOYHOOD': 'FELLOWSHIP',            
                'Boyhood': 'Fellowship', 'Girlhood': 'Fellowship',
                'GIRLHOOD': 'FELLOWSHIP',                 
                'girl': 'kiddo', 'Girl': 'Kiddo', 
                'GIRL': 'KIDDO',
                'girlfriend': 'partner', 'Girlfriend': 'Partner',
                'GIRLFRIEND': 'PARTNER', 
                'guys': 'everybody', 'Guys': 'Everybody',
                'GUYS': 'EVERYBODY',
                'guy': ' folk', 'Guy': 'Folk', 
                'GUY': 'FOLK ',
                'good-guy': 'good folk', 'bad-guy': 'bad folk', 
                'BAD-GUY': 'BAD FOLK',
                'Good-guy': 'Good folk', 'Bad-guy': 'Bad folk', 
                'GOOD-GUY': 'GOOD FOLK', 
                'wife': 'spouse', 'Wife': 'Spouse',
                'WIFE': 'SPOUSE', 
                'wives': 'spouses', 'Wives': 'Spouses',
                'WIVES': 'SPOUSES',
                'husband': 'spouse', 'Husband': 'Spouse',
                'HUSBAND': 'SPOUSE',
                'ladies and gentleman': 'everybody', 
                'LADIES AND GENTLEMAN': 'EVERYBODY',
                'Ladies and gentleman': 'Everybody', 
                'Ladies and Gentleman': 'Everybody',
                'mankind': 'humankind', 'Mankind': 'Humankind',
                'MANKIND': 'HUMANKIND',
                'womankind': 'humankind', 'Womankind': 'Humankind',
                'WOMANKIND': 'HUMANKIND',
                'man-made': 'artificial', 'Man-made': 'Artificial',
                'MAN-MADE': 'ARTIFICIAL',
                'father': 'parent', 'Father': 'Parent',
                'FATHER': 'PARENT',
                'mother': 'parent', 'Mother': 'Parent', 
                'MOTHER': 'PARENT',
                'mom': 'mada', 'dad' : 'mada', 
                'MOM': 'MADA', 'DAD': 'MADA',
                'mommy': 'maddy', 'daddy': 'maddy', 
                'Mom ': 'Mada ', 'Dad ': 'Mada ', 
                'Mommy': 'Maddy', 'Daddy': 'Maddy',
                'MOMMY': 'MADDY', 'DADDY': 'MADDY',
                'grandma' : 'grandparent', 'grandpa': 'grandparent',
                'GRANDMA' : 'GRANDPARENT', 'GRANDPA': 'GRANDPARENT',



                'nephew': 'nibling', 'Nephew': 'Nibling',
                'niece': 'nibling', 'Niece': 'Nibling',
                'uncle': "parent's sibling", 'Uncle': "Parent's sibling", 
                'Aunt': "Parent's sibling", ' aunt': " parent's sibling", 
                'aunt,': "parent's sibling,", 'aunt.': "parent's sibling.",
                'widow': 'surviving spouse', 'widower': 'surviving spouse', 
                'Widow': 'Surviving spouse', 'Widower': 'Surviving spouse', 
                ' son ': ' child ', 'Son ': 'Child ', 
                'sons': 'children', 'Sons': 'Children', 
                'steward ': 'flight attendant ', 'Steward ': 'Flight attendant ',
                'stewardess ': 'flight attendant', 'Stewardess ': 'Flight attendant', 
                'stewardesses': 'flight attendants', 'Stewardesses': 'Flight attendants',
                'waiter ': 'server', 'Waiter ': 'Server',
                'waitress ': 'server', 'Waitress ': 'Server', 
                'waitresses': 'servers', 'Waitresses': 'Servers',
                
                ' bishop': ' member of the clergy', 'archbishop ': 'member of the clergy ', 
                'clergyman': 'member of the clergy', 'clergywoman': 'member of the clergy', 
                ' bishops': ' members of the clergy', 'archbishops': 'members of the clergy', 
                'clergymen': 'members of the clergy', 'clergywomen': 'members of the clergy',
                ' Bishop': ' Member of the clergy', 'Archbishop ': 'Member of the clergy ', 
                'Clergyman': 'Member of the clergy', 'Clergywoman': 'Member of the clergy', 
                ' Bishops': ' Members of the clergy', 'Archbishops': 'Members of the clergy', 
                'Clergymen': 'Members of the clergy', 'Clergywomen': 'Members of the clergy',
                'deacon ': 'member of the diaconate ', 'deaconess ': 'member of the diaconate ', 
                'deacons': 'members of the diaconate', 'deaconesses': 'members of the diaconate',
                'Deacon ': 'Member of the diaconate ', 'Deaconess ': 'Member of the diaconate ', 
                'Deacons': 'Members of the diaconate', 'Deaconesses': 'Members of the diaconate',
                'abbot ': 'head of monastery ', 'abbots': 'heads of monastery', 'Abbot ': 'Head of monastery ', 
                'Abbots': 'Heads of monastery',
                ' nun ': ' Person belonging to a religious order ', 
                'priest ': 'performer of sacred rites in a religious community ', 
                ' nuns': ' person belonging to a religious order', 
                'priests': 'members of a religious community',
                'Nun ': 'Person belonging to a religious order ', 'Priest ': 'performers of sacred rites in a religious community ', 
                'Nuns': 'Person belonging to a religious order', 
                'Priests': 'Performers of sacred rites in a religious community',
                'Priestess': 'Performer of sacred rites in a religious community', 
                'Priestesses': 'Performers of sacred rites in a religious community',
                'priestess': 'performer of sacred rites in a religious community', 
                'priestesses': 'performers of sacred rites in religious community',
                ' pope ': ' head of the Roman catholic church ', 'Pope ': 'Head of the Roman catholic church ', 
                ' Popes ': ' Heads of the Roman catholic church ', 
                ' popes ': ' heads of the Roman catholic church ', 
                'headmaster': 'head', 'headmistress ': 'head ', 'Headmaster': 'Head', 'Headmistress ': 'Head ',
                'headmistresses': 'heads', 'Headmistresses': 'Heads',
                ' her to ': ' them to ',
                ' maid ': ' servant ',  'Maid ': 'Servant ', ' maid,': ' servant,', ' maids': ' servants', ' maid.': ' servant.', ' maid:': ' servant:', 
                'Maids': 'Servants',
                'butler': 'main servant', 'Butler': 'Main servant', 
                } #'paternalism': 'parentalism', 'misogynist': 'discriminatory', 'Misogynist': 'Discriminatory', 'matriarchal': 'egalitarian', 'patriarchal': 'egalitarian', 'Matriarchal': 'Egalitarian', 'Patriarchal': 'Egalitarian',

result = neutral_converter_sp(text, dict_neutral)


print("This is your neutral text: " + str(result))


#   |Men,|\smen\.|\smen,|\smen’|\smen'|-men|-Men|Man,|Man'|Men'\sman\s|\sman\.|\sman,|\sman’|\sman'|-man\s|-Man|\swoman\s|\swoman\.|\swoman,|\swoman’|\swoman'|-woman|-Woman|\swoman”|\sWoman”|
            #   |\swoman"|\sWoman"||\swomen\.|\swomen,||\swomen’|\swomen'|-women|-Women|\swomen”|\sWomen”|\swomen"|\sWomen"|\sactor-actor|

list_string = r"""\bUnited\sKingdom\b|\bStaunton\b|\btaunt\b|\bThe\sSportsman\b|\bTHE\sSPORTSMAN\b|\bQueens,\sNew\sYork\b|\bemotional\sintelligence\b|\bEmotional\sintelligence\b| # exceptions first
                |\bman\b|\bMan\b|\bmen\b|\bMen\b|\bWoman\b|\bwoman\b|\bwomen\b|\bWomen\b|
                |\bShe\sstill\shas\b|\bshe\sstill\shas\b|\bhe\sstill\shas\b|\bHe\sstill\shas\b|\bthan\sa\sman\b|
                |\bthan\smen\b|\bher\sout\b|\bher\sover\b|\bher\sback\sto\b|
                |\bthan\sa\swoman\b|\bthan\swomen\b|\bMr\b|\bMs\b|\bSir\b|\bLady\b|\bLord\b|
                
                |gentleman|ladies|gentlemen|bride|Bride|Groom|
                |fiancée|fiance|fiancee|Fiancée|Fiance|Fiancee|Actor|Actors|
                |\slady|groom\s|
                |actor|an\sactor|actress|actresses|Actress|Actresses|an\sactress|businessman|Businessman|
                |businessmen|Businessmen|businesswoman|Businesswoman|businesswomen|Businesswomen|heroine|Heroine|cameraman|Cameraman|cameramen|Cameramen|camerawoman|Camerawoman|
                |camerawomen|Camerawomen|congressman|Congressman|congressmen|Congressmen|congresswoman|Congresswoman|congresswomen|Congresswomen|councilman|Councilman|
                |chairman|Chairman|chairwoman|Chairwoman|chairwomen|Chairwomen|chairmen|Chairmen|
                |assemblyman|Assemblyman|assemblymen|Assemblymen|assemblywoman|Assemblywoman|assemblywomen|Assemblywomen|milkmaid|Milkmaid|
                |councilwoman|Councilwoman|fireman|Fireman|firemen|Firemen|freshman|Freshman|freshmen\s|Freshmen\s|policeman|Policeman|policemen|Policemen|policewoman|Policewoman|
                |policewomen|Policewomen|postman|Postman|postmen|Postmen|postwoman|Postwoman|postwomen|Postwomen|repairman|Repairman|repairmen|Repairmen|salesman|Salesman|
                |saleswoman|Saleswoman|salesmen|Salesmen|saleswomen|Saleswomen|spokesman|Spokesman|spokeswoman|Spokeswoman|spokeswomen|Spokeswomen|spokesmen|Spokesmen|
                |sportsman|Sportsman|sportswoman|Sportswoman|sportswomen|Sportswomen|sportsmen|Sportsmen|SPORTSMAN|
                |workman|Workman|workmen|Workmen|\she\sdoes|He\sdoes|Does\she|\sshe\sdoes|She\sdoes|Does\sshe|\she\sis|\she\swas|Is\she|Is\sshe|\she\sis\.|\she\sis\?|
                |He’s\sread|She’s\sread|he's\sread|she's\sread|he’s\sread|she’s\sread|He's\sread|She's\sread|
                |\she\shas|He\sis\s|He\swas\s|\(he\sis|\(he\swas|He\shas\s|\sshe\sis\s|\sshe\swas\s|\(she\sis|\(she\swas|\sshe\sis\.|\sshe\sis\?|\sshe\shas\s|She\sis\s|She\swas\s|
                |She\shas\s|She/he|she/he|he/she|He/she|He/She|HerName|HisName|he’ll|she’ll|he'll|she'll|he’s|she’s|he’d|she’d|he's|she's|he'd|she'd|He’s|She’s|He’d|She’d|He's|
                |She's|He'd|She'd|\she\sisn’t|\sshe\sisn’t|\she\sisn't|\sshe\sisn't|He\sisn’t|She\sisn’t|He\sisn't|She\sisn't|\she\s|He\s|He’ll|\(he\s|\sshe\s|She\s|She’ll|\(she\s|
                |His\sare|His\sis|His\swas|His\s|\shis\.|\shim,|\sher\s|Hers\sare|Hers\swere|Her\sis|Her\swas|Her\s|\shers\.|\sher,|\sher\s“that|\sher\sthat'|
                |\sher\s"that|\shim\s|himself|herself|\shim\.|\sher\.|\shim\sboy|\sthem\skiddo|\sher\sgirl|\sher\sup|takes\sher\shome|take\sher\shome|\shers\s|\sher\sby|from\sher\sis|
                |from\sher\swas|From\sher\swas|
                |From\sher\sis|female\s|Female\s|female-|Female-|feminine\s|Feminine\s|‘feminine’\s|‘Feminine’\s|'feminine'\s|'Feminine'\s|feminine,\s|feminist\s|Feminist\s|masculine\s|
                |Masculine\s|‘masculine’\s|‘Masculine’\s|'masculine'\s|'Masculine'\s|masculine,\s|male\s|Male\s|male-|Male-|dudely\s|Dudely\s|womanly\s|Womanly\s|boyish\s|Boyish\s|girly\s|Girly\s|
                |manly\s|Manly\s|the Rev.\s|feminism|Feminism|femininity|masculinity|Femininity|Masculinity|bossy|pushy|Bossy|Pushy|emotional|hormonal|Emotional|
                |Hormonal|ditsy|frigid|Ditsy|Frigid|frumpy|Frumpy|shrill|Shrill|hysterical|Hysterical|mumsy|Mumsy|virile|Virile|misandry|Mysandry|misandrist|Misandrist|emperor|
                |empress|Emperor|Empress|queen|\sking\s|Queen|King\s|Kingdom|kingdom|princess|Princess|princesses|Princesses|prince\s|Prince\s|princes\s|Princes\s|manliness\s|womanliness\s|
                |womanhood|Womanhood|manhood|Manhood|maiden|Maiden|stableboy|Stableboy|stableboys|Stableboys|\sboy\s|Boy|\sboys|Boys|boyfriend|Boyfriend|boyfriends|Boyfriends|
                |daughter|Daughter|daughters|\sbro\s|\ssis\s|\sbros\s|\ssistas\s|brother\s|\ssister\s|brothers\s|\ssisters\s|Brother\s|\sSister\s|Brothers\s|\sSisters\s|fraternity|
                |\sbro\.|\ssis\.|\sbros\.|\ssistas\.|brother\.|\ssister\.|brothers\.|\ssisters\.|Brother\.|\sSister\.|Brothers\.|\sSisters\.|
                |\sbro,|\ssis,|\sbros,|\ssistas,|brother,|\ssister,|brothers,|\ssisters,|Brother,|\sSister,|Brothers,|\sSisters,|
                |sorority|brotherhood|sisterhood|girlhood|boyhood|Fraternity|Sorority|Brotherhood|Sisterhood|Boyhood|Girlhood|father|Father|fathers|Fathers|\sgirl\s|Girl|\sgirls|
                |Girls|girlfriend|Girlfriend|girlfriends|Girlfriends|guys|Guys|\sguy|Guy\s|good-guy|bad-guy|good-guys|bad-guys|Good-guy|Good\sfolk|Bad-guy|Good-guys|Bad-guys|husband|
                |Husband|ladies\sand\sgentleman|Ladies\sand\sgentleman|Ladies\sand\sGentleman|mankind|Mankind|womankind|Womankind|man-made|Man-made|mother|Mother|
                |mom\s|dad\s|mommy|daddy|mom\.|dad\.|mommy\.|daddy\.|Mom\s|Dad\s|Mommy|Daddy|nephew|Nephew|niece|Niece|uncle|Uncle|aunt.|aunt,|Aunt|widow|widower|
                |grandma\s|grandpa\s|
                |Widow|Widower|\sson\s|Son\s|\sson\.|Son\.|\ssons|steward\s|Steward\s|stewardess\s|Stewardess\s|stewardesses|Stewardesses|waiter\s|Waiter\s|waitress\s|Waitress\s|
                |waitresses|Waitresses|wife|Wife|wives|Wives|\sbishop|archbishop\s|clergyman|clergywoman|\sbishops|archbishops|clergymen|clergywomen|\sBishop|
                |Archbishop\s|Clergyman|Clergywoman|\sBishops|Archbishops|Clergymen|Clergywomen|deacon\s|deaconess\s|deacons|deaconesses|Deacon\s|Deaconess\s|
                |Deacons|Deaconesses|abbot\s|abbots|Abbot\s|Abbots|\snun\s|priest\s|\snuns|priests|Nun\s|Priest\s|Nuns|Priests|\spope\s|Pope\s|\sPopes\s|
                |priestess|priestesses|Priestess|Priestesses|priest\n|Priest\n|
                |\spopes\s|headmaster|headmistress\s|Headmaster|Headmistress\s|headmistresses|Headmistresses|\sher\sto\s|King’|king’|
                |\shis\s|aunt\s|\smaid\s|\smaid,|\smaid\.|\smaid:|\smaids|Maid\s|Maids|butler|Butler"""


list_conversions = re.findall(list_string, text)

print(list_conversions)

counted_list = Counter(list_conversions)

print(counted_list)

# Working on the following lists:
pers_pron_fem = [' she ' , ' she was ', ' she has ', ' she still has', 'She ', ' she does', 'she’s', ' she is ', 'She/he', "she's", " she isn't", ' she is.', 'Girl', 'girlfriend',
                ' she is?', 'She has ', 'She’s', 'She was ', 'she’ll', 'she’d', '(she ']

pers_pron_masc = [' he ', 'He ', 'He’s', ' he was', 'He’ll', 'he’s', 'he’d', '(he was', 'He was ', ' he is', 'He has ', 'He is ', ' he does', ' he has', 'He does', 'He’d',
                'he’ll', 'She/he', "He's", "he's", 'he’s read']

deter_pron_fem = [' her out', ' her over',' her ', ' her.', 'herself', ' her,', 'Her ',  'HerName', 'from her is', 'takes her home', 'from her was', ' her back to', ' hers.']

deter_pron_masc = [' his ', ' him ', 'His ', ' his.', 'himself', ' him.', ' him,', 'His are', 'His was']

noun_fem = [' women.', ' women ', 'queen', 'Queen', 'spokeswoman', 'wife', 'mother', 'Women', 'Mom ', 'mommy', 'businesswomen', 'daughter', 'businesswoman', ' woman ', ' women,',
            'Woman', ' Woman”', ' girl ', ' women’', 'Bride', 'Mother', 'aunt ', ' women"', " women'", 'congresswoman', 'congresswomen', ' sisters ', ' girls', ' woman.', " woman'",
            ' woman.', 'feminism', ' lady', 'niece', 'girlhood', 'Assemblywoman', 'aunt,', 'aunt.', 'Daughter', ' sisters,', ' sisters.', ' sisters ', ' sister,', ' sister.', 
            ' sister ', 'Milkmaid', 'milkmaid', 'priestess', 'Priestess', 'ladies', 'sportswoman', 'sportswomen', 'Sportswoman', 'Sportswomen', 'princess', 'chairwoman',
            'Chairwoman', 'chairwomen', 'Chairwomen', ' maid ', 'Maid ', 'Maids', ' maids', ' maid,', 'maid.', 'maid:', 'actress' , 'grandma ']

noun_masc = [' men ', 'father', ' man ', ' son.', 'husband', 'Prince ', 'spokesman', ' man.', ' men,', 'Boy', ' sons', ' men’', 'King ', 'emperor', ' man,', " man'", 'Kingdom',
            'King’', ' king ', 'Men ', 'Man ', 'an actor', ' actor', '-Man', ' guy', ' man’', ' Bishop', ' bishop', 'Pope ', '-man', 'than men',' men.', 'the Rev. ', 'good-guy',
            'bad-guy', 'dad ', '-actor', ' boy ', 'Men,', 'Man,' , "Men'", 'Guy ', ' man\n', ' son ', 'priest ', 'priest\n', 'Priest ', 'nephew', 'uncle', 'Brothers,', 'brother ',
            'sportsman', 'sportsmen', 'Sportsman', 'Sportsmen', 'SPORTSMAN', '-man ', 'businessman', 'brother,', 'brothers.', 'congressman', 'chairman', 'Chairman',
            'chairmen', 'Chairmen', 'butler', 'Butler', 'grandpa ', 'Son.']

adj_conn_fem = ['female ','Emotional', 'feminist ', 'emotional', 'Female ', 'femininity', 'feminine ']
adj_conn_masc = ['male-', 'Male ', 'male ', '‘masculine’ ', 'masculine, ', 'masculine ']
title_fem = ['Ms']
title_masc = ['Mr', 'Sir']

# Function that gives an integer, which is the quantity of conversions per category
values = []
def recounting(param):
    for original_unit in param:
        for key, value in counted_list.items():
            if key == original_unit:
                values.append(value)
    return sum(values)


num_fem_pron = recounting(pers_pron_fem)
print("Quantity of female pronouns (she) =                 " + str(num_fem_pron))

values = []
num_male_pron = recounting(pers_pron_masc)
print("Quantity of male pronouns (he) =                    " + str(num_male_pron))

values = []
num_det_fem = recounting(deter_pron_fem)
print("Quantity of female determiners (her, herself) =     " + str(num_det_fem))

values = []
num_det_masc = recounting(deter_pron_masc)
print("Quantity of male determiners (him, his, himself) =  " + str(num_det_masc))

values = []
num_noun_fem = recounting(noun_fem)
print("Quantity of female nouns =                          " + str(num_noun_fem))

values = []
num_noun_masc = recounting(noun_masc)
print("Quantity of male nouns =                            " + str(num_noun_masc))

values = []
num_adj_fem = recounting(adj_conn_fem)
print("Quantity of adjectives with femenine connotation =  " + str(num_adj_fem))

values = []
num_adj_masc = recounting(adj_conn_masc)
print("Quantity of adjectives with masculine connotation = " + str(num_adj_masc))

values = []
num_title_fem = recounting(title_fem)
print("Quantity of female titles =                         " + str(num_title_fem))

values = []
num_title_masc = recounting(title_masc)
print("Quantity of male titles =                           " + str(num_title_masc))


print("Total = " + str(num_male_pron + num_fem_pron + num_det_fem + num_det_masc + num_noun_fem + num_noun_masc + num_adj_masc + num_adj_fem + num_title_masc + num_title_fem))


# Function that gives a list containing units converted per category
values = []
def recounting_special(param):
    for original_unit in param:
        for key, value in counted_list.items():
            if key == original_unit:
                 values.append(key)
    return values

print("Female nouns = " + str(recounting_special(noun_fem)))

values = []
print("Male nouns = " + str(recounting_special(noun_masc)))

values = []
print("Adjectives with masculine connotation = " + str(recounting_special(adj_conn_masc)))

values = []
print("Adjectives with femenine connotation = " + str(recounting_special(adj_conn_fem)))

values = []
print("Male titles = " + str(recounting_special(title_masc)))

values = []
print("Female titles = " + str(recounting_special(title_fem)))