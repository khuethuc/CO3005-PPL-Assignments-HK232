import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
func gPT (var ob2, dynamic nD)
	return
## g~"6_#YjcUiSd
bool MU ## >MasKDQ?}vqS?mPfn
var tvbw <- KERX([Ej()])[OQz, "'"H'"I" <= "L'"", "'"'"'"'""] ## q?fNA>Pv?L-QM3#pC
number C3CT <- Nvz ## ZHJGu
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
number EbfT[79.680E+21] <- "r'"" ## wF32:Z5@Q
string E3c2 ## -V
## Ov(F:Yuobj
string ks[224E-26,7] <- true ## dYv><R
var DU <- 39E51
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
func MzHW (var Qe, var mY_N[779,51.948])	begin
	end
func HZ0 (number WW)
	return "'"'"'""
func m7pm (var POKH)	return wl

func pPpL ()	return
number P1X8 <- "'"'"'"" ## _@u
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
## b9.%)Kxzg>851mB"zW&
func XBHP (dynamic oe6W, number kye)	return WRjj

dynamic zQnM ## RRRXZyz
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
func Tc6K (bool qaS)
	return xaZL
dynamic GWo
func Fj (number Dh[405.624,2E+09,6e81], var ICe[74.577,58.622])	return "'"'"7'"'""

## Y-uba%cb
dynamic Uw[6e87,4,384.782]
'''
		expect = '''Error on line 5 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
func Esx (number oC__[5e27,0E+54], var um[9], number AcUA)
	begin
		string iCJT
		## t{;ov@=5xO&Wi
		return l5
	end

## }DF$*;
var ho_
bool pp[95.330E69,12E+45,66] ## N0UdE
'''
		expect = '''Error on line 2 col 35: var'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
func Bq (var Pc8)
	return

## F[m:$y." ,zJ
func PjF ()	return "'"'"'""

bool g9 <- true
## a"?Zb
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
func EnIM (string Qx_, bool uf)
	return S5X

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
func DN (dynamic Xp[94.426])	return 86
bool MH
dynamic rAmb
## ?DU%u*
func vtX (var ZZl[488.276E+09], string BvZo[8E66,727])
	return
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
var E6e <- true ## /,nL;2zY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
func kfV (dynamic YNF[193,635,7])	return
## rws;<HwRd
## A]vde
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
func J2tB (dynamic hrYc, dynamic QO, dynamic i5z[99e94,35e+60])
	return "c"

var pW ## JGW?iH=#K]P7b*o2_[c
var lPj[396E29,277.737]
dynamic RSsg[55.657E-04,398.222,50.516e+29] <- 30
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
## <&,nU
string AY[69.122,4] ## /q3D<e>~JU]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
func gz (var qUQ, string Azup[6.239,54,58e+88])
	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
func OqcK ()	return true
## 89QBK
dynamic DM3[44.761] <- true ## Z/-d3BJq!IN@I<nR
bool MZ[689.871e69,9.581] <- "'"E'"(x"
## &4
'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
## BQPOHZPKO<{oR
func hgkK ()	begin
		I3u[false, b37] <- false
		return
		begin
			break
		end
	end
func QMO (var Qyw, dynamic KG, dynamic xG4h[742.896E+59])	return false
dynamic yl
'''
		expect = '''Error on line 10 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
func R9G (number IY[881], bool Waw, string LXkn)
	begin
		continue
		break
		Ffi <- "'"'""
	end

func SvKd (bool fh[221e+09], bool Aw[0.237E+35,1,6.531e11])	return

## xEn615w
## Vh)pmvne[^=Ae0s*}gIA
func jxrC ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
func Pie ()	return "S|'"'""
func AFV ()	return
var m2sG[7.459,38,1.272E+34] <- 881.060e-86 ## &C8CD4
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
func nrd (var OR[851,0.326,6], number fx, string HGNY)	return
## BcLwf
func tPG ()	return

func UhZ (number dlF[5.994e-97,0e14], string Bi5X[2e89,389.360,8.382e-68], number MNO)
	begin
		## n>.j
	end
dynamic tMJh <- false
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
dynamic RZ4
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func nD (var Hto, bool S2ns, dynamic BiZG[468.976])	return

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
bool fH[3.556,4,41] ## MLSc*^&"i
number lg_L ## !B
func iv (number Yjvl[3.589e12,4.876e80,333.395], dynamic pQyQ[0])
	return

'''
		expect = '''Error on line 4 col 49: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
func WSkF (dynamic QZcn[6.329])	return

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
dynamic kXA[66,8.079e81,82E95]
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
func kpT (dynamic Kw[376.065E-10,2E78], string N5IH[98.937E81,158.945])	begin
		return 20E+12
		## )}fg<G9OL5_X:8!X+=l5
	end

##  
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
func akT (bool A8[67,86.502,18.827])	begin
		Kh7()["'",", W8e, 266.067E-49] <- 315.724
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
dynamic x4g ## /arUf8}r?05/
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
## *gMn#Q^1ia/A0~
func ZK1 ()
	begin
		if (CNCz)
		begin
			continue
			## ISP0MO2
		end
		elif (false)
		continue
		elif (true)
		for vHx until "M2'"" by false
			if (65e+73) Rs(XY, "'"Y", true)
			elif (4.279)
			begin
				## *J]mWX%_`&
			end
			elif (75.409E+05)
			if ("?'":N")
			NZT9(clkR)
			else break
			elif (96.362) return
		elif ("'"'"F'"'"")
		continue
		elif (726e67) string bC[916.271,3.997] <- true ## )ZWz LO[oQebhxi
		elif (false)
		continue
		else begin
			break
			if (BY)
			for SBu until 173.972 by 363
				Qyjy <- "'"~.%b"
			lBRH <- "'""
		end
		## 0VJl_M[g
		continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
func AdV (bool Im[624.598E08,59], number HZ[6e+11,9.353,89e26])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## a3p]80Dg [F.<R):q x
bool eu89[68.806,8.884e13,3.060] ## Bi6v:W3
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
func dyC ()	return

bool xYwO[6E-57,916.836,3.528E-10] ## {[]Crohy
func HvkO (dynamic oZh, dynamic PF6H, string NYN)
	return false
func kQ (string Gwl[0.461,2.472,362.160], dynamic KE[1e18,968])	return "*'"'""

## bS&e0et
'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
number MV7 <- iu_
bool Wbxc <- zL ## I@A
bool NcL
func sX (string NB8q[1.965,6.970,6])
	return "'"'"'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
dynamic cdF <- 39E03
func GN (number iqI, var FYt, string n_pw[370.919,28E74])	return

string gI[3.738E+83]
'''
		expect = '''Error on line 3 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
var zS <- dfiU
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
bool Re[4.983e-12,576.460E+96,701E93] ## f&l(z>
bool Cg1q[57.097e-82] <- 20.870E21
func QtE ()
	begin
		vm <- 90
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
number DL[328,88.354e22,0] ## q>ZSh0V3sZ)
func Ez7 (var Vo[28])
	begin
		## i/Y3e
		for zFN9 until "[U" by 3.823E+35
			return CDZ
		return "'""
	end

func x5r ()	return false
string N1Ql[54.833e+74,65e+66] ## 7IB^]zi9x}l:HjShJw
var lI2G[930.439e-48,146.669e+16] <- Ex
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
func q7u (bool i7, number cAwf, dynamic o1)	return "6'""

var nPlo <- false
'''
		expect = '''Error on line 2 col 32: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
func bVbR (bool bV2, bool bVI[4.064e49,5.197])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
func RMi (string Bahb, dynamic xy[731E-18,64,84])
	return "'"'"w'"*"

string eAs[3.519e18] ## YGI0^k~;GQb;
'''
		expect = '''Error on line 2 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
bool Jk <- "Q'"'"" ## L)Ghpbb
## +3B"Hc+1
func bEx ()
	begin
		hVp("_'"H'"k", ksQ, 2.028E-39)
		return
	end
string MEyV <- false
func dIX (var gh[63.925E-71,65E-57], number w7gt[66.007E32,52.630,48E-41], dynamic e1)	begin
		mdt <- "'"'""
		## t$2``iz,QVGb@8Nv
		## }?~;V/"2#*~ULmb^obfq
	end
'''
		expect = '''Error on line 10 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
## )I<hy<}J6
func nn8 (string oMrK)
	return Xdz_
number CG1[0e56,77.502E-72] <- false ## HvNuP/,L&XSS8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
var xc[199.494E+74,31E70]
dynamic Ep8
func gDC (number W9xz[31])	begin
		if (35e+48) begin
			## MX)$.*
		end
		else continue
		begin
			## g
			## +~)yuk32
			if (24)
			begin
			end
		end
		## qyrh9$K72*zS0nt01oY
	end

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
func bnk (string Wl, bool kwq_[613E-36,670.452])
	return

bool Vv <- Wn ## QJfHik_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func RTX9 (bool ywNo[37.374,27.259e-03])	return false
## Q[?{r=8RB
func pvTG (bool sCnK, number zhjq[638E31,846e-24], bool Ta[421.890])	return

func OzW ()	return
bool cIw[70.863e72] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
func Cp3 ()	return
func GQp4 (string uV, var gbl2[868.037E-30,174.325,1.121])	return false

var C0N[8.244e+75,657.825,349.183] <- bcW
func Plus (number ng1, bool lI[7.412,3e+02,71.420], dynamic Oqfu)
	return true

'''
		expect = '''Error on line 3 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
string fcE ## L+4Ln_6kCP7Im-$6?
## sbgW|_
## m}4%YBHJ
dynamic achR <- 885E00 ## W|cK? ~o+
## ^k2W|a{? t7W[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
## S(t?A""sE
## M1%3Ih&BM/)G}<>
func ittM (string dbx, var mbrc[8,75e-34,73E+66], bool th8l[86e39,39.762E50,69])
	return "'""
func RAX (dynamic Z09[8e+06,88E66,54E+83])	begin
		RwA()
		Gbl("#'"X'"", true)["w'"r2", "'"'"'"'"B"] <- vAGr
		## fJG@(|,B?oFT
	end
'''
		expect = '''Error on line 4 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
dynamic hdXU ## O7I*W SnW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
## :N%rOhV8Dv<~v#9k|5df
func O9PZ (string KPU, string XHxg)
	return "'">'"x'""
func plCo ()
	begin
		for zk until "M'"I'"" by 6
			Pdp(false)
		## A-dFv]nz2)l:iVOD
		vk <- "k'"'""
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
var Qdlf[165,44.069e-14,97.571e-47] <- bW5 ## qgA-t.Cjb
bool NB[324.783,79]
number N9W <- 6.569 ## ?.67bA(52??Bl|O
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
## enH@?X^
## Hm{0CK#uzi8%,f
func qFTf (bool DbBu[42,1])
	begin
		HrOp(Fx5k, "|")[false, "x"] <- pabQ
		##  3?vfv
		if (7) u3(58.984)[T9_7, 2.421e+06] <- "'"K"
		elif (true)
		if (24.680E-12)
		dynamic Oeh[44E+89] <- y_z
		elif ("'"")
		return "'"'"L'""
		elif ("'"'"g'"") return true
		else A7Cl["@'"'"", 2e+94, true] <- Gc
		elif (75.650) number x4lZ[448.252,47] <- "'"'"'"r5" ## .:=_8pw)8-GlV#I#u|;5
		elif (7) lZ(8e-82)
		elif (U3h) bool Hcd[1e38,3.937] ## +0
		elif ("f") return
		else if (57.738E-33)
		dynamic B2xD[910,5.608,66.476]
		elif (nJ)
		string d6kh[5.254e-52,72e31,6.169e-37]
		elif (Bx)
		return 94.297
		elif (7e+71)
		zX2()[Sx, 502, true] <- true
		elif (154.997e+08) kg(Ov2, true)
		elif (ZC) if (7.053) return
		elif (5.079e31)
		if ("'"")
		continue
		elif (Jjs) if ("=")
		sN(true)
		elif (xS6)
		return true
		elif (false)
		return
		elif ("'"")
		if (vobh)
		return
		elif (jd) break
		elif ("'"'"")
		for dkQe until false by oXu
			St(false, GT, false)
		else f6Tp("?'"'"", Kmy, 45.112)
		elif (false) return
		elif (g8uc) RZl[y3] <- 14.075
		else W8e6 <- ED
		elif (false) for Om until 236.284 by "'"'""
			begin
				var gq[61.103,32,4] <- J0m
				break
				## /]+2^s;I-hpt~TUeUg
			end
		elif (false)
		dynamic D8v <- 8.193E86
		elif (true) if ("KCJ")
		continue
		elif (825E-99)
		begin
			if (8.894E82) lAaf(true, "$6", ps)["eJkmO", true, hp1C] <- 934.047
			else continue
			return true
		end
		elif (false)
		begin
			string JKLy
			if ("k")
			for UU until YL by zh
				return false
			elif (true) begin
				## .Wa
				for d4 until oqC by "q'"'"c"
					string cvS[2.821]
			end
			elif (665.522e47) if (">") begin
			end
			else break
			break
		end
		elif ("'"'"BW") R2m("s")
		elif (Zq)
		continue
		elif (69e+13) pYg <- false
		else return 4.999e87
		elif (QqCm)
		continue
		elif ("p`'"") return true
		elif (526.612) ncB()
		else XgVn("'"'"6K")
	end
func hq (var Is2[87])	return

func Yw ()	return
'''
		expect = '''Error on line 11 col 13: ['''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
func Jb9H (var Xfj[861e-62,4], bool tc1b, dynamic JK[0.486,23])	begin
		## 7yW[5
	end
## (vSvyH8_?+uFKRk4)hU>
func CHsi (bool WH)	return true
func lVx5 (string AE, dynamic gR[4.273,27], dynamic u8o)	begin
		break
		## V|iouQ
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
## !o6V}olVI]E
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
func hs (dynamic WM)
	begin
		ZS("'"x=Tz", "0", "'"d'"'"'"")
		var R7L[51.484e-87] <- "mi'"" ## oya}FpLm
		begin
		end
	end
## iCS]tI
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
func z6PH ()
	return

func Tme (bool nTD[3.734,1.676,734.186], number Rx, var VOQH[3.311])	begin
	end
number VH6[40.819E15] <- 6.210 ## DcbyQP"Q]O~o[N`}B7{
var H_Sj
'''
		expect = '''Error on line 5 col 52: var'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
func Hq (var NRrJ, var LB)	return

## xcDM!;b>twqS9+[@=)=z
func oCA ()
	return
var jx[290.601,50.183e+25,58]
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
func Rg (dynamic g8[0.358e-74], string FR)
	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
bool dUrg <- 57
func fim (bool gLuJ, number nC8[561.730E-07,0.281E+50,642E-09], bool rR)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
var JE8l[297.389e-60,549e+17,914.489] ## tE
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
dynamic jlG[62,9.493]
## <
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
## s#:_$E#*d@"j|i6D*_$B
dynamic lS ## ay/V+OK
number yD3[58.831e+19,918]
## D&6O@|D;;lxh9)
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
func tV (bool uL[56])
	begin
	end
## puxz>r>X-%BN+;Ivui~
func Xhd (var KQ[5E-64,9e-89,16.428e-35], number q6k[64.313])	begin
		return true
		## (u*&}|8
		return
	end

## EnXmrm
'''
		expect = '''Error on line 6 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
func qx (dynamic kD[71.257,5.195,1.807], string MTfV)	begin
		## M7g<R[QEI
	end
var Oi <- 27.403e+94
## =[^;dp}o0M(
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
func CGl ()	begin
		## $,S-6KE=)JCxa?3ma
		## gB;
	end

number z6iN[550,8e-45] <- 8.668 ##  |7_B4HY8s+N36!u f
func i7 ()	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
func EKh4 (bool Q2[0E-94,52E00], bool ps)
	begin
		## &l<l&Xwq}~NtA
		## 0g[Q
		for xgr until true by "'"Zn'")"
			continue
	end

func sX4 (number m7e)
	return
bool K5T <- Ejw ## wZ)N`[CvfRM1)
dynamic fdHx[6E+96,0E-24] <- false ## pq
'''
		expect = '''Error on line 13 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
func qo (number wJu[45])	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
## )
string DKK[599.016] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
func oqLX ()
	return
func HC (bool WSX1[2,68,31.244e+07], var hSH[321.143,73E-61], string f4[452])
	return "%j'"'""

'''
		expect = '''Error on line 4 col 37: var'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
var txm <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
func Oy8T (string of[5E24,54E-40,96E97], string Iw, var ImL[2.961])
	return
'''
		expect = '''Error on line 2 col 52: var'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
func tIr (dynamic k9, bool P1, var frI[584.175,656.518])	return OE
string OWm <- "}'"2m" ## 8RVmEzX/"o{
func xb (number Qo0[80.760e16])	begin
		## ()<g5t6l1s{
		## ~ik4Du]??148
		## :=b?)mi{EjNz=#
	end
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
func CqL ()	return 765E72
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
func NEP (dynamic hP3i)	begin
	end

bool wK9J
bool do45 <- fy0g ## N`u4M9MVD7
func E8z (number c488)
	return
## _l]wM:kdiF>^<n!
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
bool Ti ## XMyz_ysV^dR-wI6~6ngC
dynamic sKe ## YX7h]H*k:~ER.Jf`
dynamic Qe <- true
## my"]gr_J:1$ zg}@
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
## )As4rz mn-n0O
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
func BLL (bool Lg[586E+94], bool gGd)
	begin
	end
## w`iK9X]xO&GUi)9AzCXg
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
dynamic c5GR[308.990E+45,77E13] <- false ## 3"dbb1xu
func LM (string cd[5.198])
	begin
		## ; 8EAG@l9$#+T8Sbz
		## >tli
		begin
			for j5 until true by vO
				U8d(Oa, Yd_)[Gha] <- "it'"'""
			## pOWR,)>|8NZ<Oi:l?`Zz
		end
	end

func X3 (var WT[4,2e-95,182.391e+31])
	return EgZO

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
func Q97 (bool PG[748.762e+00,20.502e21,9.009], string Hk, dynamic J0wH[1.232e+00])	begin
		if (660.435) break
		elif (I5)
		return "0'"F'"a"
		elif (false) return RQjX
		elif (4E+51)
		string aXC <- eONP
		elif ("'"h,'"Z")
		string wW <- YIi
		## 3_Cb+PZH$q)
		return aqz
	end

'''
		expect = '''Error on line 2 col 59: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
## 9NK"]@:vZF#$G
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
string RMcg[6E+20,5.226e+45,9.334] <- 4E25
func NE7 ()	return false
string SGE <- 25
## a//y3A91$FFj
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
dynamic kyj <- 8.045
var afoN[9.433E60,18,95.394E+74]
func nDy (string Hb[295.819], var D2L[907.118e+10,8.806])
	begin
	end

## p%e9 <Tg,GwSqHg;Ka
var QQKQ <- 78.507e+54
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
string ruJ[14.475E-32,3E47,7]
number fs2P[851E-43,7] <- "+" ## d-|o&(Hr$FRP-=-W1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
var OgT5 ## GJUV_VbwLmi|Bntt->
func Afp (bool ZJ, var EH6)	return
func JK6 (var LTU[41.575], dynamic n1, string j4wE[27,42e54])	begin
		## i
		begin
			begin
				begin
					## o?Q&2pdMQ>z<K~YX @
				end
				## rY:
				bool eBg
			end
			string jrX[79.783,3.979] <- "K)Y^" ## z)ktWc<w
		end
		Te(true)
	end

func mTDP (bool HK8)	return Cm0w

## . 
'''
		expect = '''Error on line 2 col 30: 
'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
func Vbi (bool ulLa)
	begin
		yvPz(false, false, "m'"")
		## DSvRRHM/S3Tr)h
	end
dynamic Dj[51.853,42.538]
func eu1 (var F5S[246.594E-27], string cOu[23E55], bool sI)
	return "'"r"
'''
		expect = '''Error on line 7 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
## wd8}l1>5M"*Yqnul
func h4 (string zR, dynamic qB, dynamic DNY[9.881,32.058,0])	return 657e-78
func Y8e ()	begin
	end
var hUuk[201] <- 5e-06 ## R]_qR$
func J8 ()	return true
'''
		expect = '''Error on line 3 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
var lsW[737.177,305e68] <- 262e-21
var K6[916.785E96,30.567,45e+91]
## ]l8&RkPx:v;=FUIT4]x
func OO (bool T1, string qpik[250,6.616E-68,765.274])
	begin
		sgul("L'"'"")
		## w8ki
	end
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
dynamic etRo ## A[8zxFNO5U!/2RJ
func XSrD (bool jYOp[85E+37,8E+49,82.631e-51])	return false

func cgI (number Oss2, number ME, bool K2x)	return

func Jvi ()	begin
		## mHnu#
		continue
		## @/s~k<@x7m:C9GC8
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
string hk[59e-02,239.080e+52,27.760e+46] ## @R,sFUvDVybXQ}bz`)
bool mnoW
## c{eS&-(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
## C(*.e[thYj?hi)"n
number vCX[496.632,75.489] <- AD ## -hkEb-0Db5z_y`e
func vCt (string RN, var EC)
	return
'''
		expect = '''Error on line 4 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
## d#H&t/Lgd%@
func pbwT (dynamic Vn, dynamic kL[8.318e-26], bool mZ[9.911e+07,0e01,690.038])
	return
bool a7C[3,64E+73]
func bG (dynamic dr[98e90,5.642])
	return Gju

func HL (string e_[33.178e+55,96.093e44,538.358], dynamic hrE)
	return false

'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
string Otu
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
bool Zz7[156.418e81] <- 8E21
## C3XJ$B3*^xd
## W^u~4/"
## 5oc
func W5h ()	return 8.009E62

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
## VCMqIFx1U`KQXUWr
string Iuax[352.075e45,7E-12,2.536]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
## Y$Xxy[
## RQ1Y5WT~+eAt8^%T
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
## ?
func B27 (bool Lpt, var mooL[378.607])	begin
	end
func m4kP (var r5B[5,51e92], string Z7, dynamic mE)	begin
		## %"=FM>0(+J
		## MpMbiF 9Rb!y
	end
'''
		expect = '''Error on line 3 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
## h<T3p5YE
string yv ## +>)ko>TUd{M?MUm4
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
## =r9+`]0XdlhJ?LSknvd9
func nQ (string Ap[6], var lYwh[66E+06], string dT[269,175,9])
	return 7.170E-86
## /!l,4h7
func P9KV (var p93r, string QH[56,8.593e-61,80.628e-13])
	begin
	end

number hPz7
'''
		expect = '''Error on line 3 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
## q!6?}+>(#H
func dN_E (string AzVc[0E-85,1e+95,23])	return false
number tpJr ## vOiH>_2#|41waF[otx
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
func Tu (string tAd[0.266E-33], var qada)	return 3

'''
		expect = '''Error on line 2 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
## ,em
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 300))
