# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\u01c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3x\n\3\3\4\3\4\3\4\5\4}\n\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0083\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\5\13\u00a1\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00a8\n\f\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00b0")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00b7\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c3")
        buf.write("\n\20\3\21\3\21\5\21\u00c7\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00ce\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00d7\n\23\3\24\3\24\3\24\5\24\u00dc\n\24\3\25\3")
        buf.write("\25\3\25\5\25\u00e1\n\25\3\26\3\26\5\26\u00e5\n\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u00f5\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0100\n\31\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0106\n\32\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u010e")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u011e\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u012b\n \3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\5%\u0141\n%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\5(\u0152\n(\3)\3)\3)\3)\3)\5)\u0159\n)\3")
        buf.write("*\3*\5*\u015d\n*\3+\3+\3+\3+\3+\5+\u0164\n+\3,\3,\3,\3")
        buf.write(",\3,\5,\u016b\n,\3-\3-\3-\3-\3-\3-\7-\u0173\n-\f-\16-")
        buf.write("\u0176\13-\3.\3.\3.\3.\3.\3.\7.\u017e\n.\f.\16.\u0181")
        buf.write("\13.\3/\3/\3/\3/\3/\3/\7/\u0189\n/\f/\16/\u018c\13/\3")
        buf.write("\60\3\60\3\60\5\60\u0191\n\60\3\61\3\61\3\61\5\61\u0196")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\7\62\u019d\n\62\f\62\16")
        buf.write("\62\u01a0\13\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01ab\n\63\3\64\3\64\3\65\3\65\5\65\u01b1\n")
        buf.write("\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u01bc\n\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\2")
        buf.write("\6XZ\\b9\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\7\3\2\5")
        buf.write("\7\3\2\30\31\3\2\32\33\3\2\34\36\4\2\37$\'\'\2\u01c7\2")
        buf.write("p\3\2\2\2\4w\3\2\2\2\6|\3\2\2\2\b\u0082\3\2\2\2\n\u0086")
        buf.write("\3\2\2\2\f\u008b\3\2\2\2\16\u008f\3\2\2\2\20\u0093\3\2")
        buf.write("\2\2\22\u0095\3\2\2\2\24\u00a0\3\2\2\2\26\u00a7\3\2\2")
        buf.write("\2\30\u00a9\3\2\2\2\32\u00af\3\2\2\2\34\u00b6\3\2\2\2")
        buf.write("\36\u00c2\3\2\2\2 \u00c6\3\2\2\2\"\u00cd\3\2\2\2$\u00cf")
        buf.write("\3\2\2\2&\u00db\3\2\2\2(\u00e0\3\2\2\2*\u00e4\3\2\2\2")
        buf.write(",\u00e6\3\2\2\2.\u00f4\3\2\2\2\60\u00ff\3\2\2\2\62\u0105")
        buf.write("\3\2\2\2\64\u0107\3\2\2\2\66\u010d\3\2\2\28\u010f\3\2")
        buf.write("\2\2:\u011d\3\2\2\2<\u011f\3\2\2\2>\u012a\3\2\2\2@\u012c")
        buf.write("\3\2\2\2B\u0130\3\2\2\2D\u0139\3\2\2\2F\u013b\3\2\2\2")
        buf.write("H\u0140\3\2\2\2J\u0142\3\2\2\2L\u0147\3\2\2\2N\u0151\3")
        buf.write("\2\2\2P\u0158\3\2\2\2R\u015c\3\2\2\2T\u0163\3\2\2\2V\u016a")
        buf.write("\3\2\2\2X\u016c\3\2\2\2Z\u0177\3\2\2\2\\\u0182\3\2\2\2")
        buf.write("^\u0190\3\2\2\2`\u0195\3\2\2\2b\u0197\3\2\2\2d\u01aa\3")
        buf.write("\2\2\2f\u01ac\3\2\2\2h\u01b0\3\2\2\2j\u01bb\3\2\2\2l\u01bd")
        buf.write("\3\2\2\2n\u01c2\3\2\2\2pq\5\4\3\2qr\7\2\2\3r\3\3\2\2\2")
        buf.write("st\5\6\4\2tu\5\4\3\2ux\3\2\2\2vx\5\6\4\2ws\3\2\2\2wv\3")
        buf.write("\2\2\2x\5\3\2\2\2y}\5\b\5\2z}\5,\27\2{}\7\60\2\2|y\3\2")
        buf.write("\2\2|z\3\2\2\2|{\3\2\2\2}\7\3\2\2\2~\u0083\5\n\6\2\177")
        buf.write("\u0083\5\f\7\2\u0080\u0083\5\16\b\2\u0081\u0083\5\22\n")
        buf.write("\2\u0082~\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2")
        buf.write("\2\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085")
        buf.write("\5(\25\2\u0085\t\3\2\2\2\u0086\u0087\7\t\2\2\u0087\u0088")
        buf.write("\7-\2\2\u0088\u0089\7%\2\2\u0089\u008a\5T+\2\u008a\13")
        buf.write("\3\2\2\2\u008b\u008c\7\n\2\2\u008c\u008d\7-\2\2\u008d")
        buf.write("\u008e\5&\24\2\u008e\r\3\2\2\2\u008f\u0090\5\20\t\2\u0090")
        buf.write("\u0091\7-\2\2\u0091\u0092\5&\24\2\u0092\17\3\2\2\2\u0093")
        buf.write("\u0094\t\2\2\2\u0094\21\3\2\2\2\u0095\u0096\5\20\t\2\u0096")
        buf.write("\u0097\7-\2\2\u0097\u0098\7*\2\2\u0098\u0099\5\24\13\2")
        buf.write("\u0099\u009a\7+\2\2\u009a\u009b\5\26\f\2\u009b\23\3\2")
        buf.write("\2\2\u009c\u009d\7.\2\2\u009d\u009e\7,\2\2\u009e\u00a1")
        buf.write("\5\24\13\2\u009f\u00a1\7.\2\2\u00a0\u009c\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\25\3\2\2\2\u00a2\u00a3\7%\2\2\u00a3")
        buf.write("\u00a8\5\30\r\2\u00a4\u00a5\7%\2\2\u00a5\u00a8\5T+\2\u00a6")
        buf.write("\u00a8\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a4\3\2\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\27\3\2\2\2\u00a9\u00aa\7*\2")
        buf.write("\2\u00aa\u00ab\5\32\16\2\u00ab\u00ac\7+\2\2\u00ac\31\3")
        buf.write("\2\2\2\u00ad\u00b0\5\34\17\2\u00ae\u00b0\5\36\20\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\33\3\2\2\2\u00b1")
        buf.write("\u00b2\5T+\2\u00b2\u00b3\7,\2\2\u00b3\u00b4\5\34\17\2")
        buf.write("\u00b4\u00b7\3\2\2\2\u00b5\u00b7\5T+\2\u00b6\u00b1\3\2")
        buf.write("\2\2\u00b6\u00b5\3\2\2\2\u00b7\35\3\2\2\2\u00b8\u00b9")
        buf.write("\7*\2\2\u00b9\u00ba\5\34\17\2\u00ba\u00bb\7+\2\2\u00bb")
        buf.write("\u00bc\7,\2\2\u00bc\u00bd\5\36\20\2\u00bd\u00c3\3\2\2")
        buf.write("\2\u00be\u00bf\7*\2\2\u00bf\u00c0\5\34\17\2\u00c0\u00c1")
        buf.write("\7+\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00b8\3\2\2\2\u00c2")
        buf.write("\u00be\3\2\2\2\u00c3\37\3\2\2\2\u00c4\u00c7\5\"\22\2\u00c5")
        buf.write("\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2")
        buf.write("\u00c7!\3\2\2\2\u00c8\u00c9\5$\23\2\u00c9\u00ca\7,\2\2")
        buf.write("\u00ca\u00cb\5\"\22\2\u00cb\u00ce\3\2\2\2\u00cc\u00ce")
        buf.write("\5$\23\2\u00cd\u00c8\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("#\3\2\2\2\u00cf\u00d6\5\20\t\2\u00d0\u00d7\7-\2\2\u00d1")
        buf.write("\u00d2\7-\2\2\u00d2\u00d3\7*\2\2\u00d3\u00d4\5\24\13\2")
        buf.write("\u00d4\u00d5\7+\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d0\3")
        buf.write("\2\2\2\u00d6\u00d1\3\2\2\2\u00d7%\3\2\2\2\u00d8\u00d9")
        buf.write("\7%\2\2\u00d9\u00dc\5T+\2\u00da\u00dc\3\2\2\2\u00db\u00d8")
        buf.write("\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\'\3\2\2\2\u00dd\u00de")
        buf.write("\7\60\2\2\u00de\u00e1\5(\25\2\u00df\u00e1\7\60\2\2\u00e0")
        buf.write("\u00dd\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1)\3\2\2\2\u00e2")
        buf.write("\u00e5\5(\25\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e5+\3\2\2\2\u00e6\u00e7\7\13\2")
        buf.write("\2\u00e7\u00e8\7-\2\2\u00e8\u00e9\7(\2\2\u00e9\u00ea\5")
        buf.write(" \21\2\u00ea\u00eb\7)\2\2\u00eb\u00ec\5.\30\2\u00ec-\3")
        buf.write("\2\2\2\u00ed\u00f5\5(\25\2\u00ee\u00ef\5*\26\2\u00ef\u00f0")
        buf.write("\5H%\2\u00f0\u00f5\3\2\2\2\u00f1\u00f2\5*\26\2\u00f2\u00f3")
        buf.write("\5L\'\2\u00f3\u00f5\3\2\2\2\u00f4\u00ed\3\2\2\2\u00f4")
        buf.write("\u00ee\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f5/\3\2\2\2\u00f6")
        buf.write("\u0100\5\62\32\2\u00f7\u0100\5\64\33\2\u00f8\u0100\5D")
        buf.write("#\2\u00f9\u0100\58\35\2\u00fa\u0100\5B\"\2\u00fb\u0100")
        buf.write("\5F$\2\u00fc\u0100\5H%\2\u00fd\u0100\5J&\2\u00fe\u0100")
        buf.write("\5L\'\2\u00ff\u00f6\3\2\2\2\u00ff\u00f7\3\2\2\2\u00ff")
        buf.write("\u00f8\3\2\2\2\u00ff\u00f9\3\2\2\2\u00ff\u00fa\3\2\2\2")
        buf.write("\u00ff\u00fb\3\2\2\2\u00ff\u00fc\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u00ff\u00fe\3\2\2\2\u0100\61\3\2\2\2\u0101\u0106")
        buf.write("\5\n\6\2\u0102\u0106\5\f\7\2\u0103\u0106\5\16\b\2\u0104")
        buf.write("\u0106\5\22\n\2\u0105\u0101\3\2\2\2\u0105\u0102\3\2\2")
        buf.write("\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106\63\3")
        buf.write("\2\2\2\u0107\u0108\5\66\34\2\u0108\u0109\7%\2\2\u0109")
        buf.write("\u010a\5T+\2\u010a\65\3\2\2\2\u010b\u010e\7-\2\2\u010c")
        buf.write("\u010e\5h\65\2\u010d\u010b\3\2\2\2\u010d\u010c\3\2\2\2")
        buf.write("\u010e\67\3\2\2\2\u010f\u0110\7\21\2\2\u0110\u0111\7(")
        buf.write("\2\2\u0111\u0112\5T+\2\u0112\u0113\7)\2\2\u0113\u0114")
        buf.write("\5*\26\2\u0114\u0115\5\60\31\2\u0115\u0116\5:\36\2\u0116")
        buf.write("\u0117\5> \2\u01179\3\2\2\2\u0118\u0119\5(\25\2\u0119")
        buf.write("\u011a\5<\37\2\u011a\u011b\5:\36\2\u011b\u011e\3\2\2\2")
        buf.write("\u011c\u011e\3\2\2\2\u011d\u0118\3\2\2\2\u011d\u011c\3")
        buf.write("\2\2\2\u011e;\3\2\2\2\u011f\u0120\7\23\2\2\u0120\u0121")
        buf.write("\7(\2\2\u0121\u0122\5T+\2\u0122\u0123\7)\2\2\u0123\u0124")
        buf.write("\5*\26\2\u0124\u0125\5\60\31\2\u0125=\3\2\2\2\u0126\u0127")
        buf.write("\5(\25\2\u0127\u0128\5@!\2\u0128\u012b\3\2\2\2\u0129\u012b")
        buf.write("\3\2\2\2\u012a\u0126\3\2\2\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("?\3\2\2\2\u012c\u012d\7\22\2\2\u012d\u012e\5*\26\2\u012e")
        buf.write("\u012f\5\60\31\2\u012fA\3\2\2\2\u0130\u0131\7\f\2\2\u0131")
        buf.write("\u0132\7-\2\2\u0132\u0133\7\r\2\2\u0133\u0134\5T+\2\u0134")
        buf.write("\u0135\7\16\2\2\u0135\u0136\5T+\2\u0136\u0137\5*\26\2")
        buf.write("\u0137\u0138\5\60\31\2\u0138C\3\2\2\2\u0139\u013a\7\17")
        buf.write("\2\2\u013aE\3\2\2\2\u013b\u013c\7\20\2\2\u013cG\3\2\2")
        buf.write("\2\u013d\u0141\7\b\2\2\u013e\u013f\7\b\2\2\u013f\u0141")
        buf.write("\5T+\2\u0140\u013d\3\2\2\2\u0140\u013e\3\2\2\2\u0141I")
        buf.write("\3\2\2\2\u0142\u0143\7-\2\2\u0143\u0144\7(\2\2\u0144\u0145")
        buf.write("\5P)\2\u0145\u0146\7)\2\2\u0146K\3\2\2\2\u0147\u0148\7")
        buf.write("\24\2\2\u0148\u0149\5(\25\2\u0149\u014a\5N(\2\u014a\u014b")
        buf.write("\7\25\2\2\u014bM\3\2\2\2\u014c\u014d\5\60\31\2\u014d\u014e")
        buf.write("\5(\25\2\u014e\u014f\5N(\2\u014f\u0152\3\2\2\2\u0150\u0152")
        buf.write("\3\2\2\2\u0151\u014c\3\2\2\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("O\3\2\2\2\u0153\u0154\5R*\2\u0154\u0155\7,\2\2\u0155\u0156")
        buf.write("\5P)\2\u0156\u0159\3\2\2\2\u0157\u0159\5R*\2\u0158\u0153")
        buf.write("\3\2\2\2\u0158\u0157\3\2\2\2\u0159Q\3\2\2\2\u015a\u015d")
        buf.write("\5T+\2\u015b\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015dS\3\2\2\2\u015e\u015f\5V,\2\u015f\u0160")
        buf.write("\7&\2\2\u0160\u0161\5V,\2\u0161\u0164\3\2\2\2\u0162\u0164")
        buf.write("\5V,\2\u0163\u015e\3\2\2\2\u0163\u0162\3\2\2\2\u0164U")
        buf.write("\3\2\2\2\u0165\u0166\5X-\2\u0166\u0167\5f\64\2\u0167\u0168")
        buf.write("\5X-\2\u0168\u016b\3\2\2\2\u0169\u016b\5X-\2\u016a\u0165")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016bW\3\2\2\2\u016c\u016d")
        buf.write("\b-\1\2\u016d\u016e\5Z.\2\u016e\u0174\3\2\2\2\u016f\u0170")
        buf.write("\f\4\2\2\u0170\u0171\t\3\2\2\u0171\u0173\5Z.\2\u0172\u016f")
        buf.write("\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175Y\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0178\b.\1\2\u0178\u0179\5\\/\2\u0179\u017f\3\2\2\2\u017a")
        buf.write("\u017b\f\4\2\2\u017b\u017c\t\4\2\2\u017c\u017e\5\\/\2")
        buf.write("\u017d\u017a\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180[\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0182\u0183\b/\1\2\u0183\u0184\5^\60\2\u0184")
        buf.write("\u018a\3\2\2\2\u0185\u0186\f\4\2\2\u0186\u0187\t\5\2\2")
        buf.write("\u0187\u0189\5^\60\2\u0188\u0185\3\2\2\2\u0189\u018c\3")
        buf.write("\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b]")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\7\27\2\2\u018e")
        buf.write("\u0191\5^\60\2\u018f\u0191\5`\61\2\u0190\u018d\3\2\2\2")
        buf.write("\u0190\u018f\3\2\2\2\u0191_\3\2\2\2\u0192\u0193\t\4\2")
        buf.write("\2\u0193\u0196\5`\61\2\u0194\u0196\5b\62\2\u0195\u0192")
        buf.write("\3\2\2\2\u0195\u0194\3\2\2\2\u0196a\3\2\2\2\u0197\u0198")
        buf.write("\b\62\1\2\u0198\u0199\5d\63\2\u0199\u019e\3\2\2\2\u019a")
        buf.write("\u019b\f\4\2\2\u019b\u019d\5h\65\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019fc\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01ab")
        buf.write("\7-\2\2\u01a2\u01ab\7.\2\2\u01a3\u01ab\7\3\2\2\u01a4\u01ab")
        buf.write("\7\4\2\2\u01a5\u01ab\7/\2\2\u01a6\u01ab\5\30\r\2\u01a7")
        buf.write("\u01ab\5h\65\2\u01a8\u01ab\5l\67\2\u01a9\u01ab\5n8\2\u01aa")
        buf.write("\u01a1\3\2\2\2\u01aa\u01a2\3\2\2\2\u01aa\u01a3\3\2\2\2")
        buf.write("\u01aa\u01a4\3\2\2\2\u01aa\u01a5\3\2\2\2\u01aa\u01a6\3")
        buf.write("\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01abe\3\2\2\2\u01ac\u01ad\t\6\2\2\u01adg\3\2")
        buf.write("\2\2\u01ae\u01b1\7-\2\2\u01af\u01b1\5l\67\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b3\7*\2\2\u01b3\u01b4\5j\66\2\u01b4\u01b5\7+\2\2\u01b5")
        buf.write("i\3\2\2\2\u01b6\u01b7\5T+\2\u01b7\u01b8\7,\2\2\u01b8\u01b9")
        buf.write("\5j\66\2\u01b9\u01bc\3\2\2\2\u01ba\u01bc\5T+\2\u01bb\u01b6")
        buf.write("\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bck\3\2\2\2\u01bd\u01be")
        buf.write("\7-\2\2\u01be\u01bf\7(\2\2\u01bf\u01c0\5P)\2\u01c0\u01c1")
        buf.write("\7)\2\2\u01c1m\3\2\2\2\u01c2\u01c3\7(\2\2\u01c3\u01c4")
        buf.write("\5T+\2\u01c4\u01c5\7)\2\2\u01c5o\3\2\2\2%w|\u0082\u00a0")
        buf.write("\u00a7\u00af\u00b6\u00c2\u00c6\u00cd\u00d6\u00db\u00e0")
        buf.write("\u00e4\u00f4\u00ff\u0105\u010d\u011d\u012a\u0140\u0151")
        buf.write("\u0158\u015c\u0163\u016a\u0174\u017f\u018a\u0190\u0195")
        buf.write("\u019e\u01aa\u01b0\u01bb")
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
    RULE_declare_list = 1
    RULE_declaration = 2
    RULE_variable_decl = 3
    RULE_var = 4
    RULE_dynamic = 5
    RULE_normal_type = 6
    RULE_type_list = 7
    RULE_array_type = 8
    RULE_size = 9
    RULE_array_rhs = 10
    RULE_array_literal = 11
    RULE_array_elements = 12
    RULE_one_element = 13
    RULE_multiple_elements = 14
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
    RULE_elif_list = 28
    RULE_elif_part = 29
    RULE_else_list = 30
    RULE_else_part = 31
    RULE_for_stmt = 32
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_return_stmt = 35
    RULE_function_call_stmt = 36
    RULE_block_stmt = 37
    RULE_block_body = 38
    RULE_expression_list = 39
    RULE_expression_prime = 40
    RULE_expression = 41
    RULE_expression2 = 42
    RULE_expression3 = 43
    RULE_expression4 = 44
    RULE_expression5 = 45
    RULE_expression6 = 46
    RULE_expression7 = 47
    RULE_expression8 = 48
    RULE_expression9 = 49
    RULE_relational_sign = 50
    RULE_index_operators_expr = 51
    RULE_index_operators = 52
    RULE_function_call_expr = 53
    RULE_sub_expr = 54

    ruleNames =  [ "program", "declare_list", "declaration", "variable_decl", 
                   "var", "dynamic", "normal_type", "type_list", "array_type", 
                   "size", "array_rhs", "array_literal", "array_elements", 
                   "one_element", "multiple_elements", "parameter_list", 
                   "parameter_prime", "parameter", "nullable_vardecl_expr", 
                   "atleast_newline", "nullable_newline", "function_decl", 
                   "function_body", "statement", "variable_decl_stmt", "assignment_stmt", 
                   "assignment_type", "if_stmt", "elif_list", "elif_part", 
                   "else_list", "else_part", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "function_call_stmt", "block_stmt", "block_body", 
                   "expression_list", "expression_prime", "expression", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "expression9", 
                   "relational_sign", "index_operators_expr", "index_operators", 
                   "function_call_expr", "sub_expr" ]

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

        def declare_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.declare_list()
            self.state = 111
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def declare_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_list" ):
                return visitor.visitDeclare_list(self)
            else:
                return visitor.visitChildren(self)




    def declare_list(self):

        localctx = ZCodeParser.Declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare_list)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.declaration()
                self.state = 114
                self.declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.declaration()
                pass


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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.variable_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.function_decl()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(ZCodeParser.NEWLINE)
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
        self.enterRule(localctx, 6, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 124
                self.var()
                pass

            elif la_ == 2:
                self.state = 125
                self.dynamic()
                pass

            elif la_ == 3:
                self.state = 126
                self.normal_type()
                pass

            elif la_ == 4:
                self.state = 127
                self.array_type()
                pass


            self.state = 130
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
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ZCodeParser.VAR)
            self.state = 133
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 134
            self.match(ZCodeParser.ASSIGN)
            self.state = 135
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
        self.enterRule(localctx, 10, self.RULE_dynamic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ZCodeParser.DYNAMIC)
            self.state = 138
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 139
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
        self.enterRule(localctx, 12, self.RULE_normal_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.type_list()
            self.state = 142
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 143
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
        self.enterRule(localctx, 14, self.RULE_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
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


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def size(self):
            return self.getTypedRuleContext(ZCodeParser.SizeContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

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
        self.enterRule(localctx, 16, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.type_list()
            self.state = 148
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 149
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 150
            self.size()
            self.state = 151
            self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
            self.state = 152
            self.array_rhs()
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
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
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
        self.enterRule(localctx, 20, self.RULE_array_rhs)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(ZCodeParser.ASSIGN)
                self.state = 161
                self.array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(ZCodeParser.ASSIGN)
                self.state = 163
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
        self.enterRule(localctx, 22, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 168
            self.array_elements()
            self.state = 169
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
        self.enterRule(localctx, 24, self.RULE_array_elements)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.one_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
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
        self.enterRule(localctx, 26, self.RULE_one_element)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.expression()
                self.state = 176
                self.match(ZCodeParser.COMMA)
                self.state = 177
                self.one_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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
        self.enterRule(localctx, 28, self.RULE_multiple_elements)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 183
                self.one_element()
                self.state = 184
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
                self.state = 185
                self.match(ZCodeParser.COMMA)
                self.state = 186
                self.multiple_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 189
                self.one_element()
                self.state = 190
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
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
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
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

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def size(self):
            return self.getTypedRuleContext(ZCodeParser.SizeContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

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
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 206
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 207
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 208
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 209
                self.size()
                self.state = 210
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.ASSIGN)
                self.state = 215
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
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(ZCodeParser.NEWLINE)
                self.state = 220
                self.atleast_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
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
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
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
            self.state = 228
            self.match(ZCodeParser.FUNC)
            self.state = 229
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 230
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 231
            self.parameter_list()
            self.state = 232
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 233
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
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.atleast_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.nullable_newline()
                self.state = 237
                self.return_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.nullable_newline()
                self.state = 240
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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.variable_decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.break_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
                self.function_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 252
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
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.dynamic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.normal_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
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
            self.state = 261
            self.assignment_type()
            self.state = 262
            self.match(ZCodeParser.ASSIGN)
            self.state = 263
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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
            self.state = 275
            self.elif_list()
            self.state = 276
            self.else_list()
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
        self.enterRule(localctx, 56, self.RULE_elif_list)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.atleast_newline()
                self.state = 279
                self.elif_part()
                self.state = 280
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
        self.enterRule(localctx, 58, self.RULE_elif_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ZCodeParser.ELIF)
            self.state = 286
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 287
            self.expression()
            self.state = 288
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 289
            self.nullable_newline()
            self.state = 290
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
        self.enterRule(localctx, 60, self.RULE_else_list)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.atleast_newline()
                self.state = 293
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
        self.enterRule(localctx, 62, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(ZCodeParser.ELSE)
            self.state = 299
            self.nullable_newline()
            self.state = 300
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
        self.enterRule(localctx, 64, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ZCodeParser.FOR)
            self.state = 303
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 304
            self.match(ZCodeParser.UNTIL)
            self.state = 305
            self.expression()
            self.state = 306
            self.match(ZCodeParser.BY)
            self.state = 307
            self.expression()
            self.state = 308
            self.nullable_newline()
            self.state = 309
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
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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
        self.enterRule(localctx, 70, self.RULE_return_stmt)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(ZCodeParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(ZCodeParser.RETURN)
                self.state = 317
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
        self.enterRule(localctx, 72, self.RULE_function_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 321
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 322
            self.expression_list()
            self.state = 323
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
        self.enterRule(localctx, 74, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.BEGIN)
            self.state = 326
            self.atleast_newline()
            self.state = 327
            self.block_body()
            self.state = 328
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
        self.enterRule(localctx, 76, self.RULE_block_body)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.statement()
                self.state = 331
                self.atleast_newline()
                self.state = 332
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
        self.enterRule(localctx, 78, self.RULE_expression_list)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expression_prime()
                self.state = 338
                self.match(ZCodeParser.COMMA)
                self.state = 339
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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
        self.enterRule(localctx, 80, self.RULE_expression_prime)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
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
        self.enterRule(localctx, 82, self.RULE_expression)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.expression2()
                self.state = 349
                self.match(ZCodeParser.CONCAT)
                self.state = 350
                self.expression2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
        self.enterRule(localctx, 84, self.RULE_expression2)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.expression3(0)
                self.state = 356
                self.relational_sign()
                self.state = 357
                self.expression3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 365
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 366
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 367
                    self.expression4(0) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 378
                    self.expression5(0) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 389
                    self.expression6() 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_expression6)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(ZCodeParser.NOT)
                self.state = 396
                self.expression6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
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

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

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
        self.enterRule(localctx, 94, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.PLUS, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 401
                self.expression7()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expression8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.expression9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 408
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    self.index_operators_expr() 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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


        def function_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_exprContext,0)


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
        self.enterRule(localctx, 98, self.RULE_expression9)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 418
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 419
                self.match(ZCodeParser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 420
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 421
                self.index_operators_expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 422
                self.function_call_expr()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 423
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
        self.enterRule(localctx, 100, self.RULE_relational_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
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

        def function_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators_expr" ):
                return visitor.visitIndex_operators_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_operators_expr(self):

        localctx = ZCodeParser.Index_operators_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_index_operators_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 428
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 429
                self.function_call_expr()
                pass


            self.state = 432
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 433
            self.index_operators()
            self.state = 434
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
        self.enterRule(localctx, 104, self.RULE_index_operators)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.expression()
                self.state = 437
                self.match(ZCodeParser.COMMA)
                self.state = 438
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_exprContext(ParserRuleContext):
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
            return ZCodeParser.RULE_function_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_expr" ):
                return visitor.visitFunction_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def function_call_expr(self):

        localctx = ZCodeParser.Function_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_function_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 444
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 445
            self.expression_list()
            self.state = 446
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
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
            self.state = 448
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 449
            self.expression()
            self.state = 450
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
        self._predicates[43] = self.expression3_sempred
        self._predicates[44] = self.expression4_sempred
        self._predicates[45] = self.expression5_sempred
        self._predicates[48] = self.expression8_sempred
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
         




