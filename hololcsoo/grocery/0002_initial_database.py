from django.db import migrations

spar_product_dict = {'Mizo Light sovány, laktózmentes kakaós tej édesítőszerekkel 450 ml': {'name': 'Mizo Light sovány, laktózmentes kakaós tej édesítőszerekkel 450 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '539', 'unit_price': '(1 197,78 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': True, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/mizo-light-sovany-laktozmentes-kakaos-tej-edesitoszerekkel-450-ml/p/414975000'}, 'Mizo zsírszegény tejeskávé 450 ml': {'name': 'Mizo zsírszegény tejeskávé 450 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '525', 'unit_price': '(1 166,67 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': True, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/mizo-zsirszegeny-tejeskave-450-ml/p/349520009'}, 'Zöldfarm BIO UHT tej 2,8% 1 l': {'name': 'Zöldfarm BIO UHT tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '449', 'unit_price': '(449,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': True, 'product_url': '/onlineshop/zoldfarm-bio-uht-tej-28-1-l/p/270273005'}, 'Mizo zsírszegény kakaós ital 450 ml': {'name': 'Mizo zsírszegény kakaós ital 450 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '525', 'unit_price': '(1 166,67 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': True, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/mizo-zsirszegeny-kakaos-ital-450-ml/p/348727003'}, 'Mizo UHT zsírszegény, laktózmentes tej 1,5% 1 l': {'name': 'Mizo UHT zsírszegény, laktózmentes tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '669', 'unit_price': '(669,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/mizo-uht-zsirszegeny-laktozmentes-tej-15-1-l/p/294177006'}, 'Garabonciás házi aludttej 0,5 l': {'name': 'Garabonciás házi aludttej 0,5 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '425', 'unit_price': '(850,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/garaboncias-hazi-aludttej-05-l/p/290128002'}, 'Mizo UHT zsírszegény tej 1,5% 1 l': {'name': 'Mizo UHT zsírszegény tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '565', 'unit_price': '(565,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/mizo-uht-zsirszegeny-tej-15-1-l/p/270261002'}, 'Garabonciás teljes tehéntej 1 l': {'name': 'Garabonciás teljes tehéntej 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '545', 'unit_price': '(545,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/garaboncias-teljes-tehentej-1-l/p/290121003'}, 'Magyar Tej ESL tej 1,5% 1 l': {'name': 'Magyar Tej ESL tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '619', 'unit_price': '(619,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/magyar-tej-esl-tej-15-1-l/p/324959008'}, 'Mizo UHT félzsíros tej 2,8% 1 l': {'name': 'Mizo UHT félzsíros tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '329', 'unit_price': '(329,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/mizo-uht-felzsiros-tej-28-1-l/p/270262009'}, 'Zöldfarm BIO tej 1,5% 0,5 l': {'name': 'Zöldfarm BIO tej 1,5% 0,5 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '489', 'unit_price': '(978,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': True, 'product_url': '/onlineshop/zoldfarm-bio-tej-15-05-l/p/291286008'}, 'Magyar Tej ESL tej 2,8% 1 l': {'name': 'Magyar Tej ESL tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '629', 'unit_price': '(629,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/magyar-tej-esl-tej-28-1-l/p/324961001'}, 'Tolle ESL kakaós tej 0,5 l': {'name': 'Tolle ESL kakaós tej 0,5 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '435', 'unit_price': '(870,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/tolle-esl-kakaos-tej-05-l/p/293369006'}, 'S-Budget UHT félzsíros tej 2,8% 1 l': {'name': 'S-Budget UHT félzsíros tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '209', 'unit_price': '(209,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/s-budget-uht-felzsiros-tej-28-1-l/p/296438006'}, 'Riska Zero UHT sovány tej 0,1% 1 l': {'name': 'Riska Zero UHT sovány tej 0,1% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '389', 'unit_price': '(389,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/riska-zero-uht-sovany-tej-01-1-l/p/382952003'}, 'Müller Müllermilch csokoládé ízű zsírszegény tejital 377 ml': {'name': 'Müller Müllermilch csokoládé ízű zsírszegény tejital 377 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '349', 'unit_price': '(1 047.50 Ft/kg)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/muller-mullermilch-csokolade-izu-zsirszegeny-tejital-377-ml/p/247446005'}, 'Zöldfarm BIO tej 3,5% 1 l': {'name': 'Zöldfarm BIO tej 3,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '869', 'unit_price': '(869,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': True, 'product_url': '/onlineshop/zoldfarm-bio-tej-35-1-l/p/254907001'}, 'Zöldfarm BIO UHT zsírszegény tej 1,5% 1 l': {'name': 'Zöldfarm BIO UHT zsírszegény tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '779', 'unit_price': '(779,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': True, 'product_url': '/onlineshop/zoldfarm-bio-uht-zsirszegeny-tej-15-1-l/p/270272008'}, 'Mizo félzsíros tej 2,8% 1 l': {'name': 'Mizo félzsíros tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '545', 'unit_price': '(545,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/mizo-felzsiros-tej-28-1-l/p/108714007'}, 'Riska UHT zsírszegény tej 1,5% 1 l': {'name': 'Riska UHT zsírszegény tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '249', 'unit_price': '(369.00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/riska-uht-zsirszegeny-tej-15-1-l/p/401667000'}, 'Mizo Coffee Selection Cappuccino UHT laktózmentes, félzsíros kávés tej 330 ml': {'name': 'Mizo Coffee Selection Cappuccino UHT laktózmentes, félzsíros kávés tej 330 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '619', 'unit_price': '(1 875,76 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/mizo-coffee-selection-cappuccino-uht-laktozmentes-felzsiros-kaves-tej-330-ml/p/463951000'}, 'Mizo Coffee Selection Espresso UHT zsírszegény kávés tej 330 ml': {'name': 'Mizo Coffee Selection Espresso UHT zsírszegény kávés tej 330 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '639', 'unit_price': '(1 936,36 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/mizo-coffee-selection-espresso-uht-zsirszegeny-kaves-tej-330-ml/p/463954001'}, 'Riska UHT laktózmentes tej 2,8% 1 l': {'name': 'Riska UHT laktózmentes tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '379', 'unit_price': '(379,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/riska-uht-laktozmentes-tej-28-1-l/p/431602002'}, 'Milli Oké! UHT kakaós tej 450 ml': {'name': 'Milli Oké! UHT kakaós tej 450 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '309', 'unit_price': '(686,67 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/milli-oke-uht-kakaos-tej-450-ml/p/431516002'}, 'Riska UHT laktózmentes, zsírszegény tej 1,5% 1 l': {'name': 'Riska UHT laktózmentes, zsírszegény tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '649', 'unit_price': '(649,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/riska-uht-laktozmentes-zsirszegeny-tej-15-1-l/p/426573003'}, 'Milli Oké! UHT karamellás tej 450 ml': {'name': 'Milli Oké! UHT karamellás tej 450 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '309', 'unit_price': '(686,67 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/milli-oke-uht-karamellas-tej-450-ml/p/428671004'}, 'Müller Müllermilch banán ízű zsírszegény tejital 377 ml': {'name': 'Müller Müllermilch banán ízű zsírszegény tejital 377 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '349', 'unit_price': '(1 047.50 Ft/kg)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/muller-mullermilch-banan-izu-zsirszegeny-tejital-377-ml/p/428839008'}, 'Milli UHT jegeskávé 300 ml': {'name': 'Milli UHT jegeskávé 300 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '415', 'unit_price': '(1 383,33 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/milli-uht-jegeskave-300-ml/p/393596005'}, 'Magyar Tej UHT zsírszegény tej 1,5% 1 l': {'name': 'Magyar Tej UHT zsírszegény tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '549', 'unit_price': '(549,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/magyar-tej-uht-zsirszegeny-tej-15-1-l/p/342155000'}, 'S-Budget Cappuccino zsírszegény kávés tejital 250 ml': {'name': 'S-Budget Cappuccino zsírszegény kávés tejital 250 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '295', 'unit_price': '(1 180,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/s-budget-cappuccino-zsirszegeny-kaves-tejital-250-ml/p/342355004'}, 'S-Budget UHT zsírszegény tej 1,5% 1 l': {'name': 'S-Budget UHT zsírszegény tej 1,5% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '329', 'unit_price': '(329,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/s-budget-uht-zsirszegeny-tej-15-1-l/p/306594005'}, 'Mizo félzsíros tej 2,8% 1,5 l': {'name': 'Mizo félzsíros tej 2,8% 1,5 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '539', 'unit_price': '(359,33 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': True, 'is_bio': False, 'product_url': '/onlineshop/mizo-felzsiros-tej-28-15-l/p/376997003'}, 'Magyar Tej UHT tej 2,8% 1 l': {'name': 'Magyar Tej UHT tej 2,8% 1 l', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '299', 'unit_price': '(299,00 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/magyar-tej-uht-tej-28-1-l/p/324965009'}, 'Mizo Coffee Selection Melange UHT félzsíros kávés tej 330 ml': {'name': 'Mizo Coffee Selection Melange UHT félzsíros kávés tej 330 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '639', 'unit_price': '(1 936,36 Ft/l)', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/mizo-coffee-selection-melange-uht-felzsiros-kaves-tej-330-ml/p/471804008'}, 'S-Budget Latte Espresso zsírszegény kávés tejital 250 ml': {'name': 'S-Budget Latte Espresso zsírszegény kávés tejital 250 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '295', 'unit_price': '(1 180,00 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/s-budget-latte-espresso-zsirszegeny-kaves-tejital-250-ml/p/469846003'}, 'Starbucks Cappuccino félzsíros tejital 220 ml': {'name': 'Starbucks Cappuccino félzsíros tejital 220 ml', 'category': 'H3-1', 'sold_by': 'SPAR', 'price': '939', 'unit_price': '(4 268,18 Ft/l)', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_hungarian_product': False, 'is_bio': False, 'product_url': '/onlineshop/starbucks-cappuccino-felzsiros-tejital-220-ml/p/477980003'}}
auchan_product_dict = {'Abaúj tej dobozos 2,8% 1 l': {'name': 'Abaúj tej dobozos 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '329', 'unit_price': '329\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/abauj-tej-dobozos-28percent-1-l.p-578339'}, 'Auchan Nívó Pasztőrözött dobozos tej 1,5% 1 l': {'name': 'Auchan Nívó Pasztőrözött dobozos tej 1,5% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '369', 'unit_price': '369\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/auchan-nivo-pasztorozott-dobozos-tej-15percent-1-l.p-119589'}, 'Auchan Nívó ESL Palackozott tej 1,5% 1 l': {'name': 'Auchan Nívó ESL Palackozott tej 1,5% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '399', 'unit_price': '399\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/auchan-nivo-esl-palackozott-tej-15percent-1-l.p-391628'}, 'Auchan Nívó Pasztőrözött dobozos tej 2,8% 1 l': {'name': 'Auchan Nívó Pasztőrözött dobozos tej 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '399', 'unit_price': '399\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/auchan-nivo-pasztorozott-dobozos-tej-28percent-1-l.p-119590'}, 'Auchan Nívó ESL Palackozott tej 2,8% 1 l': {'name': 'Auchan Nívó ESL Palackozott tej 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '449', 'unit_price': '449\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/auchan-nivo-esl-palackozott-tej-28percent-1-l.p-391627'}, 'Auchan Nívó Pasztőrözött dobozos tej 3,5% 1 l': {'name': 'Auchan Nívó Pasztőrözött dobozos tej 3,5% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '449', 'unit_price': '449\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/auchan-nivo-pasztorozott-dobozos-tej-35percent-1-l.p-137397'}, 'Magyar és Finom tej dobozos 2,8% 1 l': {'name': 'Magyar és Finom tej dobozos 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '459', 'unit_price': '459\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/magyar-es-finom-tej-dobozos-28percent-1-l.p-856867'}, 'Abaúj tej dobozos 1,5% 1 l': {'name': 'Abaúj tej dobozos 1,5% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '479', 'unit_price': '479\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/abauj-tej-dobozos-15percent-1-l.p-578337'}, 'AP Gazdától az asztalig Friss tej 1,5% 1 l': {'name': 'AP Gazdától az asztalig Friss tej 1,5% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '479', 'unit_price': '479\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/ap-gazdatol-az-asztalig-friss-tej-15percent-1-l.p-308178'}, 'Mizo zsírszegény tej 1,5% 1 l': {'name': 'Mizo zsírszegény tej 1,5% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '479', 'unit_price': '479\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': True, 'is_local_product': True, 'is_bio': False, 'product_url': '/shop/mizo-zsirszegeny-tej-15percent-1-l.p-52679'}, 'Garabonciás teljes tehéntej 1 l': {'name': 'Garabonciás teljes tehéntej 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '485', 'unit_price': '485\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/garaboncias-teljes-tehentej-1-l.p-780175'}, 'Mizo félzsíros tej 2,8% 1 l': {'name': 'Mizo félzsíros tej 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '489', 'unit_price': '489\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/mizo-felzsiros-tej-28percent-1-l.p-52677'}, 'Parmalat ESL félzsíros tej 1 l': {'name': 'Parmalat ESL félzsíros tej 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '499', 'unit_price': '499\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/parmalat-esl-felzsiros-tej-1-l.p-873946'}, 'AP Gazdától az asztalig Friss tej 2,8% 1 l': {'name': 'AP Gazdától az asztalig Friss tej 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '539', 'unit_price': '539\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/ap-gazdatol-az-asztalig-friss-tej-28percent-1-l.p-308087'}, 'Tarka ESL félzsíros tej 2,8% 1 l': {'name': 'Tarka ESL félzsíros tej 2,8% 1 l', 'category': 'c-6537', 'sold_by': 'Auchan', 'price': '539', 'unit_price': '539\xa0Ft / 1 liter', 'is_vegan': False, 'is_cooled': False, 'is_local_product': False, 'is_bio': False, 'product_url': '/shop/tarka-esl-felzsiros-tej-28percent-1-l.p-520523'}}


def create_model_instances(apps, schema_editor):
    Grocery = apps.get_model("grocery", "Grocery")
    Category = apps.get_model("grocery", "Category")
    Item = apps.get_model("grocery", "Item")
    Price = apps.get_model("grocery", "Price")

    create_groceries(Grocery)
    create_categories(Category, Grocery)
    create_items(Item, Category)
    create_prices(Price, Item)


def create_groceries(Grocery):
    groceries = [
        Grocery(
            grocery_name="SPAR",
        ),
        Grocery(
            grocery_name="Auchan",
        ),
    ]

    for grocery in groceries:
        grocery.save()


def create_categories(Category, Grocery):
    categories = [
        Category(
            category_name="Friss tej",
            category_id="c-6537",
            sold_by=Grocery.objects.get(grocery_name="Auchan")
        ),
        Category(
            category_name="Friss tej",
            category_id="H3-1",
            sold_by=Grocery.objects.get(grocery_name="SPAR")
        ),
    ]

    for category in categories:
        category.save()


def create_items(Item, Category):
    for item_attributes in spar_product_dict.values():
        spar_item = Item(
                name=item_attributes['name'],
                categories=Category.objects.get(category_id=item_attributes['category']),
                product_link=item_attributes['product_url'],
                is_vegan=item_attributes['is_vegan'],
                is_cooled=item_attributes['is_cooled'],
                is_local_product=item_attributes['is_local_product'],
                is_hungarian_product=item_attributes['is_hungarian_product'],
                is_bio=item_attributes['is_bio'],
            )
        spar_item.save()

    for item_attributes in auchan_product_dict.values():
        auchan_item = Item(
                name=item_attributes['name'],
                categories=Category.objects.get(category_id=item_attributes['category']),
                product_link=item_attributes['product_url'],
                is_vegan=item_attributes['is_vegan'],
                is_cooled=item_attributes['is_cooled'],
                is_local_product=item_attributes['is_local_product'],
                is_hungarian_product=False,
                is_bio=item_attributes['is_bio'],
                on_stock=True,
                on_sale=False,
            )

        auchan_item.save()


def create_prices(Price, Item):
    for item_attributes in spar_product_dict.values():
        spar_price = Price(
                item=Item.objects.filter(categories__sold_by__grocery_name="SPAR", name=item_attributes["name"]).get(),
                value=item_attributes['price'],
                sale_value=item_attributes['price'],
                unit='SI',
                unit_price=1000.0,
            )

        spar_price.save()

    for item_attributes in auchan_product_dict.values():
        auchan_price = Price(
                item=Item.objects.filter(categories__sold_by__grocery_name="Auchan", name=item_attributes["name"]).get(),
                value=item_attributes['price'],
                sale_value=item_attributes['price'],
                unit='SI',
                unit_price=1000.0,
            )
        auchan_price.save()


class Migration(migrations.Migration):

    dependencies = [
        ("grocery", "0001_initial"),
         ]

    operations = [
        migrations.RunPython(create_model_instances),
    ]