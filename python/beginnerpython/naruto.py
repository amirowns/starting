from tkinter import *

# make list of character names
# somehow connect them to the build  path of that character
# display it on the tkinter gui

NormalNaruto = "[Normal]Naruto"
NormalSakura = "[Normal]Sakura"
NormalSasuke = "[Normal]Sasuke"
NormalTemari = "[Normal]Temari"
NormalSasori = "[Normal]Sasori"
NormalAnbu = "[Normal]Anbu"
NormalSai = "[Normal]Sai"
NormalYamato = "[Normal]Yamato"
NormalKabuto = "[Normal]Kabuto"
NormalKarin = "[Normal]Karin"
#########################################################################
MagicJiraiya = "[Magic]Jiraiya"
MagicKankuro = "[Magic]Kankuro"
MagicOrochimaru = "[Magic]Orochimaru"
MagicSasuke = "[Magic]Sasuke"
MagicJugo = "[Magic]Jugo"
MagicChoji = "[Magic]Choji"
MagicShikamaru = "[Magic]Shikamaru"
MagicZetsu = "[Magic]Zetsu"
MagicTsunade = "[Magic]Tsunade"
MagicKiba = "[Magic]Kiba"
##########################################################################
RareGamaken = f"[Rare]Gamaken = {MagicJiraiya} + {NormalNaruto} + {NormalSakura}"
RareGaara = f"[Rare]Gaara = {MagicKankuro} + {NormalTemari} + {NormalSasori}"
RareGuyTurtle = f"[Rare]GuyTurtle = {NormalAnbu} + {NormalSai} + {NormalTemari}"
RareNaruto = f"[Rare]Naruto = {NormalNaruto} + {MagicJiraiya} + {NormalYamato}"
RareManda = f"[Rare]Manda = {MagicOrochimaru} + {NormalKabuto} + {NormalSasuke}"
RareSasori = f"[Rare]Sasori = {NormalSasori} + {MagicOrochimaru} + {NormalAnbu}"
RareSasuke = f"[Rare]Sasuke = {MagicSasuke} + {NormalKarin} + {NormalKabuto}"
RareSuigetsu = f"[Rare]Suigetsu = {NormalSasuke} + {NormalKarin} + {MagicJugo}"
RareAsuma = f"[Rare]Asuma = {MagicChoji} + {NormalNaruto} + {NormalYamato}"
RareAoba = f"[Rare]Aoba = {NormalYamato} + {NormalSai} + {MagicShikamaru}"
RareInoichi = f"[Rare]Inoichi = {NormalSakura} + {NormalKabuto} + {MagicChoji}"
RareIzumo = f"[Rare]Izumo = {NormalYamato} + {MagicShikamaru} + {NormalAnbu}"
RareItachi = f"[Rare]Itachi = {MagicSasuke} + {MagicSasuke} + {NormalAnbu}"
RareKarui = f"[Rare]Karui = {MagicChoji} + {NormalKarin} + {NormalSasuke}"
RareKatsuyu = f"[Rare]Katsuyu = {MagicTsunade} + {MagicTsunade} + {NormalSakura}"
RareKakashi = f"[Rare]Kakashi = {NormalSai} + {NormalNaruto} + {NormalSasuke}"
RareKakuzu = f"[Rare]Kakuzu = {MagicZetsu} + {MagicChoji} + {NormalSasori}"
RareKotetsu = f"[Rare]Kotetsu = {MagicShikamaru} + {MagicChoji} + {MagicTsunade}"
RareMaskedMan = f"[Rare]MaskedMan = {MagicZetsu} + {MagicZetsu} + {MagicKankuro}"
RareHaku = f"[Rare]Haku = {MagicJugo} + {MagicOrochimaru} + {NormalTemari}"
RareHinata = f"[Rare]Hinata = {MagicKiba} + {NormalSakura} + {NormalSai}"
############################################################################
UniqueGamabunta = f"[Unique]Gamabunta = 1{RareGamaken}1{RareGamaken}"
UniqueGamahiro = f"[Unique]Gamahiro = 1{RareGamaken}1{MagicZetsu}1{MagicShikamaru}"
UniqueGaara = f"[Unique]Gaara = 1{RareGaara}1{RareKakashi}"
UniqueRockLee = f"[Unique]RockLee = 1{RareGuyTurtle}1{RareGaara}"
UniqueTenten = f"[Unique]Tenten = 1{NormalTemari}1{RareGuyTurtle}1{MagicTsunade}"
UniqueKushina = f"[Unique]Kushina = 1{RareNaruto}1{RareMaskedMan}"
UniqueNaruto = f"[Unique]Naruto = 1{RareNaruto}1{RareKakuzu}"
UniqueJiraiya = f"[Unique]Jiraiya = 1{MagicJiraiya}1{MagicTsunade}1{RareNaruto}"
UniqueSasori = f"[Unique]Sasori = 1{RareSasori}1{RareSasori}"
UniqueKankuro = f"[Unique]Kankuro = 1{MagicKankuro}1{RareSasori}1{NormalSasori}"
UniqueOmoi = f"[Unique]Omoi = 1{MagicKankuro}1{RareSasori}1{NormalAnbu}1{NormalNaruto}"
UniqueDeidara = f"[Unique]Deidara = 1{RareMaskedMan}1{RareSasuke}"
UniqueSai = f"[Unique]Sai = 1{NormalSai}1{NormalNaruto}1{MagicJugo}1{RareSasuke}"
UniqueJugo = f"[Unique]Jugo = 1{MagicJugo}1{MagicJugo}1{RareSasuke}1{NormalKabuto}"
UniqueSasuke = f"[Unique]Sasuke = 1{RareSuigetsu}1{NormalYamato}1{MagicJiraiya}"
UniqueChojuro = f"[Unique]Chojuro = 1{RareSuigetsu}1{RareHaku}"
UniqueWhiteZetsu = f"[Unique]WhiteZetsu = 1{MagicZetsu}1{NormalKarin}1{NormalKabuto}1{RareSuigetsu}"
UniqueKisame = f"[Unique]Kisame = 1{RareAsuma}1{RareItachi}"
UniqueEnma = f"[Unique]Enma = 1{RareAsuma}1{RareIzumo}"
UniqueYuhiKurenai = f"[Unique]YuhiKurenai = 1{RareHinata}1{RareAsuma}"
UniqueOrochimaru = f"[Unique]Orochimaru = 1{RareManda}1{RareKotetsu}"
UniqueMitarashi = f"[Unique]Mitarashi = 1{MagicOrochimaru}1{RareManda}1{MagicSasuke}"
UniqueYamanakaFu = f"[Unique]YamanakaFu = 1{RareInoichi}1{RareAoba}"
UniqueSizune = f"[Unique]Sizune = 1{RareInoichi}1{RareKatsuyu}"
UniqueIno = f"[Unique]Ino = 1{RareInoichi}1{MagicShikamaru}1{NormalSai}"
UniqueItachi = f"[Unique]Itachi = 1{RareItachi}1{RareMaskedMan}"
UniqueYamato = f"[Unique]Yamato = 1{NormalYamato}1{MagicTsunade}1{RareItachi}"
UniqueKillerBee = f"[Unique]KillerBee = 1{RareKarui}1{RareAoba}"
UniqueSamui = f"[Unique]Samui = 1{RareKarui}1{MagicTsunade}1{NormalKarin}"
UniqueNagato = f"[Unique]Nagato = 1{MagicJiraiya}1{MagicJiraiya}1{RareKatsuyu}"
UniqueKakashi = f"[Unique]Kakashi = 1{RareKakashi}1{RareHaku}"
UniqueNoharaRin = f"[Unique]NoharaRin = 1{RareKakashi}1{RareMaskedMan}"
UniqueZabuza = f"[Unique]Zabuza = 1{RareHaku}1{RareKakashi}"
UniqueHinata = f"[Unique]Hinata = 1{RareHinata}1{NormalSai}1{NormalNaruto}"
UniqueNeji = f"[Unique]Neji = 1{RareHinata}1{MagicKiba}1{MagicSasuke}"
UniqueShino = f"[Unique]Shino = 1{MagicKiba}1{RareHinata}1{MagicShikamaru}"
UniqueHidan = f"[Unique]Hidan = 1{RareKakuzu}1{RareIzumo}"
UniqueKakuzu = f"[Unique]Kakuzu = 1{RareKakuzu}1{RareKotetsu}"
UniqueAnko = f"[Unique]Anko = 1{MagicOrochimaru}1{RareManda}1{MagicSasuke}"
###############################################################################
HiddenGamakichi = f"[Hidden]Gamakichi = 2{UniqueGamabunta}2{UniqueGamahiro}2type: gamakichi"
HiddenNaruto = f"[Hidden]Naruto = 2{UniqueNaruto}2{UniqueNagato}2type: sixtails"
HiddenMaki = f"[Hidden]Maki = 2{UniqueKakashi}2{UniqueGaara}2type: maki"
HiddenHashirama = f"[Hidden]Hashirama = 2{UniqueItachi}2{UniqueYamato}2type: hashirama"
HiddenTobirama = f"[Hidden]Tobirama = 2{UniqueNaruto}2{UniqueAnko}2type: tobirama"
HiddenTemari = f"[Hidden]Temari = 2{UniqueKankuro}2{UniqueTenten}2{MagicKankuro}2type: temari"
HiddenKurotsuchi = f"[Hidden]Kurotsuchi = 2{UniqueSai}2{UniqueDeidara}2type: kurotsuchi"
HiddenAkatsuchi = f"[Hidden]Akatsuchi = 2{UniqueTenten}2{UniqueWhiteZetsu}2type: akatsuchi"
HiddenKitsuchi = f"[Hidden]Kitsuchi = 2{UniqueIno}2{UniqueOmoi}2type: kitsuchi"
HiddenTorune = f"[Hidden]Torune = 2{UniqueYamanakaFu}2{UniqueShino}2type: torune"
HiddenOrochimaru = f"[Hidden]Orochimaru = 2{UniqueOrochimaru}2{UniqueJugo}2type: orochimaru"
HiddenHanzo = f"[Hidden]Hanzo = 2{UniqueJiraiya}2{UniqueAnko}2{MagicTsunade}2type: hanzo"
HiddenKabuto = f"[Hidden]Kabuto = 2{UniqueYuhiKurenai}2{UniqueAnko}2type: spy"
HiddenDanzo = f"[Hidden]Danzo = 2{UniqueKakashi}2{UniqueYamanakaFu}2type: danzo"
HiddenJugo = f"[Hidden]Jugo = 2{UniqueJugo}2{UniqueJugo}2type: jugo"
HiddenHinata = f"[Hidden]Hinata = 2{UniqueHinata}2{UniqueShino}2{NormalKabuto}2type: hinata"
HiddenSasori = f"[Hidden]Sasori = 2{UniqueSasori}2{UniqueKankuro}2type: sasori"
HiddenJiraiya = f"[Hidden]Jiraiya = 2{UniqueJiraiya}2{UniqueGamabunta}2type: jiraiya"
HiddenShii = f"[Hidden]Shii = 2{UniqueKillerBee}2{UniqueOmoi}2type: shii"
HiddenKiba = f"[Hidden]Kiba = 2{UniqueYuhiKurenai}2{UniqueNeji}2{MagicKiba}2type: kiba"
HiddenKirin = f"[Hidden]Kirin = 2{UniqueItachi}2{UniqueSasuke}2type: kirin"
HiddenAo = f"[Hidden]Ao = 2{UniqueKisame}2{UniqueChojuro}2type: ao"
"""
HiddenSevenNinjaSworsdsman = f"[Hidden] = ????2type: "
HiddenKushimaruKirarare = f"[Hidden] = ????2type: "
HiddenHozukiMangetsu = f"[Hidden] = ????2type: "
HiddenAmeyuriRingo = f"[Hidden] = ????2type: "
HiddenZabuza = f"[Hidden] = ????2type: "
HiddenJininAkebino = f"[Hidden] = ????2type: "
HiddenFugukiSuikazan = f"[Hidden] = ????2type: "
HiddenJinpachiMunashi = f"[Hidden] = ????2type: "
"""
# i dont see these in game????
HiddenAnko = f"[Hidden]Anko = 2{UniqueYuhiKurenai}2{UniqueOrochimaru}2type: anko"
HiddenNinjado = f"[Hidden]Ninjado = 2{UniqueZabuza}2{UniqueRockLee}2{UniqueChojuro}2type: ninjado"
#################################################################################################
LegendaryItachi = f"[Legendary]Itachi = 3{UniqueItachi}3{HiddenKirin}"
LegendaryKabuto = f"[Legendary]Kabuto = 3{HiddenKabuto}3{UniqueSasori}"
LegendaryShisui = f"[Legendary]Shisui = 3{UniqueItachi}3{HiddenDanzo}"
LegendaryDeidara = f"[Legendary]Deidara = 3{UniqueDeidara}3{HiddenAkatsuchi}"
LegendaryDodai = f"[Legendary]Dodai = 3{HiddenTemari}3{UniqueNaruto}"
LegendaryNagato = f"[Legendary]Nagato = 3{UniqueNagato}3{HiddenHanzo}3{MagicZetsu}"
LegendaryChiyo = f"[Legendary]Chiyo = 3{HiddenSasori}3{UniqueOrochimaru}"
LegendaryTsunade = f"[Legendary]Tsunade = 3{UniqueSizune}3{HiddenHashirama}"
LegendaryTobi = f"[Legendary]Tobi = 3{UniqueNoharaRin}3{HiddenTorune}"
LegendaryGaara = f"[Legendary]Gaara = 3{UniqueGaara}3{UniqueJugo}3{UniqueNeji}"
LegendarySasuke = f"[Legendary]Sasuke = 3{UniqueSasuke}3{UniqueChojuro}3{UniqueWhiteZetsu}"
LegendaryKillerBee = f"[Legendary]KillerBee = 3{UniqueKillerBee}3{UniqueSamui}3{UniqueKisame}"
LegendaryDarui = f"[Legendary]Darui = 3{UniqueSamui}3{UniqueOmoi}3{RareKarui}3{RareKakashi}"
LegendaryKakashi = f"[Legendary]Kakashi = 3{UniqueKakashi}3{UniqueZabuza}3{UniqueNoharaRin}"
LegendarySarutobi = f"[Legendary]Sarutobi = 3{UniqueEnma}3{UniqueYuhiKurenai}3{RareKotetsu}3{RareManda}"
LegendaryShikamaru = f"[Legendary]Shikamaru = 3{MagicShikamaru}3{MagicShikamaru}3{UniqueHidan}3{UniqueKakuzu}3{RareKatsuyu}"
LegendaryChoji = f"[Legendary]Choji = 3{MagicShikamaru}3{UniqueSai}3{UniqueNagato}3{RareAsuma}3{RareKotetsu}"
LegendaryYamato = f"[Legendary]Yamato = 3{UniqueYamato}3{UniqueSai}3{UniqueSizune}"
LegendaryKushina = f"[Legendary]Kushina = 3{UniqueKushina}3{UniqueNaruto}3{UniqueJiraiya}"
LegendaryMinato = f"[Legendary]Minato = 3{UniqueKushina}3{UniqueKillerBee}3{UniqueEnma}"
LegendaryRockLee = f"[Legendary]RockLee = 3{UniqueRockLee}3{UniqueNeji}3{UniqueGaara}"
LegendaryGuy = f"[Legendary]Guy = 3{UniqueRockLee}3{UniqueTenten}3{UniqueNeji}"
LegendaryZabuza = f"[Legendary]Zabuza = 3{UniqueZabuza}3{UniqueRockLee}3{UniqueSasuke}"
#below are for tailed beasts

#Legendary = f"[Legendary] = 3{}3{}3{}"
LegendaryFu = f"[Legendary]Fu = 3Tobi(special)3{UniqueKakuzu}"
LegendaryHan = f"[Legendary]Han = 3Tobi(special)3{UniqueItachi}"
LegendaryRoshi = f"[Legendary]Roshi = 3Tobi(special)3{UniqueKisame}"
LegendaryUtakata = f"[Legendary]Utakata = 3Tobi(special)3{UniqueNagato}"
LegendaryYugito = f"[Legendary]Yugito = 3Tobi(special)3{UniqueHidan}"
LegendaryYagura = f"[Legendary]Yagura = 3Tobi(special)3{UniqueNoharaRin}"
LegendaryMadara = f"[Legendary]Madara = 3Kabuto(Special)3{UniqueNaruto}"
####################################################################################################
EliteA = f"[Elite]A = 4Kabuto(Special)4{LegendaryDodai}4{UniqueKillerBee}4{NormalNaruto}4{NormalNaruto}"
EliteGedoMazo = f"[Elite]GedoMazo = 4{LegendaryNagato}4{LegendaryChoji}"
EliteGengetsu = f"[Elite]Gengetsu = 4Kabuto(special)4{HiddenAo}4{LegendaryZabuza}"
EliteGinkaku = f"[Elite]Ginkaku = 4{HiddenKitsuchi}4{LegendaryKabuto}4{UniqueSamui}"
EliteGuren = f"[Elite]Guren = 4{LegendaryKabuto}4{UniqueSizune}4{UniqueGamahiro}4{HiddenHinata}"
EliteGari = f"[Elite]Gari = 4{UniqueRockLee}4Kabuto(special)4{LegendaryDeidara}4{NormalSakura}4{NormalSakura}"
EliteHaku = f"[Elite]Haku = 4{LegendaryZabuza}4{LegendaryKakashi}"
EliteKankuro = f"[Elite]Kankuro = 4{UniqueKankuro}4{LegendaryChiyo}4{LegendaryGaara}"
EliteKiba = f"[Elite]Kiba = 4{HiddenKiba}4{HiddenHinata}4{UniqueShino}4{UniqueSasuke}4{MagicKankuro}"
EliteKinkaku = f"[Elite]Kinkaku = 4{LegendaryChoji}4{LegendaryDarui}"
EliteKisame = f"[Elite]Kisame = 4{UniqueKisame}4{HiddenShii}4{LegendaryKillerBee}"
EliteMifune = f"[Elite]Mifune = 4{HiddenHanzo}4{HiddenDanzo}4{HiddenOrochimaru}"
EliteMu = f"[Elite]Mu = 4Kabuto(special)4{LegendaryDodai}4{RareKotetsu}4{RareIzumo}4{RareGaara}"
EliteNaruto = f"[Elite]Naruto = 4{HiddenNaruto}4{HiddenGamakichi}4{HiddenJiraiya}4{RareKatsuyu}"
EliteOrochimaru = f"[Elite]Orochimaru = 4{UniqueAnko}4{LegendaryItachi}4{HiddenOrochimaru}4{RareKatsuyu}"
ElitePakura = f"[Elite]Pakura = 4{HiddenMaki}4Kabuto(special)4{LegendaryZabuza}"
EliteRasa = f"[Elite]Rasa = 4{LegendaryGaara}4Kabuto(special)4{HiddenTemari}"
EliteSai = f"[Elite]Sai = 4{LegendaryRockLee}4{UniqueSai}4{HiddenSasori}"
EliteShino = f"[Elite]Shino = 4{UniqueShino}4{HiddenTemari}4{LegendaryTobi}"
EliteTemari = f"[Elite]Temari = 4{HiddenTemari}4{LegendaryShikamaru}4{UniqueGaara}"
####################################################################################################
EpicGaara = f"[Epic]Gaara = 5{LegendaryGaara}5{LegendaryKakashi}5{LegendaryChiyo}"
EpicGai = f"[Epic]Gai = 5{LegendaryGuy}5{EliteKisame}"
EpicHashirama = f"[Epic]Hashirama = 5{HiddenTobirama}5{LegendaryYamato}5{LegendaryTobi}5{UniqueWhiteZetsu}"
EpicHidan = f"[Epic]Hidan = 5{UniqueHidan}5{LegendaryDeidara}5{LegendaryShikamaru}5{UniqueIno}5one NinjaScroll"
EpicHinata = f"[Epic]Hinata = 5{HiddenHinata}5{HiddenKurotsuchi}5{HiddenGamakichi}5{HiddenNaruto}5{UniqueNeji}"
EpicIno = f"[Epic]Ino = 5{UniqueIno}5{HiddenAo}5{LegendaryYagura}5{LegendaryYamato}"
EpicInoChikaCho = f"[Epic]InoChikaCho = 5{LegendaryShikamaru}5{LegendaryChoji}5{UniqueIno}5ChakraYin"
EpicItachi = f"[Epic]Itachi = 5{LegendaryItachi}5{LegendaryNagato}5{LegendaryKillerBee}"
EpicJiraiya = f"[Epic]Jiraiya = 5{HiddenJiraiya}5{LegendaryTsunade}5{UniqueEnma}5{LegendaryGuy}"
EpicKabuchimaru = f"[Epic]Kabuchimaru = 5{LegendaryKabuto}5{HiddenOrochimaru}5{HiddenKiba}5{UniqueSasuke}"
EpicKakashi = f"[Epic]Kakashi = 5{LegendaryKakashi}5{LegendaryTobi}5{LegendaryZabuza}"
EpicKillerA = f"[Epic]KillerA = 5{LegendaryDarui}5{LegendaryKillerBee}5{HiddenShii}5{UniqueGaara}"
EpicKonan = f"[Epic]Konan = 5{LegendaryNagato}5{LegendaryTobi}5Tobi(Special)5{UniqueJiraiya}"
EpicMadara = f"[Epic]Madara = 5{LegendaryMadara}5{LegendaryDarui}5{HiddenHashirama}5{UniqueSasuke}"
EpicMei = f"[Epic]Mei = 5{HiddenAo}5{LegendaryZabuza}5{LegendaryTsunade}5{RareGaara}5{NormalKarin}"
EpicMinato = f"[Epic]Minato = 5{LegendaryMinato}5{LegendaryKushina}5{LegendaryRockLee}"
EpicMomoshiki = f"[Epic]Momoshiki = 5{HiddenKurotsuchi}5{LegendaryDarui}5{LegendaryYamato}5{UniqueChojuro}"
EpicNaruto = f"[Epic]Naruto = 5{HiddenNaruto}5{LegendaryKushina}5{LegendaryMinato}5{RareHinata}"
EpicObito = f"[Epic]Obito = 5{LegendaryTobi}5{LegendaryGuy}5{LegendaryKillerBee}"
EpicOonoki = f"[Epic]Oonoki = 5{HiddenKurotsuchi}5{HiddenKitsuchi}5{HiddenAkatsuchi}5{LegendaryDodai}"
EpicOrochimaru = f"[Epic]Orochimaru = 5{HiddenJugo}5{EliteOrochimaru}"
EpicPain = f"[Epic]Pain = 5{LegendaryNagato}5{HiddenHinata}5{HiddenGamakichi}5{UniqueNaruto}5Tobi(Special)"
EpicRinneMadara = f"[Epic]RinneMadara = 5{LegendaryMadara}5{LegendaryTobi}5{HiddenTobirama}5{UniqueWhiteZetsu}"
EpicSakura = f"[Epic]Sakura = 5{NormalSakura}5{LegendaryChiyo}5{LegendarySasuke}5{HiddenGamakichi}"
EpicSarutobi = f"[Epic]Sarutobi = 5{LegendarySarutobi}5{LegendaryShisui}5{LegendaryYamato}"
EpicSasuke = f"[Epic]Sasuke = 5{LegendarySasuke}5{HiddenKirin}5{HiddenDanzo}5{HiddenJugo}"
EpicShisui = f"[Epic]Shisui = 5{LegendaryShisui}5{LegendaryItachi}5{LegendarySarutobi}"
EpicTenTails = f"[Epic]TenTails = 5{EliteGedoMazo}5{HiddenGamakichi}5{UniqueRockLee}"
EpicTenten = f"[Epic]Tenten = 5{UniqueTenten}5{UniqueKakuzu}5{HiddenMaki}5{HiddenKitsuchi}5{LegendaryDarui}"
EpicTobirama = f"[Epic]Tobirama = 5{HiddenTobirama}5{EliteNaruto}5{RareGamaken}"
EpicToneri = f"[Epic]Toneri = 5{HiddenHinata}5{LegendaryKakashi}5{LegendaryShikamaru}5{UniqueSai}"
EpicTsunade = f"[Epic]Tsunade = 5{LegendaryTsunade}5{LegendaryShikamaru}5ChakraYang"
EpicZetsu = f"[Epic]Zetsu = 5{UniqueWhiteZetsu}5{LegendaryYamato}5{LegendarySarutobi}5{HiddenOrochimaru}"
#####################################################################################################################

def findUnitsNeeded(name):
    """
    rares = "\n               [Rare]".join(name.split("[Rare]"))
    uniques = "\n          [Unique]".join(rares.split("[Unique]"))
    hidden = "\n     [Hidden]".join(uniques.split("[Hidden]"))
    """

    test1 = "\n                         ".join(name.split("1"))
    test2 = "\n                    ".join(test1.split("2"))
    test3 = "\n               ".join(test2.split("3"))
    test4 = "\n          ".join(test3.split("4"))
    test5 = "\n     ".join(test4.split("5"))
    return test5

#####################################################################################################

unitcombolist = []
unitnamelist = []
lookingfor = ["Normal", "Magic", "Rare", "Unique", "Hidden", "Legendary", "Elite", "Epic"]

for i in list(vars().values()):
    if type(i) == str:
        if any(x in i for x in lookingfor):
            unitcombolist.append(i)

for i in unitcombolist:
    unitnamelist.append(("[".join(i.split("[")).split(" = "))[0])

normalmagicunitlist = []
for i in unitnamelist:
    if "[Normal]" in i or "[Magic]" in i:
        normalmagicunitlist.append(i)



#testing out tkinter gui
root = Tk()
root.title("Naruto Helper")
#root.iconbitmap("C:/gui/codemy.ico")
#root.geometry("600x1000")
root.configure(bg="#2C2F33")

#update the listbox
def update(data):
    #Clear the listbox
    my_list.delete(0, END)

    #add toppings to listbox
    for i in data:
        my_list.insert(END, i)

#update entry box with listbox clicked

def fillout(event):
    if (event.widget.curselection() == ()):
        return
    if (event.widget.get(event.widget.curselection())) == "":
        return

    #delete whatever is in the entry box
    my_entry.delete(0, END)

    #add clicked list item to entry box
    my_entry.insert(0, event.widget.get(event.widget.curselection()))

    typed = my_entry.get()
    
    if typed != "":
        for i, unitname in enumerate(unitnamelist):
            if typed == unitname:
                v1.set(findUnitsNeeded(unitcombolist[i]))

                newlist = []
                for j in normalmagicunitlist:
                    count = unitcombolist[i].count(j)
                    stringy = f'{j}: {count}'
                    if count > 0:
                        newlist.append(stringy)
                my_list3.delete(0, END)
                for k in newlist:
                    my_list3.insert(END, k)
                v3.set("\n".join(newlist))

    newlist = []
    if typed != "":
        for i, unitname in enumerate(unitcombolist):
            if typed in unitname:
                newlist.append(unitnamelist[i])
        v2.set("\n".join(newlist[1:]))

        my_list2.delete(0, END)
        for i in newlist[1:]:
            my_list2.insert(END, i)
            

#create function to check entry vs listbox
def check(event):
    #grab what was typed
    typed = my_entry.get()

    if typed == "":
        data = unitnamelist
    else:
        data = []
        for i in unitnamelist:
            if typed.lower() in i.lower():
                data.append(i)
    
    #update our listbox with selected items
    update(data)

#create a label
my_label = Label(root, text="Type in a unit...", font=("Helvetica", 10), fg="White", bg="#2C2F33")
my_label.grid(row = 0, column = 0, pady=10, sticky="w")

my_label2 = Label(root, text="Builds into:", font=("Helvetica", 10), fg="White", bg="#2C2F33")
my_label2.grid(row = 1, column = 2, pady=10, sticky="w")

my_label3 = Label(root, text="Total units:", font=("Helvetica", 10), fg="White", bg="#2C2F33")
my_label3.grid(row = 1, column = 1, pady=10, sticky="w")

#create an entry box
my_entry = Entry(root, font=("Helvetica", 15), bg="#99AAB5", width=20)
my_entry.grid(row = 1, column = 0, sticky="w")

#create a listbox
my_list = Listbox(root, width=25, bg="#99AAB5")
my_list.grid(row = 2, column = 0, pady=5, sticky=("n", "w"), )

my_list2 = Listbox(root, width=25, bg="#99AAB5")
my_list2.grid(row = 2, column = 2, pady=5, padx=5, sticky=("n", "w"), )

my_list3 = Listbox(root, width=25, bg="#99AAB5")
my_list3.grid(row = 2, column = 1, pady=5, sticky=("n", "w"), )


v1 = StringVar()
characterinfo = Label(root, textvariable=v1, font=("Helvetica", 10),fg="White", bg="#2C2F33", justify=LEFT)
characterinfo.grid(row = 3, column = 0, sticky=("n", "w"), columnspan=3)

v2 = StringVar()
"""
cinfo = Label(root, textvariable=v2, font=("Helvetica", 10),fg="White", bg="#2C2F33", justify=LEFT)
cinfo.grid(row = 2, column = 2, sticky=("n", "w"))
"""
v3 = StringVar()
"""
totalunitcount = Label(root, textvariable=v3, font=("Helvetica", 10),fg="White", bg="#2C2F33", justify=LEFT)
totalunitcount.grid(row = 2, column = 1, sticky=("n", "w"))
"""

#add the names to our list
update(unitnamelist)

#create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)
my_list2.bind("<<ListboxSelect>>", fillout)

#create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()
