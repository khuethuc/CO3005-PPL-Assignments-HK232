# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01c0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\6\2s\n\2")
        buf.write("\r\2\16\2t\3\2\3\2\3\3\3\3\5\3{\n\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u0081\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00a1\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\5\r\u00a9\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00b0\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00bc\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00c3\n\20\3\21\3\21\5\21\u00c7\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00ce\n\22\3\23\3\23\3\23\5\23\u00d3")
        buf.write("\n\23\3\24\3\24\3\24\5\24\u00d8\n\24\3\25\3\25\3\25\5")
        buf.write("\25\u00dd\n\25\3\26\3\26\5\26\u00e1\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u00f1\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u00fc\n\31\3\32\3\32\3\32\3\32\5\32\u0102")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u010a\n\34\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u011c\n\37\3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\5!\u0129\n!\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\5&\u013f\n")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\5")
        buf.write(")\u0150\n)\3*\3*\3*\3*\3*\5*\u0157\n*\3+\3+\5+\u015b\n")
        buf.write("+\3,\3,\3,\3,\3,\5,\u0162\n,\3-\3-\3-\3-\3-\5-\u0169\n")
        buf.write("-\3.\3.\3.\3.\3.\3.\7.\u0171\n.\f.\16.\u0174\13.\3/\3")
        buf.write("/\3/\3/\3/\3/\7/\u017c\n/\f/\16/\u017f\13/\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\7\60\u0187\n\60\f\60\16\60\u018a\13")
        buf.write("\60\3\61\3\61\3\61\5\61\u018f\n\61\3\62\3\62\3\62\5\62")
        buf.write("\u0194\n\62\3\63\3\63\3\63\3\63\3\63\7\63\u019b\n\63\f")
        buf.write("\63\16\63\u019e\13\63\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u01a9\n\64\3\65\3\65\3\66\3\66\5\66")
        buf.write("\u01af\n\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3")
        buf.write("\67\5\67\u01ba\n\67\38\38\38\38\38\2\6Z\\^d9\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjln\2\7\3\2\5\7\3\2\30\31\3\2\32")
        buf.write("\33\3\2\34\36\4\2\37$\'\'\2\u01c0\2r\3\2\2\2\4z\3\2\2")
        buf.write("\2\6\u0080\3\2\2\2\b\u0084\3\2\2\2\n\u0089\3\2\2\2\f\u008d")
        buf.write("\3\2\2\2\16\u0091\3\2\2\2\20\u0093\3\2\2\2\22\u0097\3")
        buf.write("\2\2\2\24\u00a0\3\2\2\2\26\u00a2\3\2\2\2\30\u00a8\3\2")
        buf.write("\2\2\32\u00af\3\2\2\2\34\u00bb\3\2\2\2\36\u00c2\3\2\2")
        buf.write("\2 \u00c6\3\2\2\2\"\u00cd\3\2\2\2$\u00cf\3\2\2\2&\u00d7")
        buf.write("\3\2\2\2(\u00dc\3\2\2\2*\u00e0\3\2\2\2,\u00e2\3\2\2\2")
        buf.write(".\u00f0\3\2\2\2\60\u00fb\3\2\2\2\62\u0101\3\2\2\2\64\u0103")
        buf.write("\3\2\2\2\66\u0109\3\2\2\28\u010b\3\2\2\2:\u010f\3\2\2")
        buf.write("\2<\u011b\3\2\2\2>\u011d\3\2\2\2@\u0128\3\2\2\2B\u012a")
        buf.write("\3\2\2\2D\u012e\3\2\2\2F\u0137\3\2\2\2H\u0139\3\2\2\2")
        buf.write("J\u013e\3\2\2\2L\u0140\3\2\2\2N\u0145\3\2\2\2P\u014f\3")
        buf.write("\2\2\2R\u0156\3\2\2\2T\u015a\3\2\2\2V\u0161\3\2\2\2X\u0168")
        buf.write("\3\2\2\2Z\u016a\3\2\2\2\\\u0175\3\2\2\2^\u0180\3\2\2\2")
        buf.write("`\u018e\3\2\2\2b\u0193\3\2\2\2d\u0195\3\2\2\2f\u01a8\3")
        buf.write("\2\2\2h\u01aa\3\2\2\2j\u01ae\3\2\2\2l\u01b9\3\2\2\2n\u01bb")
        buf.write("\3\2\2\2ps\7\60\2\2qs\5\4\3\2rp\3\2\2\2rq\3\2\2\2st\3")
        buf.write("\2\2\2tr\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\7\2\2\3w\3\3\2")
        buf.write("\2\2x{\5\6\4\2y{\5,\27\2zx\3\2\2\2zy\3\2\2\2{\5\3\2\2")
        buf.write("\2|\u0081\5\b\5\2}\u0081\5\n\6\2~\u0081\5\f\7\2\177\u0081")
        buf.write("\5\20\t\2\u0080|\3\2\2\2\u0080}\3\2\2\2\u0080~\3\2\2\2")
        buf.write("\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\5(")
        buf.write("\25\2\u0083\7\3\2\2\2\u0084\u0085\7\t\2\2\u0085\u0086")
        buf.write("\7-\2\2\u0086\u0087\7%\2\2\u0087\u0088\5V,\2\u0088\t\3")
        buf.write("\2\2\2\u0089\u008a\7\n\2\2\u008a\u008b\7-\2\2\u008b\u008c")
        buf.write("\5&\24\2\u008c\13\3\2\2\2\u008d\u008e\5\16\b\2\u008e\u008f")
        buf.write("\7-\2\2\u008f\u0090\5&\24\2\u0090\r\3\2\2\2\u0091\u0092")
        buf.write("\t\2\2\2\u0092\17\3\2\2\2\u0093\u0094\5\16\b\2\u0094\u0095")
        buf.write("\5\22\n\2\u0095\u0096\5\36\20\2\u0096\21\3\2\2\2\u0097")
        buf.write("\u0098\7-\2\2\u0098\u0099\7*\2\2\u0099\u009a\5\24\13\2")
        buf.write("\u009a\u009b\7+\2\2\u009b\23\3\2\2\2\u009c\u009d\7.\2")
        buf.write("\2\u009d\u009e\7,\2\2\u009e\u00a1\5\24\13\2\u009f\u00a1")
        buf.write("\7.\2\2\u00a0\u009c\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\25\3\2\2\2\u00a2\u00a3\7*\2\2\u00a3\u00a4\5\30\r\2\u00a4")
        buf.write("\u00a5\7+\2\2\u00a5\27\3\2\2\2\u00a6\u00a9\5\32\16\2\u00a7")
        buf.write("\u00a9\5\34\17\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a9\31\3\2\2\2\u00aa\u00ab\5V,\2\u00ab\u00ac\7,\2")
        buf.write("\2\u00ac\u00ad\5\32\16\2\u00ad\u00b0\3\2\2\2\u00ae\u00b0")
        buf.write("\5V,\2\u00af\u00aa\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\33")
        buf.write("\3\2\2\2\u00b1\u00b2\7*\2\2\u00b2\u00b3\5\32\16\2\u00b3")
        buf.write("\u00b4\7+\2\2\u00b4\u00b5\7,\2\2\u00b5\u00b6\5\34\17\2")
        buf.write("\u00b6\u00bc\3\2\2\2\u00b7\u00b8\7*\2\2\u00b8\u00b9\5")
        buf.write("\32\16\2\u00b9\u00ba\7+\2\2\u00ba\u00bc\3\2\2\2\u00bb")
        buf.write("\u00b1\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bc\35\3\2\2\2\u00bd")
        buf.write("\u00be\7%\2\2\u00be\u00c3\5\26\f\2\u00bf\u00c0\7%\2\2")
        buf.write("\u00c0\u00c3\5V,\2\u00c1\u00c3\3\2\2\2\u00c2\u00bd\3\2")
        buf.write("\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\37")
        buf.write("\3\2\2\2\u00c4\u00c7\5\"\22\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7!\3\2\2\2\u00c8")
        buf.write("\u00c9\5$\23\2\u00c9\u00ca\7,\2\2\u00ca\u00cb\5\"\22\2")
        buf.write("\u00cb\u00ce\3\2\2\2\u00cc\u00ce\5$\23\2\u00cd\u00c8\3")
        buf.write("\2\2\2\u00cd\u00cc\3\2\2\2\u00ce#\3\2\2\2\u00cf\u00d2")
        buf.write("\5\16\b\2\u00d0\u00d3\7-\2\2\u00d1\u00d3\5\22\n\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3%\3\2\2\2\u00d4")
        buf.write("\u00d5\7%\2\2\u00d5\u00d8\5V,\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00d4\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\'\3\2\2\2\u00d9")
        buf.write("\u00da\7\60\2\2\u00da\u00dd\5(\25\2\u00db\u00dd\7\60\2")
        buf.write("\2\u00dc\u00d9\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd)\3\2")
        buf.write("\2\2\u00de\u00e1\5(\25\2\u00df\u00e1\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1+\3\2\2\2\u00e2\u00e3")
        buf.write("\7\13\2\2\u00e3\u00e4\7-\2\2\u00e4\u00e5\7(\2\2\u00e5")
        buf.write("\u00e6\5 \21\2\u00e6\u00e7\7)\2\2\u00e7\u00e8\5.\30\2")
        buf.write("\u00e8-\3\2\2\2\u00e9\u00f1\5(\25\2\u00ea\u00eb\5*\26")
        buf.write("\2\u00eb\u00ec\5J&\2\u00ec\u00f1\3\2\2\2\u00ed\u00ee\5")
        buf.write("*\26\2\u00ee\u00ef\5N(\2\u00ef\u00f1\3\2\2\2\u00f0\u00e9")
        buf.write("\3\2\2\2\u00f0\u00ea\3\2\2\2\u00f0\u00ed\3\2\2\2\u00f1")
        buf.write("/\3\2\2\2\u00f2\u00fc\5\62\32\2\u00f3\u00fc\5\64\33\2")
        buf.write("\u00f4\u00fc\5F$\2\u00f5\u00fc\58\35\2\u00f6\u00fc\5D")
        buf.write("#\2\u00f7\u00fc\5H%\2\u00f8\u00fc\5J&\2\u00f9\u00fc\5")
        buf.write("L\'\2\u00fa\u00fc\5N(\2\u00fb\u00f2\3\2\2\2\u00fb\u00f3")
        buf.write("\3\2\2\2\u00fb\u00f4\3\2\2\2\u00fb\u00f5\3\2\2\2\u00fb")
        buf.write("\u00f6\3\2\2\2\u00fb\u00f7\3\2\2\2\u00fb\u00f8\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\61\3\2")
        buf.write("\2\2\u00fd\u0102\5\b\5\2\u00fe\u0102\5\n\6\2\u00ff\u0102")
        buf.write("\5\f\7\2\u0100\u0102\5\20\t\2\u0101\u00fd\3\2\2\2\u0101")
        buf.write("\u00fe\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2")
        buf.write("\u0102\63\3\2\2\2\u0103\u0104\5\66\34\2\u0104\u0105\7")
        buf.write("%\2\2\u0105\u0106\5V,\2\u0106\65\3\2\2\2\u0107\u010a\7")
        buf.write("-\2\2\u0108\u010a\5j\66\2\u0109\u0107\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\67\3\2\2\2\u010b\u010c\5:\36\2\u010c\u010d")
        buf.write("\5<\37\2\u010d\u010e\5@!\2\u010e9\3\2\2\2\u010f\u0110")
        buf.write("\7\21\2\2\u0110\u0111\7(\2\2\u0111\u0112\5V,\2\u0112\u0113")
        buf.write("\7)\2\2\u0113\u0114\5*\26\2\u0114\u0115\5\60\31\2\u0115")
        buf.write(";\3\2\2\2\u0116\u0117\5(\25\2\u0117\u0118\5> \2\u0118")
        buf.write("\u0119\5<\37\2\u0119\u011c\3\2\2\2\u011a\u011c\3\2\2\2")
        buf.write("\u011b\u0116\3\2\2\2\u011b\u011a\3\2\2\2\u011c=\3\2\2")
        buf.write("\2\u011d\u011e\7\23\2\2\u011e\u011f\7(\2\2\u011f\u0120")
        buf.write("\5V,\2\u0120\u0121\7)\2\2\u0121\u0122\5*\26\2\u0122\u0123")
        buf.write("\5\60\31\2\u0123?\3\2\2\2\u0124\u0125\5(\25\2\u0125\u0126")
        buf.write("\5B\"\2\u0126\u0129\3\2\2\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u0124\3\2\2\2\u0128\u0127\3\2\2\2\u0129A\3\2\2\2\u012a")
        buf.write("\u012b\7\22\2\2\u012b\u012c\5*\26\2\u012c\u012d\5\60\31")
        buf.write("\2\u012dC\3\2\2\2\u012e\u012f\7\f\2\2\u012f\u0130\7-\2")
        buf.write("\2\u0130\u0131\7\r\2\2\u0131\u0132\5V,\2\u0132\u0133\7")
        buf.write("\16\2\2\u0133\u0134\5V,\2\u0134\u0135\5*\26\2\u0135\u0136")
        buf.write("\5\60\31\2\u0136E\3\2\2\2\u0137\u0138\7\17\2\2\u0138G")
        buf.write("\3\2\2\2\u0139\u013a\7\20\2\2\u013aI\3\2\2\2\u013b\u013f")
        buf.write("\7\b\2\2\u013c\u013d\7\b\2\2\u013d\u013f\5V,\2\u013e\u013b")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013fK\3\2\2\2\u0140\u0141")
        buf.write("\7-\2\2\u0141\u0142\7(\2\2\u0142\u0143\5R*\2\u0143\u0144")
        buf.write("\7)\2\2\u0144M\3\2\2\2\u0145\u0146\7\24\2\2\u0146\u0147")
        buf.write("\5(\25\2\u0147\u0148\5P)\2\u0148\u0149\7\25\2\2\u0149")
        buf.write("O\3\2\2\2\u014a\u014b\5\60\31\2\u014b\u014c\5(\25\2\u014c")
        buf.write("\u014d\5P)\2\u014d\u0150\3\2\2\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u014a\3\2\2\2\u014f\u014e\3\2\2\2\u0150Q\3\2\2\2\u0151")
        buf.write("\u0152\5T+\2\u0152\u0153\7,\2\2\u0153\u0154\5R*\2\u0154")
        buf.write("\u0157\3\2\2\2\u0155\u0157\5T+\2\u0156\u0151\3\2\2\2\u0156")
        buf.write("\u0155\3\2\2\2\u0157S\3\2\2\2\u0158\u015b\5V,\2\u0159")
        buf.write("\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2")
        buf.write("\u015bU\3\2\2\2\u015c\u015d\5X-\2\u015d\u015e\7&\2\2\u015e")
        buf.write("\u015f\5X-\2\u015f\u0162\3\2\2\2\u0160\u0162\5X-\2\u0161")
        buf.write("\u015c\3\2\2\2\u0161\u0160\3\2\2\2\u0162W\3\2\2\2\u0163")
        buf.write("\u0164\5Z.\2\u0164\u0165\5h\65\2\u0165\u0166\5Z.\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0169\5Z.\2\u0168\u0163\3\2\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169Y\3\2\2\2\u016a\u016b\b.\1\2\u016b")
        buf.write("\u016c\5\\/\2\u016c\u0172\3\2\2\2\u016d\u016e\f\4\2\2")
        buf.write("\u016e\u016f\t\3\2\2\u016f\u0171\5\\/\2\u0170\u016d\3")
        buf.write("\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173[\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176")
        buf.write("\b/\1\2\u0176\u0177\5^\60\2\u0177\u017d\3\2\2\2\u0178")
        buf.write("\u0179\f\4\2\2\u0179\u017a\t\4\2\2\u017a\u017c\5^\60\2")
        buf.write("\u017b\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3")
        buf.write("\2\2\2\u017d\u017e\3\2\2\2\u017e]\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u0180\u0181\b\60\1\2\u0181\u0182\5`\61\2\u0182")
        buf.write("\u0188\3\2\2\2\u0183\u0184\f\4\2\2\u0184\u0185\t\5\2\2")
        buf.write("\u0185\u0187\5`\61\2\u0186\u0183\3\2\2\2\u0187\u018a\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189_")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c\7\27\2\2\u018c")
        buf.write("\u018f\5`\61\2\u018d\u018f\5b\62\2\u018e\u018b\3\2\2\2")
        buf.write("\u018e\u018d\3\2\2\2\u018fa\3\2\2\2\u0190\u0191\7\33\2")
        buf.write("\2\u0191\u0194\5b\62\2\u0192\u0194\5d\63\2\u0193\u0190")
        buf.write("\3\2\2\2\u0193\u0192\3\2\2\2\u0194c\3\2\2\2\u0195\u0196")
        buf.write("\b\63\1\2\u0196\u0197\5f\64\2\u0197\u019c\3\2\2\2\u0198")
        buf.write("\u0199\f\4\2\2\u0199\u019b\5j\66\2\u019a\u0198\3\2\2\2")
        buf.write("\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019de\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a9")
        buf.write("\7-\2\2\u01a0\u01a9\7.\2\2\u01a1\u01a9\7\3\2\2\u01a2\u01a9")
        buf.write("\7\4\2\2\u01a3\u01a9\7/\2\2\u01a4\u01a9\5\26\f\2\u01a5")
        buf.write("\u01a9\5j\66\2\u01a6\u01a9\5L\'\2\u01a7\u01a9\5n8\2\u01a8")
        buf.write("\u019f\3\2\2\2\u01a8\u01a0\3\2\2\2\u01a8\u01a1\3\2\2\2")
        buf.write("\u01a8\u01a2\3\2\2\2\u01a8\u01a3\3\2\2\2\u01a8\u01a4\3")
        buf.write("\2\2\2\u01a8\u01a5\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9g\3\2\2\2\u01aa\u01ab\t\6\2\2\u01abi\3\2")
        buf.write("\2\2\u01ac\u01af\7-\2\2\u01ad\u01af\5L\'\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b1\7*\2\2\u01b1\u01b2\5l\67\2\u01b2\u01b3\7+\2\2\u01b3")
        buf.write("k\3\2\2\2\u01b4\u01b5\5V,\2\u01b5\u01b6\7,\2\2\u01b6\u01b7")
        buf.write("\5l\67\2\u01b7\u01ba\3\2\2\2\u01b8\u01ba\5V,\2\u01b9\u01b4")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01bam\3\2\2\2\u01bb\u01bc")
        buf.write("\7(\2\2\u01bc\u01bd\5V,\2\u01bd\u01be\7)\2\2\u01beo\3")
        buf.write("\2\2\2&rtz\u0080\u00a0\u00a8\u00af\u00bb\u00c2\u00c6\u00cd")
        buf.write("\u00d2\u00d7\u00dc\u00e0\u00f0\u00fb\u0101\u0109\u011b")
        buf.write("\u0128\u013e\u014f\u0156\u015a\u0161\u0168\u0172\u017d")
        buf.write("\u0188\u018e\u0193\u019c\u01a8\u01ae\u01b9")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'while'", 
                     "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'<-'", "'...'", "'=='", "'('", "')'", "'['", "']'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOLEAN", 
                      "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "WHILE", "NOT", "AND", "OR", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NEQ", 
                      "LESS", "GREATER", "LEQ", "GEQ", "ASSIGN", "CONCAT", 
                      "EQUAL_STRING", "OPEN_ROUND_BRACKET", "CLOSE_ROUND_BRACKET", 
                      "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", "COMMA", 
                      "IDENTIFIER", "NUMBER_LITERAL", "STRING_LITERAL", 
                      "NEWLINE", "COMMENT", "WHITE_SPACE", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variable_decl = 2
    RULE_var = 3
    RULE_dynamic = 4
    RULE_normal_type = 5
    RULE_type_list = 6
    RULE_array_type = 7
    RULE_array_variable_decl = 8
    RULE_size = 9
    RULE_array_literal = 10
    RULE_array_elements = 11
    RULE_one_element = 12
    RULE_multiple_elements = 13
    RULE_array_rhs = 14
    RULE_parameter_list = 15
    RULE_parameter_prime = 16
    RULE_parameter = 17
    RULE_nullable_vardecl_expr = 18
    RULE_atleast_newline = 19
    RULE_nullable_newline = 20
    RULE_function_decl = 21
    RULE_function_body = 22
    RULE_statement = 23
    RULE_variable_decl_stmt = 24
    RULE_assignment_stmt = 25
    RULE_assignment_type = 26
    RULE_if_stmt = 27
    RULE_if_part = 28
    RULE_elif_list = 29
    RULE_elif_part = 30
    RULE_else_list = 31
    RULE_else_part = 32
    RULE_for_stmt = 33
    RULE_break_stmt = 34
    RULE_continue_stmt = 35
    RULE_return_stmt = 36
    RULE_function_call_stmt = 37
    RULE_block_stmt = 38
    RULE_block_body = 39
    RULE_expression_list = 40
    RULE_expression_prime = 41
    RULE_expression = 42
    RULE_expression2 = 43
    RULE_expression3 = 44
    RULE_expression4 = 45
    RULE_expression5 = 46
    RULE_expression6 = 47
    RULE_expression7 = 48
    RULE_expression8 = 49
    RULE_expression9 = 50
    RULE_relational_sign = 51
    RULE_index_operators_expr = 52
    RULE_index_operators = 53
    RULE_sub_expr = 54

    ruleNames =  [ "program", "declaration", "variable_decl", "var", "dynamic", 
                   "normal_type", "type_list", "array_type", "array_variable_decl", 
                   "size", "array_literal", "array_elements", "one_element", 
                   "multiple_elements", "array_rhs", "parameter_list", "parameter_prime", 
                   "parameter", "nullable_vardecl_expr", "atleast_newline", 
                   "nullable_newline", "function_decl", "function_body", 
                   "statement", "variable_decl_stmt", "assignment_stmt", 
                   "assignment_type", "if_stmt", "if_part", "elif_list", 
                   "elif_part", "else_list", "else_part", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "function_call_stmt", 
                   "block_stmt", "block_body", "expression_list", "expression_prime", 
                   "expression", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "expression9", "relational_sign", "index_operators_expr", 
                   "index_operators", "sub_expr" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOLEAN=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    WHILE=20
    NOT=21
    AND=22
    OR=23
    PLUS=24
    MINUS=25
    MUL=26
    DIV=27
    MOD=28
    EQUAL=29
    NEQ=30
    LESS=31
    GREATER=32
    LEQ=33
    GEQ=34
    ASSIGN=35
    CONCAT=36
    EQUAL_STRING=37
    OPEN_ROUND_BRACKET=38
    CLOSE_ROUND_BRACKET=39
    OPEN_SQUARE_BRACKET=40
    CLOSE_SQUARE_BRACKET=41
    COMMA=42
    IDENTIFIER=43
    NUMBER_LITERAL=44
    STRING_LITERAL=45
    NEWLINE=46
    COMMENT=47
    WHITE_SPACE=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 110
                    self.match(ZCodeParser.NEWLINE)
                    pass
                elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                    self.state = 111
                    self.declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.NEWLINE))) != 0)):
                    break

            self.state = 116
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.variable_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.function_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def var(self):
            return self.getTypedRuleContext(ZCodeParser.VarContext,0)


        def dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicContext,0)


        def normal_type(self):
            return self.getTypedRuleContext(ZCodeParser.Normal_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = ZCodeParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 122
                self.var()
                pass

            elif la_ == 2:
                self.state = 123
                self.dynamic()
                pass

            elif la_ == 3:
                self.state = 124
                self.normal_type()
                pass

            elif la_ == 4:
                self.state = 125
                self.array_type()
                pass


            self.state = 128
            self.atleast_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = ZCodeParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ZCodeParser.VAR)
            self.state = 131
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 132
            self.match(ZCodeParser.ASSIGN)
            self.state = 133
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def nullable_vardecl_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_vardecl_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic" ):
                return visitor.visitDynamic(self)
            else:
                return visitor.visitChildren(self)




    def dynamic(self):

        localctx = ZCodeParser.DynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dynamic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ZCodeParser.DYNAMIC)
            self.state = 136
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 137
            self.nullable_vardecl_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_listContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def nullable_vardecl_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_vardecl_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normal_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_type" ):
                return visitor.visitNormal_type(self)
            else:
                return visitor.visitChildren(self)




    def normal_type(self):

        localctx = ZCodeParser.Normal_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.type_list()
            self.state = 140
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 141
            self.nullable_vardecl_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_list" ):
                return visitor.visitType_list(self)
            else:
                return visitor.visitChildren(self)




    def type_list(self):

        localctx = ZCodeParser.Type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_listContext,0)


        def array_variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Array_variable_declContext,0)


        def array_rhs(self):
            return self.getTypedRuleContext(ZCodeParser.Array_rhsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = ZCodeParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.type_list()
            self.state = 146
            self.array_variable_decl()
            self.state = 147
            self.array_rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def size(self):
            return self.getTypedRuleContext(ZCodeParser.SizeContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_variable_decl" ):
                return visitor.visitArray_variable_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_variable_decl(self):

        localctx = ZCodeParser.Array_variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 150
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 151
            self.size()
            self.state = 152
            self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(ZCodeParser.SizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = ZCodeParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_size)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 155
                self.match(ZCodeParser.COMMA)
                self.state = 156
                self.size()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def array_elements(self):
            return self.getTypedRuleContext(ZCodeParser.Array_elementsContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 161
            self.array_elements()
            self.state = 162
            self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_element(self):
            return self.getTypedRuleContext(ZCodeParser.One_elementContext,0)


        def multiple_elements(self):
            return self.getTypedRuleContext(ZCodeParser.Multiple_elementsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = ZCodeParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_elements)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.one_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.multiple_elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def one_element(self):
            return self.getTypedRuleContext(ZCodeParser.One_elementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_one_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_element" ):
                return visitor.visitOne_element(self)
            else:
                return visitor.visitChildren(self)




    def one_element(self):

        localctx = ZCodeParser.One_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_one_element)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.expression()
                self.state = 169
                self.match(ZCodeParser.COMMA)
                self.state = 170
                self.one_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def one_element(self):
            return self.getTypedRuleContext(ZCodeParser.One_elementContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def multiple_elements(self):
            return self.getTypedRuleContext(ZCodeParser.Multiple_elementsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_multiple_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_elements" ):
                return visitor.visitMultiple_elements(self)
            else:
                return visitor.visitChildren(self)




    def multiple_elements(self):

        localctx = ZCodeParser.Multiple_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_multiple_elements)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 176
                self.one_element()
                self.state = 177
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
                self.state = 178
                self.match(ZCodeParser.COMMA)
                self.state = 179
                self.multiple_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 182
                self.one_element()
                self.state = 183
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_rhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_rhs" ):
                return visitor.visitArray_rhs(self)
            else:
                return visitor.visitChildren(self)




    def array_rhs(self):

        localctx = ZCodeParser.Array_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_rhs)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(ZCodeParser.ASSIGN)
                self.state = 188
                self.array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(ZCodeParser.ASSIGN)
                self.state = 190
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.parameter_prime()
                pass
            elif token in [ZCodeParser.CLOSE_ROUND_BRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_prime" ):
                return visitor.visitParameter_prime(self)
            else:
                return visitor.visitChildren(self)




    def parameter_prime(self):

        localctx = ZCodeParser.Parameter_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameter_prime)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.parameter()
                self.state = 199
                self.match(ZCodeParser.COMMA)
                self.state = 200
                self.parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_listContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Array_variable_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.type_list()
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 206
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 207
                self.array_variable_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_vardecl_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_vardecl_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_vardecl_expr" ):
                return visitor.visitNullable_vardecl_expr(self)
            else:
                return visitor.visitChildren(self)




    def nullable_vardecl_expr(self):

        localctx = ZCodeParser.Nullable_vardecl_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_nullable_vardecl_expr)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(ZCodeParser.ASSIGN)
                self.state = 211
                self.expression()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atleast_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_atleast_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtleast_newline" ):
                return visitor.visitAtleast_newline(self)
            else:
                return visitor.visitChildren(self)




    def atleast_newline(self):

        localctx = ZCodeParser.Atleast_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_atleast_newline)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ZCodeParser.NEWLINE)
                self.state = 216
                self.atleast_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline" ):
                return visitor.visitNullable_newline(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline(self):

        localctx = ZCodeParser.Nullable_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_nullable_newline)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.atleast_newline()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = ZCodeParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ZCodeParser.FUNC)
            self.state = 225
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 226
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 227
            self.parameter_list()
            self.state = 228
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 229
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def nullable_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlineContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_body)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.atleast_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.nullable_newline()
                self.state = 233
                self.return_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.nullable_newline()
                self.state = 236
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_decl_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def function_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.variable_decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.break_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 247
                self.function_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 248
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(ZCodeParser.VarContext,0)


        def dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicContext,0)


        def normal_type(self):
            return self.getTypedRuleContext(ZCodeParser.Normal_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl_stmt" ):
                return visitor.visitVariable_decl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl_stmt(self):

        localctx = ZCodeParser.Variable_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_variable_decl_stmt)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.dynamic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.normal_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_type(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_typeContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = ZCodeParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.assignment_type()
            self.state = 258
            self.match(ZCodeParser.ASSIGN)
            self.state = 259
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def index_operators_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operators_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_type" ):
                return visitor.visitAssignment_type(self)
            else:
                return visitor.visitChildren(self)




    def assignment_type(self):

        localctx = ZCodeParser.Assignment_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_type)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.index_operators_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(ZCodeParser.If_partContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def else_list(self):
            return self.getTypedRuleContext(ZCodeParser.Else_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.if_part()
            self.state = 266
            self.elif_list()
            self.state = 267
            self.else_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def nullable_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = ZCodeParser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.IF)
            self.state = 270
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 271
            self.expression()
            self.state = 272
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 273
            self.nullable_newline()
            self.state = 274
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def elif_part(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_partContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elif_list)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.atleast_newline()
                self.state = 277
                self.elif_part()
                self.state = 278
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def nullable_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_part" ):
                return visitor.visitElif_part(self)
            else:
                return visitor.visitChildren(self)




    def elif_part(self):

        localctx = ZCodeParser.Elif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elif_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ZCodeParser.ELIF)
            self.state = 284
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 285
            self.expression()
            self.state = 286
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 287
            self.nullable_newline()
            self.state = 288
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def else_part(self):
            return self.getTypedRuleContext(ZCodeParser.Else_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_list" ):
                return visitor.visitElse_list(self)
            else:
                return visitor.visitChildren(self)




    def else_list(self):

        localctx = ZCodeParser.Else_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_list)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.atleast_newline()
                self.state = 291
                self.else_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullable_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = ZCodeParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(ZCodeParser.ELSE)
            self.state = 297
            self.nullable_newline()
            self.state = 298
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlineContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.FOR)
            self.state = 301
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 302
            self.match(ZCodeParser.UNTIL)
            self.state = 303
            self.expression()
            self.state = 304
            self.match(ZCodeParser.BY)
            self.state = 305
            self.expression()
            self.state = 306
            self.nullable_newline()
            self.state = 307
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_return_stmt)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(ZCodeParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(ZCodeParser.RETURN)
                self.state = 315
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_stmt" ):
                return visitor.visitFunction_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def function_call_stmt(self):

        localctx = ZCodeParser.Function_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_function_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 319
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 320
            self.expression_list()
            self.state = 321
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def block_body(self):
            return self.getTypedRuleContext(ZCodeParser.Block_bodyContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.BEGIN)
            self.state = 324
            self.atleast_newline()
            self.state = 325
            self.block_body()
            self.state = 326
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def atleast_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Atleast_newlineContext,0)


        def block_body(self):
            return self.getTypedRuleContext(ZCodeParser.Block_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_body" ):
                return visitor.visitBlock_body(self)
            else:
                return visitor.visitChildren(self)




    def block_body(self):

        localctx = ZCodeParser.Block_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_body)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.statement()
                self.state = 329
                self.atleast_newline()
                self.state = 330
                self.block_body()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_primeContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression_list)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.expression_prime()
                self.state = 336
                self.match(ZCodeParser.COMMA)
                self.state = 337
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.expression_prime()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_prime" ):
                return visitor.visitExpression_prime(self)
            else:
                return visitor.visitChildren(self)




    def expression_prime(self):

        localctx = ZCodeParser.Expression_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression_prime)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.expression()
                pass
            elif token in [ZCodeParser.CLOSE_ROUND_BRACKET, ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expression)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.expression2()
                self.state = 347
                self.match(ZCodeParser.CONCAT)
                self.state = 348
                self.expression2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.expression2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression3Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression3Context,i)


        def relational_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_signContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)




    def expression2(self):

        localctx = ZCodeParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression2)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.expression3(0)
                self.state = 354
                self.relational_sign()
                self.state = 355
                self.expression3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.expression3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 365
                    self.expression4(0) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 376
                    self.expression5(0) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 387
                    self.expression6() 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expression6)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(ZCodeParser.NOT)
                self.state = 394
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.MINUS, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expression7)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.MINUS)
                self.state = 399
                self.expression7()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.expression8(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(ZCodeParser.Expression9Context,0)


        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def index_operators_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operators_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)



    def expression8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expression8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.expression9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    self.index_operators_expr() 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRING_LITERAL(self):
            return self.getToken(ZCodeParser.STRING_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def index_operators_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operators_exprContext,0)


        def function_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_stmtContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)




    def expression9(self):

        localctx = ZCodeParser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression9)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 416
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 417
                self.match(ZCodeParser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 418
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 419
                self.index_operators_expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 420
                self.function_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 421
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def EQUAL_STRING(self):
            return self.getToken(ZCodeParser.EQUAL_STRING, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LEQ(self):
            return self.getToken(ZCodeParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(ZCodeParser.GEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_sign" ):
                return visitor.visitRelational_sign(self)
            else:
                return visitor.visitChildren(self)




    def relational_sign(self):

        localctx = ZCodeParser.Relational_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_relational_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.LEQ) | (1 << ZCodeParser.GEQ) | (1 << ZCodeParser.EQUAL_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operators_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def function_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators_expr" ):
                return visitor.visitIndex_operators_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_operators_expr(self):

        localctx = ZCodeParser.Index_operators_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_index_operators_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 426
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 427
                self.function_call_stmt()
                pass


            self.state = 430
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 431
            self.index_operators()
            self.state = 432
            self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_operators)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.expression()
                self.state = 435
                self.match(ZCodeParser.COMMA)
                self.state = 436
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = ZCodeParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 442
            self.expression()
            self.state = 443
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[44] = self.expression3_sempred
        self._predicates[45] = self.expression4_sempred
        self._predicates[46] = self.expression5_sempred
        self._predicates[49] = self.expression8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression8_sempred(self, localctx:Expression8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




