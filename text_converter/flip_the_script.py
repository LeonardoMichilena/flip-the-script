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


text=u''''We were discussing something, and I said, “An advanced computer user knows what she needs…”, [when] a male colleague, suddenly interrupted, “Are you saying men cannot be advanced computer users?” I thought he was joking and laughed, but then realised I was the only one laughing, and he was looking at me as if I were his personal enemy'. '''

result = flip_the_script(text)

print("This is your reverse gendered text: " + str(result))

