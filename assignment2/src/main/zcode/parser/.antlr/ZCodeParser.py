# Generated from /Users/thuckhue/Desktop/HCMUT/HK232/Principles of Programming Language/Assignments/Assignment 2/assignment2/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,453,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,118,8,1,1,2,
        1,2,1,2,3,2,123,8,2,1,3,1,3,1,3,1,3,3,3,129,8,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,159,8,9,1,10,1,10,1,10,1,10,
        1,10,3,10,166,8,10,1,11,1,11,1,11,1,11,1,12,1,12,3,12,174,8,12,1,
        13,1,13,1,13,1,13,1,13,3,13,181,8,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,193,8,14,1,15,1,15,3,15,197,8,15,1,16,
        1,16,1,16,1,16,1,16,3,16,204,8,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,213,8,17,1,18,1,18,1,18,3,18,218,8,18,1,19,1,19,1,19,3,
        19,223,8,19,1,20,1,20,3,20,227,8,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,243,8,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,254,8,23,1,24,1,24,1,24,
        1,24,3,24,260,8,24,1,25,1,25,1,25,1,25,1,26,1,26,3,26,268,8,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,
        28,3,28,284,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,
        30,1,30,3,30,297,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,35,3,35,319,
        8,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,
        1,38,1,38,1,38,3,38,336,8,38,1,39,1,39,1,39,1,39,1,39,3,39,343,8,
        39,1,40,1,40,3,40,347,8,40,1,41,1,41,1,41,1,41,1,41,3,41,354,8,41,
        1,42,1,42,1,42,1,42,1,42,3,42,361,8,42,1,43,1,43,1,43,1,43,1,43,
        1,43,5,43,369,8,43,10,43,12,43,372,9,43,1,44,1,44,1,44,1,44,1,44,
        1,44,5,44,380,8,44,10,44,12,44,383,9,44,1,45,1,45,1,45,1,45,1,45,
        1,45,5,45,391,8,45,10,45,12,45,394,9,45,1,46,1,46,1,46,3,46,399,
        8,46,1,47,1,47,1,47,3,47,404,8,47,1,48,1,48,1,48,1,48,1,48,5,48,
        411,8,48,10,48,12,48,414,9,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        1,49,1,49,3,49,425,8,49,1,50,1,50,1,51,1,51,3,51,431,8,51,1,51,1,
        51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,3,52,442,8,52,1,53,1,53,1,
        53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,0,4,86,88,90,96,55,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,
        96,98,100,102,104,106,108,0,5,1,0,3,5,1,0,22,23,1,0,24,25,1,0,26,
        28,2,0,29,34,37,37,453,0,110,1,0,0,0,2,117,1,0,0,0,4,122,1,0,0,0,
        6,128,1,0,0,0,8,132,1,0,0,0,10,137,1,0,0,0,12,141,1,0,0,0,14,145,
        1,0,0,0,16,147,1,0,0,0,18,158,1,0,0,0,20,165,1,0,0,0,22,167,1,0,
        0,0,24,173,1,0,0,0,26,180,1,0,0,0,28,192,1,0,0,0,30,196,1,0,0,0,
        32,203,1,0,0,0,34,205,1,0,0,0,36,217,1,0,0,0,38,222,1,0,0,0,40,226,
        1,0,0,0,42,228,1,0,0,0,44,242,1,0,0,0,46,253,1,0,0,0,48,259,1,0,
        0,0,50,261,1,0,0,0,52,267,1,0,0,0,54,269,1,0,0,0,56,283,1,0,0,0,
        58,285,1,0,0,0,60,296,1,0,0,0,62,298,1,0,0,0,64,302,1,0,0,0,66,311,
        1,0,0,0,68,313,1,0,0,0,70,318,1,0,0,0,72,320,1,0,0,0,74,325,1,0,
        0,0,76,335,1,0,0,0,78,342,1,0,0,0,80,346,1,0,0,0,82,353,1,0,0,0,
        84,360,1,0,0,0,86,362,1,0,0,0,88,373,1,0,0,0,90,384,1,0,0,0,92,398,
        1,0,0,0,94,403,1,0,0,0,96,405,1,0,0,0,98,424,1,0,0,0,100,426,1,0,
        0,0,102,430,1,0,0,0,104,441,1,0,0,0,106,443,1,0,0,0,108,448,1,0,
        0,0,110,111,3,2,1,0,111,112,5,0,0,1,112,1,1,0,0,0,113,114,3,4,2,
        0,114,115,3,2,1,0,115,118,1,0,0,0,116,118,3,4,2,0,117,113,1,0,0,
        0,117,116,1,0,0,0,118,3,1,0,0,0,119,123,3,6,3,0,120,123,3,42,21,
        0,121,123,5,46,0,0,122,119,1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,
        0,123,5,1,0,0,0,124,129,3,8,4,0,125,129,3,10,5,0,126,129,3,12,6,
        0,127,129,3,16,8,0,128,124,1,0,0,0,128,125,1,0,0,0,128,126,1,0,0,
        0,128,127,1,0,0,0,129,130,1,0,0,0,130,131,3,38,19,0,131,7,1,0,0,
        0,132,133,5,7,0,0,133,134,5,43,0,0,134,135,5,35,0,0,135,136,3,82,
        41,0,136,9,1,0,0,0,137,138,5,8,0,0,138,139,5,43,0,0,139,140,3,36,
        18,0,140,11,1,0,0,0,141,142,3,14,7,0,142,143,5,43,0,0,143,144,3,
        36,18,0,144,13,1,0,0,0,145,146,7,0,0,0,146,15,1,0,0,0,147,148,3,
        14,7,0,148,149,5,43,0,0,149,150,5,40,0,0,150,151,3,18,9,0,151,152,
        5,41,0,0,152,153,3,20,10,0,153,17,1,0,0,0,154,155,5,44,0,0,155,156,
        5,42,0,0,156,159,3,18,9,0,157,159,5,44,0,0,158,154,1,0,0,0,158,157,
        1,0,0,0,159,19,1,0,0,0,160,161,5,35,0,0,161,166,3,22,11,0,162,163,
        5,35,0,0,163,166,3,82,41,0,164,166,1,0,0,0,165,160,1,0,0,0,165,162,
        1,0,0,0,165,164,1,0,0,0,166,21,1,0,0,0,167,168,5,40,0,0,168,169,
        3,24,12,0,169,170,5,41,0,0,170,23,1,0,0,0,171,174,3,26,13,0,172,
        174,3,28,14,0,173,171,1,0,0,0,173,172,1,0,0,0,174,25,1,0,0,0,175,
        176,3,82,41,0,176,177,5,42,0,0,177,178,3,26,13,0,178,181,1,0,0,0,
        179,181,3,82,41,0,180,175,1,0,0,0,180,179,1,0,0,0,181,27,1,0,0,0,
        182,183,5,40,0,0,183,184,3,26,13,0,184,185,5,41,0,0,185,186,5,42,
        0,0,186,187,3,28,14,0,187,193,1,0,0,0,188,189,5,40,0,0,189,190,3,
        26,13,0,190,191,5,41,0,0,191,193,1,0,0,0,192,182,1,0,0,0,192,188,
        1,0,0,0,193,29,1,0,0,0,194,197,3,32,16,0,195,197,1,0,0,0,196,194,
        1,0,0,0,196,195,1,0,0,0,197,31,1,0,0,0,198,199,3,34,17,0,199,200,
        5,42,0,0,200,201,3,32,16,0,201,204,1,0,0,0,202,204,3,34,17,0,203,
        198,1,0,0,0,203,202,1,0,0,0,204,33,1,0,0,0,205,212,3,14,7,0,206,
        213,5,43,0,0,207,208,5,43,0,0,208,209,5,40,0,0,209,210,3,18,9,0,
        210,211,5,41,0,0,211,213,1,0,0,0,212,206,1,0,0,0,212,207,1,0,0,0,
        213,35,1,0,0,0,214,215,5,35,0,0,215,218,3,82,41,0,216,218,1,0,0,
        0,217,214,1,0,0,0,217,216,1,0,0,0,218,37,1,0,0,0,219,220,5,46,0,
        0,220,223,3,38,19,0,221,223,5,46,0,0,222,219,1,0,0,0,222,221,1,0,
        0,0,223,39,1,0,0,0,224,227,3,38,19,0,225,227,1,0,0,0,226,224,1,0,
        0,0,226,225,1,0,0,0,227,41,1,0,0,0,228,229,5,9,0,0,229,230,5,43,
        0,0,230,231,5,38,0,0,231,232,3,30,15,0,232,233,5,39,0,0,233,234,
        3,44,22,0,234,43,1,0,0,0,235,243,3,38,19,0,236,237,3,40,20,0,237,
        238,3,70,35,0,238,243,1,0,0,0,239,240,3,40,20,0,240,241,3,74,37,
        0,241,243,1,0,0,0,242,235,1,0,0,0,242,236,1,0,0,0,242,239,1,0,0,
        0,243,45,1,0,0,0,244,254,3,48,24,0,245,254,3,50,25,0,246,254,3,66,
        33,0,247,254,3,54,27,0,248,254,3,64,32,0,249,254,3,68,34,0,250,254,
        3,70,35,0,251,254,3,72,36,0,252,254,3,74,37,0,253,244,1,0,0,0,253,
        245,1,0,0,0,253,246,1,0,0,0,253,247,1,0,0,0,253,248,1,0,0,0,253,
        249,1,0,0,0,253,250,1,0,0,0,253,251,1,0,0,0,253,252,1,0,0,0,254,
        47,1,0,0,0,255,260,3,8,4,0,256,260,3,10,5,0,257,260,3,12,6,0,258,
        260,3,16,8,0,259,255,1,0,0,0,259,256,1,0,0,0,259,257,1,0,0,0,259,
        258,1,0,0,0,260,49,1,0,0,0,261,262,3,52,26,0,262,263,5,35,0,0,263,
        264,3,82,41,0,264,51,1,0,0,0,265,268,5,43,0,0,266,268,3,102,51,0,
        267,265,1,0,0,0,267,266,1,0,0,0,268,53,1,0,0,0,269,270,5,15,0,0,
        270,271,5,38,0,0,271,272,3,82,41,0,272,273,5,39,0,0,273,274,3,40,
        20,0,274,275,3,46,23,0,275,276,3,56,28,0,276,277,3,60,30,0,277,55,
        1,0,0,0,278,279,3,38,19,0,279,280,3,58,29,0,280,281,3,56,28,0,281,
        284,1,0,0,0,282,284,1,0,0,0,283,278,1,0,0,0,283,282,1,0,0,0,284,
        57,1,0,0,0,285,286,5,17,0,0,286,287,5,38,0,0,287,288,3,82,41,0,288,
        289,5,39,0,0,289,290,3,40,20,0,290,291,3,46,23,0,291,59,1,0,0,0,
        292,293,3,38,19,0,293,294,3,62,31,0,294,297,1,0,0,0,295,297,1,0,
        0,0,296,292,1,0,0,0,296,295,1,0,0,0,297,61,1,0,0,0,298,299,5,16,
        0,0,299,300,3,40,20,0,300,301,3,46,23,0,301,63,1,0,0,0,302,303,5,
        10,0,0,303,304,5,43,0,0,304,305,5,11,0,0,305,306,3,82,41,0,306,307,
        5,12,0,0,307,308,3,82,41,0,308,309,3,40,20,0,309,310,3,46,23,0,310,
        65,1,0,0,0,311,312,5,13,0,0,312,67,1,0,0,0,313,314,5,14,0,0,314,
        69,1,0,0,0,315,319,5,6,0,0,316,317,5,6,0,0,317,319,3,82,41,0,318,
        315,1,0,0,0,318,316,1,0,0,0,319,71,1,0,0,0,320,321,5,43,0,0,321,
        322,5,38,0,0,322,323,3,78,39,0,323,324,5,39,0,0,324,73,1,0,0,0,325,
        326,5,18,0,0,326,327,3,38,19,0,327,328,3,76,38,0,328,329,5,19,0,
        0,329,75,1,0,0,0,330,331,3,46,23,0,331,332,3,38,19,0,332,333,3,76,
        38,0,333,336,1,0,0,0,334,336,1,0,0,0,335,330,1,0,0,0,335,334,1,0,
        0,0,336,77,1,0,0,0,337,338,3,80,40,0,338,339,5,42,0,0,339,340,3,
        78,39,0,340,343,1,0,0,0,341,343,3,80,40,0,342,337,1,0,0,0,342,341,
        1,0,0,0,343,79,1,0,0,0,344,347,3,82,41,0,345,347,1,0,0,0,346,344,
        1,0,0,0,346,345,1,0,0,0,347,81,1,0,0,0,348,349,3,84,42,0,349,350,
        5,36,0,0,350,351,3,84,42,0,351,354,1,0,0,0,352,354,3,84,42,0,353,
        348,1,0,0,0,353,352,1,0,0,0,354,83,1,0,0,0,355,356,3,86,43,0,356,
        357,3,100,50,0,357,358,3,86,43,0,358,361,1,0,0,0,359,361,3,86,43,
        0,360,355,1,0,0,0,360,359,1,0,0,0,361,85,1,0,0,0,362,363,6,43,-1,
        0,363,364,3,88,44,0,364,370,1,0,0,0,365,366,10,2,0,0,366,367,7,1,
        0,0,367,369,3,88,44,0,368,365,1,0,0,0,369,372,1,0,0,0,370,368,1,
        0,0,0,370,371,1,0,0,0,371,87,1,0,0,0,372,370,1,0,0,0,373,374,6,44,
        -1,0,374,375,3,90,45,0,375,381,1,0,0,0,376,377,10,2,0,0,377,378,
        7,2,0,0,378,380,3,90,45,0,379,376,1,0,0,0,380,383,1,0,0,0,381,379,
        1,0,0,0,381,382,1,0,0,0,382,89,1,0,0,0,383,381,1,0,0,0,384,385,6,
        45,-1,0,385,386,3,92,46,0,386,392,1,0,0,0,387,388,10,2,0,0,388,389,
        7,3,0,0,389,391,3,92,46,0,390,387,1,0,0,0,391,394,1,0,0,0,392,390,
        1,0,0,0,392,393,1,0,0,0,393,91,1,0,0,0,394,392,1,0,0,0,395,396,5,
        21,0,0,396,399,3,92,46,0,397,399,3,94,47,0,398,395,1,0,0,0,398,397,
        1,0,0,0,399,93,1,0,0,0,400,401,7,2,0,0,401,404,3,94,47,0,402,404,
        3,96,48,0,403,400,1,0,0,0,403,402,1,0,0,0,404,95,1,0,0,0,405,406,
        6,48,-1,0,406,407,3,98,49,0,407,412,1,0,0,0,408,409,10,2,0,0,409,
        411,3,102,51,0,410,408,1,0,0,0,411,414,1,0,0,0,412,410,1,0,0,0,412,
        413,1,0,0,0,413,97,1,0,0,0,414,412,1,0,0,0,415,425,5,43,0,0,416,
        425,5,44,0,0,417,425,5,1,0,0,418,425,5,2,0,0,419,425,5,45,0,0,420,
        425,3,22,11,0,421,425,3,102,51,0,422,425,3,106,53,0,423,425,3,108,
        54,0,424,415,1,0,0,0,424,416,1,0,0,0,424,417,1,0,0,0,424,418,1,0,
        0,0,424,419,1,0,0,0,424,420,1,0,0,0,424,421,1,0,0,0,424,422,1,0,
        0,0,424,423,1,0,0,0,425,99,1,0,0,0,426,427,7,4,0,0,427,101,1,0,0,
        0,428,431,5,43,0,0,429,431,3,106,53,0,430,428,1,0,0,0,430,429,1,
        0,0,0,431,432,1,0,0,0,432,433,5,40,0,0,433,434,3,104,52,0,434,435,
        5,41,0,0,435,103,1,0,0,0,436,437,3,82,41,0,437,438,5,42,0,0,438,
        439,3,104,52,0,439,442,1,0,0,0,440,442,3,82,41,0,441,436,1,0,0,0,
        441,440,1,0,0,0,442,105,1,0,0,0,443,444,5,43,0,0,444,445,5,38,0,
        0,445,446,3,78,39,0,446,447,5,39,0,0,447,107,1,0,0,0,448,449,5,38,
        0,0,449,450,3,82,41,0,450,451,5,39,0,0,451,109,1,0,0,0,35,117,122,
        128,158,165,173,180,192,196,203,212,217,222,226,242,253,259,267,
        283,296,318,335,342,346,353,360,370,381,392,398,403,412,424,430,
        441
    ]

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
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

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
        self.checkVersion("4.13.1")
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




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.variable_decl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.function_decl()
                pass
            elif token in [46]:
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




    def type_list(self):

        localctx = ZCodeParser.Type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.parameter_prime()
                pass
            elif token in [39]:
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




    def nullable_vardecl_expr(self):

        localctx = ZCodeParser.Nullable_vardecl_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_nullable_vardecl_expr)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.ASSIGN)
                self.state = 215
                self.expression()
                pass
            elif token in [46]:
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




    def nullable_newline(self):

        localctx = ZCodeParser.Nullable_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_nullable_newline)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.atleast_newline()
                pass
            elif token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 43]:
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




    def block_body(self):

        localctx = ZCodeParser.Block_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block_body)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.statement()
                self.state = 331
                self.atleast_newline()
                self.state = 332
                self.block_body()
                pass
            elif token in [19]:
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




    def expression_prime(self):

        localctx = ZCodeParser.Expression_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression_prime)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 21, 24, 25, 38, 40, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.expression()
                pass
            elif token in [39, 42]:
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
                    if not(_la==22 or _la==23):
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
                    if not(_la==24 or _la==25):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
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




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expression6)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(ZCodeParser.NOT)
                self.state = 396
                self.expression6()
                pass
            elif token in [1, 2, 24, 25, 38, 40, 43, 44, 45]:
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




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 401
                self.expression7()
                pass
            elif token in [1, 2, 38, 40, 43, 44, 45]:
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




    def relational_sign(self):

        localctx = ZCodeParser.Relational_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_relational_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 171261820928) != 0)):
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
         




