import re
from collections import Counter

text= u'''She is a woman'''

def neutral_converter(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(lambda x: '\\b' + x + '\\b', map(re.escape, substrings))))
    return regex.subn(lambda match: substitutions[match.group(0)], string) #subn to count conversions

dict_neutral = {'United Kingdom': 'United Kingdom', 'Staunton': 'Staunton', 'taunt': 'taunt', 'The Sportsman': 'The Sportsman,', #first exceptions
                'THE SPORTSMAN': 'THE SPORTSMAN', 'Queens, New York' : 'Queens, New York', 'emotional intelligence': 'emotional intelligence', #first exceptions
                'Emotional inteligence': 'Emotional inteligence', #first exceptions 

                #PENDING: ADD PLURAL FORMS FOR WORDS WIHOUT IT
                'men': 'people', 'Men': 'People', 'man' :  'person',  
                'Man': 'Person', 'MAN': 'PERSON', 'MEN': 'PEOPLE',
                'woman': 'person',  'Woman': 'Person', 'women': 'people', 
                'Women': 'People', 'WOMAN': 'PERSON', 'WOMEN': 'PEOPLE',
                'Mr': 'Mx', 'Ms': 'Mx', 'Sir': 'Mx', 'Lady': 'Mx', 'Lord': 'Mx', 
                'MR' : 'MX', 'MS': 'MX', 'SIR': 'MX', 'LORD': 'MX', 
                'lady': 'person', 'gentleman': 'person', 
                'ladies': 'people', 'gentlemen': 'people',  
                'LADY': 'PERSON', 'GENTLEMAN': 'PERSON', 
                'LADIES': 'PEOPLE', 'GENTLEMEN': 'PEOPLE',
                'bride': 'nearlywed', 'groom': 'nearlywed', 
                'Bride': 'Nearlywed', 'Groom': 'Nearlywed',
                'BRIDE': 'NEARLYWED', 'GROOM': 'NEARLYWED',
                'brides': 'nearlyweds', 'grooms': 'nearlyweds', 
                'Brides': 'Nearlyweds', 'Grooms': 'Nearlyweds',
                'BRIDES': 'NEARLYWEDS', 'GROOMS': 'NEARLYWEDS',
                'fiancée': 'nearlywed', 'fiance': 'nearlywed', 
                'fiancee': 'nearlywed', 'Fiancée': 'Nearlywed', 
                'FIANCÉE': 'NEARLYWED',
                'fiancées': 'nearlyweds', 'fiances': 'nearlyweds', 
                'fiancees': 'nearlyweds', 'Fiancées': 'Nearlyweds', 
                'FIANCÉES': 'NEARLYWEDS',
                'Fiance': 'Nearlywed', 'Fiancee': 'Nearlywed',
                'FIANCES': 'NEARLYWEDS', 'FIANCEES': 'NEARLYWEDS',
                'Fiances': 'Nearlyweds', 'Fiancees': 'Nearlyweds',
                'FIANCES': 'NEARLYWEDS',
                'actor': 'performer',  'Actor': 'Performer', 
                'ACTOR': 'PERFORMER', 
                'actress': 'performer', 'actresses': 'performers', 
                'Actress': 'Performer', 'Actresses': 'Performers', 
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
                'boys': 'kiddos', 'Boys': 'Kiddos', 
                'BOYS': 'KIDDOS',
                'boyfriend': 'partner', 'Boyfriend': 'Partner', 
                'BOYFRIEND': 'PARTNER',
                'boyfriends': 'partners', 'Boyfriends': 'Partners', 
                'BOYFRIENDS': 'PARTNERS',
                'daughter': 'child', 'Daughter': 'Child', 
                'daughters': 'children',
                'DAUGHTERS': 'CHILDREN',
                'bro': 'sibling', 'sis': 'sibling', 
                'BRO': 'SIBLING', 'SIS': 'SIBLING',
                'sistas': 'siblings', 
                'SISTAS': 'SIBLINGS',
                'brother': 'siblings', 'sister': 'sibling',
                'brothers': 'siblings', 'sisters': 'siblings',
                'SISTER': 'SIBLING', 'SISTERS': 'SIBLINGS', 
                'Brother': 'Sibling',  'Sister': 'Sibling', 
                'Brothers': 'Siblings',  'Sisters': 'Siblings',
                'BROTHER': 'SIBLING', 'BROTHER': 'SIBLING', 
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
                'girls': 'kiddos', 'Girls': 'Kiddos',
                'GIRL': 'KIDDO', 'GIRLS': 'KIDDOS',
                'girlfriend': 'partner', 'Girlfriend': 'Partner',
                'GIRLFRIEND': 'PARTNER', 
                'GIRLFRIENDS': 'PARTNERS',
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
                'NEPHEW': 'NIBLING',
                'niece': 'nibling', 'Niece': 'Nibling',
                'NIECE': 'NIBLING',
                'uncle': "parent's sibling", 'Uncle': "Parent's sibling", 
                'UNCLE': "PARENT'S SIBLING",
                'Aunt': "Parent's sibling", ' aunt': " parent's sibling",
                'AUNT': "PARENT'S SIBLING",
                'widow': 'surviving spouse', 'widower': 'surviving spouse', 
                'WIDOWER': 'SURVIVING SPOUSE',
                'Widow': 'Surviving spouse', 'Widower': 'Surviving spouse', 
                'WIDOW': 'SURVIVING SPOUSE',
                'son': 'child', 'Son': 'Child', 
                'SON': 'CHILD',
                'sons': 'children', 'Sons': 'Children', 
                'SONS': 'CHILDREN',
                'steward ': 'flight attendant ', 'Steward': 'Flight attendant',
                'STEWARD': 'FLIGHT ATTENDANT',
                'stewardess ': 'flight attendant', 'Stewardess ': 'Flight attendant',
                'STEWARDESS ': 'FLIGHT ATTENDANT', 
                'stewardesses': 'flight attendants', 'Stewardesses': 'Flight attendants',
                'STEWARDESSES': 'FLIGHT ATTENDANTS',
                'waiter': 'server', 'Waiter ': 'Server',
                'WAITER': 'SERVER',
                'waitress ': 'server', 'Waitress ': 'Server', 
                'WAITRESS ': 'SERVER',
                'waitresses': 'servers', 'Waitresses': 'Servers',
                'WAITRESSES': 'SERVERS',                
                'Bishop': 'Member of the clergy', 'bishop': 'member of the clergy',
                'BISHOP': 'MEMBER OF THE CLERGY',
                'bishops': 'members of the clergy','Bishops': 'Members of the clergy', 
                'BISHOPS': 'MEMBERS OF THE CLERGY',
                'archbishop': 'Higher rank member of the clergy', 'Archbishop': 'Higher rank member of the clergy',
                'ARCHBISHOP': 'HIGHER RANK MEMBER OF THE CLERGY',
                'archbishops': 'Higher rank members of the clergy','Archbishops': 'Higher rank members of the clergy',
                'ARCHBISHOPS': 'HIGHER RANK MEMBERS OF THE CLERGY',
                'clergyman': 'member of the clergy', 'clergywoman': 'member of the clergy', 
                'CLERGYMAN': 'MEMBER OF THE CLERGY',
                'clergymen': 'members of the clergy', 'clergywomen': 'members of the clergy',
                'CLERGYWOMAN': 'MEMBER OF THE CLERGY', 
                'Clergyman': 'Member of the clergy', 'Clergywoman': 'Member of the clergy',
                'CLERGYWOMEN': 'MEMBERS OF THE CLERGY',
                'Clergymen': 'Members of the clergy', 'Clergywomen': 'Members of the clergy',
                'CLERGYMEN': 'MEMBERS OF THE CLERGY',
                'deacon': 'member of the diaconate', 'Deacon': 'Member of the diaconate',
                'deacons': 'members of the diaconate', 'Deacons': 'Members of the diaconate',
                'DEACONS': 'MEMBERS OF THE DIACONATE',
                'deaconess': 'member of the diaconate', 'Deaconess': 'Member of the diaconate',
                'DEACONESS': 'MEMBER OF THE DIACONATE',
                'deaconesses': 'members of the diaconate','Deaconesses': 'Members of the diaconate',
                'abbot': 'head of monastery', 'abbots': 'heads of monastery',
                'ABBOT': 'HEAD OF MONASTERY', 
                'Abbot': 'Head of monastery', 'Abbots': 'Heads of monastery',
                'ABBOTS': 'HEADS OF MONASTERY',
                'nun': 'person belonging to a religious order',
                'NUN': 'PERSON BELONGING TO A RELIGIOUS ORDER', 
                'nuns': 'people belonging to a religious order',                 
                'Nun': 'Person belonging to a religious order',
                'NUNS': 'PEOPLE BELONGING TO A RELIGIOUS ORDER',
                'Nuns': 'Person belonging to a religious order', 
                'priest': 'performer of sacred rites in a religious community', 
                'PRIEST ': 'PERFORMER OF SACRED RITES IN A RELIGIOUS COMMUNITY',
                'priests': 'performers of sacred rites in a religious community',
                'Priest ': 'performer of sacred rites in a religious community',
                'PRIESTS': 'PERFORMERS OF SACRED RITES IN A RELIGIOUS COMMUNITY',
                'Priests': 'Performers of sacred rites in a religious community',
                'Priestess': 'Performer of sacred rites in a religious community', 
                'PRIESTESS': 'PERFORMER OF SACRED RITES IN A RELIGIOUS COMMUNITY',
                'Priestesses': 'Performers of sacred rites in a religious community',
                'priestess': 'performer of sacred rites in a religious community', 
                'PRIESTESSES': 'PERFORMERS OF SACRED RITES IN A RELIGIOUS COMMUNITY',
                'priestesses': 'performers of sacred rites in religious community',
                'pope': 'head of the Roman catholic church', 
                'POPE': 'HEAD OF THE ROMAN CATHOLIC CHURCH',
                'Pope': 'Head of the Roman catholic church', 
                'Popes': 'Heads of the Roman catholic church',
                'POPES': 'HEADS OF THE ROMAN CATHOLIC CHURCH', 
                'popes': 'heads of the Roman catholic church', 
                'headmaster': 'head', 'Headmaster': 'Head',
                'HEADMASTER': 'HEAD',
                'headmistress': 'head', 'Headmistress ': 'Head',
                'HEADMISTRESS': 'HEAD',
                'headmistresses': 'heads', 'Headmistresses': 'Heads',
                'HEADMISTRESSES': 'HEADS',                
                'maid': 'servant', 'Maid': 'Servant', 
                'MAID': 'SERVANT',
                'butler': 'main servant', 'Butler': 'Main servant', 
                'BUTLER': 'MAIN SERVANT',
                
                #Permutations
                'than a man': 'than a person', 'than men': 'than people',
                'than a woman': 'than a person', 'than women': 'than people',
                'Than a man': 'Than a person', 'Than men': 'Than people',
                'Than a woman': 'Than a person', 'Than women': 'Than people',
                'THAN A MAN': 'THAN A PERSON', 'THAN MEN': 'THAN PEOPLE',
                'THAN A WOMAN': 'THAN A PERSON', 'THAN WOMEN': 'THAN PEOPLE',
                
                'he is': 'they are', 'He is': 'They are',
                'he was': 'they were', 'He was': 'They were',            
                'he has': 'they have', 'He has': 'They have',
                'is he': 'are they', 'Is he': 'Are they', 
                'he does': 'they do', 'He does': 'They do',
                'does he': 'do they', 'Does he': 'Do they',
                'HE IS': 'THEY ARE', 
                'HE WAS': 'THEY WERE',            
                'HE HAS': 'THEY HAVE', 
                'IS HE': 'ARE THEY', 
                'HE DOES': 'THEY DO',
                'DOES HE': 'DO THEY',

                'she is': 'they are','She is': 'They are',
                'she was': 'they were', 'She was': 'They were',
                'she has': 'they have','She has': 'They have',
                'is she': 'are they','Is she': 'Are they',
                'she does': 'they do', 'She does': 'They do',
                'does she': 'do they', 'Does she': 'Do they',
                'SHE IS': 'THEY ARE',
                'SHE WAS': 'THEY WERE', 
                'SHE HAS': 'THEY HAVE',
                'IS SHE': 'ARE THEY',
                'SHE DOES': 'THEY DO', 
                'DOES SHE': 'DO THEY', 

                'she’s read': 'they’ve read', "she's read": "they've read", 
                'She’s read': 'They’ve read', "She's read": "They've read",
                'he’s read': 'they’ve read', "he's read": "they've read", 
                'He’s read': 'They’ve read', "He's read": "They've read",
                'SHE’S READ': 'THEY’VE READ', "SHE'S READ": "THEY'VE READ", 
                'HE’S READ': 'THEY’VE READ', "HE'S READ": "THEY'VE READ", 

                'an actor': 'a performer', 'an actress': 'a performer',
                'An actor': 'A performer', 'An actress': 'A performer',
                'AN ACTOR': 'A PERFORMER', 'AN ACTRESS': 'A PERFORMER',

                "he isn’t": "they aren’t", "she isn’t": "they aren’t", 
                "he isn't": "they aren't", "she isn't": "they aren't",
                "He isn’t": "They aren’t", "She isn’t": "They aren’t", 
                "He isn't": "They aren't", "She isn't": "They aren't",
                "HE ISN’T": "THEY AREN’T", "SHE ISN’T": "THEY AREN’T", 
                "HE ISN'T": "THEY AREN'T", "SHE ISN'T": "THEY AREN'T",

                'he still has': 'they still have', 'He still has': 'They still have', 
                'she still has': 'they still have', 'She still has': 'They still have', 
                'HE STILL HAS': 'THEY STILL HAVE', 
                'SHE STILL HAS': 'THEY STILL HAVE', 

                'His are': 'Theirs are', 'His is': 'Theirs is', 
                'His was': 'Theirs was', 'His were': 'Theirs were',
                'Hers are': 'Theirs are', 'Her is': 'Their is', 
                'Her was': 'Theirs was','Hers were': 'Theirs were',
                'his are': 'theirs are', 'his is': 'theirs is', 
                'his was': 'theirs was', 'his were': 'theirs were',
                'hers are': 'theirs are', 'her is': 'theirs is', 
                'her was': 'theirs was','hers were': 'theirs were',
                'HIS ARE': 'THEIRS ARE', 'HIS IS': 'THEIRS IS', 
                'HIS WAS': 'THEIRS WAS', 'HIS WERE': 'THEIRS WERE',
                'HERS ARE': 'THEIRS ARE', 'HER IS': 'THEIR IS', 
                'HER WAS': 'THEIRS WAS','HERS WERE': 'THEIRS WERE',

                'her “that' : 'them “that', 'her that' : 'them that', 'her "that' : 'them "that',
                'HER “THAT' : 'THEM “THAT', 'HER THAT' : 'THEM THAT', 'HER "THAT' : 'THEM "THAT',

                'from her is': 'from them is', 'From her is': 'From them is',
                'from her was': 'from them was', 'From her was': 'From them was',                
                'her back to' : 'them back to', 
                'her up': 'them up', 
                'her to': 'them to', 
                'her over': 'them over', 
                'her by': 'them by',
                'her out': 'them out',
                'takes her home': 'takes them home', 
                'take her home': 'take them home',
                'call him': 'call them', 'Call him': 'Call them',
                'call her': 'call them', 'Call her': 'Call them',
                'FROM HER IS': 'FROM THEM IS', 
                'FROM HER WAS': 'FROM THEM WAS',               
                'HER BACK TO' : 'THEM BACK TO', 
                'HER UP': 'THEM UP', 
                'HER TO': 'THEM TO', 
                'HER OVER': 'THEM OVER', 
                'HER BY': 'THEM BY',
                'HER OUT': 'THEM OUT',
                'TAKES HER HOME': 'TAKES THEM HOME', 
                'TAKE HER HOME': 'TAKE THEM HOME',
                'CALL HIM': 'CALL THEM', 
                'CALL HER': 'CALL THEM', 
                
                
                } #'paternalism': 'parentalism', 'misogynist': 'discriminatory', 'Misogynist': 'Discriminatory', 'matriarchal': 'egalitarian', 'patriarchal': 'egalitarian', 'Matriarchal': 'Egalitarian', 'Patriarchal': 'Egalitarian',

result = neutral_converter(text, dict_neutral)


print("This is your neutral text: " + str(result))


list_string = r"""\bUnited\sKingdom\b|\bStaunton\b|\btaunt\b|\bThe\sSportsman\b|\bTHE\sSPORTSMAN\b|\bQueens,\sNew\sYork\b|\bemotional\sintelligence\b|\bEmotional\sintelligence\b| # exceptions first
                |\bman\b|\bMan\b|\bmen\b|\bMen\b|\bWoman\b|\bwoman\b|\bwomen\b|\bWomen\b|\bShe\sstill\shas\b|\bshe\sstill\shas\b|\bhe\sstill\shas\b|\bHe\sstill\shas\b|\bthan\sa\sman\b|
                |\bthan\smen\b|\bher\sout\b|\bher\sover\b|\bher\sback\sto\b|\bthan\sa\swoman\b|\bthan\swomen\b|\bMr\b|\bMs\b|\bSir\b|\bLady\b|\bLord\b|\bgentleman\b|             
                |\bladies\b|\bgentlemen\b|\bbride\b|\bBride\b|\bGroom\b|\bfiancée\b|\bfiance\b|\bfiancee\b|\bFiancée\b|\bFiance\b|\bFiancee\b|\bActor\b|\bActors\b|
                |\blady\b|groom\b|\bactor\b|\ban\sactor\b|\bactress\b|\bactresses\b|\bActress\b|\bActresses\b|\ban\sactress\b|\bbusinessman\b|\bBusinessman\b|
                |\bbusinessmen\b|\bBusinessmen\b|\bbusinesswoman\b|\bBusinesswoman\b|\bbusinesswomen\b|\bBusinesswomen\b|\bheroine\b|\bHeroine\b|\bcameraman\b|\bCameraman\b|
                |\bcameramen\b|\bCameramen\b|\bcamerawoman\b|\bCamerawoman\b|\bcamerawomen\b|\bCamerawomen\b|\bcongressman\b|\bCongressman\b|\bcongressmen\b|\bCongressmen\b|
                |\bcongresswoman\b|\bCongresswoman\b|\bcongresswomen\b|\bCongresswomen\b|\bcouncilman\b|\bCouncilman\b|\bchairman\b|\bChairman\b|\bchairwoman\b|vChairwoman\b|
                |\bchairwomen\b|\bChairwomen\b|\bchairmen\b|\bChairmen\b|\bassemblyman\b|\bAssemblyman\b|\bassemblymen\b|\bAssemblymen\b|\bassemblywoman\b|\bAssemblywoman\b|
                |\bassemblywomen\b|\bAssemblywomen\b|\bmilkmaid\b|Milkmaid\b|\bcouncilwoman\b|\bCouncilwoman\b|\bfireman\b|\bFireman\b|\bfiremen\b|\bFiremen\b|\bfreshman\b|
                |\bFreshman\b|\bfreshmen\b|\bFreshmen\b|\bpoliceman\b|\bPoliceman\b|\bpolicemen\b|\bPolicemen\b|\bpolicewoman\b|\bPolicewoman\b|\bpolicewomen\b|\bPolicewomen\b|
                |\bpostman\b|\bPostman\b|\bpostmen\b|\bPostmen\b|\bpostwoman\b|\bPostwoman\b|\bpostwomen\b|\bPostwomen\b|\brepairman\b|\bRepairman\b|\brepairmen\b|\bRepairmen\b|
                |\bsalesman\b|\bSalesman\b|\bsaleswoman\b|\bSaleswoman\b|\bsalesmen\b|\bSalesmen\b|\bsaleswomen\b|\bSaleswomen\b|\bspokesman\b|\bSpokesman\b|\bspokeswoman\b|
                |\bSpokeswoman\b|\bspokeswomen\b|\bSpokeswomen\b|\bspokesmen\b|\bSpokesmen\b|\bsportsman\b|\bSportsman\b|\bsportswoman\b|\bSportswoman\b|\bsportswomen\b|
                |\bSportswomen\b|\bsportsmen\b|\bSportsmen\b|SPORTSMAN\b|\bworkman\b|\bWorkman\b|\bworkmen\b|\bWorkmen\b|\bhe\sdoes\b|\bHe\sdoes\b|\bDoes\she\b|\bshe\sdoes\b|
                |\bShe\sdoes\b|\bDoes\sshe\b|\bhe\sis\b|\bhe\swas\b|\bIs\she\b|\bIs\sshe\b|\bHe’s\srea\b|\bShe’s\sread\b|\bhe's\sread\b|\bshe's\sread\b|\bhe’s\sread\b|
                |\bshe’s\sread\b|\bHe's\sread\b|\bShe's\sread\b|\bhe\shas\b|\bHe\sis\b|\bHe\swas\b|\bHe\shas\b|\bshe\sis\b|\bshe\swas\b|\bshe\shas\b|                
                |\bShe\sis\b|\bShe\swas\b|\bShe\shas\b|\bShe/he\b|\bshe/he\b|\bhe/she\b|\bHe/she\b|\bHe/She\b|\bHerName\b|\bHisName\b|\bhe’ll\b|\bshe’ll\b|\bhe'll\b|
                |\bshe'll\b|\bhe’s\b|\bshe’s\b|\bhe’d\b|\bshe’d\b|\bhe's\b|\bshe's\b|\bhe'd\b|\bshe'd\b|\bHe’s\b|\bShe’s\b|\bHe’d\b|\bShe’d\b|\bHe's\b|
                |\bShe's\b|\bHe'd\b|\bShe'd\b|\bhe\sisn’t\b|\bshe\sisn’t\b|\bhe\sisn't\b|\bshe\sisn't\b|\bHe\sisn’t\b|\bShe\sisn’t\b|\bHe\sisn't\b|\bShe\sisn't\b|
                |\bhe\b|\bHe\b|\bHe’ll\b|\bshe\b|\bShe\b|\bShe’ll\b|\bHis\sare\b|\bHis\sis\b|\bHis\swas\b|\bHis\s\b|\bher\b|\bHers\sare\b|\bHers\swere\b|\bHer\sis\b|
                |\bHer\swas\b|\bHer\b|\bhers\.\b|\bher,\b|\bher\s“that\b|\bher\sthat'\b|\bher\s"that\b|\bhim\b|\bhimself\b|\bherself\b|\bhim\sboy\b|\bher\sgirl\b|\bher\sup\b|
                |\btakes\sher\shome\b|\btake\sher\shome\b|\bhers\b|\bher\sby\b|\bfrom\sher\sis\b|\bfrom\sher\swas\b|\bFrom\sher\swas\b|\bFrom\sher\sis\b|\bfemale\b|\bFemale\b|
                |\bfeminine\b|\bFeminine\b|\bfeminist\b|\bFeminist\b|\bmasculine\b|\bMasculine\b|\bmale\b|\bMale\b|\bdudely\b|\bDudely\b|\bwomanly\b|\bWomanly\b|
                |\bboyish\b|\bBoyish\b|\bgirly\b|\bGirly\b|\bmanly\b|\bManly\b|\bthe Rev.\b|\bfeminism\b|\bFeminism\b|\bfemininity\b|\bmasculinity\b|\bFemininity\b|
                |\bMasculinity\b|\bbossy\b|\bpushy\b|\bBossy\b|\bPushy\b|\bemotional\b|\bhormonal\b|\bEmotional\b|\bHormonal\b|\bditsy\b|\bfrigid\b|\bDitsy\b|\bFrigid\b|
                |\bfrumpy\b|\bFrumpy\b|\bshrill\b|\bShrill\b|\bhysterical\b|\bHysterical\b|\bmumsy\b|\bMumsy\b|\bvirile\b|\bVirile\b|\bmisandry\b|\bMysandry\b|\bmisandrist\b|
                |\bMisandrist\b|\bemperor\b|\bempress\b|\bEmperor\b|\bEmpress\b|\bqueen\b|\bking\b|\bQueen\b|\bKing\b|\bKingdom\b|\bkingdom\b|\bprincess\b|\bPrincess\b|\bprincesses\b|
                |\bPrincesses|\bprince\b|\bPrince\b|\bmanliness\b|\bwomanliness\b|\bwomanhood\b|\bWomanhood\b|\bmanhood\b|\bManhood\b|\bmaiden\b|\bMaiden\b|\bstableboy\b|
                |\bStableboy\b|\bboy\b|\bBoy\b|\bboyfriend\b|\bBoyfriend\b|\bdaughter\b|\bDaughter\b|\bbro\b|\bsis\b|\bbros\b|\bsistas\b|\bbrother\b|\bsister\b|\bBrother\b|
                |\bSister\b|\bfraternity\b|\bsorority\b|\bbrotherhood\b|\bsisterhood\b|\bgirlhood\b|\bboyhood\b|\bFraternity\b|\bSorority\b|\bBrotherhood\b|\bSisterhood\b|\bBoyhood\b|
                |\bGirlhood\b|\bfather\b|\bFather\b|\bfathers\b|\bFathers\b|\bgirl\b|\bGirl\b|\bgirlfriend\b|\bGirlfriend\b|\bguy\b|\bGuy\b|\bgood-guy\b|\bbad-guy\b|\bGood-guy\b|
                |\bBad-guy\b|\bhusband\b|\bHusband\b|\bladies\sand\sgentleman\b|\bLadies\sand\sgentleman\b|\bLadies\sand\sGentleman\b|\bmankind\b|\bMankind\b|\bwomankind\b|
                |\bWomankind\b|\bman-made\b|\bMan-made\b|\bmother\b|\bMother\b|\bmom\b|\bdad\b|\bmommy\b|\bdaddy\b|\bMom\b|\bDad\b|\bMommy\b|\bDaddy\b|\bnephew\b|\bNephew\b|
                |\bniece\b|\bNiece\b|\buncle\b|\bUncle\b|\bAunt\b|\bwidow\b|\bwidower\b|\bgrandma\b|\bgrandpa\b|\bWidow\b|\bWidower\b|\bson\b|\bSon\b|\bsteward\b|\bSteward\b|
                |\bstewardess\b|\bStewardess\b|\bstewardesses\b|\bStewardesses\b|\bwaiter\b|\bWaiter\b|\bwaitress\b|\bWaitress\b|\bwaitresses\b|\bWaitresses\b|\bwife\b|\bWife\b|
                |\bwives\b|Wives|\bbishop\b|\barchbishop\b|\bclergyman\b|\bclergywoman\b|\bclergymen\b|\bclergywomen\b|\bBishop\b|\bArchbishop\b|\bClergyman\b|\bClergywoman\b|
                |\bClergymen\b|\bClergywomen\b|\bdeacon\b|\bdeaconess\b|\bdeacons\b|\bdeaconesses\b|\bDeacon\b|\bDeaconess\b|\bDeacons\b|\bDeaconesses\b|\babbot\b|\bAbbot\b|\bnun\b|
                |\bpriest\b|\bpriests\b|\bNun\b|\bPriest\b|\bPriests\b|\bpope\b|\bPope\b|\bpriestess\b|\bpriestesses\b|\bPriestess\b|\bPriestesses\b|\bpriest\b|\bPriest\b|
                |\bpopes\b|\bheadmaster\b|\bheadmistress\b|\bHeadmaster\b|\bHeadmistress\b|\bheadmistresses\b|\bHeadmistresses\b|\bher\sto\b|\bhis\b|\baunt\b|\bmaid\b|
                |\bmaids\b|\bMaid\b|\bMaids\b|\bbutler\b|\bButler\b|\bBoys\b|\bboys\b|\bgirls\s|\bGirls\b|\bsons\b|\bSons\b"""


list_conversions = re.findall(list_string, text)

print(list_conversions)

counted_list = Counter(list_conversions)

print(counted_list)

# Working on the following lists:
pers_pron_fem = ['she', 'she was', 'she has', 'she\sstill\shas', 'She', 'she does', 'she’s', 'she is', 'She/he', "she's", "she isn't", 
                'She has', 'She’s', 'She was', 'she’ll', 'she’d']

pers_pron_masc = ['he was', '\bhe\b', 'He', 'He’s', 'He’ll', 'he’s', 'he', 'He was', 'he is', 'He has', 'He is', 'he does', 'he has', 'He does', 'He’d',
                'he’ll', 'She/he', "He's", "he's", 'he’s read']

deter_pron_fem = ['her out', 'her over','her', 'herself', 'Her', 'HerName', 'from her is', 'takes her home', 'from her was', 'her back to', 'hers']

deter_pron_masc = ['his', 'him', 'His', 'himself', 'His are', 'His was']

noun_fem = ['women', 'queen', 'Queen', 'spokeswoman', 'wife', 'mother', 'Women', 'Mom ', 'mommy', 'businesswomen', 'daughter', 'businesswoman', 'woman',
            'Woman', 'girl', 'Bride', 'Mother', 'aunt', 'congresswoman', 'congresswomen', 'sisters', 'girls', 
            'feminism', 'lady', 'niece', 'girlhood', 'Assemblywoman', 'Daughter', 'sisters', 'Girl', 'girlfriend',
            'sister', 'Milkmaid', 'milkmaid', 'priestess', 'Priestess', 'ladies', 'sportswoman', 'sportswomen', 
            'Sportswoman', 'Sportswomen', 'princess', 'chairwoman', 'Chairwoman', 'chairwomen', 'Chairwomen', 
            'maid', 'Maid', 'actress' , 'grandma']

noun_masc = ['men', 'father', 'man', 'husband', 'Prince ', 'spokesman', 'Boy', 'King', 'emperor', 'Kingdom',
            'King’', ' king ', 'Men', 'Man', 'an actor', 'actor', ' guy', ' Bishop', 'bishop', 'Pope ', 'than men', 'the Rev. ', 'good-guy',
            'bad-guy', 'dad ', 'boy', 'Guy', 'son', 'priest ', 'priest', 'Priest ', 'nephew', 'uncle', 'brother',
            'sportsman', 'sportsmen', 'Sportsman', 'Sportsmen', 'SPORTSMAN' , 'businessman', 'congressman', 'chairman', 'Chairman',
            'chairmen', 'Chairmen', 'butler', 'Butler', 'grandpa', 'Son', 'Boys', 'boys', 'sons', 'Sons']

adj_conn_fem = ['female ','Emotional', 'feminist ', 'emotional', 'Female ', 'femininity', 'feminine']
adj_conn_masc = ['Male ', 'male', 'masculine']
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