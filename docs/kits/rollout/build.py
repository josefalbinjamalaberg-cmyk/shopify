"""Kit page v3 rollout (2026-10-02): the seven remaining kits.

Generates, from one verified content table:
  templates/product.kit-<suffix>.json   (main section copied from Stort)
  docs/kits/rollout/metafields.json      (metafieldsSet inputs, kit-page-only keys)

All copy is taken from the kits' registered components (custom.kit_components)
and the component products' own pdp.* instructions – see docs/kits/rollout/README.md.
Run from the repo root:  python3 docs/kits/rollout/build.py
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
STORT = ROOT / "templates/product.kit-interiorstort.json"

HEADER = STORT.read_text().split("{", 1)[0]  # Shopify's auto-generated comment
base = json.loads(STORT.read_text()[len(HEADER):])

CORE_APC_NOTE = "För plast, vinyl, textil och gummi. Späds efter smutsgrad enligt etiketten."
SCRUB_NOTE = "Bearbetar ingrodd smuts på plast, vinyl, gummi och textil."
TOWEL_NOTE = "För avtorkning efter rengöringen."
BRUSH_NOTE = "Mjuka borstar för luftventiler, knappar och trånga detaljer."
REVOLT_NOTE = "Löser upp flygrost och bromsdamm så att det kan spolas bort. Blir lila när den arbetar."
WHEELBRUSH_NOTE = "Mjukt mikrofiberhuvud som når mellan ekrarna och in bakom fälgen. 36 × 4,5 cm."
PRISTINE_NOTE = "Ger däck och utvändig plast en djup, naturlig finish – inte blöt och blank."
APPLICATOR_NOTE = "Fördelar Pristine jämnt runt hela däcket. Kan rengöras och återanvändas."

FAQ_HOME = "Vad behöver jag ha hemma? | En tom sprayflaska och vatten för att späda Core APC efter smutsgrad enligt etiketten."
FAQ_APC_DILUTE = "Hur späder jag Core APC? | Efter smutsgrad och yta enligt produktetiketten – svagare för underhåll, starkare för kraftig smuts."
FAQ_APC_SURFACES = "Vilka ytor kan jag rengöra? | Core APC är avsedd för plast, vinyl, textil och gummi. Testa alltid på en liten, mindre synlig yta först och följ produktetiketten."
FAQ_REVOLT_TIME = "Hur länge ska Revolt verka? | Följ verkningstiden på produktetiketten. Låt aldrig produkten torka in på fälgen."
FAQ_REVOLT_BRUSH = "Behöver jag borsta fälgen? | Vid lätt smuts räcker det ofta att låta Revolt verka och sedan spola av. Vid fastbränd bromsdamm kan du arbeta in produkten med fälgborsten."
FAQ_REVOLT_PURPLE = "Varför blir Revolt lila? | Färgen visar att produkten reagerar med järnpartiklar och bromsdamm under verkningstiden – så ser du var den arbetar."
FAQ_REVOLT_RIMS = "Kan jag använda Revolt på alla fälgar? | Följ produktetiketten och testa först på en liten, mindre synlig yta om du är osäker på materialet."
FAQ_DEGREASERS = "Vad är skillnaden mellan DeepDegrease och Alkastrike? | DeepDegrease är en kallavfettning för asfalt, tjära och oljebaserad smuts. Alkastrike är en alkalisk förtvätt för trafikfilm, insekter och organisk smuts. Har bilen båda typerna av smuts kan båda behövas."
FAQ_DEEPDEGREASE_FIRE = "Är DeepDegrease brandfarlig? | Ja, den är klassificerad som brandfarlig (H226). Använd den aldrig nära öppen låga, gnistor eller värmekällor och arbeta i ett väl ventilerat utrymme."

STORT_AUDIENCE = "För hela kupén – ytor, detaljer och glas."
EXT_START_AUDIENCE = "För grunden – avfettning, förtvätt och handtvätt."
EXT_KOMPLETT_AUDIENCE = "För hela tvätten – även skum, fälgar, glas, däck och lackskydd."

KITS = {
    # ------------------------------------------------------------- Interiör
    "interiorlitet": {
        "handle": "interiorpaket-grundlaggande-interiorvard",
        "id": "gid://shopify/Product/15996560376142",
        "metafields": {
            "kit_display_title": "Litet interiörkit",
            "kit_audience": "För dig som vill grundrengöra kupén – plast, vinyl, textil och gummi.",
            "kit_descriptor": "3 produktgrupper, inklusive 5 mikrofiberdukar",
            "kit_points": [
                "Core APC 500 ml – koncentrat som späds efter behov",
                "Scrub Pad för ingrodd smuts på plast, vinyl, gummi och textil",
                "5 mikrofiberdukar för avtorkning",
            ],
            "kit_component_notes": [CORE_APC_NOTE, SCRUB_NOTE, TOWEL_NOTE],
            "kit_faq": "\n".join([
                FAQ_HOME, FAQ_APC_DILUTE, FAQ_APC_SURFACES,
                "Vad skiljer Litet från Mellan interiörkit? | Mellan innehåller även Detail Brush Duo – två mjuka borstar för luftventiler, knappar och trånga detaljer. Övrigt innehåll är detsamma.",
            ]),
        },
        "included": {
            "lead": "Allrengöring, skrubb och dukar – grunden för kupéns ytor.",
            "not_included_label": "Behöver du hemma:",
            "not_included": "en tom sprayflaska och vatten för att späda Core APC.",
        },
        "usage": {
            "video_product": "core-apc-allrengoring",
            "video_heading": "Lär känna Core APC",
            "note": "Arbeta inte på varma ytor eller i direkt solljus, och låt aldrig Core APC torka in.",
            "steps": [
                ("Späd Core APC", "Blanda Core APC och vatten i en tom sprayflaska, efter smutsgrad enligt etiketten.", ["core-apc-allrengoring"]),
                ("Spraya och bearbeta", "Spraya jämnt på ytan och arbeta in med Scrub Pad efter yta och smutsgrad.", ["scrub-pad-interior"]),
                ("Torka av", "Torka av med en ren mikrofiberduk.", ["mikrofiberduk"]),
            ],
        },
        "compare": {
            "alternative": "mellan-interior-startkit",
            "alt_audience": "För ytor och detaljer som ventiler och knappar.",
            "alternative_2": "stort-interior-startkit",
            "alt_2_audience": STORT_AUDIENCE,
            "current_audience": "För kupéns ytor – plast, vinyl, textil och gummi.",
        },
    },
    "interiormellan": {
        "handle": "mellan-interior-startkit",
        "id": "gid://shopify/Product/16015851487566",
        "metafields": {
            "kit_display_title": "Mellan interiörkit",
            "kit_audience": "För dig som vill rengöra både ytor och detaljer i kupén – som ventiler och knappar.",
            "kit_descriptor": "4 produktgrupper, inklusive 5 mikrofiberdukar och 2 detaljborstar",
            "kit_points": [
                "Core APC 500 ml – koncentrat som späds efter behov",
                "Scrub Pad och 2 detaljborstar för ytor och trånga detaljer",
                "5 mikrofiberdukar för avtorkning",
            ],
            "kit_component_notes": [CORE_APC_NOTE, SCRUB_NOTE, TOWEL_NOTE, BRUSH_NOTE],
            "kit_faq": "\n".join([
                FAQ_HOME, FAQ_APC_DILUTE, FAQ_APC_SURFACES,
                "Vad skiljer Mellan från Litet och Stort interiörkit? | Jämfört med Litet innehåller Mellan även Detail Brush Duo. Stort innehåller dessutom Clarity glasrengöring och Glass Towel.",
            ]),
        },
        "included": {
            "lead": "Varje del har en egen uppgift – från större ytor till trånga detaljer.",
            "not_included_label": "Behöver du hemma:",
            "not_included": "en tom sprayflaska och vatten för att späda Core APC.",
        },
        "usage": {
            "video_product": "core-apc-allrengoring",
            "video_heading": "Lär känna Core APC",
            "note": "Arbeta inte på varma ytor eller i direkt solljus, och låt aldrig Core APC torka in.",
            "steps": [
                ("Rengör ytorna", "Späd Core APC efter smutsgrad enligt etiketten och spraya på ytan. Arbeta in med Scrub Pad och torka av med en ren mikrofiberduk.", ["core-apc-allrengoring", "scrub-pad-interior", "mikrofiberduk"]),
                ("Kom åt detaljerna", "Använd Detail Brush Duo i luftventiler, runt knappar och i trånga detaljer. Torka av med mikrofiberduk.", ["detail-brush"]),
            ],
        },
        "compare": {
            "alternative": "interiorpaket-grundlaggande-interiorvard",
            "alt_audience": "För kupéns ytor – utan detaljborstarna.",
            "alternative_2": "stort-interior-startkit",
            "alt_2_audience": STORT_AUDIENCE,
            "current_audience": "För ytor och detaljer som ventiler och knappar.",
        },
    },
    # ------------------------------------------------------------- Fälg & däck
    "falgstart": {
        "handle": "falg-startkit",
        "id": "gid://shopify/Product/16016364077390",
        # Active automatic discount "revolt + mikrofiber": buy Revolt → 30 % off
        # Mikrofiber Fälgborste (189 kr × 0.3 = 56,70 kr) when bought one by one.
        "separate_adjust": "56,70",
        "metafields": {
            "kit_display_title": "Fälg startkit",
            "kit_audience": "För dig som vill få bort bromsdamm och flygrost från fälgarna.",
            "kit_descriptor": "2 produkter: Revolt 500 ml och Mikrofiber Fälgborste",
            "kit_points": [
                "Revolt 500 ml löser upp flygrost och bromsdamm",
                "Blir lila när den arbetar – du ser reaktionen",
                "Fälgborste, 36 cm – når mellan ekrarna",
            ],
            "kit_component_notes": [REVOLT_NOTE, WHEELBRUSH_NOTE],
            "kit_faq": "\n".join([
                FAQ_REVOLT_TIME, FAQ_REVOLT_BRUSH, FAQ_REVOLT_PURPLE, FAQ_REVOLT_RIMS,
                "Kan borsten användas på lackade fälgar? | Ja, mikrofiberhuvudet är gjort för att vara skonsamt. Testa på en mindre synlig yta först om du är osäker.",
                "Vad skiljer Fälg startkit från Fälg & däck komplett kit? | Fälg & däck innehåller även Pristine däck- och plastförnyare och en däckapplikator.",
            ]),
        },
        "included": {
            "lead": "Två delar – en som löser smutsen och en som når in i fälgen.",
            "not_included_label": "Behöver du hemma:",
            "not_included": "vatten att spola av fälgarna med.",
        },
        "usage": {
            "video_product": "revolt-flygrostborttagare",
            "video_heading": "Lär känna Revolt",
            "note": "Använd inte Revolt på varma fälgar eller i direkt solljus, och låt aldrig produkten torka in.",
            "steps": [
                ("Spraya på en sval fälg", "Arbeta i skugga och spraya Revolt jämnt över hela fälgen.", ["revolt-flygrostborttagare"]),
                ("Låt verka", "Följ verkningstiden på etiketten. Revolt blir lila när den reagerar med järnpartiklar och bromsdamm.", []),
                ("Borsta vid behov och skölj", "Vid fastbränd bromsdamm: arbeta in Revolt med fälgborsten. Spola sedan av med rikligt med vatten.", ["mikrofiber-falgborste"]),
            ],
        },
        "compare": {
            "alternative": "falg-och-dack-komplett-kit",
            "alt_audience": "För både fälgar och däck – med däckfinish.",
            "current_audience": "För rena fälgar.",
        },
    },
    "falgdack": {
        "handle": "falg-och-dack-komplett-kit",
        "id": "gid://shopify/Product/16016378134862",
        "separate_adjust": "56,70",  # same automatic discount as above
        "metafields": {
            "kit_display_title": "Fälg & däck komplett kit",
            "kit_audience": "För dig som vill göra hela hjulet – rena fälgar och däck med finish.",
            "kit_descriptor": "4 produkter: Revolt, fälgborste, Pristine och däckapplikator",
            "kit_points": [
                "Revolt 500 ml för flygrost och bromsdamm på fälgen",
                "Fälgborste som når mellan ekrarna",
                "Pristine 500 ml och applikator för däckens finish",
            ],
            "kit_component_notes": [REVOLT_NOTE, WHEELBRUSH_NOTE, PRISTINE_NOTE, APPLICATOR_NOTE],
            "kit_faq": "\n".join([
                FAQ_REVOLT_TIME, FAQ_REVOLT_BRUSH, FAQ_REVOLT_RIMS,
                "Hur applicerar jag Pristine på däck? | Med däckapplikatorn, jämnt runt hela däcket. Torka bort överskott med en ren mikrofiberduk och låt torka innan bilen körs.",
                "Blir däcken blöta och blanka? | Nej, målet är en naturlig, jämn finish. Applicera tunna lager och torka bort överskott.",
                "Vad skiljer Fälg & däck från Fälg startkit? | Fälg & däck innehåller även Pristine däck- och plastförnyare och en däckapplikator. Revolt och fälgborsten ingår i båda.",
            ]),
        },
        "included": {
            "lead": "Först fälgen, sedan däcket – varje del har sin uppgift.",
            "not_included_label": "Behöver du hemma:",
            "not_included": "vatten att spola av fälgarna med och en ren duk för att torka bort överskott av Pristine.",
        },
        "usage": {
            "video_product": "pristine-dack-plastfornyare",
            "video_heading": "Lär känna Pristine",
            "note": "Arbeta inte på varma ytor eller i direkt solljus och låt aldrig Revolt torka in. Undvik bromsskivorna med Pristine och låt den torka innan körning eller regn.",
            "steps": [
                ("Lös smutsen på fälgen", "Spraya Revolt jämnt på en sval fälg i skugga och låt verka enligt etiketten.", ["revolt-flygrostborttagare"]),
                ("Borsta och skölj", "Arbeta in Revolt med fälgborsten vid fastbränd bromsdamm och spola av med rikligt med vatten.", ["mikrofiber-falgborste"]),
                ("Ge däcken finish", "När däcket är rent och torrt: lägg lite Pristine på applikatorn, fördela jämnt och torka bort överskott.", ["pristine-dack-plastfornyare", "dackapplikator"]),
            ],
        },
        "compare": {
            "alternative": "falg-startkit",
            "alt_audience": "För rena fälgar – utan däckfinish.",
            "current_audience": "För både fälgar och däck – med däckfinish.",
        },
    },
    # ------------------------------------------------------------- Exteriör / Foam
    "exteriorstart": {
        "handle": "litet-exterior-startkit",
        "id": "gid://shopify/Product/16018450940238",
        "metafields": {
            "kit_display_title": "Exteriör startkit",
            "kit_descriptor": "3 produkter: DeepDegrease 1000 ml, Alkastrike 500 ml och Pure Shampoo 500 ml",
            "kit_points": [
                "DeepDegrease 1000 ml för asfalt, tjära och oljerester",
                "Alkastrike 500 ml för trafikfilm, insekter och vägsmuts",
                "Pure Shampoo 500 ml – skonsamt mot vax och keramiska lackskydd",
            ],
            "kit_component_notes": [
                "För asfalt, tjära och oljebaserad smuts. Används outspädd.",
                "För trafikfilm, insekter och vägsmuts. Koncentrat som späds efter smutsgrad.",
                "För själva handtvätten – skonsamt mot vax och keramiska lackskydd.",
            ],
            "kit_faq": "\n".join([
                FAQ_DEGREASERS,
                "Hur späder jag Alkastrike? | Alkastrike är koncentrerad och kan spädas upp till 1:25. Blanda efter smutsgrad och följ produktetiketten.",
                FAQ_DEEPDEGREASE_FIRE,
                "Vad ingår inte? | Verktyg ingår inte: tryckspruta för Alkastrike, tvätthinkar och washpad eller tvätthandske för handtvätten, och duk för att torka bort DeepDegrease.",
                "Vad får jag mer i Exteriör komplett kit? | Komplett innehåller även Foamtastic, Revolt, Clarity, Pristine och GlossCoat – för skumförtvätt, fälgar, glas, däck och lackskydd.",
            ]),
        },
        "included": {
            "lead": "Tre produkter – tre tydliga uppgifter.",
            "not_included_label": "Ingår inte:",
            "not_included": "tryckspruta för Alkastrike, tvätthinkar och washpad eller tvätthandske, och duk för DeepDegrease.",
        },
        "usage": {
            "video_product": "alkastrike-alkalisk-avfettning",
            "video_heading": "Lär känna Alkastrike",
            "note": "Arbeta inte på varma ytor eller i direkt solljus, och låt aldrig produkterna torka in. DeepDegrease är brandfarlig – använd den aldrig nära öppen låga, gnistor eller värmekällor.",
            "steps": [
                ("Asfalt och tjära", "Applicera DeepDegrease outspädd direkt på fläckarna, låt verka enligt etiketten och torka bort med en duk. Arbeta väl ventilerat.", ["deepdegrease-kallavfettning"]),
                ("Förtvätt", "Späd Alkastrike efter smutsgrad enligt etiketten, spraya jämnt med en tryckspruta, låt verka och spola av med högtryck.", ["alkastrike-alkalisk-avfettning"]),
                ("Handtvätt", "Späd Pure Shampoo i tvätthinken enligt etiketten och tvätta panel för panel med två hinkar. Spola av hela bilen.", ["pure-shampoo-ph-neutralt-bilschampo"]),
            ],
        },
        "compare": {
            "alternative": "exterior-komplett-kit",
            "alt_audience": EXT_KOMPLETT_AUDIENCE,
            "current_audience": EXT_START_AUDIENCE,
        },
    },
    "foamwash": {
        "handle": "foam-wash-kit",
        "id": "gid://shopify/Product/16016437608782",
        "summary_note": "Kräver högtryckstvätt, som inte ingår. Anslutningen varierar mellan modeller och vi säljer i dag inga adaptrar – kontrollera din högtryckstvätt före köp.",
        "metafields": {
            "kit_display_title": "Foam Wash Kit",
            "kit_audience": "För dig med högtryckstvätt som vill skumtvätta bilen före handtvätten.",
            "kit_descriptor": "2 produkter: Foamtastic 1000 ml och Foam Cannon",
            "kit_points": [
                "Foamtastic 1000 ml – tjockt, vidhäftande skum",
                "Foam Cannon med justerbar dosering och spraybild",
                "Skummet löser upp smuts innan handtvätten",
            ],
            "kit_component_notes": [
                "Ger det tjocka, vidhäftande skummet för förtvätten.",
                "Sprider skummet med din högtryckstvätt – justerbar dosering och spraybild.",
            ],
            "kit_faq": "\n".join([
                "Behöver jag en högtryckstvätt? | Ja. Foam Cannon monteras på en högtryckstvätt, som inte ingår i paketet.",
                "Passar Foam Cannon min högtryckstvätt? | Anslutningen varierar mellan märken och modeller, och vi säljer i dag inga adaptrar. Kontrollera anslutningen på din högtryckstvätt innan köp, eller kontakta oss om du är osäker.",
                "Hur blandar jag Foamtastic? | Följ doseringen på produktetiketten och din Foam Cannons inställning.",
                "Är Foamtastic ett schampo? | Nej. Foamtastic är en förtvätt som löser smuts innan handtvätten. Efter avspolning fortsätter tvätten med ett bilschampo, till exempel Pure Shampoo, som inte ingår.",
                "Vad ingår inte? | Högtryckstvätt och eventuell adapter ingår inte.",
            ]),
        },
        "included": {
            "lead": "Två delar som hör ihop – skummet och kanonen som sprider det.",
            "not_included_label": "Ingår inte:",
            "not_included": "högtryckstvätt och eventuell adapter. Handtvätten efteråt görs med ett bilschampo, som inte ingår.",
        },
        "usage": {
            "video_product": "foamtastic-hogkoncentrerat-snow-foam",
            "video_heading": "Lär känna Foamtastic",
            "note": "Applicera inte i direkt solljus eller på varma ytor. Skölj av innan skummet torkar.",
            "steps": [
                ("Fyll Foam Cannon", "Dosera Foamtastic enligt etiketten och kanonens inställning, och montera Foam Cannon på högtryckstvätten.", ["foamtastic-hogkoncentrerat-snow-foam", "foam-lance-skumlans"]),
                ("Skumma uppifrån och ner", "Täck hela bilen med ett jämnt, tjockt lager och ge skummet tid att lösa upp smutsen.", []),
                ("Skölj innan det torkar", "Spola av med högtryck och fortsätt med handtvätten.", []),
            ],
        },
        "compare": None,  # separate use case – no level comparison
    },
    "exteriorkomplett": {
        "handle": "exterior-komplett-kit",
        "id": "gid://shopify/Product/16018547671374",
        "summary_note": "Paketet innehåller endast kemikalier. Verktyg som Foam Cannon, tryckspruta, tvätthinkar, washpad, fälgborste, applikator och dukar köps separat.",
        "metafields": {
            "kit_display_title": "Exteriör komplett kit",
            "kit_audience": "För dig som vill ha kemikalierna för hela utvändiga tvätten – från förtvätt till finish och lackskydd.",
            "kit_descriptor": "8 produkter – från avfettning och förtvätt till fälgar, glas, däck och lackskydd",
            "kit_points": [
                "Förtvätt: DeepDegrease, Alkastrike och Foamtastic",
                "Handtvätt och fälgar: Pure Shampoo och Revolt",
                "Finish: Clarity, Pristine och GlossCoat",
            ],
            "kit_component_notes": [
                "För asfalt, tjära och oljebaserad smuts. Används outspädd.",
                "För trafikfilm, insekter och vägsmuts. Koncentrat som späds efter smutsgrad.",
                "För skumförtvätten – används med Foam Cannon och högtryckstvätt, som inte ingår.",
                "För handtvätten – skonsamt mot vax och keramiska lackskydd.",
                "Löser upp flygrost och bromsdamm på fälgarna. Blir lila när den arbetar.",
                "För in- och utvändigt glas. Invändigt sprayar du på duken, inte på rutan.",
                "Ger däck och utvändig plast en djup, naturlig finish.",
                "För glans och vattenavrinning – sista steget efter tvätten.",
            ],
            "kit_faq": "\n".join([
                "Ingår verktyg? | Nej. Paketet innehåller endast kemikalier. Foam Cannon och högtryckstvätt för Foamtastic, tryckspruta för Alkastrike, tvätthinkar, washpad, fälgborste, däckapplikator och mikrofiberdukar köps separat.",
                FAQ_DEGREASERS,
                "Behöver jag en Foam Cannon? | Ja, för Foamtastic. Foam Cannon monteras på en högtryckstvätt – ingen av dem ingår i paketet.",
                FAQ_DEEPDEGREASE_FIRE,
                "Vad skiljer Komplett från Exteriör startkit? | Komplett innehåller även Foamtastic, Revolt, Clarity, Pristine och GlossCoat. DeepDegrease, Alkastrike och Pure Shampoo ingår i båda.",
            ]),
        },
        "included": {
            "lead": "Åtta kemprodukter för hela utvändiga tvätten – varje produkt har en egen uppgift.",
            "not_included_label": "Ingår inte:",
            "not_included": "verktyg – t.ex. Foam Cannon och högtryckstvätt för Foamtastic, tryckspruta för Alkastrike, tvätthinkar och washpad, fälgborste, däckapplikator och mikrofiberdukar.",
        },
        "usage": {
            "video_product": "glosscoat-hydrofobisk-sprayforsegling",
            "video_heading": "Lär känna GlossCoat",
            "note": "Arbeta inte på varma ytor eller i direkt solljus, och låt aldrig produkterna torka in. DeepDegrease är brandfarlig – använd den aldrig nära öppen låga, gnistor eller värmekällor.",
            "steps": [
                ("Fälgar", "Spraya Revolt på svala fälgar, låt verka enligt etiketten och spola av noggrant.", ["revolt-flygrostborttagare"]),
                ("Förtvätt", "Torka bort asfalt och tjära med DeepDegrease. Spraya på Alkastrike och skumma sedan med Foamtastic – låt verka och spola av innan det torkar.", ["deepdegrease-kallavfettning", "alkastrike-alkalisk-avfettning", "foamtastic-hogkoncentrerat-snow-foam"]),
                ("Handtvätt", "Späd Pure Shampoo i tvätthinken och tvätta panel för panel med två hinkar. Spola av och torka bilen.", ["pure-shampoo-ph-neutralt-bilschampo"]),
                ("Finish", "På en ren, torr och sval yta: GlossCoat på lacken, Pristine på däck och plast och Clarity på glaset.", ["glosscoat-hydrofobisk-sprayforsegling", "pristine-dack-plastfornyare", "clarity-glasrengoring"]),
            ],
        },
        "compare": {
            "alternative": "litet-exterior-startkit",
            "alt_audience": EXT_START_AUDIENCE,
            "current_audience": EXT_KOMPLETT_AUDIENCE,
        },
    },
}


def template(cfg):
    t = json.loads(json.dumps(base))
    summary = t["sections"]["main"]["blocks"]["product-details"]["blocks"]["summary"]
    summary["settings"] = {}
    if cfg.get("separate_adjust"):
        summary["settings"]["separate_adjust"] = cfg["separate_adjust"]
    if cfg.get("summary_note"):
        summary["settings"]["note"] = cfg["summary_note"]

    inc = t["sections"]["included"]["settings"]
    inc.update(cfg["included"])

    u = cfg["usage"]
    usage = t["sections"]["usage"]
    usage["settings"] = {
        "heading": "Så använder du kitet",
        "lead": "",
        "video_product": u["video_product"],
        "video_heading": u["video_heading"],
        "video_caption": "",
        "note": u["note"],
    }
    usage["blocks"] = {}
    usage["block_order"] = []
    for i, (title, text, products) in enumerate(u["steps"], 1):
        key = f"s{i}"
        settings = {"title": title, "text": text}
        if products:
            settings["products"] = products
        usage["blocks"][key] = {"type": "step", "settings": settings}
        usage["block_order"].append(key)

    if cfg["compare"]:
        c = {"heading": "Välj rätt nivå", **cfg["compare"]}
        t["sections"]["compare"]["settings"] = c
    else:
        del t["sections"]["compare"]
        t["order"].remove("compare")
    return t


def main():
    metafields = []
    for suffix, cfg in KITS.items():
        out = ROOT / f"templates/product.kit-{suffix}.json"
        out.write_text(HEADER + json.dumps(template(cfg), ensure_ascii=False, indent=2) + "\n")
        for key, value in cfg["metafields"].items():
            if isinstance(value, list):
                mtype, mvalue = "list.single_line_text_field", json.dumps(value, ensure_ascii=False)
            elif key == "kit_faq":
                mtype, mvalue = "multi_line_text_field", value
            else:
                mtype, mvalue = "single_line_text_field", value
            metafields.append({"ownerId": cfg["id"], "namespace": "custom", "key": key, "type": mtype, "value": mvalue})
    (ROOT / "docs/kits/rollout/metafields.json").write_text(json.dumps(metafields, ensure_ascii=False, indent=1) + "\n")
    print(len(metafields), "metafields;", len(KITS), "templates")


if __name__ == "__main__":
    main()
