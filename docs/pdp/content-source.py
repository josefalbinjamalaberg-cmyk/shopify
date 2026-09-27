import json
G='gid://shopify/Product/'
V='gid://shopify/Video/'
ID=dict(alkastrike='15959788814670',pure='15963382055246',foamtastic='15963388379470',glosscoat='15963394867534',revolt='15963399553358',pristine='15963415740750',deepdegrease='15963418362190',coreapc='15963421442382',clarity='15963424031054',tvatthink='15963454832974',tryckspruta='15963460075854',foamcannon='15963462795598',scrubpad='15963468333390',falgborste='15963479048526',washpad='15963482751310',dackapplikator='15963484750158',torkduk70='15963493466446',torkduk50='15963500609870',torkduk40='15963501134158',mikrofiberduk='15963505688910',detailbrush='16015861219662',deepreach='16015891235150',glasstowel='16015909454158',
 k_falgstart='16016364077390',k_falgdack='16016378134862',k_foamwash='16016437608782',k_extstart='16018450940238',k_extkomplett='16018547671374',k_intlitet='15996560376142',k_intmellan='16015851487566',k_intstort='16015857221966')
VID=dict(alkaliskhemsida='73252319297870',foamhemsida='73250165883214',foambanner1='73183249793358',glosscoattttt='73250234433870',avrinning='73183386403150',pristine='73249670562126',schampo='73250194784590',coreapc='73250208481614',falgborste='73250048835918',washpad='73250258026830',hink='73252404527438')

C={}
C['alkastrike']=dict(preset='kemikalie',type_label='Alkalisk förtvätt',
 value_line='Löser trafikfilm, insekter och organisk smuts före kontaktvätten.',
 benefits=['För trafikfilm, insekter och vägsmuts','Späds efter hur smutsig bilen är','Mindre smuts kvar när handtvätten börjar'],
 problems=['Trafikfilm | Grå smutsfilm på sidor och nedre paneler.','Insektsrester | Insektsrester på front och speglar.','Pollen och organisk beläggning | Beläggning som sätter sig på lacken.','Vägsmuts | Vägsmuts inför skum- och kontaktvätt.'],
 compare_with='deepdegrease',compare_heading='Vilken avfettning behöver du?',best_for=['Trafikfilm','Insekter','Pollen','Organisk smuts'],compare_note='Har bilen både asfaltsstänk och trafikfilm kan båda produkterna behövas.',
 why=['Smuts som sitter kvar när handtvätten börjar följer ofta med tvätthandsken över lacken.','Alkastrike löser upp trafikfilm, insekter och organisk smuts innan kontaktvätten börjar, så att mer kan spolas bort innan lacken berörs.'],
 demo_heading='Se Alkastrike arbeta',demo_media=['alkaliskhemsida'],
 steps=['Späd produkten | Blanda efter smutsgrad och enligt produktetiketten.','Applicera jämnt | Spraya jämnt över ytan med en tryckspruta.','Låt verka | Följ verkningstiden på etiketten. Produkten får aldrig torka in.','Skölj noggrant | Spola av med högtryck och fortsätt med nästa steg i tvätten.'],
 usage_note='Koncentrat – späds upp till 1:25 beroende på smutsgrad.',
 safety_note='Använd inte på varma ytor eller i direkt solljus, och låt aldrig produkten torka in.',
 routine_note='Förtvätt: används före skumtvätt och kontaktvätt.',
 kit_upgrade='k_extstart',kit_heading='Bygg hela förtvätten',
 accessories=['tryckspruta','foamtastic','pure'],accessory_reasons=['För jämn applicering av Alkastrike.','Nästa steg: skumförtvätt före handtvätten.','Bilschampo för kontaktvätten efter förtvätten.'],
 specs=['Typ | Koncentrerad alkalisk förtvätt','Volym | 500 ml','Spädning | Upp till 1:25','Doft | Citrus','Applicering | Tryckspruta'],
 faq=['Vad är skillnaden mellan Alkastrike och DeepDegrease? | Alkastrike är en alkalisk förtvätt för trafikfilm, insekter, pollen och annan organisk smuts. DeepDegrease är en kallavfettning för asfalt, tjära och oljerester. Vissa bilar behöver båda.',
  'Ersätter Alkastrike handtvätten? | Nej. Alkastrike är en förtvätt som löser smuts innan kontaktvätten, till exempel med Pure Shampoo.',
  'Hur späder jag Alkastrike? | Alkastrike är koncentrerad och kan spädas upp till 1:25. Blanda efter smutsgrad och följ produktetiketten.',
  'Kan jag använda Alkastrike i solen? | Nej. Använd den inte på varma ytor eller i direkt solljus, och låt den aldrig torka in.'])

C['deepdegrease']=dict(preset='kemikalie',type_label='Kallavfettning',
 value_line='Löser upp asfalt, tjära och oljebaserad smuts – före handtvätten.',
 benefits=['För asfalt, tjära och oljerester','Tar det som vanligt bilschampo inte klarar','Används före handtvätten'],
 problems=['Asfalt | Asfaltsstänk från nyasfalterade vägar och stenskott.','Tjära | Tjärfläckar på nedre paneler och trösklar.','Oljerester | Olje- och fettrester på bilens exteriör.'],
 compare_with='alkastrike',compare_heading='Vilken avfettning behöver du?',best_for=['Asfalt','Tjära','Oljerester','Petroleumbaserad smuts'],compare_note='Har bilen både asfaltsstänk och trafikfilm kan båda produkterna behövas.',
 why=['Asfalt, tjära och oljerester sitter hårdare än vanlig vägsmuts och löses inte upp av vatten eller vanligt bilschampo.','DeepDegrease är en lösningsmedelsbaserad kallavfettning som bryter ner smutsen innan handtvätten börjar.'],
 steps=['Ventilera | Arbeta utomhus eller i ett väl ventilerat utrymme, långt från öppen låga och gnistor.','Applicera på smutsen | Applicera direkt på asfaltsstänk, tjära eller oljerester.','Låt verka | Följ verkningstiden på etiketten. Inte i solljus eller på varma ytor – och låt aldrig produkten torka in.','Torka av | Torka bort den upplösta smutsen med en duk. Se etiketten för eventuell avsköljning.'],
 usage_note='Används outspädd – ska inte blandas med vatten.',
 safety_note='Brandfarlig (H226). Använd aldrig nära öppen låga, gnistor eller värmekällor och arbeta i ett väl ventilerat utrymme.',
 routine_note='Förtvätt: används på fläckarna före handtvätten.',
 kit_upgrade='k_extstart',kit_heading='Bygg hela förtvätten',
 accessories=['mikrofiberduk','pure'],accessory_reasons=['För att torka bort den upplösta smutsen.','Bilschampo för handtvätten efteråt.'],
 specs=['Typ | Lösningsmedelsbaserad kallavfettning','Volym | 1000 ml','Spädning | Används outspädd','Vattenlöslig | Nej (enligt säkerhetsdatabladet)','Faroklass | Brandfarlig (H226)'],
 faq=['Vad är skillnaden mellan DeepDegrease och Alkastrike? | DeepDegrease är en kallavfettning för asfalt, tjära, oljerester och annan petroleumbaserad smuts. Alkastrike är en alkalisk förtvätt för trafikfilm, insekter, pollen och organisk smuts. Vissa bilar behöver båda.',
  'Ska DeepDegrease spädas? | Nej. Enligt säkerhetsdatabladet är den inte vattenlöslig och används outspädd.',
  'Är DeepDegrease brandfarlig? | Ja, den är klassificerad som brandfarlig (H226). Använd den aldrig nära öppen låga, gnistor eller värmekällor och arbeta i ett väl ventilerat utrymme.',
  'Kan jag använda DeepDegrease i garaget? | Endast i ett väl ventilerat utrymme. Se säkerhetsdatabladet för fullständig information om säker hantering.',
  'Ska jag spola av efteråt? | Eftersom produkten inte är vattenlöslig rekommenderas i första hand avtorkning med en ren duk. Se produktetiketten för eventuell avspolning.'])

C['foamtastic']=dict(preset='kemikalie',type_label='Snow foam / förtvätt',
 value_line='Tjockt, vidhäftande skum som löser upp smuts innan handtvätten.',
 benefits=['Tjockt skum som stannar kvar och arbetar','Löser upp smuts innan du rör lacken','Minskar risken för tvättrepor'],
 problems=['Förtvätt | Löser upp smuts och trafikfilm innan handtvätten.','Kraftigt smutsig bil | Mer smuts spolas bort innan tvätthandsken rör lacken.','Underhållstvätt | Ett skonsamt första steg vid regelbunden tvätt.'],
 compare_with='pure',compare_heading='Förtvätt eller kontaktvätt?',best_for=['Förtvätt med Foam Cannon','Används före handtvätten','Löser smuts innan kontakt'],compare_note='De ersätter inte varandra – Foamtastic kommer först, Pure Shampoo sedan.',
 why=['Ett tunt skum rinner av innan det hinner verka. Foamtastic ger ett tjockt lager som stannar kvar på bilen.','Skummet kapslar in och löser upp smuts och trafikfilm, så att mer spolas bort innan tvätthandsken rör lacken.'],
 demo_heading='Se Foamtastic skumma',demo_media=['foamhemsida','foambanner1'],
 steps=['Fyll Foam Cannon | Dosera enligt produktetiketten och kanonens inställning.','Skumma uppifrån och ner | Täck hela bilen med ett jämnt, tjockt lager.','Låt skummet verka | Ge skummet tid att lösa upp smutsen.','Skölj innan det torkar | Spola av med högtryck och fortsätt med handtvätten.'],
 usage_note='Används med Foam Cannon och högtryckstvätt.',
 safety_note='Applicera inte i direkt solljus eller på varma ytor. Skölj av innan skummet torkar.',
 routine_note='Förtvätt: skumma bilen innan handtvätten.',
 kit_upgrade='k_foamwash',kit_heading='Skumtvätta direkt',
 accessories=['foamcannon','pure'],accessory_reasons=['Behövs för att skapa skummet.','Kontaktvätten efter förtvätten.'],
 specs=['Typ | Snow foam (förtvätt)','Volym | 1000 ml','Applicering | Foam Cannon'],
 faq=['Är Foamtastic ett schampo? | Nej. Foamtastic är en förtvätt som löser smuts innan handtvätten. Efter avspolning fortsätter tvätten med ett kontaktvätt-schampo som Pure Shampoo.',
  'Behöver jag en Foam Cannon? | Ja. Foamtastic är gjord för att användas i en foam cannon – det är den som ger det tjocka, jämna skummet.',
  'Hur blandar jag Foamtastic? | Följ doseringen på produktetiketten och din foam cannons inställning.',
  'Hur länge ska skummet verka? | Följ verkningstiden på produktetiketten och skölj alltid av innan skummet torkar på lacken.',
  'Vad gör jag om skummet börjar torka? | Spola omedelbart av ytan med rikligt med vatten. Undvik direkt solljus och varma ytor.'])

C['pure']=dict(preset='kemikalie',type_label='Bilschampo för kontaktvätt',
 value_line='Skonsamt mot vax och keramiska lackskydd – ändå kraftfullt mot smuts och vägfilm.',
 benefits=['Skonsamt mot vax och keramiska lackskydd','Högkoncentrerat – en liten mängd räcker långt','Rent, blankt resultat efter sköljning'],
 problems=['Kontaktvätt | Handtvätt med washpad eller tvätthandske efter förtvätten.','Underhållstvätt | Regelbunden tvätt utan att påverka vax eller lackskydd.','Behandlad lack | Bilar med vax, lackförsegling eller keramiskt skydd.'],
 compare_with='foamtastic',compare_heading='Förtvätt eller kontaktvätt?',best_for=['Kontaktvätt i tvätthinken','Används med washpad','Efter förtvätten'],compare_note='De ersätter inte varandra – Foamtastic kommer först, Pure Shampoo sedan.',
 why=['Pure Shampoo blandas i tvätthinken och används med washpad eller tvätthandske.','Det rengör lacken utan att bryta ner befintligt vax, lackförsegling eller keramiskt lackskydd.'],
 demo_heading='Se Pure Shampoo i tvätthinken',demo_media=['schampo'],
 steps=['Späd i tvätthinken | Blanda enligt produktetiketten.','Tvätta med två hinkar | Panel för panel, uppifrån och ner, med en separat sköljhink.','Skölj washpaden ofta | Skölj i sköljhinken innan den doppas i schampot igen.','Spola av | Avsluta med att spola av hela bilen med rent vatten.'],
 usage_note='Högkoncentrerat – späds upp till 1:1900 enligt produktetiketten.',
 safety_note='Låt inte produkten torka på ytan. Skölj av grundligt och arbeta gärna i skugga.',
 routine_note='Handtvätt: kontaktvätten efter förtvätten.',
 kit_upgrade='k_extstart',kit_heading='Bygg hela tvätten',
 accessories=['washpad','tvatthink','torkduk70'],accessory_reasons=['Mjuk mikrofiber för kontaktvätten.','Grit Guard håller smutsen nere – för tvåhinksmetoden.','Torka bilen direkt efter tvätten.'],
 specs=['Typ | Bilschampo för kontaktvätt','Volym | 500 ml','Spädning | Upp till 1:1900','Applicering | Tvätthink med washpad eller tvätthandske','Vattenavvisande effekt | Nej – rent schampo utan vax'],
 faq=['Vad är skillnaden mellan Pure Shampoo och en förtvätt? | Pure Shampoo används i tvätthinken med washpad eller tvätthandske. En förtvätt som Alkastrike eller Foamtastic löser smuts innan kontaktvätten börjar. De kompletterar varandra.',
  'Vad är tvåhinksmetoden? | En hink med utspätt schampo och en separat sköljhink med rent vatten. Washpaden sköljs mellan varje panel, vilket minskar risken för repor och virvelmärken.',
  'Behöver jag förtvätta först? | Vid kraftig nedsmutsning rekommenderar vi en förtvätt, till exempel med Alkastrike eller Foamtastic, innan kontaktvätten.',
  'Ger Pure Shampoo en vattenavvisande effekt? | Nej. Det är ett rent schampo utan vax, framtaget för att rengöra utan att påverka befintliga behandlingar.',
  'Hur späder jag Pure Shampoo? | Det är högkoncentrerat och späds upp till 1:1900. Följ doseringen på produktetiketten.'])

C['glosscoat']=dict(preset='kemikalie',type_label='Sprayförsegling',
 value_line='Glans och vattenavrinning på några minuter – sista steget efter tvätten.',
 benefits=['Djupare glans direkt efter tvätten','Vattnet rinner av – bilen är enklare att hålla ren','Spraya på, fördela, torka av'],
 problems=['Efter tvätten | Sista steget på en ren och torr bil.','Mer glans | När lacken ska få djupare glans.','Vattenavrinning | När vatten ska rinna av istället för att lägga sig platt.'],
 why=['GlossCoat lägger ett hydrofobiskt lager på ytan – vatten pärlar av istället för att lägga sig platt.','Resultatet syns direkt i reflektionerna, och bilen blir enklare att hålla ren mellan tvättarna.'],
 demo_heading='Se GlossCoat på lacken',demo_media=['avrinning','glosscoattttt'],
 steps=['Förbered ytan | Tvätta och torka bilen. Arbeta på en ren, torr och sval yta.','Spraya | Ett tunt, jämnt lager på en mindre sektion i taget.','Fördela och torka av | Buffa med en ren mikrofiberduk tills ytan är jämn och blank.','Låt torka | Låt ytan torka innan den utsätts för vatten. Följ torktiden på etiketten.'],
 safety_note='Applicera inte i direkt solljus eller på en varm yta.',
 routine_note='Finish och skydd: sista steget efter tvätt och torkning.',
 kit_upgrade='k_extkomplett',kit_heading='Hela tvätten i ett paket',
 accessories=['mikrofiberduk','torkduk40','pure'],accessory_reasons=['För att fördela och torka av GlossCoat.','Kompakt duk för eftertorkning och detaljer.','Tvätta bilen innan GlossCoat appliceras.'],
 specs=['Typ | Hydrofobisk sprayförsegling','Används på | Lack, glas och andra exteriöra ytor enligt produktetiketten','Applicering | Spray och mikrofiberduk'],
 faq=['När applicerar jag GlossCoat? | Som sista steg, när bilen är tvättad och torr.','Behöver bilen vara ren? | Ja. Applicera på en ren, torr och sval yta – inte i direkt solljus.','Hur applicerar jag GlossCoat? | Spraya ett tunt lager på en mindre sektion och fördela med en ren mikrofiberduk tills ytan är jämn och blank.',
  'Kan GlossCoat användas på glas? | Ja, på lack, glas och andra exteriöra ytor enligt produktetiketten.','Hur länge håller skyddet? | Se produktetiketten för information om hållbarhet vid normal användning och väder.','Kan jag kombinera GlossCoat med vax eller keramisk coating? | Se produktetiketten och säkerhetsdatabladet för kompatibilitet innan kombinerad användning.'])

C['clarity']=dict(preset='kemikalie',type_label='Glasrengöring',
 value_line='Klart glas utan ränder – in- och utvändigt.',
 benefits=['Rengör utan ränder','Löser fett, fingeravtryck och trafikfilm','För in- och utvändigt glas'],
 problems=['Fingeravtryck | Fett och fingeravtryck på insidan av rutorna.','Trafikfilm | Beläggning på vindruta och sidorutor.','Ränder | När glaset ska bli klart utan ränder.'],
 why=['Clarity är gjord för snabb avdunstning och enkel avtorkning.','Fett, fingeravtryck och trafikfilm löses upp utan att lämna beläggning på glaset.'],
 steps=['Invändigt | Spraya på en ren duk istället för direkt på glaset – så undviker du överskott på instrumentpanelen.','Utvändigt | Spraya direkt på glaset när ytan inte är varm eller i direkt solljus.','Torka | Torka med lätta, jämna rörelser med en ren mikrofiberduk.','Eftertorka | Eftertorka med en torr glasduk för en klar finish.'],
 safety_note='Använd inte på varma ytor eller i direkt solljus.',
 routine_note='Finish: glasen när resten av bilen är ren.',
 kit_upgrade='k_intstort',kit_heading='Komplett interiörvård',
 accessories=['glasstowel','mikrofiberduk'],accessory_reasons=['Glasduk för en klar, randfri eftertorkning.','För avtorkningen innan eftertorkningen.'],
 specs=['Typ | Glasrengöring','Volym | 500 ml','Används på | In- och utvändigt glas','Applicering | Sprayflaska'],
 faq=['Är Clarity ränderfri? | Ja, när rena dukar används och produkten inte överappliceras.','Kan Clarity användas både invändigt och utvändigt? | Ja. Invändigt sprayar du på duken, utvändigt direkt på glaset.','Hur får jag bäst resultat? | Torka bort smutsen med en ren mikrofiberduk och eftertorka med en torr glasduk.','Kan jag använda Clarity i solen? | Nej. Använd den inte på varma ytor eller i direkt solljus.','Vilken duk ska jag använda? | En ren mikrofiberduk för avtorkning och en torr glasduk för eftertorkning. Smutsiga dukar kan ge ränder.'])

C['pristine']=dict(preset='kemikalie',type_label='Däck- och plastförnyare',
 value_line='Djupare färg och jämn finish på däck och utvändig plast.',
 benefits=['Djup, naturlig finish – inte blöt och blank','För däck och utvändig plast','Enkel att applicera med däckapplikator'],
 problems=['Gråa däck | Däck som blivit torra och grå.','Blekt plast | Utvändiga plastdetaljer som stötfångare och lister.','Sista finishen | När bilen är tvättad och ska se komplett ut.'],
 why=['Pristine återställer den djupa färgen i däck och utvändig plast – utan den blöta, överdrivet glansiga finishen.','Resultatet är en naturligt mörk och jämn yta.'],
 demo_heading='Se Pristine på däcket',demo_media=['pristine'],
 steps=['Förbered ytan | Tvätta däcket eller plasten och låt torka.','Applicera | Lägg en liten mängd Pristine på en applikator.','Fördela jämnt | Arbeta in produkten jämnt över ytan.','Eftertorka | Torka bort eventuellt överskott och låt finishen sätta sig.'],
 safety_note='Applicera inte på varma ytor eller i solljus. Undvik bromsskivor och låt torka innan körning eller regn.',
 routine_note='Finish: sista steget på däck och plast.',
 kit_upgrade='k_falgdack',kit_heading='Gör fälg och däck kompletta',
 accessories=['dackapplikator','revolt','mikrofiberduk'],accessory_reasons=['Fördelar Pristine jämnt runt hela däcket.','Rengör fälgen innan däcket får sin finish.','Torka bort överskott efter appliceringen.'],
 specs=['Typ | Däck- och plastförnyare','Volym | 500 ml','pH | 6–7 (enligt säkerhetsdatabladet)','Faroklassning | Inte klassificerad som farlig','Färg | Rosa','Doft | Parfymerad'],
 faq=['Kan Pristine användas på både däck och plast? | Ja, på däck och utvändiga plastdetaljer.','Ska Pristine spädas? | Se produktetiketten för information om dosering innan användning.','Hur applicerar jag Pristine på däck? | Med en däckapplikator, jämnt runt hela däcket. Torka bort överskott med en ren mikrofiberduk och låt torka innan bilen körs.','Blir däcken blöta och blanka? | Nej, målet är en naturlig, jämn finish. Applicera tunna lager och torka bort överskott.','Är Pristine klassificerad som farlig? | Nej. Enligt säkerhetsdatabladet är den inte klassificerad som farlig.','Hur ofta ska jag använda Pristine? | Som återkommande underhåll efter tvätt. Se produktetiketten för fler rekommendationer.'])

C['coreapc']=dict(preset='kemikalie',type_label='Allrengöring (APC)',
 value_line='Koncentrerad rengöring för smuts, fett och fläckar – invändigt och utvändigt.',
 benefits=['Löser smuts, fett och fläckar','Späds efter hur smutsigt det är','För plast, vinyl, textil och gummi'],
 problems=['Plastytor | Instrumentbräda, mittkonsol och dörrsidor.','Textil | Mattor och tygklädsel.','Gummi och lister | Dörrsillar och gummilister.'],
 why=['Bilar samlar smuts på många olika ytor.','Core APC späds efter behov och fungerar på plast, vinyl, textil och gummi – mildare för underhåll, starkare för tuff smuts.'],
 demo_heading='Se Core APC arbeta',demo_media=['coreapc'],
 steps=['Späd efter behov | Mildare för underhåll, starkare för tuff smuts – enligt etiketten.','Spraya på ytan | Jämnt över ytan. Undvik direkt solljus och varma ytor.','Bearbeta | Arbeta in med duk, borste eller Scrub Pad efter yta och smutsgrad.','Torka av | Torka av med en ren mikrofiberduk. Vid kraftig smuts: skölj först.'],
 usage_note='Koncentrat – späds efter smutsgrad enligt produktetiketten.',
 safety_note='Undvik varma ytor och direkt solljus. Låt aldrig produkten torka in.',
 kit_upgrade='k_intlitet',kit_heading='Komplett interiörstart',
 accessories=['scrubpad','detailbrush','mikrofiberduk'],accessory_reasons=['Arbetar loss smuts ur textil och strukturerad plast.','Når in i ventiler, knappar och skarvar.','Torka av efter rengöringen.'],
 specs=['Typ | Allrengöring (APC)','Används på | Plast, vinyl, textil, gummi, motorrum (tvättbara ytor)','Applicering | Spray','Spädning | Efter smutsgrad enligt produktetiketten'],
 faq=['Kan Core APC användas både invändigt och utvändigt? | Ja, på plast, vinyl, textil och gummi – i och utanpå bilen.','Hur späder jag Core APC? | Efter smutsgrad och yta enligt produktetiketten – svagare för underhåll, starkare för kraftig smuts.','Kan jag använda Core APC på textil och mattor? | Ja. Arbeta in den med en Scrub Pad eller detaljborste och torka av med en ren duk.','Kan Core APC användas i motorrummet? | På tvättbara ytor. Undvik känsliga elektriska komponenter och följ produktetiketten.','Vad gör jag om produkten börjar torka? | Spola eller torka bort den direkt. Undvik direkt solljus och varma ytor.'])

C['foamcannon']=dict(preset='verktyg',type_label='Foam cannon / skumkanon',
 value_line='Ger ett tjockt skumlager med din högtryckstvätt – för en säkrare förtvätt.',
 benefits=['Justerbar dosering och spraybild','Tjockt, jämnt skum över hela bilen','Gjord för Foamtastic'],
 key_facts=['Används med | Högtryckstvätt','Justerbart | Dosering och spraybild','Anslutning | Kontrollera anslutningen mot din högtryckstvätt före köp'],
 problems=['Förtvätt | Skumma bilen innan handtvätten.','Snow foam | Ger det tjocka skummet som gör förtvätten effektiv.'],
 why=['Ett tjockt och vidhäftande skumlager ger smutsen tid att lösas upp innan handtvätten börjar.','Mer smuts kan spolas bort innan tvättsvampen rör lacken.'],
 kit_upgrade='k_foamwash',kit_heading='Skumtvätta direkt',
 accessories=['foamtastic'],accessory_reasons=['Snow foam som är gjord för att användas i Foam Cannon.'],
 specs=['Typ | Skumkanon för högtryckstvätt','Justerbart | Dosering och spraybild'],
 faq=['Vilken högtryckstvätt fungerar Foam Cannon med? | Den monteras på en högtryckstvätt, men anslutningen varierar mellan modeller. Kontrollera anslutningen mot din högtryckstvätt innan köp.','Vilket skum ska jag använda? | Vi rekommenderar Foamtastic för ett tjockt, effektivt skum.'])

C['tryckspruta']=dict(preset='verktyg',type_label='Kemikalieresistent tryckspruta',
 value_line='Snabb och jämn applicering av förtvätt och rengöring.',
 benefits=['2 liter – färre påfyllningar','Utbytbara munstycken för olika produkter','Kemikalieresistent konstruktion'],
 key_facts=['Volym | 2 liter','Munstycken | Rak stråle, skumstråle och munstycke för alkaliska medel','Används för | Avfettning, snow foam och allrengöring'],
 problems=['Förtvätt | Jämn applicering av alkalisk förtvätt.','Allrengöring | Spraya ut allrengöring över större ytor.'],
 accessories=['alkastrike'],accessory_reasons=['Alkalisk förtvätt att applicera med sprutan.'],
 specs=['Volym | 2 liter','Munstycken | 3 st: rak stråle, skumstråle, alkaliskt'],
 faq=['Vilka munstycken följer med? | Rak stråle, skumstråle och ett munstycke för alkaliska rengöringsmedel – så att du kan växla efter produkt.'])

C['tvatthink']=dict(preset='verktyg',type_label='Tvätthink med Grit Guard, 20 L',
 value_line='Håll smutsen på botten – inte i tvätthandsken.',
 benefits=['Grit Guard håller smuts och grus på botten','20 liter – rymlig för tvåhinksmetoden','Slitstark med ergonomiskt handtag'],
 key_facts=['Volym | 20 liter','Ingår | Grit Guard'],
 problems=['Tvåhinksmetoden | En hink med schampo, en med rent sköljvatten.','Handtvätt | Skölj tvätthandsken utan att smutsen följer med upp.'],
 why=['Utan Grit Guard kan smuts och grus på hinkens botten virvla upp och fastna i tvättsvampen igen.','Grit Guarden håller partiklarna kvar på botten.'],
 demo_heading='Se Grit Guarden i hinken',demo_media=['hink'],
 accessories=['pure','washpad'],accessory_reasons=['Schampot i tvätthinken.','Doppas och sköljs mot Grit Guarden.'],
 specs=['Volym | 20 liter','Ingår | Grit Guard'],
 faq=['Vad gör Grit Guarden? | Ett rutnät i botten av hinken som håller kvar smuts och grus när tvättsvampen sköljs, så att partiklarna inte följer med upp till lacken.'])

C['washpad']=dict(preset='tillbehor',type_label='Tvättpad i mikrofiber',
 value_line='Mjuk mikrofiber för en skonsam handtvätt.',
 benefits=['Kapslar in smuts istället för att dra den över lacken','Tar upp mycket schampo – jämnt glid','Ergonomisk form med säkert grepp'],
 problems=['Kontaktvätt | Handtvätt med schampo efter förtvätten.','Stora paneler | Tak, huv och dörrar.'],
 why=['En vanlig tvättsvamp kan dra smutspartiklar över lacken och orsaka tvättrepor.','Washpadens mjuka mikrofiber kapslar istället in smuts och partiklar.'],
 demo_heading='Se Washpad i användning',demo_media=['washpad'],
 accessories=['pure','tvatthink'],accessory_reasons=['Bilschampo för kontaktvätten.','Skölj washpaden mot Grit Guarden.'],
 specs=['Material | Mikrofiber'],
 faq=['Hur tvättar jag washpaden? | Skölj noggrant i rent vatten efter varje användning och låt lufttorka. Undvik sköljmedel – det minskar mikrofiberns förmåga att fånga smuts.'])

C['scrubpad']=dict(preset='tillbehor',type_label='Rengöringspad för interiör',
 value_line='Arbetar loss ingrodd smuts ur textil, plast och vinyl.',
 benefits=['Löser ingrodd smuts mekaniskt','Bekvämt grepp och god kontroll','För både detaljer och större ytor'],
 problems=['Textil och mattor | Ingrodd smuts i tygklädsel och mattor.','Strukturerad plast | Smuts i ytor med struktur.','Vinyl och gummi | Dörrsidor och lister.'],
 kit_upgrade='k_intlitet',kit_heading='Komplett interiörstart',
 accessories=['coreapc','mikrofiberduk'],accessory_reasons=['Allrengöring att arbeta in med paden.','Torka av efteråt.'],
 faq=['Vilka ytor är Scrub Pad avsedd för? | Bilens interiör – plast, vinyl, gummi och textil. Testa alltid på en liten, mindre synlig yta först.'])

C['dackapplikator']=dict(preset='tillbehor',type_label='Applikator för däckglans',
 value_line='Jämn och kontrollerad applicering av Pristine – utan kladd.',
 benefits=['Följer däckets konturer','Fördelar produkten jämnt','Kan rengöras och återanvändas'],
 problems=['Däck | Applicera Pristine runt hela däcket.','Utvändig plast | Även för utvändiga plastdetaljer.'],
 kit_upgrade='k_falgdack',kit_heading='Gör fälg och däck kompletta',
 accessories=['pristine'],accessory_reasons=['Däck- och plastförnyaren att applicera.'],
 faq=['Kan den användas till annat än däckglans? | Den är gjord för däckglans och plastförnyare, till exempel Pristine, och fungerar även för utvändiga plastdetaljer.'])

C['falgborste']=dict(preset='verktyg',type_label='Fälgborste i mikrofiber',
 value_line='Skonsam rengöring mellan ekrar och bakom fälgen.',
 benefits=['Mjukt huvud lyfter bort bromsdamm','Smal – når mellan ekrarna','36 cm lång – når djupt in'],
 key_facts=['Storlek | 36 × 4,5 cm','Huvud | Mjuk mikrofiber'],
 problems=['Mellan ekrarna | Där en svamp inte kommer åt.','Bakom fälgen | Den inre delen av djupa fälgar.'],
 demo_heading='Se fälgborsten i användning',demo_media=['falgborste'],
 kit_upgrade='k_falgstart',kit_heading='Gör fälgtvätten komplett',
 accessories=['revolt','deepreach'],accessory_reasons=['Löser bromsdammet – borsten arbetar in den.','Fastare borst för ingrodd smuts.'],
 specs=['Storlek | 36 × 4,5 cm','Material | Mikrofiber'],
 faq=['Kan borsten användas på lackade fälgar? | Ja, mikrofiberhuvudet är gjort för att vara skonsamt. Testa på en mindre synlig yta först om du är osäker.'])

C['deepreach']=dict(preset='verktyg',type_label='Fälgborste',
 value_line='Fastare borst som når långt in i fälgen.',
 benefits=['Tät borst för tuffare smuts','Når bakom ekrarna och långt in','Bekvämt grepp och bra kontroll'],
 problems=['Ingrodd bromsdamm | Tuffare smuts som kräver mer mekanisk kraft.','Fälgens insida | Långt in, där vanliga verktyg inte når.'],
 accessories=['revolt','falgborste'],accessory_reasons=['Löser bromsdammet innan du borstar.','Mjukare borste för känsliga ytor.'])

C['detailbrush']=dict(preset='verktyg',type_label='Detaljborstar, 2-pack',
 value_line='Mjuka borstar för ventiler, knappar och emblem.',
 benefits=['2 storlekar för små och större ytor','Mjuka, följsamma borststrån','För både interiör och exteriör'],
 problems=['Luftventiler | Damm och smuts i trånga springor.','Knappar och emblem | Detaljer där en duk inte kommer åt.','Grillar | Trånga ytor utvändigt.'],
 kit_upgrade='k_intmellan',kit_heading='Komplett interiörvård',
 accessories=['coreapc','mikrofiberduk'],accessory_reasons=['Allrengöring att arbeta in med borsten.','Torka av efteråt.'])

C['torkduk70']=dict(preset='duk',type_label='Torkduk för biltorkning',
 value_line='Torkar hela bilen snabbt och skonsamt.',
 benefits=['Suger upp mycket vatten på få drag','Räcker till hela bilen – även SUV','Mjuk yta som glider lätt över lacken'],
 key_facts=['Storlek | 70 × 90 cm','Material | Mikrofiber'],
 problems=['Efter tvätten | Torka hela bilen direkt efter sköljning.','Större bilar | SUV och transportbilar.'],
 accessories=['pure','torkduk40'],accessory_reasons=['Tvätta bilen innan torkningen.','Mindre duk för detaljer.'],
 faq=['Hur tvättar jag torkduken? | Följ tvättrådet på etiketten för bästa resultat och längsta livslängd.'])

C['torkduk50']=dict(preset='duk',type_label='Torkduk för biltorkning',
 value_line='Snabb, skonsam avtorkning – bra balans mellan räckvidd och kontroll.',
 benefits=['Suger upp mycket vatten','Lätt att hantera på både stora och små ytor','Mjuk mikrofiber som glider lätt'],
 key_facts=['Storlek | 50 × 80 cm','Material | Mikrofiber'],
 problems=['Efter tvätten | Torka bilen direkt efter sköljning.','Karossytor och detaljer | Både stora ytor och mindre detaljer.'],
 accessories=['pure','torkduk40'],accessory_reasons=['Tvätta bilen innan torkningen.','Mindre duk för detaljer.'],
 faq=['Hur tvättar jag torkduken? | Följ tvättrådet på etiketten för bästa resultat och längsta livslängd.'])

C['torkduk40']=dict(preset='duk',type_label='Torkduk för detaljarbete',
 value_line='Precision för lack, glas och detaljer.',
 benefits=['Tät 1400 GSM-mikrofiber','Kompakt – bra kontroll i detaljarbete','För lack, glas, dörrgångar och interiör'],
 key_facts=['Storlek | 40 × 40 cm','Densitet | 1400 GSM'],
 problems=['Detaljer | Dörrgångar, glas och mindre ytor.','Efter skydd | Torka av efter vax, lackskydd eller quick detailer.'],
 accessories=['glosscoat','torkduk70'],accessory_reasons=['Buffa av sprayförseglingen.','Större duk för hela bilen.'],
 faq=['Vad använder jag Torkduk 40×40 till? | Avtorkning av detaljer, lack, glas, dörrgångar och interiör – till exempel efter ett lackskydd eller en quick detailer.'])

C['mikrofiberduk']=dict(preset='duk',type_label='Mikrofiberduk',
 value_line='Mångsidig duk för lack, glas, interiör och buffning.',
 benefits=['Fångar upp smuts, damm och produktrester','Luddfri – inga fibrer kvar','Finns i 1-, 5- och 10-pack'],
 key_facts=['Förpackning | 1-, 5- eller 10-pack','Material | Mikrofiber'],
 problems=['Avtorkning | Lack, glas och plast.','Interiör | Instrumentbräda och detaljer.','Buffning | Vax, lackskydd och quick detailers.'],
 kit_upgrade='k_intlitet',kit_heading='Komplett interiörstart',
 accessories=['clarity','coreapc','glosscoat'],accessory_reasons=['Glasrengöring att torka av med duken.','Rengör interiören innan avtorkning.','Buffa av för jämn finish.'],
 faq=['Vilket pack ska jag välja? | 1-pack för att testa, 5- eller 10-pack om du vill ha separata dukar för lack, glas och interiör.'])

C['glasstowel']=dict(preset='duk',type_label='Glasduk',
 value_line='Slät mikrofiber för glas och speglar.',
 benefits=['Slät, följsam mikrofiber för glas','Hjälper till att minimera ludd och ränder','För in- och utvändigt glas'],
 problems=['Rutor | In- och utvändigt glas.','Speglar | Speglar och andra blanka ytor.'],
 kit_upgrade='k_intstort',kit_heading='Komplett interiörvård',
 accessories=['clarity'],accessory_reasons=['Glasrengöringen duken är gjord för.'])

LIST_TEXT={'benefits','best_for','accessory_reasons'}
MULTI={'problems','steps','dilution','specs','faq','key_facts','why'}
REF={'compare_with','kit_upgrade'}
out=[]
for k,d in C.items():
    owner=G+ID[k]
    for f,v in d.items():
        if f in LIST_TEXT: t='list.single_line_text_field'; val=json.dumps(v,ensure_ascii=False)
        elif f in MULTI: t='multi_line_text_field'; val='\n'.join(v)
        elif f in REF: t='product_reference'; val=G+ID[v]
        elif f=='accessories': t='list.product_reference'; val=json.dumps([G+ID[x] for x in v])
        elif f=='demo_media': t='list.file_reference'; val=json.dumps([V+VID[x] for x in v])
        else: t='single_line_text_field'; val=v
        out.append({'ownerId':owner,'namespace':'pdp','key':f,'type':t,'value':val})
# sanity
for k,d in C.items():
    assert len(d.get('benefits',[]))<=3, k
    assert len(d.get('accessories',[]))<=3, k
    assert len(d.get('accessories',[]))==len(d.get('accessory_reasons',[])), k
    for f in ('problems','steps','specs','faq','key_facts'):
        for line in d.get(f,[]): assert line.count('|')==1, (k,f,line)
print(len(C),'products',len(out),'metafields')
batches=[out[i:i+25] for i in range(0,len(out),25)]
for i,b in enumerate(batches): open(f'batch{i}.json','w').write(json.dumps({'m':b},ensure_ascii=False))
print(len(batches),'batches')
