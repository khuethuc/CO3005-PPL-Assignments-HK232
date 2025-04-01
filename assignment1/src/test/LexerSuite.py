import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test("Yl8xeH6gTR", "Yl8xeH6gTR,<EOF>", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("swb4", "swb4,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test("@ys9ohynq", "Error Token @", 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''## +,THV*A"$R%:zZ''', '''<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test('''"'";'6"''', '''\'";'6,<EOF>''', 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("$SplhrtH", "Error Token $", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"\\x'""''', '''Error Token "''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("8.405", "8.405,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("Z_", "Z_,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("Ecdrn", "Ecdrn,<EOF>", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("C3", "C3,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test('''"I'"}"''', '''I'"},<EOF>''', 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("DOVA#1lF", "DOVA,Error Token #", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("5y71psol8n", "5,y71psol8n,<EOF>", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''## MjWyh9$;YwILnPA)q79S''', '''<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test("87", "87,<EOF>", 119))

	def test_120(self):
		self.assertTrue(TestLexer.test("5e+19", "5e+19,<EOF>", 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''## Y@|vm''', '''<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''## 9$yO{{#FS<@J1XOQLEz''', '''<EOF>''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("56.010e+50", "56.010e+50,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("a\n", "a,\n,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("Zlwg", "Zlwg,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("YK0", "YK0,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("389.752E11", "389.752E11,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"$C
vv"''', '''Error Token "''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("4544ge", "4544,ge,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("y", "y,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## juN4avuf''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("x^B1ZVQp", "x,Error Token ^", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''## /3D~ER)E6''', '''<EOF>''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''"\\a4"''', '''Error Token "''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("40.983e43", "40.983e43,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''## b)T''', '''<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''\'"',<EOF>''', 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''## }.">ykC;q''', '''<EOF>''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''"'"0\\i4f"''', '''\',0,Error Token \\''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("27.962", "27.962,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## Zn3YK L[''', '''<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''"'"\\hW'""''', '''\',Error Token \\''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test("6E-06", "6E-06,<EOF>", 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("6E+00", "6E+00,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("25.045E73", "25.045E73,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("J3p#x9D", "J3p,Error Token #", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("33", "33,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''## SJ|fq''', '''<EOF>''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''## ]p<=Ns''', '''<EOF>''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''"\\cNG'"'"'""''', '''Error Token "''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("YURG$", "YURG,Error Token $", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("fMrlU3B", "fMrlU3B,<EOF>", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test('''"'"HJ/'""''', '''\'"HJ/'",<EOF>''', 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("5.252E+69", "5.252E+69,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("QvTPpvz7", "QvTPpvz7,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("952.841E+49", "952.841E+49,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("t", "t,<EOF>", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''"'"{\\u'"S"''', '''\',Error Token {''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test("230.624E50", "230.624E50,<EOF>", 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("U", "U,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("K4VKU", "K4VKU,<EOF>", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("sN7qq7", "sN7qq7,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"\\h'""''', '''\'"'"'"',Error Token \\''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''"'";'"'"'""''', '''\'";'"'"'",<EOF>''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("&ZgYKvz", "Error Token &", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("&Q", "Error Token &", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''## 4"=)Fau:9GP9_''', '''<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("9.917", "9.917,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''"'"D'"'""''', '''\'"D'"'",<EOF>''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''## a7a?|&S3~euw?''', '''<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'""''', '''\'"'"'"'",<EOF>''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test('''"u'"\\j/u"''', '''u',Error Token \\''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("aztJ2D", "aztJ2D,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''"<"''', '''<,<EOF>''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test('''## [:EDeC)T%j:''', '''<EOF>''', 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("48", "48,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("667.535", "667.535,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''\',<EOF>''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''"\\o|'"'"+"''', '''Error Token "''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("r", "r,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''## Ujlh''', '''<EOF>''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test("7.544", "7.544,<EOF>", 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("300.337", "300.337,<EOF>", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("94", "94,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"s"''', '''\'"'"'"'"s,<EOF>''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## gHK&u&9fiZF''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''"\\h'"'"'"'""''', '''Error Token "''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''"s'""''', '''s'",<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("Xf0kR", "Xf0kR,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''## `sDGn~t[Izzj3EQt9P9''', '''<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("710", "710,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("b", "b,<EOF>", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("20.329", "20.329,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''"\\l_"''', '''Error Token "''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("100.514E+03", "100.514E+03,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("Hi ##nwduewidnuwdnewiduewhd", "Hi,<EOF>", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("0.381e80", "0.381e80,<EOF>", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("4yvBGVvS", "4,yvBGVvS,<EOF>", 200))
    
