from hind-mal_transliteration.sanscript.schemes.brahmic import BrahmicScheme


class DevanagariScheme(BrahmicScheme):
    def __init__(self):
        super(DevanagariScheme, self).__init__({
            'vowels': str.split("""अ आ इ ई उ ऊ ऋ ॠ ऌ ॡ ए ऐ ओ औ ऎ ऒ"""),
            'marks': str.split("""ा ि ी ु ू ृ ॄ ॢ ॣ े ै ो ौ ॆ ॊ"""),
            'virama': str.split('्'),
            'yogavaahas': str.split('ं ः ँ ᳵ ᳶ ़'),
            'consonants': str.split("""
                            क ख ग घ ङ
                            च छ ज झ ञ
                            ट ठ ड ढ ण
                            त थ द ध न
                            प फ ब भ म
                            य र ल व
                            श ष स ह
                            ळ क्ष ज्ञ
                            """)
                          + str.split("""ऩ ऱ ऴ क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़"""),
            'symbols': str.split("""
                       ॐ ऽ । ॥
                       ० १ २ ३ ४ ५ ६ ७ ८ ९
                       """)
        }, name=DEVANAGARI, synonym_map={'फ़': ["फ़"], "ड़": ["ड़"]})

    @classmethod
    def fix_lazy_visarga(cls, data_in):
        data_out = data_in
        import regex
        data_out = regex.sub(r'ः( *)([क-ङ])', r'ᳵ\1\2',   data_out)
        data_out = regex.sub(r'ः( *)([प-म])', r'ᳶ\1\2',   data_out)
        return data_out

    def fix_lazy_anusvaara(self, data_in, omit_sam=False, omit_yrl=False, ignore_padaanta=False):
        # Overriding because we don't want to turn जगइ to जगै
        if ignore_padaanta:
            return self.fix_lazy_anusvaara_except_padaantas(data_in=data_in, omit_sam=omit_sam, omit_yrl=omit_yrl)
        data_out = data_in
        import regex
        if omit_sam:
            prefix = "(?<!स)"
        else:
            prefix = ""
        data_out = regex.sub('%sं( *)([क-ङ])' % (prefix), r'ङ्\1\2',   data_out)
        data_out = regex.sub('%sं( *)([च-ञ])' % (prefix), r'ञ्\1\2',   data_out)
        data_out = regex.sub('%sं( *)([त-न])' % (prefix), r'न्\1\2',   data_out)
        data_out = regex.sub('%sं( *)([ट-ण])' % (prefix), r'ण्\1\2',   data_out)
        data_out = regex.sub('%sं( *)([प-म])' % (prefix), r'म्\1\2',   data_out)
        if not omit_yrl:
            data_out = regex.sub('%sं( *)([यलव])' % (prefix), r'\2्ँ\1\2',   data_out)
        return data_out







DEVANAGARI = 'devanagari'
SCHEMES = {
    DEVANAGARI: DevanagariScheme(),
}
