from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class VoidType(Type):
    def __str__(self):
        return "VoidType"

class ZCode(Type):
    pass

class Var(ZCode):
    def __init__(self, name, typ): 
        self.name = name
        self.typ = typ
        self.forLoop = 0

class Func(ZCode):
    def __init__(self, name, param, body = False, typ = None):
        self.name = name
        self.param = param
        self.body = body
        self.typ = typ
		
class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.io = [{
            "readNumber": Func("readNumber", [], True, NumberType()),
            "writeNumber": Func("writeNumber", [NumberType()], True, VoidType()),
            "readBool": Func("readBool", [], True, BoolType()),
            "writeBool": Func("writeBool", [BoolType()], True, VoidType()),
            "readString": Func("readString", [], True, StringType()),
            "writeString": Func("writeString", [StringType()], True, VoidType())
        }]
        self.nobodyFunction = {}
        self.forLoop = 0

    def check(self):
        self.visit(self.ast, self.io)
    
    # = = = = = Declarations = = = = = #

    def visitProgram(self, ast, o):
        o = [{}]
        o[-1] = self.io[0]
        for decl in ast.decl:
            self.visit(decl, o)
        # Error: NoDefinition
        if self.nobodyFunction:
            keylist = list(self.nobodyFunction.keys())
            raise NoDefinition(keylist[0])
        # Error: NoEntryPoint
        funcmain = False
        if "main" in o[-1]:
            if type(o[-1]["main"]) is Func and o[-1]["main"].param == [] and type(o[-1]["main"].typ) is VoidType:
                funcmain = True
                
        if funcmain == False:
            raise NoEntryPoint()
            
    def visitVarDecl(self, ast, o):
        typ = None
        eleCount = 0
        # Error: Redeclared
        if ast.name.name in o[0] and type(o[0][ast.name.name]) is Var:
            raise Redeclared(Variable(), ast.name.name)
        # Error: TypeCannotBeInferred
        if ast.varInit:
            if ast.varType is None and self.visit(ast.varInit, o) is None:
                raise TypeCannotBeInferred(ast)
        # Error TypeMismatchInStatement/Expression and infer type
        if ast.varType and ast.varInit:
            self.visit(ast.varInit, o)
            # Only LHS is ArrayType
            if type(ast.varType) is ArrayType and type(ast.varInit) is not ArrayType:
                if type(ast.varInit) is not ArrayLiteral:
                    raise TypeMismatchInStatement(ast)
                else:
                    # Check number of elements and size of array
                    if len(ast.varType.size) == 1:
                        for ele in ast.varInit.value:
                            eleCount = eleCount + 1
                            checkTyp = self.visit(ele, o)
                            if type(checkTyp) is ArrayType:
                                raise TypeMismatchInExpression(ast.varInit)
                        if eleCount != ast.varType.size[0]:
                            raise TypeMismatchInStatement(ast)
                    # Check type(varType) and type(varInit)
                    eleTyp = None
                    for ele in ast.varInit.value:
                        if self.visit(ele, o) is not None:
                            eleTyp = self.visit(ele, o)
                            break
                    if eleTyp is None:
                        for ele in ast.varInit.value:
                            o[0][ele.name].typ = ast.varType.eleType
                    else:
                        if type(eleTyp) is not type(ast.varType.eleType):
                            raise TypeMismatchInStatement(ast)
                        
            # LHS and RHS is ArrayType
            elif type(ast.varType) is ArrayType and type(ast.varInit) is ArrayType:
                if ast.varType.size != ast.varInit.size:
                    raise TypeMismatchInStatement(ast)
                elif ast.varType.eleType != ast.varInit.eleType:
                    raise TypeMismatchInStatement(ast)
            # Primitive type
            elif type(ast.varType) in [NumberType, BoolType, StringType]:
                if type(ast.varType) != type(self.visit(ast.varInit, o)):
                    if self.visit(ast.varInit, o) is None:
                        o[0][ast.varInit.name].typ = ast.varType
                    else:
                        raise TypeMismatchInStatement(ast)
        # Infer typ for assign Var
        if ast.varType is None and ast.varInit is not None:
            typ = self.visit(ast.varInit, o)
        elif ast.varType is not None and ast.varInit is None:
            typ = ast.varType
        o[0][ast.name.name] = Var(ast.name.name, typ)
    def visitFuncDecl(self, ast, o):
        flag = False
        if ast.name.name not in o[0]:
            if ast.body:
                o[0][ast.name.name] = Func(ast.name.name, [], True, None)
            else:
                o[0][ast.name.name] = Func(ast.name.name, [], False, None)
                self.nobodyFunction[ast.name.name] = []
        elif ast.name.name in o[0] and type(o[0][ast.name.name]) is Func:
            if ast.name.name not in self.nobodyFunction:
                raise Redeclared(Function(), ast.name.name)
            else:
                flag = True
                if not ast.body:
                    raise Redeclared(Function(), ast.name.name)
        newEnv = [{}] + o
        # Visit parameters
        paramNameList = []
        paramTypList = []
        for param in ast.param:
            if param.name.name in paramNameList:
                raise Redeclared(Parameter(), param.name.name)
            self.visit(param, newEnv)
            paramNameList += [newEnv[0][param.name.name].name]
            paramTypList += [newEnv[0][param.name.name].typ]
        if ast.name.name in self.nobodyFunction:
            if flag == True:
                if self.nobodyFunction[ast.name.name] != paramTypList:
                    raise Redeclared(Function(), ast.name.name)
                else:
                    del self.nobodyFunction[ast.name.name]
            else:
                self.nobodyFunction[ast.name.name] = paramTypList
        o[0][ast.name.name].param = paramTypList
        # Body and returned type
        returnList = []
        returnListStmt = []
        if ast.body:
            o[0][ast.name.name].body = True
            if type(ast.body) is Block:
                for stmt in ast.body.stmt:
                    result = self.visit(stmt, newEnv)
                    if result is not None:
                        returnList += result
                        returnListStmt += [stmt]
            else:
                result = self.visit(ast.body, newEnv)
                if result is not None:
                    returnList = result
                    returnListStmt = [ast.body]
        if returnList is not None:
            returnTypes = [type(x) for x in returnList]
            if len(set(returnTypes)) > 1:
                raise TypeMismatchInStatement(returnListStmt[-1])
            elif len(set(returnTypes)) == 1:
                o[0][ast.name.name].typ = returnList[0]
            else:
                o[0][ast.name.name].typ = VoidType()

    # = = = = = Statements = = = = = #

    def visitBlock(self, ast, o):
        newEnv = [{}] + o
        returnList = []
        for stmt in ast.stmt:
            result = self.visit(stmt, newEnv)
            if result is not None:
                returnList += result
        return returnList

    def visitIf(self, ast, o):
        returnList = []
        expr = self.visit(ast.expr, o)
        # If statement
        if expr is not None:
            if type(expr) is not BoolType and type(expr) is not VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            expr = BoolType()
        if type(self.visit(ast.thenStmt, o)) is not VoidType:
            returnList += self.visit(ast.thenStmt, [{}] + o)
        # Elif statement
        for expr, stmt in ast.elifStmt:
            if type(self.visit(expr, o)) is not BoolType:
                raise TypeMismatchInStatement(ast)
            returnList += self.visit(stmt, [{}] + o)
        # Else statement
        if ast.elseStmt:
            returnList += self.visit(ast.elseStmt, [{}] + o)
        
    def visitFor(self, ast, o):
        nameTyp = self.visit(ast.name, o)
        condExpr = self.visit(ast.condExpr, o)
        updExpr = self.visit(ast.updExpr, o)
        # Error: TypeMismatchInStatement
        # Number variable
        if nameTyp is not None:
            if type(nameTyp) is not NumberType:
                raise TypeMismatchInStatement(ast)
        else:
            nameTyp = NumberType()
        # Condition expression
        if condExpr is not None:
            if type(condExpr) is not BoolType:
                raise TypeMismatchInStatement(ast)
        else:
            condExpr = BoolType()
        # Update expression
        if updExpr is not None:
            if type(updExpr) is not NumberType:
                raise TypeMismatchInStatement(ast)
        else:
            updExpr = NumberType()
        # Visit loop
        newEnv = [{}] + o
        returnList = []
        self.forLoop += 1
        returnList += self.visit(ast.body, newEnv)
        self.forLoop -= 1
        return returnList
    
    def visitContinue(self, ast, o):
        if self.forLoop == 0:
            raise MustInLoop(ast)
        return []

    def visitBreak(self, ast, o):
        if self.forLoop == 0:
            raise MustInLoop(ast)
        return []

    def visitReturn(self, ast, o):
        if not ast.expr:
            return [VoidType()]
        else:
            if self.visit(ast.expr, o) is None:
                raise TypeCannotBeInferred(ast)
            return [self.visit(ast.expr, o)]

    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        # Error: TypeMismatchInStatement
        if type(lhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if lhs is not None and rhs is not None:
            if type(lhs) is not type(rhs):
                raise TypeMismatchInStatement(ast)
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if lhs.size != rhs.size:
                raise TypeMismatchInStatement(ast)
            elif lhs.eleType != rhs.eleType:
                raise TypeMismatchInStatement(ast)
        # Error: TypeCannotBeInferred
        if lhs is None and rhs is None:
            raise TypeCannotBeInferred(ast)
        if lhs is not None and rhs is None:
            if type(lhs) is ArrayType:
                if rhs.eleType is None:
                    rhs = lhs
                else:
                    if lhs.size != rhs.size:
                        raise TypeMismatchInStatement(ast)
                    elif lhs.eleType != rhs.eleType:
                        raise TypeMismatchInStatement(ast)
            else:
                for env in o:
                    if ast.rhs.name in env:
                        env[ast.rhs.name].typ = lhs
                        rhs = lhs
                        break
        if rhs is not None and lhs is None:
            for env in o:
                if ast.lhs.name in env:
                    env[ast.lhs.name].typ = rhs
                    lhs = rhs
                    break
        return []

    def visitCallStmt(self, ast, o):
        param = []
        foundFunction = False
        envIndex = 0
        # Get parameters
        for env in o:   
            if (ast.name.name in env and type(env[ast.name.name]) is Func):
                foundFunction = True
                param = env[ast.name.name].param
                break
            envIndex += 1
        if foundFunction == False:
            raise Undeclared(Function(), ast.name.name)
        # Get arguments
        argList = [] 
        for arg in ast.args:
            argList += [self.visit(arg, o)]
        # Num(args) != Num(param) 
        if len(argList) != len(param):
            raise TypeMismatchInStatement(ast)
        # Check type and infer type
        for i in range(len(argList)):
            if argList[i] is None and param[i] is None:
                raise TypeCannotBeInferred(ast)
            if argList[i] is not None and param[i] is not None:
                if type(argList[i]) is not type(param[i]):
                    raise TypeMismatchInStatement(ast)
            if argList[i] is not None and param[i] is None:
                if ast.name.name in o[0]:
                    o[0][ast.name.name][i].param = argList[i]
                    param[i] = argList[i]
            if param[i] is not None and argList[i] is None:
                if type(param[i]) is ArrayType:
                    argList[i] = param[i]
                else:
                    if ast.args[i].name in o[0]:
                        o[0][ast.args[i].name].typ = param[i]
                        argList[i] = param[i]
        if o[envIndex][ast.name.name].typ is None:
            o[envIndex][ast.name.name].typ = VoidType()   
        return []
    
    # = = = = = Expressions = = = = = #

    def visitId(self, ast, o):
        for env in o:
            if ast.name in env and type(env[ast.name]) is Var:
                return env[ast.name].typ
        raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast, o):
        right = self.visit(ast.right, o)
        left = self.visit(ast.left, o)
        acceptType = None
        returnType = None
        # Assign type for acceptType and returnType
        if ast.op in ['+', '-', '*', '/', '%']:
            acceptType = NumberType()
            returnType = NumberType()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            acceptType = NumberType()
            returnType = BoolType()
        elif ast.op in ['and', 'or']:
            acceptType = BoolType()
            returnType = BoolType()
        elif ast.op == '...':
            acceptType = StringType()
            returnType = StringType()
        # Infer type
        if left is None:
            o[0][ast.left.name].typ = acceptType
            left = acceptType
        if right is None:
            o[0][ast.right.name].typ = acceptType
            right = acceptType
        if left == acceptType and right == acceptType:
            return returnType
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, o):
        typ = self.visit(ast.operand, o)
        acceptType = None
        returnType = None
        # Assign type for acceptType and returnType
        if ast.op == '-':
            acceptType = NumberType()
            returnType = NumberType()
        elif ast.op == 'not':
            acceptType = BoolType()
            returnType = BoolType()
        # Infer type
        if typ is None:
            o[0][ast.operand.name].typ = acceptType
            typ = acceptType
        if typ == acceptType:
            return returnType
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, o):
        param = []
        foundFuncCall = False
        envIndex = 0
        # Get parameters
        for env in o:
            if ast.name.name in env:
                param = env[ast.name.name].param
                foundFuncCall = True
                break
            envIndex += 1
        if foundFuncCall == False:
            raise Undeclared(Function(), ast.name.name)
        # Get arguments
        argList = [] 
        for arg in ast.args:
            argList += [self.visit(arg, o)]
        # Num(args) != Num(param) 
        if len(argList) != len(param):
            raise TypeMismatchInExpression(ast)
        # Check type and infer type
        for i in range(len(argList)):
            if argList[i] is None and param[i] is None:
                raise TypeCannotBeInferred(ast)
            if argList[i] is not None and param[i] is not None:
                if type(argList[i]) is not type(param[i]):
                    raise TypeMismatchInExpression(ast)
            if argList[i] is not None and param[i] is None:
                if ast.name.name in o[0]:
                    o[envIndex][ast.name.name][i].param = argList[i]
                    param[i] = argList[i]
            if param[i] is not None and argList[i] is None:
                if type(param[i]) is ArrayType:
                    argList[i] = param[i]
                else:
                    if ast.args[i].name in o[0]:
                        o[envIndex][ast.args[i].name] = param[i]
                        argList[i] = param[i]
        if o[envIndex][ast.name.name].typ is None:
            raise TypeCannotBeInferred(ast)
        elif o[envIndex][ast.name.name].typ is VoidType:
            raise TypeMismatchInExpression(ast)
        return o[envIndex][ast.name.name].typ
    
    def visitArrayCell(self, ast, o):
        # E1[E2] -> E1: ArrayType
        arr = self.visit(ast.arr, o)
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        # E1[E2] -> E2: NumberType
        for idx in ast.idx:
            if self.visit(idx, o) is not None:
                if type(self.visit(idx, o)) is not NumberType:
                    raise TypeMismatchInExpression(ast)
            else:
                o[0][idx.name].typ = NumberType()
        # Check length
        array = o[0][ast.arr.name]
        declaredDim = array.typ.size # typ: ArrayType
        declaredTyp = array.typ.eleType # typ: ArrayType
        if len(declaredDim) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(declaredDim) > len(ast.idx):
            return ArrayType(declaredDim[len(ast.idx):], declaredTyp)
        return declaredTyp

    # = = = = = Types and Literals = = = = = #

    def visitNumberLiteral(self, ast, o):
        return NumberType()

    def visitBooleanLiteral(self, ast, o):
        return BoolType()

    def visitStringLiteral(self, ast, o):
        return StringType()

    def visitArrayLiteral(self, ast, o):
        typ = None
        # Finding the type of the nearest element
        for expr in ast.value:
            initTyp = self.visit(expr, o)
            if initTyp is not None and type(initTyp) is not ArrayType:
                typ = initTyp
                break
            elif type(initTyp) is ArrayType:
                typ = initTyp.eleType
                break
        # Case: None
        if typ is None:
            return ArrayType([0], None)
        # Case: Primitive types
        elif type(typ) in [StringType, BoolType, NumberType]:
            for expr in ast.value:
                exprTyp = self.visit(expr, o)
                if exprTyp is not None:
                    if type(typ) != type(exprTyp):
                        raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)], typ)
        # Case: ArrayType
        else:
            innerDim = self.visitArrayLiteral(ast.value[0], o).size
            innerTyp = self.visitArrayLiteral(ast.value[0], o).eleType
            for expr in ast.value:
                if type(self.visit(expr, o)) != innerTyp:
                    raise TypeMismatchInExpression(ast)
            return ArrayType([len(ast.value)] + innerDim, innerTyp)

    def visitNumberType(self, ast, o):
        return ast

    def visitBoolType(self, ast, o):
        return ast

    def visitStringType(self, ast, o):
        return ast

    def visitArrayType(self, ast, o):
        return ast
