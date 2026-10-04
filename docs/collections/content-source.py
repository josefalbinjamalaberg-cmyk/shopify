"""Collection-page data: filter values and product-card copy.

Source of truth for the nrc.* product metafields. Run to print metafieldsSet
batches (max 25 per call). Card copy is condensed from the verified PDP
content in docs/pdp/content-source.py – no new product claims.
"""
import json

G = 'gid://shopify/Product/'
MO = 'gid://shopify/Metaobject/'

# nr_filter_value metaobjects (handle -> id). label = customer copy, key = internal.
V = dict(
    traffic_film='1836072599886', tar='1836072632654', iron='1836072665422', foam='1836072698190',
    contact_wash='1836072730958', protection='1836072763726', glass='1836072796494', tyres_trim='1836072829262',
    int_surfaces='1836072862030', int_stubborn='1836072894798', int_details='1836072927566', int_wipe='1836072960334',
    kits='1836072993102',
    acc_prewash='1836073025870', acc_wheels='1836073058638', acc_drying='1836073091406',
    acc_interior='1836073124174', acc_detailing='1836073156942',
    kind_chem='1836073222478', kind_sprayer='1836073255246', kind_brush='1836073288014', kind_pad='1836073320782',
    kind_towel='1836073353550', kind_bucket='1836073386318', kind_applicator='1836073419086', kind_kit='1836073451854',
)

# id, card_name, card_line, exterior, interior, accessories, kind, card_label
P = [
    # --- Exteriör (chemicals) ---
    ('15963399553358', 'Revolt', 'Löser flygrost och bromsdamm på lack och fälgar.', ['iron'], [], [], 'kind_chem', None),
    ('15959788814670', 'Alkastrike', 'Löser trafikfilm, insekter och vägsmuts.', ['traffic_film'], [], [], 'kind_chem', None),
    ('15963418362190', 'DeepDegrease', 'Löser asfalt, tjära och oljebaserad smuts.', ['tar'], [], [], 'kind_chem', None),
    ('15963388379470', 'Foamtastic', 'Tjockt skum som löser smuts före handtvätten.', ['foam'], [], [], 'kind_chem', None),
    ('15963382055246', 'Pure Shampoo', 'Skonsamt bilschampo för handtvätten.', ['contact_wash'], [], [], 'kind_chem', None),
    ('15963394867534', 'GlossCoat', 'Glans och vattenavrinning efter tvätten.', ['protection'], [], [], 'kind_chem', None),
    ('15963424031054', 'Clarity', 'Klart glas utan ränder – in- och utvändigt.', ['glass'], ['glass'], [], 'kind_chem', None),
    ('15963415740750', 'Pristine', 'Djupare färg på däck och utvändig plast.', ['tyres_trim'], [], [], 'kind_chem', None),
    # --- Interiör ---
    ('15963421442382', 'Core APC', 'Rengör smuts, fett och fläckar – in- och utvändigt.', [], ['int_surfaces', 'int_stubborn'], [], 'kind_chem', None),
    ('15963468333390', 'Scrub Pad', 'Arbetar loss ingrodd smuts ur textil och plast.', [], ['int_stubborn'], ['acc_interior'], 'kind_pad', None),
    ('16015861219662', 'Detail Brush Duo', 'Mjuka borstar för ventiler, knappar och emblem.', [], ['int_details'], ['acc_interior', 'acc_detailing'], 'kind_brush', None),
    ('15963505688910', 'Mikrofiberduk', 'Mångsidig duk för lack, glas och interiör.', [], ['int_wipe'], ['acc_interior', 'acc_detailing'], 'kind_towel', None),
    ('16015909454158', 'Glass Towel', 'Slät mikrofiber för glas och speglar.', [], ['glass'], ['glass'], 'kind_towel', None),
    ('15996560376142', 'Litet Interiör Startkit', 'Core APC, Scrub Pad och mikrofiberdukar.', [], ['kits'], [], 'kind_kit', 'Grundrutin'),
    ('16015851487566', 'Mellan Interiör Startkit', 'Grundrutinen plus detaljborstar.', [], ['kits'], [], 'kind_kit', 'Grundrutin + detaljer'),
    ('16015857221966', 'Stort Interiör Startkit', 'Komplett – inklusive glasrengöring och glasduk.', [], ['kits'], [], 'kind_kit', 'Komplett inkl. glas'),
    # --- Tillbehör ---
    ('15963462795598', 'Foam Cannon', 'Tjockt skum med din högtryckstvätt.', [], [], ['acc_prewash'], 'kind_sprayer', None),
    ('15963460075854', 'Tryckspruta', 'Jämn applicering av förtvätt och rengöring.', [], [], ['acc_prewash'], 'kind_sprayer', None),
    ('15963482751310', 'Washpad', 'Mjuk mikrofiber för en skonsam handtvätt.', [], [], ['contact_wash'], 'kind_pad', None),
    ('15963454832974', 'Tvätthink', '20 liter med Grit Guard för tvåhinksmetoden.', [], [], ['contact_wash'], 'kind_bucket', None),
    ('15963479048526', 'Mikrofiber Fälgborste', 'Skonsam rengöring mellan ekrarna.', [], [], ['acc_wheels'], 'kind_brush', None),
    ('16015891235150', 'DeepReach', 'Fastare borst som når långt in i fälgen.', [], [], ['acc_wheels'], 'kind_brush', None),
    ('15963484750158', 'Däckapplikator', 'Jämn applicering av däckglans.', [], [], ['acc_wheels'], 'kind_applicator', None),
    ('15963493466446', 'Torkduk 70×90', 'Torkar hela bilen snabbt och skonsamt.', [], [], ['acc_drying'], 'kind_towel', None),
    ('15963500609870', 'Torkduk 50×80', 'Snabb avtorkning av kaross och detaljer.', [], [], ['acc_drying'], 'kind_towel', None),
    ('15963501134158', 'Torkduk 40×40', 'Kompakt duk för detaljer, glas och lack.', [], [], ['acc_drying', 'acc_detailing'], 'kind_towel', None),
]

# nrc.pairs_with (one "Passar med" line on accessory cards). Only pairs a kit or
# the product's own instructions already make.
PAIRS = {
    '15963462795598': '15963388379470',  # Foam Cannon -> Foamtastic (Foam Wash Kit)
    '15963460075854': '15959788814670',  # Tryckspruta -> Alkastrike (sprayed with a pressure sprayer)
    '15963482751310': '15963382055246',  # Washpad -> Pure Shampoo (two-bucket steps)
    '15963454832974': '15963382055246',  # Tvätthink -> Pure Shampoo (two-bucket steps)
    '15963479048526': '15963399553358',  # Mikrofiber Fälgborste -> Revolt (Fälg Startkit)
    '16015891235150': '15963399553358',  # DeepReach -> Revolt (Revolt steps: work in with a wheel brush)
    '15963484750158': '15963415740750',  # Däckapplikator -> Pristine (Fälg & Däck kit, Pristine steps)
    '16015909454158': '15963424031054',  # Glass Towel -> Clarity (Stort Interiör kit, Clarity steps)
    '15963468333390': '15963421442382',  # Scrub Pad -> Core APC (interior kits)
    '16015861219662': '15963421442382',  # Detail Brush Duo -> Core APC (Mellan interiör kit)
    '15963505688910': '15963394867534',  # Mikrofiberduk -> GlossCoat (GlossCoat steps: buff with microfibre)
}

# Manual collection order (customer relevance, not alphabetical)
ORDER = dict(
    exterior=['15963399553358', '15959788814670', '15963418362190', '15963388379470',
              '15963382055246', '15963394867534', '15963424031054', '15963415740750'],
    # individual products first, kits last (only prominent under "Färdiga paket")
    interior=['15963421442382', '15963468333390', '16015861219662', '15963505688910',
              '15963424031054', '16015909454158', '15996560376142', '16015851487566', '16015857221966'],
    accessories=['15963462795598', '15963460075854', '15963482751310', '15963454832974',
                 '15963479048526', '16015891235150', '15963484750158', '15963493466446',
                 '15963500609870', '15963501134158', '15963505688910', '16015909454158',
                 '15963468333390', '16015861219662'],
)


def mf(pid, key, typ, value):
    return dict(ownerId=G + pid, namespace='nrc', key=key, type=typ, value=value)


def build():
    out = []
    for pid, name, line, ext, inte, acc, kind, label in P:
        out.append(mf(pid, 'card_name', 'single_line_text_field', name))
        out.append(mf(pid, 'card_line', 'single_line_text_field', line))
        for key, vals in (('intent_exterior', ext), ('intent_interior', inte), ('intent_accessories', acc)):
            if vals:
                out.append(mf(pid, key, 'list.metaobject_reference', json.dumps([MO + V[v] for v in vals])))
        out.append(mf(pid, 'product_kind', 'metaobject_reference', MO + V[kind]))
        if label:
            out.append(mf(pid, 'card_label', 'single_line_text_field', label))
    return out


if __name__ == '__main__':
    rows = build()
    batches = [rows[i:i + 25] for i in range(0, len(rows), 25)]
    for i, b in enumerate(batches):
        with open(f'nrc-batch{i}.json', 'w') as f:
            json.dump({'m': b}, f, ensure_ascii=False)
    print(len(rows), 'metafields in', len(batches), 'batches')
