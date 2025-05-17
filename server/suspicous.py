import re

suspicious_patterns = [
    #Drug name variation
    r"\bdrug\b", r"\bdru9\b", r"\bdru6\b", r"\bdrvg\b", r"\bdru@k\b",
    r"\bdru&\b", r"\bdrvg\b", r"\bdru9\b", r"\bdr@g\b",r"\bdr*g\b",r"\bdr[u0]g\b",
    r"\bdr(u|0)g\b",r"\bdr[u@]g\b", r"\bdr[u0]g\b" ,r"\bdru9\b"
                                                    
    # Drug
    r"\bdrug\b", r"\bdru9\b", r"\bdru6\b", r"\bdrvg\b", r"\bdru@k\b", r"\bdru&\b",
    r"\bdr@g\b", r"\bdr*g\b", r"\bdr[u0]g\b", r"\bdr(u|0)g\b", r"\bdr[u@]g\b",

    # Drugs
    r"\bdrugs\b", r"\bdru9s\b", r"\bdru6s\b", r"\bdrvg5\b", r"\bdru@ks\b",
    r"\bdru&5\b", r"\bdr@g5\b", r"\bdr*g5\b", r"\bdr[u0]gs\b", r"\bdr(u|0)gs\b", r"\bdr[u@]gs\b"

    # Cocaine
    r"\bcocaine\b", r"\bcoc@ine\b", r"\bc0caine\b", r"\bc0c@ine\b", r"\bcoke\b", r"\bc0ke\b", r"\bc0k3\b",
    r"\bblow\b", r"\bbl0w\b", r"\bsnow\b", r"\bsn0w\b", r"\bflake\b", r"\bnose candy\b", r"\bwhite\b",
    r"\bwh1te\b", r"\bpowder\b", r"\bbig c\b", r"\byayo\b", r"\by@yo\b", r"\bcoca\b", r"\bc0c@1ne\b",
    r"\bc0c@1n3\b", r"\bwh1t3\b", r"\bchamak\b",


    # Cocaine in different languages
    r"\bকোকেইন\b", r"\bকোকেইন\b", r"\bकोकेन\b", r"\bकोकेन\b", r"\bકોકેન\b", r"\bकोकीन\b", r"\bಕೋಕೆನ್\b",
    r"\bکوکین\b", r"\bकокаин\b", r"\bकोकेन\b", r"\bکوکین\b", r"\bகொக்கெய்ன்\b", r"\bకొకైన్\b", r"\bکوکین\b",

    # Marijuana (Cannabis)
    r"\bganja\b", r"\bg@nja\b", r"\bweed\b", r"\bw33d\b", r"\bpot\b", r"\bp0t\b", r"\bgrass\b", r"\bgr@ss\b",
    r"\bmary jane\b", r"\bdope\b", r"\breefer\b", r"\berb\b", r"\bh3rb\b", r"\bchronic\b", r"\bcr0n1c\b",
    r"\bhash\b", r"\bh@sh\b", r"\bh4sh\b", r"\bskunk\b", r"\bbud\b", r"\btree\b", r"\bbhang\b", r"\bcharas\b",
    r"\bch@ras\b", r"\bmal\b", r"\bpotli\b", r"\bprasad\b", r"\bpudiya\b", r"\bpud!ya\b", r"\bpud!@h\b",
    r"\bpudi@h\b",

    # Marijuana (Cannabis) in different languages
    r"\bগাঞ্জা\b", r"\bগাঁজা\b", r"\bगांजा\b", r"\bगांजा\b", r"\bગાંજાઓ\b", r"\bगांजा\b", r"\bಗಂಜಾ\b",
    r"\bگانجا\b", r"\bगांजा\b", r"\bگانجا\b", r"\bगञ्जा\b", r"\bগांজা\b", r"\bଗଞ୍ଜା\b", r"\bਗਾਂਜਾ\b",
    r"\bगांजा\b", r"\bگانجا\b", r"\bகஞ்சா\b", r"\bగంజా\b", r"\bگانجا\b",

    # Heroin
    r"\bheroin\b", r"\bh[e3]r[o0]in\b", r"\bh[e3]r[o0]!n\b", r"\bsmack\b", r"\bsm@ck\b", r"\bbrownsugar\b",
    r"\bbrown sugar\b", r"\bchitta\b", r"\bsafedi\b", r"\bdope\b", r"\bjunk\b", r"\bblack tar\b", r"\bdragon\b",
    r"\bskag\b", r"\bmud\b", r"\bsugar\b", r"\bb@ng\b",

    # Heroin in different languages
    r"\bহেৰোইন\b", r"\bহেরোইন\b", r"\bहेरोइन\b", r"\bहेरोइन\b", r"\bહેરોઈન\b", r"\bहेरोइन\b", r"\bಹೆರೋಇನ್\b",
    r"\bہیروئن\b", r"\bहेरोइन\b", r"\bہیروئن\b", r"\bहेरोइन\b", r"\bहेरोइन\b", r"\bହେରୋଇନ୍\b", r"\bਹੇਰੋਇਨ\b",
    r"\bहेरोइन\b", r"\bہیروئن\b", r"\bஹெராயின்\b", r"\bహెరాయిన్\b", r"\bہیروئن\b",

    # Methamphetamine
    r"\bmeth\b", r"\bm[e3]th\b", r"\bm[e3]+h\b", r"\bm[e3]th[a@]mphetamine\b", r"\bcrystal meth\b", r"\b1ce\b",
    r"\b!ce\b", r"\bl[s5]d\b", r"\bl[\$\@]d\b", r"\b4cid\b", r"\b@cid\b", r"\b4c!d\b", r"\b[@4]c1d\b",
    r"\btrips\b", r"\bcrank\b", r"\bspeed\b", r"\b5peed\b", r"\b5p33d\b", r"\bchalk\b", r"\btina\b", r"\bt1n@\b",
    r"\bquartz\b", r"\bqu@rtz\b", r"\bbatu\b", r"\btikka\b",

    # Methamphetamine in different languages
    r"\bমেথ\b", r"\bমেথ\b", r"\bमेट\b", r"\bमैथ\b", r"\bમેથ\b", r"\bमेथ\b", r"\bಮೆತ್\b", r"\bمیتھ\b",
    r"\bमेथ\b", r"\bمیتھ\b", r"\bमेथ\b", r"\bमेथ\b", r"\bମେଥ୍\b", r"\bਮੈਥ\b", r"\bमेथ\b", r"\bمیتھ\b",
    r"\bமெத்\b", r"\bమెత్\b", r"\bمیتھ\b",

    # Ecstasy (MDMA)
    r"\bmolly\b", r"\bm0lly\b", r"\becstasy\b", r"\b3cstasy\b", r"\b3c5ta5y\b", r"\be\b", r"\bx\b",
    r"\bxtc\b", r"\bx7c\b", r"\badam\b", r"\b@dam\b", r"\bbeans\b", r"\bdisco biscuit\b", r"\bd!sc0\b",
    r"\bd15c0\b", r"\broll\b", r"\br0ll\b", r"\blove drug\b", r"\bscooby snacks\b", r"\bmd\b", r"\bmd5\b",
    r"\bmaal\b",

    # Ecstasy (MDMA) in different languages
    r"\bমলি\b", r"\bমলি\b", r"\bमॉल्ली\b", r"\bमोल्ली\b", r"\bમોલી\b", r"\bमोल्ली\b", r"\bಮೊಲ್ಲಿ\b",
    r"\bمولي\b", r"\bमोल्ली\b", r"\bمولي\b", r"\bमोल्ली\b", r"\bമോളി\b", r"\bমোল্লি\b", r"\bमोल्ली\b",
    r"\bਮੋਲੀ\b", r"\bमोल्ली\b", r"\bமொலி\b", r"\bమోలీ\b", r"\bمولی\b",

    # LSD (Lysergic Acid Diethylamide)
    r"\blsd\b", r"\bl5d\b", r"\bl\$d\b", r"\bacid\b", r"\b4cid\b", r"\b@cid\b", r"\bblotter\b", r"\bdots\b",
    r"\bd0t5\b", r"\bd0t$\b", r"\bmellow yellow\b", r"\bwindow pane\b", r"\bw1nd0wp@ne\b", r"\btabs\b", r"\bt@b5\b",
    r"\bt@b$\b", r"\btrips\b", r"\bmicrodots\b", r"\bm!cr0d0t\b", r"\bm1cr0d0t\b", r"\bsunshine\b", r"\bpaper\b",

    # LSD (Lysergic Acid Diethylamide) in different languages
    r"\bএলএসডি\b", r"\bএলএসডি\b", r"\bएलएसडी\b", r"\bएलएसडी\b", r"\bએલએસડી\b", r"\bएलएसडी\b", r"\bಎಲ್‌ಎಸ್‌ಡಿ\b",
    r"\bایل ایس ڈی\b", r"\bएलएसडी\b", r"\bایل ایس ڈی\b", r"\bएलएसडी\b", r"\bഎൽ‌എസ്‌ഡി\b", r"\bএলএসডি\b",
    r"\bएलएसडी\b", r"\bਐਲਐਸਡੀ\b", r"\bएलएसडी\b", r"\bஎல்எஸ்டி\b", r"\bఎల్‌ఎస్డీ\b", r"\bایل ایس ڈی\b",

    # Fentanyl
    r"\bfentanyl\b", r"\bf3nt@nyl\b", r"\bf3nt@n1l\b", r"\bf3nt@n!l\b", r"\bfentanyl\b", r"\bfent@n!l\b",
    r"\bfentanil\b", r"\bf3nt@nil\b", r"\bf3nt@n!l\b", r"\bfentan1l\b", r"\bf3nt@n1l\b", r"\bf3nt@n!1l\b",
    r"\bf3nt@nyl\b", r"\bf3nt@n!l\b", r"\bf3nt@n1l\b", r"\bf3nt@nyl\b",

    # Fentanyl in different languages
    r"\bফেন্টানিল\b", r"\bফেন্টানিল\b", r"\bफेंटानिल\b", r"\bफेंटानिल\b", r"\bફેન્ટેનિલ\b", r"\bफेंटानिल\b",
    r"\bಫೆಂಟಾನಿಲ್\b", r"\bفینٹانل\b", r"\bफेंटानिल\b", r"\bفینٹانل\b", r"\bफेन्टानिल\b", r"\bഫെന്റാനിൽ\b",
    r"\bফেন্টানিল\b", r"\bफेंटानिल\b", r"\bਫ਼ੈਂਟਾਨਿਲ\b", r"\bफेंटानिल\b", r"\bபெண்டனில்\b", r"\bఫెంటానిల్\b",
    r"\bفینٹانیل\b",

    # Prescription Opioids (Oxycodone, Hydrocodone, etc.)
    r"\boxycodone\b", r"\boxy\b", r"\boxy @b\$", r"\broxynol\b", r"\brox0n0l\b", r"\boxycontin\b", r"\boxyc0nt1n\b",
    r"\bhydrocodone\b", r"\bvicodin\b", r"\bpercocet\b", r"\bpainkiller\b", r"\boxy\b", r"\boxycod0n3\b",
    r"\boxyc0d3n3\b",
    r"\boxyc0d3\b", r"\bp@inb!ll3rs\b", r"\bp@1nb!ll3rs\b", r"\bpain m3dic!n3\b",

    # Prescription Opioids (Oxycodone, Hydrocodone, etc.) in different languages
    r"\bঅক্সি\b", r"\bঅক্সি\b", r"\bऑक्सी\b", r"\bऑक्सी\b", r"\bઓક્સી\b", r"\bऑक्सी\b", r"\bಆಕ್ಸಿ\b",
    r"\bآکسی\b", r"\bऑक्सी\b", r"\bآکسی\b", r"\bऑक्सी\b", r"\bഓക്സി\b", r"\bঅক্সি\b", r"\bऑक्सी\b",
    r"\bਆਕਸੀ\b", r"\bऑक्सी\b", r"\bஆக்ஸி\b", r"\bఆక్సీ\b", r"\bآکسی\b",

    # Mephedrone
    r"\bmephedrone\b", r"\bmeow meow\b", r"\bm3ow m3ow\b", r"\bm3ow m3ow\b", r"\bm3ow m3ow\b", r"\bmeow meow\b",
    r"\bm3ow m3ow\b", r"\bm3ow m3ow\b", r"\bm3ow m3ow\b", r"\bm3ow m3ow\b", r"\bm3ow m3ow\b", r"\bm3ow m3ow\b",

    # Mephedrone in different languages
    r"\bমেও মেও\b", r"\bমেও মেও\b", r"\bम्याऊं म्याऊं\b", r"\bम्याऊं म्याऊं\b", r"\bમ્યાઓ મ્યાઓ\b",
    r"\bम्याऊं म्याऊं\b", r"\bಮ್ಯಾವು ಮ್ಯಾವು\b", r"\bمےاؤں مےاؤں\b", r"\bम्याऊं म्याऊं\b", r"\bمياو مياو\b",
    r"\bम्याऊ म्याऊ\b", r"\bമ്യാവു മ്യാവു\b", r"\bমেও মেও\b", r"\bम्याऊ म्याऊ\b", r"\bਮਿਆਉ ਮਿਆਉ\b",
    r"\bम्याऊ म्याऊ\b", r"\bமியாவ் மியாவ்\b", r"\bమియావ్ మియావ్\b", r"\bمِیاؤ مِیاؤ\b",

    # Ketamine
    r"\bketamine\b", r"\bketam1ne\b", r"\bke7amine\b", r"\bke7am1ne\b", r"\bspecial k\b", r"\bspecialk\b",
    r"\bketa\b", r"\bkitty litter\b", r"\bk3t4\b", r"\bk3t@b1n3\b", r"\bke7a\b", r"\bke7a\b", r"\bsp!c!@l k\b",
    r"\bk3ta\b",

    # Ketamine in different languages
    r"\bকেটামিন\b", r"\bকেটামিন\b", r"\bकेटामिन\b", r"\bकेटामिन\b", r"\bકેટામિન\b", r"\bकेटामिन\b",
    r"\bಕೇಟಮಿನ್\b", r"\bکیٹامین\b", r"\bकेटामिन\b", r"\bکیٹامین\b", r"\bकेटामिन\b", r"\bകെറ്റാമിൻ\b",
    r"\bকেটামিন\b", r"\bकेटामिन\b", r"\bਕੇਟਾਮਿਨ\b", r"\bकेटामिन\b", r"\bகேட்டமைன்\b", r"\bకేటమైన్\b",
    r"\bکیٹامین\b",

    # GHB (Gamma-Hydroxybutyrate)
    r"\bghb\b", r"\bgamma hydroxybutyrate\b", r"\bliquid ecstasy\b", r"\b1iquid ecstasy\b", r"\bghb\b",
    r"\bgamma-hydroxybutyrate\b", r"\bl!qu1d \becstasy\b", r"\bliquid x\b", r"\bcherry meth\b", r"\bch3rry m3th\b",

    # GHB (Gamma-Hydroxybutyrate) in different languages
    r"\bজিএইচবি\b", r"\bজিএইচবি\b", r"\bजीएचबी\b", r"\bजीएचबी\b", r"\bજીએચબી\b", r"\bजीएचबी\b",
    r"\bಜಿಎಚ್‌ಬಿ\b", r"\bجی ایچ بی\b", r"\bजीएचबी\b", r"\bجی ایچ بی\b", r"\bजीएचबी\b", r"\bജിഎച്ച്ബി\b",
    r"\bজিএইচবি\b", r"\bजीएचਬੀ\b", r"\bਜੀਐਚਬੀ\b", r"\bजीएचਬੀ\b", r"\bஜிஎச்பி\b", r"\bజిహెచ్బి\b",
    r"\bجی ایچ بی\b",

    # Crack Cocaine
    r"\bcrack cocaine\b", r"\bcr@ck coc@!ne\b", r"\brock cocaine\b", r"\bcrack\b", r"\bcr@ck\b", r"\brock\b",
    r"\bbase\b", r"\bcandy\b", r"\bc00k!3s\b", r"\bcr@ckies\b", r"\bc0ok\b", r"\bc0ok!3\b", r"\bcrank\b",
    r"\bcr@nk\b", r"\b8all\b", r"\b8@11\b", r"\bbeat\b", r"\b8e@t\b", r"\bbeats\b", r"\bb3@ts\b",

    # Crack Cocaine in different languages
    r"\bক্র্যাক কোকেইন\b", r"\bক্র্যাক কোকেইন\b", r"\bक्रैक कोकेन\b", r"\bक्रैक कोकेन\b", r"\bક્રેક કોકેઇન\b",
    r"\bक्रैक कोकीन\b", r"\bಕ್ರಾಕ್ ಕೋಕೇನ್\b", r"\bکرک کوکین\b", r"\bक्रैक कोकेन\b", r"\bکرک کوکین\b",
    r"\bक्रैक कोकेन\b", r"\bക്രാക്ക് കോകെയ്ന്\b", r"\bক্র্যাক কোকেইন\b", r"\bक्रैक कोकेन\b", r"\bਕ੍ਰੈਕ ਕੋਕੇਨ\b",
    r"\bक्रैक कोकेन\b", r"\bகிராக் கோகேன்\b", r"\bక్రాక్ కోకెయిన్\b", r"\bکرک کوکین\b",

#     additional missing in the first list
# Crack Cocaine
r"\bnuggets\b", r"\bnug93ts\b", r"\bjelly beans\b", r"\bj3llyb3@ns\b", r"\bcrumbs\b", r"\bcrumb5\b"

# PCP (Phencyclidine)
r"\bangel dust\b", r"\b@ng3lduzt\b", r"\brocket fuel\b", r"\br0ck3t fu3l\b", r"\blove boat\b", r"\bl0v3 b0@t\b",
r"\bozone\b", r"\b0z0n3\b", r"\bwack\b", r"\bw@ck\b", r"\bwet\b", r"\bw3t\b", r"\bembalming fluid\b", r"\b3mb@lm1ngflu!d\b",
r"\bsupergrass\b"

# Psilocybin (Magic Mushrooms)
r"\b5hr00m5\b", r"\bm@gic mushr00ms\b", r"\bb00m3r5\b", r"\bmvsh1es\b", r"\bfungus\b"

# Synthetic Cannabinoids
r"\bspice\b", r"\b5p1c3\b", r"\bk2\b", r"\bfake weed\b", r"\bf@ke w33d\b", r"\bmoon rocks\b", r"\bm00n r0ck5\b",
r"\bblack mamba\b", r"\b8l@ck m@mba\b", r"\bbliss\b", r"\bbl!$$\b", r"\bblaze\b", r"\b8l@ze\b"

# Additional Drug Nicknames
r"\bmdma\b", r"\bm@d\b", r"\b3c5ta5y\b", r"\bnitrous\b", r"\bn0t5\b", r"\blaughing gas\b", r"\bn20\b",
r"\bwhippits\b", r"\bwhipp!ts\b", r"\bwh!pp3ts\b", r"\bcrank\b", r"\bspeed\b", r"\b5peed\b", r"\b5p33d\b",
r"\bchalk\b", r"\btina\b", r"\bt1n@\b", r"\bquartz\b", r"\bqu@rtz\b", r"\bbatu\b", r"\btikka\b", r"\bmeow meow\b",
r"\bm30wm30w\b", r"\bm34wm34w\b", r"\bm-cat\b", r"\bm-c@t\b", r"\bbubbles\b", r"\bbubb13s\b", r"\bbounce\b",
r"\b8ounc3\b", r"\bbath salts\b", r"\bb@ths@lt5\b", r"\bwhite magic\b", r"\bdrone\b", r"\bdr0n3\b", r"\bchemical\b",
r"\bch3m1c@1\b", r"\bmagic\b", r"\bspecial k\b", r"\b5pec!al k\b", r"\b5p3c1al k\b", r"\bk\b", r"\bkit kat\b",
r"\bk!t k@t\b", r"\bvitamin k\b", r"\bv!tam1n k\b", r"\bsuper acid\b", r"\bsup3r ac!d\b", r"\bcat valium\b",
r"\bc@tv@lium\b", r"\bket\b", r"\bk3t\b", r"\bliquid ecstasy\b", r"\bliq!d ec5t@5y\b", r"\bl!quid3cst@sy\b",
r"\bg\b", r"\bgeorgia home boy\b", r"\bg30rg!@ h0m3b0y\b", r"\bsoap\b", r"\bs04p\b", r"\bscoop\b", r"\bs00p\b",
r"\bliquid x\b", r"\bliq!d x\b", r"\bcherry meth\b", r"\bch3rry m3th\b"




    # Drug name variations (Standard & ASCII variations)
                                                     r"\b[dD][rR][uU0@][gG9]?[sS$]?\b", r"\b[dD][rR][uU0@]9[sS$]?\b",
    r"\b[dD][rR][uU0@]6[sS$]?\b",
    r"\b[dD][rR][vV][gG][sS$]?\b", r"\b[dD][rR][uU0@]&[sS$]?\b", r"\b[dD][rR][gG]s?\b",

    # Cocaine and its variations
    r"\b[cC][o0][cC][aA@4][iI1!][nN][eE3$]?\b", r"\b[cC][o0][kK][eE3$]?\b", r"\b[bB][lL1]?[o0]w\b",
    r"\b[sS][nN]?[o0]w\b", r"\b[fF][lL1]?[aA4@][kK][eE3$]?\b", r"\b[nN][o0][sS][eE3$]? [cC][aA@4][nN][dD][yY]\b",

    # Marijuana / Weed Variations
    r"\b[wW][eE3][eE3][dD]\b", r"\b[gG][aA@]?[nN][jJ][aA4@]?\b", r"\b[mM][aA@4][rR][iI1!][jJ][uU][aA@4]?[nN][aA@4]?\b",
    r"\b[hH][aA@4][sS$][hH]\b", r"\b[sS][kK][uU][nN][kK]\b", r"\b[bB][uU][dD]\b", r"\b[tT][rR][eE3][eE3]\b",

    # Heroin Variations
    r"\b[hH][eE3][rR][oO0][iI1!][nN]\b", r"\b[sS][mM][aA@4][cC][kK]\b", r"\b[cC][hH][iI1!][tT][tT][aA@4]\b",
    r"\b[dD][oO0][pP][eE3$]?\b", r"\b[jJ][uU][nN][kK]\b", r"\b[bB][lL1][aA4@][cC][kK] [tT][aA@4][rR]\b",

    # Methamphetamine Variations
    r"\b[mM][eE3][tT][hH]\b", r"\b[mM][eE3][tT][hH]?[aA@4][mM][pP][hH][eE3][tT][aA@4][mM][iI1!][nN][eE3$]?\b",
    r"\b[cC][rR][yY][sS][tT][aA@4][lL] [mM][eE3][tT][hH]\b", r"\b[iI1!][cC][eE3$]?\b",

    # Ecstasy / MDMA Variations
    r"\b[mM][o0][lL][lL][yY]\b", r"\b[eE3][cC][sS][tT][aA@4][cC][yY]\b", r"\b[xX][tT][cC]\b",
    r"\b[mM][dD][mM][aA@4]\b", r"\b[aA@4][dD][aA@4][mM]\b",
    r"\b[dD][iI1!][sS][cC][oO0] [bB][iI1!][sS][cC][uU][iI1!][tT]\b",

    # LSD / Acid Variations
    r"\b[lL][sS][dD]\b", r"\b[aA@4][cC][iI1!][dD]\b", r"\b[tT][rR][iI1!][pP][sS$]?\b",
    r"\b[mM][iI1!][cC][rR][oO0][dD][oO0][tT]\b",

    # Fentanyl Variations
    r"\b[fF][eE3][nN][tT][aA@4][nN][yY][lL]\b", r"\b[fF][eE3][nN][tT][aA@4][nN][iI1!][lL]\b",

    # Commonly used drug slangs with special characters
    r"\b[oO0][gG] [kK][uU][sS][hH]\b", r"\b[dD][aA@4][bB][wW][oO0][oO0][dD][sS]?\b",
    r"\b[bB][lL1][uU][eE3] [dD][rR][eE3][aA@4][mM]\b", r"\b[pP][iI1!][nN][kK] [sS][aA@4][kK][uU][rR][aA@4]\b",

    # ASCII / Unicode Variations from messages
    r"\b𝐌𝐞𝐭𝐡𝐚𝐦𝐩𝐡𝐞𝐭𝐚𝐦𝐢𝐧𝐞\b", r"\b𝐖𝐞𝐞𝐝 𝐆𝐚𝐧𝐣𝐚\b", r"\b𝐂𝐫𝐲𝐬𝐭𝐚𝐥 𝐌𝐞𝐭𝐡\b", r"\b𝐄𝐜𝐬𝐭𝐚𝐜𝐲\b",
    r"\b🄱🄻🅄🄴 🅂ᴀᴘᴘʜɪʀᴇ\b", r"\b𝑮𝒓𝒆𝒆𝒏 𝑪𝑹𝑨𝑪𝑲 𝑩𝒓𝒊𝒄𝒌\b", r"\b𝒀𝒆𝒍𝒍𝒐𝒘 𝑩𝒂𝒎𝒃𝒐𝒐\b",
    r"\b𝑹𝒆𝒅𝒔𝒕𝒓𝒊𝒏𝒈\b", r"\b𝑷𝒖𝒓𝒑𝒍𝒆 𝑹𝒖𝒏𝒕𝒛\b", r"\b𝑳𝑺𝑫 ✉\b"

    # Drug name variations (Standard)
                                           r"\bdrug\b", r"\bdru9\b", r"\bdru6\b", r"\bdrvg\b", r"\bdru@k\b",
    r"\bdru&\b", r"\bdr@g\b", r"\bdr*g\b", r"\bdr[u0]g\b", r"\bdr(u|0)g\b",

    # Cocaine and its variations
    r"\bcocaine\b", r"\bcoc@ine\b", r"\bc0caine\b", r"\bc0c@ine\b", r"\bcoke\b",
    r"\bc0ke\b", r"\bc0k3\b", r"\bblow\b", r"\bbl0w\b", r"\bsnow\b",

    # Marijuana / Weed Variations
    r"\bganja\b", r"\bg@nja\b", r"\bweed\b", r"\bw33d\b", r"\bpot\b",
    r"\bp0t\b", r"\bgrass\b", r"\bgr@ss\b", r"\bmary jane\b", r"\bdope\b",

    # Heroin Variations
    r"\bheroin\b", r"\bh[e3]r[o0]in\b", r"\bsmack\b", r"\bsm@ck\b", r"\bbrownsugar\b",
    r"\bbrown sugar\b", r"\bchitta\b", r"\bsafedi\b", r"\bdope\b", r"\bjunk\b",

    # Methamphetamine Variations
    r"\bmeth\b", r"\bm[e3]th\b", r"\bm[e3]+h\b", r"\bm[e3]th[a@]mphetamine\b",
    r"\bcrystal meth\b", r"\b1ce\b", r"\b!ce\b", r"\bspeed\b", r"\b5peed\b",

    # Ecstasy / MDMA Variations
    r"\bmolly\b", r"\bm0lly\b", r"\becstasy\b", r"\b3cstasy\b", r"\b3c5ta5y\b",
    r"\be\b", r"\bx\b", r"\bxtc\b", r"\bx7c\b", r"\badam\b",

    # LSD / Acid Variations
    r"\blsd\b", r"\bl5d\b", r"\bl\$d\b", r"\bacid\b", r"\b4cid\b", r"\b@cid\b",
    r"\bmellow yellow\b", r"\bwindow pane\b", r"\btabs\b", r"\bt@b5\b",

    # Fentanyl Variations
    r"\bfentanyl\b", r"\bf3nt@nyl\b", r"\bf3nt@n1l\b", r"\bfentanil\b", r"\bf3nt@nil\b",

    # Commonly used drug slangs
    r"\bog kush\b", r"\bdabwoods\b", r"\bblue dream\b", r"\bpink sakura\b",
    r"\bgreen crack\b", r"\byellow bamboo\b", r"\bredstring\b", r"\bpurple runtz\b",
    r"\blsd blotter\b", r"\bmdma pill\b", r"\bweed buds\b"

    # Updated drug name variations with ASCII characters
                                          r"\b[mM][eE3][tT7][hH4]+\b", r"\b[kK][eE3][tT7][aA4]m[i1][nN]+\b",
    r"\b[wW][eE3][eE3][dD]\b", r"\b[gG][aA4][nN][jJ][aA4]\b", r"\b[oO0][gG] [kK][uU][sS5][hH]\b",
    r"\b[bB][lL1][uU][eE3] [cC][rR][yY][sS5][tT7][aA4][lL1]\b",
    r"\b[pP][iI1][nN][kK] [sS5][aA4][kK][uU][rR][aA4]\b",
    r"\b[yY][eE3][lL1][lL1][oO0][wW] [bB][aA4][mM][bB][oO0][oO0]\b",

    # Ecstasy / MDMA variations
    r"\b[eE3][cC][sS5][tT7][aA4][cC][yY]\b", r"\b[mM][dD][mM][aA4]\b",
    r"\b[sS5][pP][oO0][nN][gG][eE3][bB][oO0][bB]\b", r"\b[dD][oO0][rR][eE3][aA4][mM][oO0][nN]\b",

    # Cocaine variations
    r"\b[cC][oO0][cC][aA4][iI1][nN]\b", r"\b[cC][oO0][kK][eE3]\b", r"\b[sS5][nN][oO0][wW]\b",
    r"\b[bB][lL1][oO0][wW]\b", r"\b[nN][oO0][sS5][eE3] [cC][aA4][nN][dD][yY]\b",

    # LSD / Acid Variations
    r"\b[lL1][sS5][dD]\b", r"\b[aA4][cC][iI1][dD]\b", r"\b[tT7][aA4][bB][sS5]\b",

    # Synthetic Cannabinoids
    r"\b[sS5][pP][iI1][cC][eE3]\b", r"\b[kK]2\b", r"\b[fF][aA4][kK][eE3] [wW][eE3][eE3][dD]\b",

    # Additional drug slang and names
    r"\b[bB][oO0][lL1][oO0] [rR][uU][nN][tT7][zZ2]\b", r"\b[dD][aA4][nN][tT7][eE3] [iI1][nN][fF][eE3][rR][nN][oO0]\b",
    r"\b[rR][eE3][aA4][lL1][tT7][aA4][lL1][kK] [eE3][xX][oO0][tT7][iI1][cC][sS5]\b",
    r"\b[pP][aA4][vV][eE3] [rR][uU][nN][tT7][zZ2]\b", r"\b[mM][oO0][tT7][hH4][aA4] [sS5][uU][cC][kK][aA4]\b",

    # Payment and delivery terms
    r"\b[pP][aA4][yY][lL1][aA4][hH4]\b", r"\b[pP][aA4][yY][nN][oO0][wW]\b",
    r"\b[cC][aA4][sS5][hH4] [dD][eE3][pP][oO0][sS5][iI1][tT7]\b",
    r"\b[dD][eE3][aA4][dD][dD][rR][oO0][pP]\b",

]


def check_suspicious_patterns(message):
    for pattern in suspicious_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            print(f"Debug: Pattern matched - {pattern}")  # Debug line
            return True
    return False

# Function to take user input and check if the message is suspicious
def main():
    user_input = input("Enter a message to check: ")
    if check_suspicious_patterns(user_input):
        print("⚠️ This message might be related to drug trafficking!")
    else:
        print("✅ This message seems safe.")

if __name__ == "__main__":
    main()
