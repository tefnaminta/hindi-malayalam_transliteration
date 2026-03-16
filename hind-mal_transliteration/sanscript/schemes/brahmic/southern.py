from hind-mal_transliteration.sanscript.schemes.brahmic import BrahmicScheme



class MalayalamScheme(BrahmicScheme):
    def __init__(self):
        super(MalayalamScheme, self).__init__({
            'vowels': str.split("""അ ആ ഇ ഈ ഉ ഊ ഋ ൠ ഌ ൡ ഏ ഐ ഓ ഔ എ ഒ"""),
            'marks': str.split("""ാ ി ീ ു ൂ ൃ ൄ ൢ ൣ േ ൈ ോ ൌ െ ൊ"""),
            'virama': str.split('്'),
            'yogavaahas': str.split('ം ഃ ഁ'),
            'consonants': str.split("""
                            ക ഖ ഗ ഘ ങ
                            ച ഛ ജ ഝ ഞ
                            ട ഠ ഡ ഢ ണ
                            ത ഥ ദ ധ ന
                            പ ഫ ബ ഭ മ
                            യ ര ല വ
                            ശ ഷ സ ഹ
                            ള ക്ഷ ജ്ഞ
                            """) + str.split("""ഩ റ ഴ"""),
            'symbols': str.split("""
                       ഓം ഽ । ॥
                       ൦ ൧ ൨ ൩ ൪ ൫ ൬ ൭ ൮ ൯
                       """)
        }, name=MALAYALAM)



MALAYALAM = 'malayalam'
SCHEMES = {
    MALAYALAM: MalayalamScheme(),
    }
