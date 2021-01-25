import re

from gender_dict import gender_switch_dict

text=u''''This is of hers. She called her up and jumped. We were discussing something about firemen, and I said, “An advanced computer user knows what he needs…”, [when] a female colleague, suddenly interrupted, “Are you saying women cannot be advanced computer users?” I thought she was joking and laughed, but then realised I was the only one laughing, and she was looking at me as if I were her personal enemy'. '''

def reverse_dict(d):
    return {
        value : key
        for key, value in d.items()
    }


def capitalize_dict(d):
    return {
        key.capitalize() : value.capitalize()
        for key, value in d.items()
    }


def complete_switch_dict(d):
    rev = reverse_dict(d)
  
    return {
        **d,
        **rev,
        **capitalize_dict(d),
        **capitalize_dict(rev)
    }


def text_transformer(switch_dict):
    def possibly_replace(string):
        if string in switch_dict:
            return switch_dict[string]
        return string

    re_words = re.compile(rf"\b({'|'.join(switch_dict.keys())})\b")

    def transformer(text):
        return "".join(
            possibly_replace(part)
            for part in re_words.split(text)
        )
    
    return transformer


pre_gender_converter = text_transformer(complete_switch_dict(gender_switch_dict))

result = pre_gender_converter(text)

dict_pron = {' his ': ' her ', ' her ': ' his ',
              'His is': 'Her is', 'Her is': 'His is',
              'His was': 'His was', 'Her was': 'His was',
              'His ': 'Her ', 'Her ': 'His ', 
              ' him,': ' her,', ' her,': ' him,', 
              'Hers are': 'His are', 'His are': 'Hers are',
              'Hers were': 'His were', 'Hers are': 'His are',
              ' him out': ' her out', ' her out': ' him out', 
              ' him ': ' her ', 
              ' him.': ' her.', ' her.': ' him.',
              ' hers ': ' him ',
              ' hers.': ' his.', ' his.': ' hers.',
              ' her by': ' him by', ' him by': ' her by',
              ' her up': ' him up', ' him up': ' her up',
              ' her “that' : ' him “that', ' him “that' : ' her “that',
              ' her that' : ' him that', ' him that' : ' her that',
              ' her "that' : ' him "that', ' him "that' : ' her "that',
              ' him boy': ' her girl', ' her girl': ' him boy', 
              'takes her home': 'takes him home', 'take her home': 'take him home', 
              'takes him home': 'takes her home', 'take him home': 'take her home', 
              'from her.': 'from him.', 'From her.': 'From him.',
              'from him': 'from her', 'From him': 'From her',
              'known for her': 'known for his', 'known for his': 'known for her'
              }


#Function for determiner issue (her his, her him)
def pron_converter(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string) 

gender_converter = pron_converter(result, dict_pron)

print(gender_converter)

#text=u''''This is of hers. She called her up and jumped. We were discussing something about firemen, and I said, “An advanced computer user knows what he needs…”, [when] a female colleague, suddenly interrupted, “Are you saying women cannot be advanced computer users?” I thought she was joking and laughed, but then realised I was the only one laughing, and she was looking at me as if I were her personal enemy'. '''

list_string = r"""\bmale\b|\bfemale\b|\bmaleness\b|\bfemaleness\b|males\b|\bfemales\b|
                |\bhimself\b|\bherself\b|\bhe\b|\bshe\b|\bhis\b|\bher\b|\bhers\b|\bhim\b|\bShe\b|\bHe\b|
                |\bMr\b|\bMrs\b|\bMister\b|\bMissus\b|\bMs\b|\bMr\b|\bMaster\b|\bMiss\b|\bMaster\b|\bMistress\b| 
                |\buncles\b|\baunts\b|\bnephews\b|\bnieces\b|\bsons\b|\bdaughters\b|\bgrandsons\b|\bgranddaughters\b|\bstepsons\b|
                |\bstepsisters\b|
                |\buncle\b|\baunt\b|\bnephew\b|\bniece\b|\bson\b|\bdaughter\b|\bgrandson\b|\bgranddaughter\b|\bstepson\b|
                |\bstepsister\b|
                |\bbrother\b|\bsister\b|\bman\b|\bwoman\b|\bmen\b|\bwomen\b|\bboy\b|\bgirl\b|\bpaternal\b|\bmaternal\b|
                |\bpaternity\b|\bmaternity\b|
                |\bbrothers\b|\bsisters\b|\bboys\b|\bgirls\b|
                |\bgrandfathers\b|\bgrandmothers\b|\bGodfathers\b|\bGodmothers\b|\bGodsons\b|\bGoddaughters\b| 
                |\bfiancés\b|\bfiancées\b|\bfiances\b|\bfiancees\b|\bhusband\b|\bwife\b|\bhusbands\b|\bwives\b|
                |\bgrandfather\b|\bgrandmother\b|\bGodfather\b|\bGodmother\b|\bGodson\b|\bGoddaughter\b| 
                |\bfiancé\b|\bfiancée\b|\bfiance\b|\bfiancee\b|
                |\bfather\b|\bmother\b|\bbachelor\b|\bspinster\b|\bgroom\b|\bbride\b|\bwidower\b|\bwidow\b| 
                |\bKnight\b|\bDame\b|\bSir\b|\bMadam\b|\bSir\b|\bDame\b|\bKing\b|\bQueen\b|\bDuke\b|\bDuchess\b|
                |\bPrince\b|\bPrincess\b|
                |\bfathers\b|\bmothers\b|\bbachelors\b|\bspinsters\b|\bgrooms\b|\bbrides\b|\bwidowers\b|\bwidows\b| 
                |\bKnights\b|\bDames\b|\bDames\b|\bKings\b|\bQueens\b|\bDukes\b|\bDuchesses\b|
                |\bPrinces\b|\bPrincesses\b|
                |\bMarquess\b|\bMarchioness\b|\bEarl\b|\bCountess\b|\bViscount\b|\bViscountess\b|\blad\b|\blass\b|
                |\bsir\b|\bmadam\b|
                |\bMarquesses\b|\bMarchionesses\b|\bEarlS\b|\bCountesses\b|\bViscounts\b|\bViscountesses\b|\blads\b|\blasses\b|
                |\bmadams\b|
                |\bgentleman\b|\blady\b|\bgentlemen\b|\bladies\b|\bLord\b|\bLady\b|\bLords\b|\bLadies\b|\bdude\b|\blady\b|
                |\bdudes\b|\bladies\b|
                |\bBarons\b|\bBaronesses\b|\bbaronets\b|\bbaronetesses\b|\bstallions\b|\bmares,\b|\brams\b|\bewes\b|\bcoltS\b|\bfillies\b|
                |\bBaron\b|\bBaroness\b|\bbaronet\b|\bbaronetess\b|\bstallion\b|\bmare,\b|\bram\b|\bewe\b|\bcolt\b|\bfillie\b|
                |\bbilly\b|\bnanny\b|\bbillies\b|\bnannies\b|\bbull\b|\bcow\b|\bgod\b|\bgoddess\b|\bgodhead\b|\bgoddesshead\b|
                |\bbull\b|\bcows\b|\bgods\b|\bgoddesses\b|\bgodheads\b|\bgoddessheads\b|
                |\bgodhood\b|\bgoddesshood\b|\bgodliness\b|\bgoddessliness\b|\bgodly\b|\bgoddessly\b|\bgramps\b|\bgrandma\b|
                |\bhero\b|\bheroine\b|\bheros\b|\bheroines\b|
                |\bundies\b|\bnickers\b|\bsweat\b|\bglow\b|\bjackaroo\b|\bjillaroo\b|\bgigolo\b|\bhooker\b|\blandlord\b|\blandlady\b| 
                |\blandlords\b|\blandladies\b|\bjackaroos\b|\bjillaroos\b|\bgigolos\b|\bhookers\b|
                |\bmanservant\b|\bmaidservant\b|\bactor\b|\bactress\b|\bCount\b|\bCountess\b|
                |\bEmperor\b|\bEmpress\b|\bgiant\b|\bgiantess\b|\bheir\b|\bheiress\b|\bhost\b|\bhostess\b| 
                |\blion\b|\blioness\b|\bmanager\b|\bmanageress\b|\bmurderer\b|\bmurderes\b| 
                |\bpriest\b|\bpriestess\b|\bpoet\b|\bpoetess\b|\bshepherd\b|\bshepherdess\b|
                |\bsteward\b|\bstewardess\b|\btiger\b|\btigress\b|\bwaiter\b|\bwaitress\b|
                |\bmanservants\b|\bmaidservants\b|\bactors\b|\bactresses\b|\bCounts\b|\bCountesses\b|
                |\bemperors\b|\bempresses\b|\bgiants\b|\bgiantesses\b|\bheirs\b|\bheiresses\b|\bhosts\b|\bhostesses\b| 
                |\blions\b|\blionesses\b|\bmanagers\b|\bmanageresses\b|\bmurderers\b|\bmurderesses\b| 
                |\bpriests\b|\bpriestesses\b|\bpoets\b|\bpoetesses\b|\bshepherds\b|\bshepherdesses\b|
                |\bstewards\b|\bstewardesses\b|\btigers\b|\btigresses\b|\bwaiters\b|\bwaitresses\b|
                |\bfireman\b|\bfirewoman\b|\bfiremen\b|\bfirewomen\b|\bpoliceman\b|\bpolicewoman\b|
                |\bpolicemen\b|\bpolicewomen\b|\bcongressman\b|\bcongresswoman\b|\bcongressmen\b|\bcongresswomen\b| 
                |\banchorman\b|\banchorwoman\b|\banchormen\b|\banchorwomen\b|\bcameraman\b|\bcamerawoman\b| 
                |\bcameramen\b|\bcamerawomenb|\bshowmanb|\bshowwomanb|\bshowmenb|\bshowwomenb|\bbarmanb|\bbarmaid\b| 
                |\bbarmen\b|\bbarmaidsb|\bcockb|\bhenb|\bdrake\b|\bhen\b|\bdog\b|\bvixen\b|\btom\b|\btib\b|
                |\bboar\b|\bsow\b|\bbuck\b|\broe\b|\bpeacock\b|\bpeahen\b|\bgander\b|\bgoose\b|\bganders\b|\bgeese\b|
                |\bfriar\b|\bnun\b| 
                |\bfriars\b|\bnuns\b|\bcocksb|\bhens\b|\bdrakes\b|\bhens\b|\bdogs\b|\bvixens\b|\btoms\b|\btibs\b|
                |\bboars\b|\bsows\b|\bbucks\b|\broes\b|\bpeacocks\b|\bpeahens\b|\barchduke\b|\barchduchess\b|
                |\barchdukes\b|\barchduchesses\b|\bboyish\b|\bgirly\b|\bbro\b|\bsis\b|\bbros\b|\bsistas\b|\bdeacon\b|\bdeaconess\b|
                |\bmonk\b|\bnun\b|\bbloke\b|\bgal\b|\bboyfriend\b|\bgirlfriend\b|\bmanly\b|\bwomanly\b|\bsquire\b|\bdamsel\b|
                |\bboyhood\b|\bgirlhood\b|\bbrotherhood\b|\bsisterhood\b|\bgrandpa\b|\bgrandma\b|\bmargrave\b|\bmargravine\b|
                |\bdeacons\b|\bdeaconesses\b|
                |\bmonks\b|\bnuns\b|\bboyfriends\b|\bgirlfriends\b|\bsquires\b|\bdamsels\b|
                |\bboyhoods\b|\bgirlhoods\b|\bbrotherhoods\b|\bsisterhoods\b|\bgrandpas\b|\bgrandmas\b|\bmargraves\b|\bmargravines\b|
                |\bmatriar\b|\bpatriar\b|\bpatriarchy\b|\bmatriarchy\b|\bmatroniz\b|\bpatroniz\b|\bairman\b|\bairwoman\b|\bairmen\b|\bairwomen\b| 
                |\balderman\b|\balderwoman\b|\baldermen\b|\balderwomen\b|\bassemblyman\b|\bassemblywoman\b|\bassemblymen\b|\bassemblywomen\b|
                |\bbogeyman\b|\bbogeywoman\b|\bbogeymen\b|\bbogeywomen\b|\bbondsman\b|\bbondswoman\b|\bbondsmen\b|\bbondswomen\b|\bbusinessman\b|\bbusinesswoman\b| 
                |\bbusinessmen\b|\bbusinesswomen\b|\bcaveman\b|\bcavewoman\b|\bcavemen\b|\bcavewomen\b|\bchairman\b|\bchairwoman\b|
                |\bchairmen\b|\bchairwomen\b|\bclergyman\b|\bclergywoman\b|\bclergymen\b|\bclergywomen\b|\bcongressman\b|\bcongresswoman\b| 
                |\bcongressmen\b|\bcongresswomen\b|\bcouncilman\b|\bcouncilwoman\b|\bcouncilmen\b|\bcouncilwomen\b| 
                |\bcountrymen\b|\bcountrywomen\b|\bcraftsman\b|\bcraftswoman\b|\bcraftsmen\b|\bcraftswomen\b|
                |\bdaddy\b|\bmommy\b|\bdaddies\b|\bmommies\b|\bdad\b|\bmom\b|\bpapa\b|\bmama\b|\bmomma\b|\bpoppa\b|\bmanhood\b|\bwomanhood\b| 
                |\bmankind\b|\bwomankind\b|\bmanly\b|\bwomanly\b|\bdoorman\b|\bdoorwoman\b|\bdoormen\b|\bdoorwomen\b|\bfisherman\b|
                |\bfisherwoman\b|\bdads\b|\bmoms\b|
                |\bfishermen\b|\bfisherwomen\b|\bforemen\b|\bforewomen\b|\bfreshman\b|\bfreshwoman\b|\bfreshmen\b|\bfreshwomen\b|
                |\bgarbageman\b|\bgarbagewoman\b|\bgarbagemen\b|\bgarbagewomen\b|\bguyS\b|\bgalS\b|\bhandyman\b|\bhandywoman\b|\bhandymen\b|\bhandywomen\b|
                |\bhangman\b|\bhangwoman\b|\bhangmen\b|\bhangwomen\b|\bhenchman\b|\bhenchwoman\b|\bhenchmen\b|\bhenchwomen\b|
                |\bjourneyman\b|\bjourneywoman\b|\bjourneymen\b|\bjourneywomen\b|\bkinsman\b|\bkinswoman\b|\bkinsmen\b|\bkinswomen\b|
                |\bklansman\b|\bklanswoman\b|\blayman\b|\blaywoman\b|\blaymen\b|\blaywomen\b|\bmadman\b|\bmadwoman\b|\bmadmen\b|\bmadwomen\b|  
                |\bmailman\b|\bmailwoman\b|\bmailmen\b|\bmailwomen\b|\bmansplain\b|\bladysplain\b|\bmarksman\b|\bmarkswoman\b|
                |\bmarksmen\b|\bmarkswomen\b|\bmiddleman\b|\bmiddlewoman\b|\bmiddlemen\b|\bmiddlewomen\b|\bmilkman\b|\bmilkwoman\b| 
                |\bmilkmen\b|\bmilkwomen\b|\bmisandr\b|\bmisogyn\b|\bnobleman\b|\bnoblewoman\b|\bnoblemen\b|\bnoblewomen\b|
                |\bombudsman\b|\bombudswoman\b|\bombudsmen\b|\bombudswomen\b|\bpostman\b|\bpostwoman\b|\bpostmen\b|\bpostwomen\b|
                |\brepairman\b|\brepairwoman\b|\brepairmen\b|\brepairwomen\b|\bsalesman\b|\bsaleswoman\b|\bsalesmen saleswomen\b|
                |\bsandman\b|\bsandwoman\b|\bsandmen\b|\bsandwomen\b|\bserviceman\b|\bservicewoman\b|\bservicemen\b|\bservicewomen\b| 
                |\bsnowman\b|\bsnowwoman\b|\bspaceman\b|\bspacewoman\b|\bspacemen\b|\bspacewomen\b|\bspokesman\b|\bspokeswoman\b|
                |\bspokesmen\b|\bspokeswomen\b|\bsportsmen\b|\bsportswomen\b|\bstatesman\b|\bstateswoman\b|\bstatesmen\b|\bstateswomen\b| 
                |\bstepbrother\b|\bstepsister\b|\bstepmother\b|\bstepfather\b|\bstepsister\b|\bstepbrother\b|
                |\bsuperman\b|\bsuperwoman\b|\bsupermen\b|\bsuperwomen\b|\bunman\b|\bunwoman\b|\bwatchman\b|\bwatchwoman\b| 
                |\bwatchmen\b|\bwatchwomen\b|\bweatherman\b|\bweatherwoman\b|\bweathermen\b|\bweatherwomen\b|
                |\bwhitemaleness\b|\bwhitefemaleness\b|\bworkman\b|\bworkwoman\b|\bworkmen\b|\bworkwomen\b|\bmasculinity\b|\bfemininity\b| 
                |\bmisandry\b|\bmisogyny\b|\bmanliness\b|\bwomanliness\b|\bclergyman\b|\bclergywoman\b|\bclergymen\b|\bclergywomen\b|
                |\bheadmaster\b|\bheadmistress\b|\bchauffeur\b|\bchauffeuse\b|\bwitch\b|\bwizard\b|\bbrother-in-law\b|\bsister-in-law\b|
                |\bheadmasters\b|\bheadmistresses\b|\bchauffeurs\b|\bchauffeuses\b|\bwitches\b|\bwizards\b|
                |\bfather-in-law\b|\bmother-in-law\b|\bson-in-law\b|\bdaughter-in-law\b|\bschoolboy\b|\bschoolgirl\b|
                |\bEnglishmam\b|\bEnglishwoman\b|\bDJ\b|\bDJane\b|\bconductor\b|\bconductress\b|\bconductors\b|\bconductresses\b"""

list_conversions = re.findall(list_string, text)

print(list_conversions)