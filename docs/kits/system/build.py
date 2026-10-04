"""Kit PDP system – template builder (one data table per kit).

Hero structure is copied from templates/product.standard.json (same media
gallery, same product-details column, same buy buttons and delivery line as
the standard PDPs); only the purchase-column intro and the sections below the
hero are kit-specific. Run from repo root:  python3 docs/kits/system/build.py
"""
import json, pathlib, copy

ROOT = pathlib.Path(__file__).resolve().parents[3]
std_raw = (ROOT / "templates/product.standard.json").read_text()
HEADER = std_raw[: std_raw.index("{")]
std = json.loads(std_raw[std_raw.index("{"):])


def hero(intro):
    main = copy.deepcopy(std["sections"]["main"])
    details = main["blocks"]["product-details"]
    bb = details["blocks"]["buy_buttons"]
    bb["settings"]["add_to_cart_label"] = "Lägg paketet i varukorgen"
    details["blocks"] = {
        "intro": {"type": "nr-ks-intro", "settings": intro},
        "buy_buttons": bb,
        "delivery": copy.deepcopy(std["sections"]["main"]["blocks"]["product-details"]["blocks"]["delivery"]),
    }
    details["block_order"] = ["intro", "buy_buttons", "delivery"]
    main["settings"]["enable_sticky_add_to_cart"] = True
    return main


def faq_blocks(items):
    blocks, order = {}, []
    for i, (q, a) in enumerate(items, 1):
        key = f"q{i}"
        blocks[key] = {"type": "question", "settings": {"question": q, "answer": a}}
        order.append(key)
    return blocks, order


def stages(items):
    blocks, order = {}, []
    for i, (label, products, text) in enumerate(items, 1):
        key = f"s{i}"
        blocks[key] = {"type": "stage", "settings": {"label": label, "products": products, "text": text}}
        order.append(key)
    return blocks, order


def build(cfg):
    sections = {"main": hero(cfg["intro"])}
    order = ["main"]

    def add(key, value):
        sections[key] = value
        order.append(key)

    add("contents", {"type": "nr-ks-contents", "settings": cfg["contents"]})
    sb, so = stages(cfg["system"]["stages"])
    add("system", {"type": "nr-ks-system", "settings": cfg["system"]["settings"], "blocks": sb, "block_order": so})
    add("value", {"type": "nr-ks-value", "settings": cfg.get("value", {
        "heading": "Varför paketet?",
        "separate_line": "Du väljer och kombinerar allt själv.",
        "kit_line": "Färdig kombination, utvald för uppgiften."})})
    add("fit", {"type": "nr-ks-fit", "settings": cfg["fit"]})
    add("tiers", {"type": "nr-ks-tiers", "settings": cfg["tiers"]})
    if cfg.get("proof"):
        add("proof", {"type": "nr-ks-proof", "settings": cfg["proof"]})
    add("trust", {"type": "nr-pdp-trust", "settings": {
        "heading": "Vad kunder säger om NordicReflection",
        "max_reviews": 3,
        "source_note": "Omdömen om NordicReflection som butik, hämtade från Trustpilot. Inte betyg av det här kitet."}})
    fb, fo = faq_blocks(cfg["faq"])
    add("details", {"type": "nr-ks-details", "settings": {"heading": "Bra att veta"}, "blocks": fb, "block_order": fo})
    add("final", {"type": "nr-ks-final", "settings": cfg["final"]})
    return {"sections": sections, "order": order}


KITS = {
    "kit-exteriorstart": {
        "intro": {
            "eyebrow": "Exteriör · Start",
            "value_line": "För dig som vill få grunden rätt – från avfettning till handtvätt.",
            "point_1": "3 produkter, 3 tydliga uppgifter",
            "point_2": "Asfalt, trafikfilm och handtvätt",
            "point_3": "Paketpris istället för styckköp",
        },
        "contents": {
            "heading": "Det här får du",
            "lead": "Varje produkt har en tydlig uppgift.",
            "layout": "auto",
            "note_label": "Ingår inte:",
            "note": "tryckspruta för Alkastrike, tvätthinkar och washpad eller tvätthandske.",
        },
        "system": {
            "settings": {
                "heading": "Din exteriörrutin",
                "lead": "Tre produkter. Tre jobb. I den här ordningen.",
                "note_heading": "Varför två avfettningar?",
                "note": "De löser olika sorters smuts. DeepDegrease tar asfalt, tjära och oljebaserad smuts. Alkastrike tar trafikfilm, insekter och organisk smuts. DeepDegrease används på fläckarna, när bilen har dem.",
            },
            "stages": [
                ("Grovsmuts", ["deepdegrease-kallavfettning"], "Asfalt, tjära och oljerester. Används outspädd, direkt på fläckarna."),
                ("Trafikfilm", ["alkastrike-alkalisk-avfettning"], "Trafikfilm, insekter och vägsmuts, innan du rör lacken."),
                ("Handtvätt", ["pure-shampoo-ph-neutralt-bilschampo"], "Själva tvätten. Skonsamt mot vax och keramiska lackskydd."),
            ],
        },
        "fit": {
            "heading": "Passar dig som",
            "points": "Vill få grunden rätt vid varje tvätt\nHar både vägsmuts och asfaltsstänk på bilen\nTvättar för hand med tvätthink\nInte behöver hela exteriörsortimentet än",
            "prompt_heading": "Vill du ha hela rutinen?",
            "prompt_text": "Exteriör Komplett lägger till skumförtvätt, fälgar, glas, däck och lackskydd.",
            "alternative": "exterior-komplett-kit",
        },
        "tiers": {"heading": "Vilket exteriörkit passar dig?"},
        "proof": {
            "heading": "Produkterna i kitet",
            "lead": "Filmat av NordicReflection.",
            "products": ["alkastrike-alkalisk-avfettning", "pure-shampoo-ph-neutralt-bilschampo"],
        },
        "faq": [
            ("Vilken produkt använder jag till vad?", "<p>DeepDegrease till asfalt, tjära och oljerester. Alkastrike till trafikfilm, insekter och vägsmuts. Pure Shampoo till handtvätten i tvätthinken.</p>"),
            ("Behöver jag använda allt vid varje tvätt?", "<p>Inte nödvändigtvis. Använd produkterna efter vilken smuts bilen har. DeepDegrease används på fläckarna när bilen har asfalt, tjära eller oljerester.</p>"),
            ("Passar kitet en nybörjare?", "<p>Ja. Tre produkter med var sin tydlig uppgift, och varje produkt har en steg-för-steg-guide på sin produktsida.</p>"),
            ("Hur späder jag Alkastrike?", "<p>Alkastrike är koncentrerad och kan spädas upp till 1:25. Blanda efter smutsgrad och följ produktetiketten.</p>"),
            ("Behöver jag något mer?", "<p>För Alkastrike behövs en tryckspruta, och för handtvätten tvätthinkar och en washpad eller tvätthandske. De ingår inte i kitet.</p>"),
        ],
        "final": {"line": "Avfettning, förtvätt och handtvätt i ett paket.", "button_label": "Lägg paketet i varukorgen"},
    },
}


def main():
    for suffix, cfg in KITS.items():
        out = ROOT / f"templates/product.{suffix}.json"
        out.write_text(HEADER + json.dumps(build(cfg), ensure_ascii=False, indent=2) + "\n")
        print("wrote", out.name)


if __name__ == "__main__":
    main()
