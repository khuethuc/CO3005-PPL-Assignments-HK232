from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


class Val(ABC):
    pass
class Index(Val):
    def __init__(self, value):
        self.value = value
class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readNumber", MType(list(), NumberType()), CName(self.libName)),
                Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)




class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.emit = Emitter(path)
        self.libName = "ZCodeClass"
        self.varDecl = {}
        self.funcDecl = {}
        self.clinit = {}

    def visitClassDecl(self, ast, o):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return o

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def findSymbol(self, obj, env):
        name: str = None
        if type(obj) is Id or type(obj) is Frame:
            name: str = obj.name
        elif type(obj) is CallExpr or type(obj) is CallStmt:
            name: str = obj.name.name
        for e in env[::-1]:
            for sym in e:
                if sym.name == name:
                    return sym
    # # # # # PROGRAM, DECLARATIONS, AND SUPPORT FUNCTIONS # # # # #
    def visitProgram(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(self.libName, ""))
        subBody = SubBody(None, self.env)

        for decl in ast.decl:
            self.visit(decl, subBody)

        for code in self.varDecl.values():
            if code:
                self.emit.printout(code)

        self.emit.printout(""" 
                                                                      
.method public static concatString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
  .limit stack 2
  .limit locals 3
  0: new java/lang/StringBuilder
  3: dup
  4: invokespecial java/lang/StringBuilder/<init>()V
  7: astore_2
  8: aload_2
  9: aload_0
  10: invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
  13: aload_1
  14: invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
  17: pop
  18: aload_2
  19: invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
  22: areturn
.end method   
                                              
""")

        for code in self.funcDecl.values():
            self.emit.printout(code)

        if self.clinit:
            frame = Frame(None, VoidType())
            self.emit.printout('\n.method static <clinit>()V\n')
            for name, ctx in self.clinit.items():
                code, typ = self.visit(ctx, Access(frame, self.env, False))
                self.emit.printout(code)
                self.emit.printout(self.emit.emitPUTSTATIC(self.libName + '/' + name, typ, frame))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))

        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o):
        name = ast.name.name
        if ast.varType:
            typ = ast.varType
        else:
            typ = None
        # Global variable
        if o.frame is None:
            str = self.emit.emitATTRIBUTE(name, typ, False)
            self.emit.printout(str)
            #o.sym[0].append(Symbol(name, typ, CName(self.libName)))
            return Symbol(name, typ, CName(self.className))
        # Local variable
        else:
            index = o.frame.getNewIndex()
            startLabel = o.frame.getStartLabel()
            endLabel = o.frame.getEndLabel()
            str = self.emit.emitVAR(index, name, typ, startLabel, endLabel)
            self.emit.printout(str)
            #o.sym[-1].append(Symbol(name, typ, Index(index)))
            return Symbol(name, typ, Index(index))

    def visitFuncDecl(self, ast, o):
        name = ast.name.name
        o = SubBody(Frame(name, None), o.sym)
        o.frame.enterScope(True)
        o.sym.append([])
        func_type = None
        code = ""
        symbol = None
        symName = None
        if name == 'main':
            o.frame.getNewIndex()
            func_type = MType([ArrayType([1], StringType())], VoidType())
        else:
            for p in ast.param:
                self.visit(p, o)
            pars = [Symbol(p.name.name, p.varType, Index(o.frame.getNewIndex())) for p in ast.param]
            o.sym[-1] += pars
            func_type = MType([p.mtype for p in pars], VoidType())

        #findSym = self.findSymbol(env.frame, env.sym)
        if type(o.frame) is Id or type(o.frame) is Frame:
            symName = o.frame.name
        elif type(o.frame) is CallExpr or type(o.frame) is CallStmt:
            symName = o.frame.name.name
        for env in o.sym[::-1]:
            print(type(env))
            for sym in env:
                if sym.name == symName:
                    symbol = sym
                    break

        if not symbol:
            o.sym[0].append(Symbol(name, func_type, CName(self.libName)))
        if ast.body:
            code += self.visit(ast.body, o)
            inferred_type = symbol.mtype
            if type(inferred_type.rettype) is VoidType:
                code += self.emit.emitRETURN(VoidType(), o.frame)
            code += self.emit.emitENDMETHOD(o.frame)
            code = self.emit.emitMETHOD(name, inferred_type, True, o.frame) + code
            self.funcDecl[name] = code
        o.sym.pop()
        o.frame.exitScope()


    # # # # # EXPRESSIONS # # # # #
    def visitBinaryOp(self, ast, o):
        leftCode, leftTyp = self.visit(ast.left, o)
        rightCode, rightTyp = self.visit(ast.right, o)
        returnTyp = None
        op = None
        # Get op and returnTyp
        # Arithmetic: +, -, *, /, %
        if ast.op in ['+', '-']:
            returnTyp = NumberType()
            op = self.emit.emitADDOP(ast.op, returnTyp, o.frame)
        elif ast.op in ['*', '/']:
            returnTyp = NumberType()
            op = self.emit.emitMULOP(ast.op, returnTyp, o.frame)
        elif ast.op in ['%']:
            returnTyp = NumberType()
            op = self.emit.emitMOD(o.frame)
        # Logic: and, or
        elif ast.op in ['and']:
            returnTyp = BoolType()
            op = self.emit.emitANDOP(o.frame)
        elif ast.op in ['or']:
            returnTyp = BoolType()
            op = self.emit.emitOROP(o.frame)
        # Relational: =, !=, <, >, <=, >=, == 
        elif ast.op in ['=', '!=', '<', '>', '<=', '>=', '==']:
            returnTyp = BoolType()
            op = self.emit.emitREOP(ast.op, returnTyp, o.frame)
        # Return
        return leftCode + rightCode + op, returnTyp

    def visitUnaryOp(self, ast, o):
        exprCode, exprTyp = self.visit(ast.operand, o)
        returnTyp = None
        op = None
        # not, - (sign), index operator
        if ast.op in ['not']:
            returnTyp = BoolType()
            op = self.emit.emitNOT(returnTyp, o.frame)
        elif ast.op in ['-']:
            returnTyp = NumberType()
            op = self.emit.emitNEGOP(returnTyp, o.frame)
        # Return
        return exprCode + op, returnTyp

    def visitCallExpr(self, ast, o):
        code = ""

        method = None
        if type(o.frame) is Id or type(o.frame) is Frame:
            symName = o.frame.name
        elif type(o.frame) is CallExpr or type(o.frame) is CallStmt:
            symName = o.frame.name.name
        for env in o.sym[::-1]:
            for sym in env:
                if sym.name == symName:
                    method = sym
                    break

        for i, arg in enumerate(ast.args):
            self.inter_type(arg, method.mtype.partype[i], o.sym)
            code += self.visit(arg, Access(o.frame, o.sym, False))[0]
        name = method.value.value + '/' + method.name
        code += self.emit.emitINVOKESTATIC(name, method.mtype, o.frame)  
        return code, method.mtype.rettype

    def visitId(self, ast, o):
        code = None
        typ = None
        for symbol in o.sym:
            if symbol.name == ast.name:
                typ = symbol.mtype
                index = symbol.value.value
                if o.isLeft == True:
                    if type(symbol.value) is Index:
                        code = self.emit.emitWRITEVAR(symbol.name, typ, index, o.frame)
                    else:
                        lexeme = symbol.value.value + "." + symbol.name
                        code = self.emit.emitPUTSTATIC(lexeme, typ, o.frame)
                else:
                    if type(symbol.value) is Index:
                        
                        code = self.emit.emitREADVAR(symbol.name, typ, index, o.frame)
                    else:
                        lexeme = index + "." + symbol.name
                        code = self.emit.emitGETSTATIC(lexeme, typ, o.frame)
                return code, typ
    
    def visitArrayCell(self, ast, param):
        pass
    
    # # # # # STATEMENTS # # # # #
    def visitCallStmt(self, ast, o):
        code = ""

        method = None
        if type(o.frame) is Id or type(o.frame) is Frame:
            symName = o.frame.name
        elif type(o.frame) is CallExpr or type(o.frame) is CallStmt:
            symName = o.frame.name.name
        for env in o.sym[::-1]:
            for sym in env:
                if sym.name == symName:
                    method = sym
                    break

        for i, arg in enumerate(ast.args):
            code += self.visit(arg, Access(o.frame, o.sym, False))[0]
        name = method.value.value + '/' + method.name
        code += self.emit.emitINVOKESTATIC(name, method.mtype, o.frame)  
        self.emit.printout(code)
    
    def visitBlock(self, ast, o):
        code = ""
        o.frame.enterScope(False)
        o.sym.append(list())
        # getStartLabel
        #putLabel = o.frame.getStartLabel()
        #self.emit.printout(self.emit.emitLABEL(putLabel, o.frame))
        for stmt in ast.stmt:
            code += self.visit(stmt, o)
        # getEndLabel
        #putLabel = o.frame.getEndLabel()
        #self.emit.printout(self.emit.emitLABEL(putLabel, o.frame))
        o.sym.pop()
        o.frame.exitScope()
        self.emit.printout(code)
    
    def visitIf(self, ast, o):
        """
        Generate code for expr => getNewLabel flabel => Jump to flabel if False
        => Generate code for tstmt
        """
        exprCode, exprTyp = self.visit(ast.expr, Access(o.frame, o.sym, False))
        self.emit.printout(exprCode)
        flabel = o.frame.getNewLabel()
        jumpToflabel = self.emit.emitIFFALSE(flabel, o.frame)
        self.emit.printout(jumpToflabel)
        self.visit(ast.tstmt, o)
        if ast.estmt is None:
            """ Put flabel """
            putLabel = self.emit.emitLABEL(flabel, o.frame)
            self.emit.printout(putLabel)
        else:
            """
            getNewLabel elabel => Jump to elabel => Put flabel
            => Generate code for estmt => Put elabel
            """
            elabel = o.frame.getNewLabel()
            jumpToelabel = self.emit.emitGOTO(elabel, o.frame)
            self.emit.printout(jumpToelabel)
            putLabel = self.emit.emitLABEL(flabel, o.frame)
            self.emit.printout(putLabel)
            self.visit(ast.estmt, o)
            putLabel = self.emit.emitLABEL(elabel, o.frame)
            self.emit.printout(putLabel)

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitReturn(self, ast, o):
        if ast.expr:
            exprCode, exprTyp = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(exprCode)
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))

    def visitAssign(self, ast, o):
        rightCode, rightTyp = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        leftCode, leftTyp = self.visit(ast.lhs, Access(o.frame, o.sym, True))
        if type(leftTyp) is ArrayType:
            return self.emit.emitASTORE(self.arrayCell, frame)
        else:
            return self.emit.printout(rightCode + leftCode)

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame), NumberType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.val).lower(), o.frame), BoolType()

    def visitArrayLiteral(self, ast, o):
        pass

    def visitNumberType(self, ast, o):
        return ast

    def visitBoolType(self, ast, o):
        return ast

    def visitStringType(self, ast, o):
        return ast

    def visitArrayType(self, ast, o):
        return ast