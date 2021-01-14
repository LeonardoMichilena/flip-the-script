from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)



@app.route("/mascfem", methods=["GET"])
def jsInfo():
    req = requests.get("http://localhost:3000/show") 
    print(req.content)
    data = json.loads(req.content)
    print(data)
    # textData = data['articles'][0]['article']
    textData = data['articles'][0]['article']

    print(textData)
    

    import re

    list_m_f = u"""maleS femaleS, maleness femaleness, 
    him her, himself herself, his her, his hers, he she, 
    Mr Mrs, Mister Missus, Ms Mr, Master Miss, Master Mistress, 
    uncleS auntS, nephewS nieceS, sonS daughterS, grandsonS granddaughterS, 
    brotherS sisterS, man woman, men women, boyS girlS, paternal maternal, 
    grandfatherS grandmotherS, GodfatherS GodmotherS, GodsonS GoddaughterS, 
    fiancéS fiancéeS, fianceS fianceeS, husband wife, husbands wives, 
    fatherS motherS, bachelorS spinsterS, groomS brideS, widowerS widowS, 
    KnightS DameS, Sir DameS, KingS QueenS, DukeS DuchessES, PrinceS PrincessES, 
    Lord Lady, Lords Ladies, MarquessES MarchionessES, EarlS CountessES, 
    ViscountS ViscountessES, ladS lassES, sir madam, gentleman lady, 
    gentlemen ladies, BaronS BaronessES, stallionS mareS, ramS eweS, 
    coltS fillieS, billy nanny, billies nannies, bullS cowS, 
    godS goddessES, heroS heroineS, undies nickers, sweat glow, 
    jackarooS jillarooS, gigoloS hookerS, landlord landlady, landlords landladies, 
    manservantS maidservantS, actorS actressES, CountS CountessES, 
    EmperorS EmpressES, giantS giantessES, heirS heiressES, hostS hostessES, 
    lionS lionessES, managerS manageressES, murdererS murderessES, 
    priestS priestessES, poetS poetessES, shepherdS shepherdessES, 
    stewardS stewardessES, tigerS tigressES, waiterS waitressES, 
    fireman firewoman, firemen firewomen, policeman policewoman, 
    policemen policewomen, congressman congresswoman, congressmen congresswomen, 
    anchorman anchorwoman, anchormen anchorwomen, cameraman camerawoman, 
    cameramen camerawomen, showman showwoman, showmen showwomen, barman barmaid, 
    barmen barmaids, cockS henS, dogS bitchES, drakeS henS, dogS vixenS, tomS tibS, 
    boarS sowS, buckS roeS, peacockS peahenS, gander goose, ganders geese, friarS nunS, 
    monkS nunS, archduchessES archdukeS, baronetS baronetessES, boyhood girlhood, 
    boyish girly, bro sis, bros sistas, comte comtesse, dadS momS, 
    deaconS deaconessES, duchessES dukeS, dude lady, dudelier womanlier, 
    dudeliest womanliest, dudely womanly, dudes ladies, earlS countessES, 
    fem masc, gal fellow, gentleman lady, gentlemen ladies, girlier dudelier, 
    girliest dudeliest, godhead goddesshead, godhood goddesshood, 
    godliness goddessliness, godly goddessly, gramps grandma, grandmaS grandpaS, 
    guyS galS, maiden stableboy, mama papa, manhood womanhood, mankind womankind, 
    manliness womanliness, manly womanly, marquis marquise, maternity paternity, 
    menz ladiez, mgtow wgtow, momma poppa, papa mama, priestS priestessES, 
    radfem radmasc, widow widower"""

    # compile() function returns the specified source as a code object, ready to be executed.


    re_nl = re.compile(r",[ \n]*")                          #raw string line separator
    m_f = [tok.split(" ") for tok in re_nl.split(list_m_f)] #split strings from the list_m_f, which in fact is a long string

    switch = {}
    words = []
    
    re_plural = re.compile("E*S$")                    #compile the strings with the plural form "S"
    re_ES = re.compile("ES$")                         #compile the strings with the plural form "ES"
    
    def gender_plural(m,f):                         #replace function
      yield re_plural.sub("",m),re_plural.sub("",f)
      yield re_ES.sub("es",m),re_ES.sub("es",f)
      yield re_plural.sub("s",m),re_plural.sub("s",f)
    
    def gender_cap_plural(m,f):
      for m,f in gender_plural(m,f):
        yield m.capitalize(), f.capitalize()
        yield m,f
    
    def gender_switch_role_cap_plural(m,f):
      for m,f in gender_cap_plural(m,f):
        yield m,f
        yield f,m
    
    for m,f in m_f:
      for xy,xx in gender_switch_role_cap_plural(m,f):
        if xy not in switch: 
          switch[xy]=xx
          words.append(xy)
    
    words = "|".join(words)
    
    re_word = re.compile(r"\b("+words+r")\b")
    
    def flip_the_script(text):
      text = re_word.split(text)
      return "".join([ word+switch[gen] for word,gen in zip(text[::2],text[1::2])])+text[-1]


    text= textData

    result = flip_the_script(text)

    return("This is your reverse gendered text: " + str(result))

    """ return(textData) """

    """ return render_template('index.html', data=data['article']) """

@app.route("/neutral", methods=["GET"])
def neutral():
    req = requests.get("http://localhost:3000/showneutral") 
    print(req.content)
    data = json.loads(req.content)
    print(data)
    textData = data['articles'][0]['article']
    print(textData)
    text= textData

    import re
    from collections import Counter

   

    def neutral_converter(string, substitutions):
        substrings = sorted(substitutions, key=len, reverse=True)
        regex = re.compile('|'.join(map(re.escape, substrings)))
        return regex.sub(lambda match: substitutions[match.group(0)], string)   #subn to count conversions

    dict_neutral = {' man ': ' person ', 'Man ': 'Person ', ' man.': ' person.', ' man,': ' person,', " man’": " person’", " man'": " person'", '-man': '-person', 
                    '-Man': '-Person', 'than a man': 'than a person',
                    ' men ': ' people ', 'Men ': 'People ', ' men.': ' people.', ' men,': ' people,', " men’": " people’", " men'": " people'", '-men': '-people', 
                    '-Men': '-People', 'than men': 'than people',
                    ' woman ': ' person ', 'Woman': 'Person', ' woman.': ' person.', ' woman,': ' person,', " woman’": " person’", " woman'": " person'", 
                    '-woman': '-person', '-Woman': '-Person', ' woman”': ' person”', ' Woman”': ' Person”', ' woman"': ' person"', ' Woman"': ' Person"', 'than a woman': 'than a person',
                    ' women ': ' people ', 'Women': 'People', ' women.': ' people.', ' women,': ' people,', " women’": " people’", " women'": " people'", '-women': '-people', 
                    '-Women': '-People', ' women”': ' people”', ' Women”': ' People”', ' women"': ' people"', ' Women"': ' People"', 'than women': 'than people', 
                    'Mr': 'Mx', 'Ms': 'Mx', 'Sir': 'Mx', 'Lady': 'Mx', 'Lord': 'Mx', ' lady': ' person', 'gentleman': 'person', 'ladies': 'people', 'gentlemen': 'people',  
                    'bride': 'nearlywed', 'groom ': 'nearlywed ', 'Bride': 'Nearlywed', 'Groom': 'Nearlywed', 
                    'fiancée': 'nearlywed', 'fiance': 'nearlywed', 'fiancee': 'nearlywed', 'Fiancée': 'Nearlywed', 'Fiance': 'Nearlywed', 'Fiancee': 'Nearlywed',
                    ' actor': ' performer', ' actors': ' performers', 'Actor': 'Performer', 'Actors': 'Performers', 'an actor': 'a performer', '-actor': '-performer',
                    'actress': 'performer', 'actresses': 'performers', 'Actress': 'Performer', 'Actresses': 'Performers', 'an actress': 'a performer', 
                    'businessman': 'business executive', 'Businessman': 'Business executive', 
                    'businessmen': 'business executives', 'Businessmen': 'Business executives', 
                    'businesswoman': 'business executive', 'Businesswoman': 'Business executive', 
                    'businesswomen': 'business executives', 'Businesswomen': 'Business executives', 
                    'heroine': 'hero', 'Heroine': 'Hero',
                    'cameraman': 'camera operator', 'Cameraman': 'Camera operator', 
                    'cameramen': 'camera operators', 'Cameramen': 'Camera operators', 
                    'camerawoman': 'camera operator', 'Camerawoman': 'Camera operator', 
                    'camerawomen': 'camera operators', 'Camerawomen': 'Camera operators', 
                    'congressman': 'member of congress', 'Congressman': 'Member of congress', 'congressmen': 'members of congress', 'Congressmen': 'Members of congress',
                    'congresswoman': 'member of congress', 'Congresswoman': 'Member of congress', 'congresswomen': 'members of congress', 'Congresswomen': 'Members of congress',
                    'councilman': 'council person', 'Councilman': 'Council person', 
                    'councilwoman': 'council person', 'Councilwoman': 'Council person', 
                    'fireman': 'firefighter', 'Fireman': 'Firefighter', 
                    'firemen': 'firefighters', 'Firemen': 'Firefighters', 
                    'freshman': 'first-year student', 'Freshman': 'First-year student', 
                    'freshmen ': 'first-year students', 'Freshmen ': 'First-year students', 
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
                    "he’s": "they’re", "she’s": "they’re", "he’d": "they’d", "she’d": "they’d", "he's": "they're", "she's": "they're", "he'd": "they'd", "she'd": "they'd",
                    "He’s": "They’re", "She’s": "They’re", "He’d": "They’d", "She’d": "They’d", "He's": "They're", "She's": "They're", "He'd": "They'd", "She'd": "They'd",
                    " he isn’t": " they aren’t", " she isn’t": " they aren’t", " he isn't": " they aren't", " she isn't": " they aren't",
                    "He isn’t": "They aren’t", "She isn’t": "They aren’t", "He isn't": "They aren't", "She isn't": "They aren't",
                    ' he still has ': ' they still have ', 'He still has ': 'They still have ', 
                    ' she still has ': ' they still have ', 'She still has ': 'They still have ', 
                    ' he ': ' they ', 'He ': 'They ', "He’ll": "They’ll", '(he ': '(they ',
                    ' she ': ' they ', 'She ': 'They ', "She’ll": "They’ll", '(she ': '(they ',
                    ' his ': ' their ', 'His are': 'Theirs are', 'His is': 'Theirs is', 'His was': 'Theirs was','His ': 'Their ', ' his.': ' theirs.', ' him,': ' them,',
                    ' her ': ' their ', 'Hers are': 'Theirs are', 'Hers were': 'Theirs were', 'Her is': 'Theirs is', 'Her was': 'Theirs was', 'Her ': 'Their ', ' hers.': ' theirs.', 
                    ' her out': ' them out', ' her,': ' them,', ' her “that' : ' them “that', ' her that' : ' them that', ' her "that' : ' them "that',
                    ' him ': ' them ', 'himself': 'themself', 'herself': 'themself', ' him.': ' them.', ' her.': ' them.', ' him boy': ' them kiddo', ' her girl': ' them kiddo', 
                    ' her up': ' them up', 'takes her home': 'takes them home', 'take her home': 'take them home', 
                    ' hers ': ' them ',
                    ' her by': ' them by', 
                    'from her': 'from them', 'from him': 'from them', 'From her': 'From them', 'From him': 'From them',
                    'female ': None, 'Female ': None, 'female-': None, 'Female-': None,
                    'feminine ': None, 'Feminine ': None, "‘feminine’ ": None, "‘Feminine’ ": None, "'feminine' ": None, "'Feminine' ": None, 'feminine, ': None,
                    'feminist ': None, 'Feminist ': None,
                    'masculine ': None, 'Masculine ': None, "‘masculine’ ": None, "‘Masculine’ ": None, "'masculine' ": None, "'Masculine' ": None, 'masculine, ': None, 
                    'male ': None, 'Male ': None, 'male-': None, 'Male-': None,
                    'dudely ': None, 'Dudely ': None,
                    'womanly ': None, 'Womanly ': None,
                    'boyish ': None, 'Boyish ': None,
                    'girly ': None, 'Girly ': None,
                    'manly ': None, 'Manly ': None,
                    'the Rev. ': None,
                    'feminism': 'activism', 'Feminism': 'Activism', 
                    'femininity': 'humanity', 'masculinity': 'humanity', 'Femininity': 'Humanity', 'Masculinity': 'Humanity',
                    'misogynist': 'discriminatory', 'Misogynist': 'Discriminatory', 
                    'bossy': 'assertive', 'pushy': 'assertive', 'Bossy': 'Assertive', 'Pushy': 'Assertive',
                    'emotional': 'empathetic', 'hormonal': 'passionate', 'Emotional': 'Empathetic', 'Hormonal': 'Passionate',
                    'ditsy': 'silly', 'frigid': 'lacking sexual responsivness', 'Ditsy': 'Silly', 'Frigid': 'Lacking sexual responsivness',
                    'frumpy': 'dowdy', 'Frumpy': 'Dowdy',
                    'shrill': 'high pitched', 'Shrill': 'High pitched',
                    'hysterical': 'irrational', 'Hysterical': 'Irrational',
                    'mumsy': 'old fashioned', 'Mumsy': 'Old fashioned',
                    'virile': 'energetic', 'Virile': 'Energetic',
                    'matriarchal': 'egalitarian', 'patriarchal': 'egalitarian', 
                    'Matriarchal': 'Egalitarian', 'Patriarchal': 'Egalitarian',
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
                    'nephew': 'nibling', 'Nephew': 'Nibling',
                    'niece': 'nibling', 'Niece': 'Nibling',
                    'uncle': "parent's sibling", 'Uncle': "Parent's sibling", 
                    ' aunt': " parent's sibling", 'Aunt': "Parent's sibling", 
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
                    ' nun ': ' member of a religious community ', 'priest ': 'member of a religious community ', ' nuns ': ' members of a religious community ', 
                    'priests ': 'members of a religious community',
                    ' Nun ': ' Member of a religious community ', 'Priest ': 'Member of a religious community ', ' Nuns ': ' Members of a religious community ', 
                    'Priests ': 'Members of a religious community',
                    ' pope ': ' head of the Roman catholic church ', 'Pope ': 'Head of the Roman catholic church ', ' Popes ': ' Heads of the Roman catholic church ', 
                    ' popes ': ' heads of the Roman catholic church ', 
                    'headmaster': 'head', 'headmistress ': 'head ', 'Headmaster': 'Head', 'Headmistress ': 'Head ',
                    'headmistresses': 'heads', 'Headmistresses': 'Heads',
                    ' her to ': ' them to '
                    }

    text = str(textData)

    result = neutral_converter(text, dict_neutral)

    return("This is your neutral text: " + str(result)) 

   
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)