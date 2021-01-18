import re
from collections import Counter

text= u'''Men at work'''

def neutral_converter(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.subn(lambda match: substitutions[match.group(0)], string)   #subn to count conversions

#   TO BE CONSIDERED:
#   Words such as 'woman' and 'man' as an isolated word or placed at the end of a sentence or phrase, will not be converted since the converter recognizes 'woman ' or 'man ', that is to say, with a space succeeding the word. 
#   This is to prevent conversion of words such as 'Manchester' or 'womanizer' resulting in 'Personchester' and 'personizer'.

dict_neutral = {'United Kingdom': 'United Kingdom', 'Staunton': 'Staunton', 'taunt' : 'taunt', 'The Sportsman': 'The Sportsman,', #first exceptions
                'THE SPORTSMAN': 'THE SPORTSMAN', 'Queens, New York' : 'Queens, New York', 'emotional intelligence': 'emotional intelligence', #first exceptions
                'Emotional inteligence': 'Emotional inteligence', #first exceptions 
                ' man\n' :  ' person', ' man ' :  ' person ', 'Man ': 'Person ', ' man.': ' person.', ' man,': ' person,', " man’": " person’", " man'": " person'", '-man' : '-person ', 
                '-Man': '-Person', 'Man,': 'Person,', 'than a man': 'than a person',
                ' men ': ' people ', 'Men ': 'People ', ' men.': ' people.', ' men,': ' people,', " men’": " people’", " men'": " people'", '-men': '-people', 
                'Men,': 'People,', '-Men': '-People', 'than men': 'than people', "Men'": "People'", "Man'": "Person'",
                ' woman\n': ' person', ' woman ': ' person ', 'Woman': 'Person', ' woman.': ' person.', ' woman,': ' person,', " woman’": " person’", " woman'": " person'", 
                '-woman': '-person', '-Woman': '-Person', ' woman”': ' person”', ' Woman”': ' Person”', ' woman"': ' person"', ' Woman"': ' Person"', 'than a woman': 'than a person',
                ' women ': ' people ', 'Women': 'People', ' women.': ' people.', ' women,': ' people,', " women’": " people’", " women'": " people'", '-women': '-people', 
                '-Women': '-People', ' women”': ' people”', ' Women”': ' People”', ' women"': ' people"', ' Women"': ' People"', 'than women': 'than people', 
                'Mr': 'Mx', 'Ms': 'Mx', 'Sir': 'Mx', 'Lady': 'Mx', 'Lord': 'Mx', ' lady': ' person', 'gentleman': 'person', 'ladies': 'people', 'gentlemen': 'people',  
                'bride': 'nearlywed', 'groom ': 'nearlywed ', 'Bride': 'Nearlywed', 'Groom': 'Nearlywed', 
                'fiancée': 'nearlywed', 'fiance': 'nearlywed', 'fiancee': 'nearlywed', 'Fiancée': 'Nearlywed', 'Fiance': 'Nearlywed', 'Fiancee': 'Nearlywed',
                ' actor': ' performer', ' actors': ' performers', 'Actor': 'Performer', 'Actors': 'Performers', 'an actor': 'a performer', '-actor': '-performer',
                'actress': 'performer', 'actresses': 'performers', 'Actress': 'Performer', 'Actresses': 'Performers', 'an actress': 'a performer', 
                'assemblyman': 'member of assembly', 'assemblyman': 'Member of assembly', 'assemblymen': 'members of assembly', 'Assemblymen': 'Members of assembly',
                'assemblywoman': 'member of asssembly', 'Assemblywoman': 'Member of assembly', 'assemblywomen': 'members of assembly', 'Assemblywomen': 'Members of assembly',
                'businessman': 'business executive', 'Businessman': 'Business executive', 
                'businessmen': 'business executives', 'Businessmen': 'Business executives', 
                'businesswoman': 'business executive', 'Businesswoman': 'Business executive', 
                'businesswomen': 'business executives', 'Businesswomen': 'Business executives', 
                'heroine': 'hero', 'Heroine': 'Hero',
                'cameraman': 'camera operator', 'Cameraman': 'Camera operator', 
                'cameramen': 'camera operators', 'Cameramen': 'Camera operators', 
                'camerawoman': 'camera operator', 'Camerawoman': 'Camera operator', 
                'camerawomen': 'camera operators', 'Camerawomen': 'Camera operators', 
                'chairman': 'chairperson', 'Chairman': 'Chairperson', 
                'chairmen': 'chairpeople', 'Chairmen': 'Chairpeople', 
                'chairwoman': 'chairperson', 'Chairwoman': 'Chairperson', 
                'chairwomen': 'chairpeople', 'Chairwomen': 'Chairpeople', 
                'congressman': 'member of congress', 'Congressman': 'Member of congress', 'congressmen': 'members of congress', 'Congressmen': 'Members of congress',
                'congresswoman': 'member of congress', 'Congresswoman': 'Member of congress', 'congresswomen': 'members of congress', 'Congresswomen': 'Members of congress',
                'councilman': 'council person', 'Councilman': 'Council person', 
                'councilwoman': 'council person', 'Councilwoman': 'Council person', 
                'fireman': 'firefighter', 'Fireman': 'Firefighter', 
                'firemen': 'firefighters', 'Firemen': 'Firefighters', 
                'freshman': 'first-year student', 'Freshman': 'First-year student', 
                'freshmen ': 'first-year students', 'Freshmen ': 'First-year students', 
                'milkmaid' : 'milker', 'Milkmaid': 'Milker',
                'policeman': 'police officer', 'Policeman': 'Police officer', 
                'policemen': 'police officers', 'Policemen': 'Police officers', 
                'policewoman': 'police officer', 'Policewoman': 'Police officer', 
                'policewomen': 'police officers', 'Policewomen': 'Police officers', 
                'postman': 'postal worker', 'Postman': 'Postal worker',
                'postmen': 'postal workers', 'Postmen': 'Postal workers',
                'postwoman': 'postal worker', 'Postwoman': 'Postal worker',
                'postwomen': 'postal workers', 'Postwomen': 'Postal workers',
                'repairman' : 'repairer', 'Repairman': 'Repairer', 
                'repairmen' : 'repairers', 'Repairmen': 'Repairers', 
                'salesman': 'salesperson', 'Salesman': 'Salesperson',
                'saleswoman': 'salesperson', 'Saleswoman': 'Salesperson',
                'salesmen': 'salespeople', 'Salesmen': 'Salespeople',
                'saleswomen': 'salespeople', 'Saleswomen': 'Salespeople',
                'spokesman': 'spokesperson', 'Spokesman': 'Spokesperson',
                'spokeswoman': 'spokesperson', 'Spokeswoman': 'Spokesperson',
                'spokeswomen': 'spokespeople', 'Spokeswomen': 'Spokespeople',
                'spokesmen': 'spokespeople', 'Spokesmen': 'Spokespeople',
                'sportsman': 'athlete', 'Sportsman': 'Athlete',
                'sportswoman': 'athlete', 'Sportswoman': 'Athlete',
                'sportswomen': 'athletes', 'Sportswomen': 'Athletes',
                'sportsmen': 'athletes', 'Sportsmen': 'Athletes',
                'SPORTSMAN': 'ATHLETE',
                'workman': 'worker', 'Workman': 'Worker',
                'workmen': 'workers', 'Workmen': 'Workers',
                ' he does': ' they do', 'He does': 'They do', 'Does he': 'Do they',
                ' she does': ' they do', 'She does': 'They do', 'Does she': 'Do they',
                ' he is': ' they are', ' he was': ' they were', 'Is he': 'Are they', 'Is she': 'Are they', ' he is.': ' they are.', ' he is?': ' they are?', 
                ' he has': ' they have',
                'He is ': 'They are ', 'He was ': 'They were ', '(he is': '(they are', '(he was': '(they were',
                'He has ': 'They have ',
                ' she is ': ' they are ', ' she was ': ' they were ', '(she is': '(they are', '(she was': '(they were', ' she is.': ' they are.', ' she is?': ' they are?',
                ' she has ': ' they have ',
                'She is ': 'They are ', 'She was ': 'They were ',
                'She has ': 'They have ',
                'She/he': 'They', 'she/he': 'they', 'he/she': 'they', 'He/she': 'they', 'He/She': 'They', 
                'HerName': 'TheirName', 'HisName': 'TheirName',
                "he’ll": "they’ll", "she’ll": "they’ll", "he'll": "they'll", "she'll": "they'll", 
                'she’s read': 'they’ve read', "she's read": "they've read", 'She’s read': 'They’ve read', "She's read": "They've read",
                'he’s read': 'they’ve read', "he's read": "they've read", 'He’s read': 'They’ve read', "He's read": "They've read",
                "he’s": "they’re", "she’s": "they’re", "he’d": "they’d", "she’d": "they’d", "he's": "they're", "she's": "they're", "he'd": "they'd", "she'd": "they'd",             
                "He’s": "They’re", "She’s": "They’re", "He’d": "They’d", "She’d": "They’d", "He's": "They're", "She's": "They're", "He'd": "They'd", "She'd": "They'd",
                " he isn’t": " they aren’t", " she isn’t": " they aren’t", " he isn't": " they aren't", " she isn't": " they aren't",
                "He isn’t": "They aren’t", "She isn’t": "They aren’t", "He isn't": "They aren't", "She isn't": "They aren't",
                ' he still has ': ' they still have ', 'He still has ': 'They still have ', 
                ' she still has ': ' they still have ', 'She still has ': 'They still have ', 
                ' he ': ' they ', 'He ': 'They ', "He’ll": "They’ll", '(he ': '(they ',
                ' she ': ' they ', 'She ': 'They ', "She’ll": "They’ll", '(she ': '(they ',
                ' her over': ' them over', ' her by': ' them by', 
                ' his ': ' their ', 'His are': 'Theirs are', 'His is': 'Theirs is', 'His was': 'Theirs was','His ': 'Their ', ' his.': ' theirs.', ' him,': ' them,',
                ' her ': ' their ', 'Hers are': 'Theirs are', 'Hers were': 'Theirs were', 'Her is': 'Theirs is', 'Her was': 'Theirs was', 'Her ': 'Their ', ' hers.': ' theirs.', 
                ' her out': ' them out', ' her,': ' them,', ' her “that' : ' them “that', ' her that' : ' them that', ' her "that' : ' them "that',
                ' him ': ' them ', 'himself': 'themself', 'herself': 'themself', ' him.': ' them.', ' her.': ' them.', ' him boy': ' them kiddo', ' her girl': ' them kiddo', 
                ' her up': ' them up', 'takes her home': 'takes them home', 'take her home': 'take them home', 
                ' hers ': ' them ', 
                'from her is': 'from them is', 'From her is': 'From them is',
                'from her was': 'from them was', 'From her was': 'From them was',
                ' her back to' : ' them back to', 
                'female ': None, 'Female ': None, 'female-': None, 'Female-': None,
                'feminine ': None, 'Feminine ': None, "‘feminine’ ": None, "‘Feminine’ ": None, "'feminine' ": None, "'Feminine' ": None, 'feminine, ': None,
                'feminist ': 'gender-equality activist', 'Feminist ': 'Gender-equality activist',
                'misandrist': 'gender-equality activist', 'Misandrist': 'Gender-equality activist',
                'masculine ': None, 'Masculine ': None, "‘masculine’ ": None, "‘Masculine’ ": None, "'masculine' ": None, "'Masculine' ": None, 'masculine, ': None, 
                'male ': None, 'Male ': None, 'male-': None, 'Male-': None,
                'dudely ': None, 'Dudely ': None,
                'womanly ': None, 'Womanly ': None,
                'boyish ': None, 'Boyish ': None,
                'girly ': None, 'Girly ': None,
                'manly ': None, 'Manly ': None,
                'the Rev. ': None,
                'feminism': 'gender-equality activism', 'Feminism': 'Gender-equality activism', 
                'misandry': 'gender-equality activism', 'Misandry': 'Gender-equality activism',
                'femininity': 'humanity', 'masculinity': 'humanity', 'Femininity': 'Humanity', 'Masculinity': 'Humanity',
                'bossy': 'assertive', 'pushy': 'assertive', 'Bossy': 'Assertive', 'Pushy': 'Assertive',
                'emotional': 'empathetic', 'hormonal': 'passionate', 'Emotional': 'Empathetic', 'Hormonal': 'Passionate',
                'ditsy': 'silly', 'frigid': 'lacking sexual responsivness', 'Ditsy': 'Silly', 'Frigid': 'Lacking sexual responsivness',
                'frumpy': 'dowdy', 'Frumpy': 'Dowdy',
                'shrill': 'high pitched', 'Shrill': 'High pitched',
                'hysterical': 'irrational', 'Hysterical': 'Irrational',
                'mumsy': 'old fashioned', 'Mumsy': 'Old fashioned',
                'virile': 'energetic', 'Virile': 'Energetic',
                'emperor': 'ruler', 'empress': 'ruler', 'Emperor': 'Ruler', 'Empress': 'Ruler',  
                'queen': 'monarch', ' king ': ' monarch ', 'Queen': 'Monarch', 'King ': 'Monarch ', 'Kingdom': 'Realm', 'kingdom': 'realm', 'King’': 'Monarch’',
                'king’': 'monarch’',
                'princess': "monarch's child", 'Princess': "Monarch's child", 
                'princesses': "monarch's children", 'Princesses': "Monarch's children", 
                'prince ': "monarch's child ", 'Prince ': "Monarch's child ", 
                'princes ': "monarch's children ", 'Princes ': "Monarch's children ", 
                'manliness ': 'humanness',
                'womanliness ': 'humannness',
                'womanhood': 'humanhood', 'Womanhood': 'Humanhood',
                'manhood': 'humanhood',  'Manhood': 'Humanhood',
                'maiden' : 'kiddo', 'Maiden': 'Kiddo',
                'stableboy': 'kiddo', 'Stableboy': 'Kiddo', 'stableboys': 'kiddos', 'Stableboys': 'Kiddos',
                ' boy ': ' kiddo ', 'Boy': 'Kiddo', ' boys': ' kiddos', 'Boys': 'Kiddos',
                'boyfriend': 'partner', 'Boyfriend': 'Partner', 'boyfriends': 'partners', 'Boyfriends': 'Partners',
                'daughter': 'child', 'Daughter': 'Child', 'daughters': 'children',
                ' bro ': ' sibling ',  ' sis ': ' sibling ', ' bros ': ' siblings ',  ' sistas ': ' siblings ', 
                'brother ': 'sibling ',  ' sister ': ' sibling ', 'brothers ': 'siblings ',  ' sisters ': ' siblings ', 'Brother ': 'Sibling ',  ' Sister ': ' Sibling ', 
                'Brothers ': 'Siblings ',  ' Sisters ': ' Siblings ',
                ' bro.': ' sibling.',  ' sis.': ' sibling.', ' bros.': ' siblings.',  ' sistas.': ' siblings.', 
                'brother.': 'sibling.',  ' sister.': ' sibling.', 'brothers.': 'siblings.',  ' sisters.': ' siblings.', 'Brother.': 'Sibling.',  ' Sister.': ' Sibling.', 
                'Brothers.': 'Siblings.',  ' Sisters.': ' Siblings.', 
                ' bro,': ' sibling,',  ' sis,': ' sibling,', ' bros,': ' siblings,',  ' sistas,': ' siblings,',
                'brother,': 'sibling,',  ' sister,': ' sibling,', 'brothers,': 'siblings,',  ' sisters,': ' siblings,', 'Brother,': 'Sibling,',  ' Sister,': ' Sibling,', 
                'Brothers,': 'Siblings,',  ' Sisters,': ' Siblings,', 
                'fraternity': 'fellowship', 'sorority': 'fellowship', 'brotherhood': 'fellowship', 'sisterhood': 'fellowship', 'girlhood': 'fellowship', 'boyhood': 'fellowship', 
                'Fraternity': 'Fellowship', 'Sorority': 'Fellowship', 'Brotherhood': 'Fellowship', 'Sisterhood': 'Fellowship', 'Boyhood': 'Fellowship', 'Girlhood': 'Fellowship', 
                'father': 'parent', 'Father': 'Parent', 'fathers': 'parents', 'Fathers': 'Parents',
                ' girl ': ' kiddo ', 'Girl': 'Kiddo', ' girls': ' kiddos', 'Girls': 'Kiddos',
                'girlfriend': 'partner', 'Girlfriend': 'Partner', 'girlfriends': 'partners', 'Girlfriends': 'Partners',
                'guys': 'everybody', 'Guys': 'Everybody',
                ' guy': ' folk', 'Guy ': 'Folk ', 'good-guy': 'good folk', 'bad-guy': 'bad folk', 'good-guys': 'good folks', 'bad-guys': 'bad folks',
                'Good-guy': 'Good folk', 'Bad-guy': 'Bad folk', 'Good-guys': 'Good folks', 'Bad-guys': 'Bad folks',
                'husband': 'spouse', 'Husband': 'Spouse',
                'ladies and gentleman': 'everybody', 'Ladies and gentleman': 'Everybody', 'Ladies and Gentleman': 'Everybody',
                'mankind': 'humankind', 'Mankind': 'Humankind',
                'womankind': 'humankind', 'Womankind': 'Humankind',
                'man-made': 'artificial', 'Man-made': 'Artificial',
                'mother': 'parent', 'Mother': 'Parent', 
                'mom ': 'mada ', 'dad ': 'mada ', 'mommy': 'maddy', 'daddy': 'maddy', 'mom.': 'mada.', 'dad.': 'mada.', 'mommy.': 'maddy.', 'daddy.': 'maddy.',
                'Mom ': 'Mada ', 'Dad ': 'Mada ', 'Mommy': 'Maddy', 'Daddy': 'Maddy',
                'grandma ' : 'grandparent', 'grandpa ': 'grandparent ',
                'nephew': 'nibling', 'Nephew': 'Nibling',
                'niece': 'nibling', 'Niece': 'Nibling',
                'uncle': "parent's sibling", 'Uncle': "Parent's sibling", 
                'Aunt': "Parent's sibling", 'her aunt': "their parent's sibling", ' aunt': " parent's sibling", 
                'aunt,': "parent's sibling,", 'aunt.': "parent's sibling.",
                'widow': 'surviving spouse', 'widower': 'surviving spouse', 'Widow': 'Surviving spouse', 'Widower': 'Surviving spouse', 
                ' son ': ' child ', 'Son ': 'Child ', ' sons': ' children', ' son.': ' child.', 'Son.': 'Child.',
                'steward ': 'flight attendant ', 'Steward ': 'Flight attendant ',
                'stewardess ': 'flight attendant', 'Stewardess ': 'Flight attendant', 'stewardesses': 'flight attendants', 'Stewardesses': 'Flight attendants',
                'waiter ': 'server', 'Waiter ': 'Server',
                'waitress ': 'server', 'Waitress ': 'Server', 'waitresses': 'servers', 'Waitresses': 'Servers',
                'wife': 'spouse', 'Wife': 'Spouse', 'wives': 'spouses', 'Wives': 'Spouses',
                ' bishop': ' member of the clergy', 'archbishop ': 'member of the clergy ', 'clergyman': 'member of the clergy', 'clergywoman': 'member of the clergy', 
                ' bishops': ' members of the clergy', 'archbishops': 'members of the clergy', 'clergymen': 'members of the clergy', 'clergywomen': 'members of the clergy',
                ' Bishop': ' Member of the clergy', 'Archbishop ': 'Member of the clergy ', 'Clergyman': 'Member of the clergy', 'Clergywoman': 'Member of the clergy', 
                ' Bishops': ' Members of the clergy', 'Archbishops': 'Members of the clergy', 'Clergymen': 'Members of the clergy', 'Clergywomen': 'Members of the clergy',
                'deacon ': 'member of the diaconate ', 'deaconess ': 'member of the diaconate ', 'deacons': 'members of the diaconate', 'deaconesses': 'members of the diaconate',
                'Deacon ': 'Member of the diaconate ', 'Deaconess ': 'Member of the diaconate ', 'Deacons': 'Members of the diaconate', 'Deaconesses': 'Members of the diaconate',
                'abbot ': 'head of monastery ', 'abbots': 'heads of monastery', 'Abbot ': 'Head of monastery ', 'Abbots': 'Heads of monastery',
                ' nun ': ' Person belonging to a religious order ', 'priest ': 'performer of sacred rites in a religious community ', ' nuns': ' person belonging to a religious order', 
                'priests': 'members of a religious community',
                'Nun ': 'Person belonging to a religious order ', 'Priest ': 'performers of sacred rites in a religious community ', 'Nuns': 'Person belonging to a religious order', 
                'Priests': 'Performers of sacred rites in a religious community',
                'Priestess': 'Performer of sacred rites in a religious community', 'Priestesses': 'Performers of sacred rites in a religious community',
                'priestess': 'performer of sacred rites in a religious community', 'priestesses': 'performers of sacred rites in religious community',
                ' pope ': ' head of the Roman catholic church ', 'Pope ': 'Head of the Roman catholic church ', ' Popes ': ' Heads of the Roman catholic church ', 
                ' popes ': ' heads of the Roman catholic church ', 
                'headmaster': 'head', 'headmistress ': 'head ', 'Headmaster': 'Head', 'Headmistress ': 'Head ',
                'headmistresses': 'heads', 'Headmistresses': 'Heads',
                ' her to ': ' them to ',
                ' maid ': ' servant ',  'Maid ': 'Servant ', ' maid,': ' servant,', ' maids': ' servants', ' maid.': ' servant.', ' maid:': ' servant:', 
                'Maids': 'Servants',
                'butler': 'main servant', 'Butler': 'Main servant', 
                } #'paternalism': 'parentalism', 'misogynist': 'discriminatory', 'Misogynist': 'Discriminatory', 'matriarchal': 'egalitarian', 'patriarchal': 'egalitarian', 'Matriarchal': 'Egalitarian', 'Patriarchal': 'Egalitarian',

result = neutral_converter(text, dict_neutral)


print("This is your neutral text: " + str(result))


list_string = r"""United\sKingdom|Staunton|taunt|The\sSportsman|THE\sSPORTSMAN|Queens,\sNew York|emotional\sintelligence|Emotional\sintelligence| # exceptions first
                |She\sstill\shas|\sshe\sstill\shas|\she\sstill\shas|\sHe\sstill\shas|\shis\s|\swoman\s|\sman\s|Man\s|\sman\.|\sman,|\sman’|\sman'|-man\s|-Man|than\sa\sman\s|\smen\s|
                |\sman\n|\swoman\n|Men\s|Men,|\smen\.|\smen,|\smen’|\smen'|-men|-Men|than\smen|Man,|Man'|Men'|\sher\sout|\sher\sover|\sher\sback\sto|aunt\s|
                |Woman|\swoman\.|\swoman,|\swoman’|\swoman'|-woman|-Woman|\swoman”|\sWoman”|\swoman"|\sWoman"|than\sa\swoman|\swomen\s|Women|\swomen\.|\swomen,|
                |\swomen’|\swomen'|-women|-Women|\swomen”|\sWomen”|\swomen"|\sWomen"|than\swomen|Mr|Ms|Sir|Lady|Lord|\slady|gentleman|ladies|gentlemen|bride|groom\s|Bride|Groom|
                |fiancée|fiance|fiancee|Fiancée|Fiance|Fiancee|\sactor|\sactors|Actor|Actors|an\sactor|-actor|actress|actresses|Actress|Actresses|an\sactress|businessman|Businessman|
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
                |\smaid\s|\smaid,|\smaid\.|\smaid:|\smaids|Maid\s|Maids|butler|Butler"""


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