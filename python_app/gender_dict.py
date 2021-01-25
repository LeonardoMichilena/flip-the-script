import re


re_plural = re.compile("E*S$") 


def singular(word):
    return re_plural.sub("", word)


def plural_suffix(word):
    match = re_plural.search(word)

    if match == None:
        return ''
  
    return match.group().lower()


def plural(word):
    return singular(word) + plural_suffix(word)


def word_variants(word_pair):
    m, f = word_pair

    return [
      [singular(m), singular(f)],
      [plural(m), plural(f)],
    ]


def parse_switch_dict(data_string):
    re_separator = re.compile(r",[ \n]*")
    
    # reverse to respect the order of precedence
    pair_strings = reversed(re_separator.split(data_string))

    return {
        key: value
        for pair_string in pair_strings
        for key, value in word_variants(pair_string.split(" "))
    }


gender_switch_data_string = u"""maleS femaleS, maleness femaleness, 
himself herself, he she, his her, him her,
Mr Mrs, Mister Missus, Ms Mr, Master Miss, Master Mistress, 
uncleS auntS, nephewS nieceS, sonS daughterS, grandsonS granddaughterS, stepsonS stepsisterS,
brotherS sisterS, man woman, men women, boyS girlS, paternal maternal, paternity maternity,
grandfatherS grandmotherS, GodfatherS GodmotherS, GodsonS GoddaughterS, 
fiancéS fiancéeS, fianceS fianceeS, husband wife, husbands wives, 
fatherS motherS, bachelorS spinsterS, groomS brideS, widowerS widowS, 
KnightS DameS, Sir Madam, Sir DameS, KingS QueenS, DukeS DuchessES, PrinceS PrincessES, 
MarquessES MarchionessES, EarlS CountessES, ViscountS ViscountessES, ladS lassES, sir madamS, 
gentleman lady, gentlemen ladies, Lord Lady, Lords Ladies, dude lady, dudes ladies, 
BaronS BaronessES, baronetS baronetessES, stallionS mareS, ramS eweS, coltS fillieS, 
billy nanny, billies nannies, bullS cowS, godS goddessES, godheadS goddessheadS, 
godhood goddesshood, godliness goddessliness, godly goddessly, gramps grandma, heroS heroineS, 
undies nickers, sweat glow, jackarooS jillarooS, gigoloS hookerS, landlord landlady, landlords landladies, 
manservantS maidservantS, actorS actressES, CountS CountessES, 
EmperorS EmpressES, giantS giantessES, heirS heiressES, hostS hostessES, 
lionS lionessES, managerS manageressES, murdererS murderessES, 
priestS priestessES, poetS poetessES, shepherdS shepherdessES, 
stewardS stewardessES, tigerS tigressES, waiterS waitressES, 
fireman firewoman, firemen firewomen, policeman policewoman, 
policemen policewomen, congressman congresswoman, congressmen congresswomen, 
anchorman anchorwoman, anchormen anchorwomen, cameraman camerawoman, 
cameramen camerawomen, showman showwoman, showmen showwomen, barman barmaid, 
barmen barmaids, cockS henS, drakeS henS, dogS vixenS, tomS tibS, 
boarS sowS, buckS roeS, peacockS peahenS, gander goose, ganders geese, friarS nunS, 
archdukeS archduchessES, boyish girly, bro sis, bros sistas, deaconS deaconessES,
monkS nunS, bloke gal, boyfriendS girlfriendS, manly womanly, squireS damselS, 
boyhoodS girlhoodS, brotherhoodS sisterhoodS, grandpaS grandmaS, margraveS margravineS, 
matriar patriar, patriarchy matriarchy, matroniz patroniz, airman airwoman, airmen airwomen, 
alderman alderwoman, aldermen alderwomen, assemblyman assemblywoman, assemblymen assemblywomen, 
bogeyman bogeywoman, bogeymen bogeywomen, bondsman bondswoman, bondsmen bondswomen, businessman businesswoman, 
businessmen businesswomen, caveman cavewoman, cavemen cavewomen, chairman chairwoman, 
chairmen chairwomen, clergyman clergywoman, clergymen clergywomen, congressman congresswoman, 
congressmen congresswomen, councilman councilwoman, councilmen councilwomen, 
countrymen countrywomen, craftsman craftswoman, craftsmen craftswomen, 
daddy mommy, daddies mommies, dadS momS, papa mama, momma poppa, manhood womanhood, 
mankind womankind, manly womanly, doorman doorwoman, doormen doorwomen, fisherman fisherwoman, 
fishermen fisherwomen, foremen forewomen, freshman freshwoman, freshmen freshwomen, 
garbageman garbagewoman, garbagemen garbagewomen, guyS galS, handyman handywoman, handymen handywomen,
hangman hangwoman, hangmen hangwomen, henchman henchwoman, henchmen henchwomen, 
journeyman journeywoman, journeymen journeywomen, kinsman kinswoman, kinsmen kinswomen, 
klansman klanswoman, layman laywoman, laymen laywomen, madman madwoman, madmen madwomen,  
mailman mailwoman, mailmen mailwomen, mansplain ladysplain, marksman markswoman, 
marksmen markswomen, middleman middlewoman, middlemen middlewomen, milkman milkwoman, 
milkmen milkwomen, misandr misogyn, nobleman noblewoman, noblemen noblewomen,
ombudsman ombudswoman, ombudsmen ombudswomen, postman postwoman, postmen postwomen, 
repairman repairwoman, repairmen repairwomen, salesman saleswoman, salesmen saleswomen, 
sandman sandwoman, sandmen sandwomen, serviceman servicewoman, servicemen servicewomen, 
snowman snowwoman, spaceman spacewoman, spacemen spacewomen, spokesman spokeswoman, 
spokesmen spokeswomen, sportsmen sportswomen, statesman stateswoman, statesmen stateswomen, 
stepbrother stepsister, stepmother stepfather, stepsister stepbrother,
superman superwoman, supermen superwomen, unman unwoman, watchman watchwoman, 
watchmen watchwomen, weatherman weatherwoman, weathermen weatherwomen, 
whitemaleness whitefemaleness, workman workwoman, workmen workwomen, masculinity femininity, 
misandry misogyny, manliness womanliness, clergyman clergywoman, clergymen clergywomen,
headmasterS headmistressES, chauffeurS chauffeuseS, witchES wizardS, brother-in-law sister-in-law,
father-in-law mother-in-law, son-in-law daughter-in-law, schoolboy schoolgirl,
Englishman Englishwoman, DJ DJane, conductorS conductressES"""


gender_switch_dict = parse_switch_dict(gender_switch_data_string)