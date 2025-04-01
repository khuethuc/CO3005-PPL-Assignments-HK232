from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Var:
    def __init__(self, name, typ) -> None:
        self.name = name
        self.typ = typ

    def __str__(self):
        return f"{str(self.name)}({str(self.typ)})"


class Func:
    def __init__(self, name, param, typ, body=None) -> None:
        self.name = name
        self.param = param
        self.typ = typ
        self.body = body

    def __str__(self):
        params = ""
        for x in self.param:
            params = params + str(x)
        return f"{str(self.name)}[{params}]({str(self.body)}) -> {str(self.typ)} "


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ctx):
        self.ctx = ctx
        self.noEntryPoint = True
        self.isCalled = False
        self.inferred = False
        self.inLoop = []
        self.returnType = None
        self.nobody = []
        self.hasReturn = False
        self.returnList = []
        self.arrayLiteral = []
        self.currentFunction = None
        
        self.o = [
            [
                Func("readNumber", [], NumberType(), []),
                Func("readBool", [], BoolType(), []),
                Func("readString", [], StringType(), []),
                Func("writeNumber", [Var("arg", NumberType())], VoidType(), []),
                Func("writeBool", [Var("arg", BoolType())], VoidType(), []),
                Func("writeString", [Var("arg", StringType())], VoidType(), []),
            ]
        ]

        
        

    def infer(self, expr, typ, o):
        if type(expr) is Id:
            for sym in o:
                id_sym = self.lookup(expr.name, sym, lambda x: x.name)
                if id_sym is not None and type(id_sym) is Var:
                    id_sym.typ = typ
                    self.inferred = True
                    return

        elif type(expr) in [CallStmt, CallExpr]:
            for idx in range(len(o[-1])):
                func_sym = o[-1][idx]
                if (
                    type(func_sym) is Func
                    and func_sym.name == expr.name.name
                    and func_sym.typ is None
                ):
                    func_sym.typ = typ
                    self.isCalled = True
                    self.visit(
                        FuncDecl(
                            Id(func_sym.name),
                            list(
                                map(
                                    lambda x: VarDecl(Id(x.name), x.typ, None, None),
                                    func_sym.param,
                                )
                            ),
                            func_sym.body,
                        ),
                        o,
                    )
                    self.isCalled = False
                    o[-1][idx] = func_sym
                    self.inferred = True
                    return

        elif type(expr) is ArrayCell:
            self.inferred = True
            if type(typ) is not ArrayType:
                self.infer(expr.arr, ArrayType([1] * len(expr.idx), typ), o)
            else:
                self.infer(
                    expr.arr,
                    ArrayType([1] * len(expr.idx) + typ.size, typ.eleType),
                    o,
                )

        else:
            if type(typ) is not ArrayType:
                self.inferred = False
                return
            else:
                self.inferred = True
                # Infer elements
                for val in expr.value:
                    if len(typ.size) == 1:
                        self.infer(val, typ.eleType, o)
                    else:
                        self.infer(val, ArrayType(typ.size[1:], typ.eleType), o)
                # Element check
                typ_check = expr.value[0]
                for val in expr.value:
                    if type(typ_check) is not type(val):
                        print("1")
                        raise TypeMismatchInExpression(expr)
                    if type(typ_check) is ArrayType and (
                        typ_check.size != val.size
                        or type(typ_check.eleType) is not type(val.eleType)
                    ):
                        
                        print("2")
                        raise TypeMismatchInExpression(expr)

    def check(self):
        self.visitProgram(self.ctx, self.o)

    def table_check(self, o):
        for symlst in o:
            strlst = "[\n"
            for sym in symlst:
                strlst += str(sym)
                strlst += "\n"
            strlst += "]"
            print(strlst)

    def visitProgram(self, ctx, o):
        for decl in ctx.decl:
            self.visit(decl, o)
            
        if self.nobody != []:
            raise NoDefinition(self.nobody[0].name.name)
        for func in o[0]:
            if (
                type(func) is Func
                and func.name == "main"
                and type(func.typ) is VoidType
                and func.param == []
            ):
                self.noEntryPoint = False
                break
        if self.noEntryPoint:
            raise NoEntryPoint()

    def visitVarDecl(self, ctx, o):
        var = self.lookup(ctx.name.name, o[0], lambda x: x.name)
        if var is not None and type(var) is Var:
            raise Redeclared(Variable(), ctx.name.name)

        l_type = ctx.varType
        o[0] += [Var(ctx.name.name, l_type)]
        if ctx.varInit is not None:
            r_type = self.visit(ctx.varInit, o)
            if l_type is not None and r_type is not None:
                if type(l_type) is not type(r_type):
                    raise TypeMismatchInStatement(ctx)
                if type(l_type) is ArrayType:
                    if l_type.size[: len(r_type.size)] != r_type.size:
                        raise TypeMismatchInStatement(ctx)
                    if r_type.eleType is None:
                        self.infer(ctx.varInit, l_type, o)
                        if self.inferred == False:
                            raise TypeCannotBeInferred(ctx)
                    else:
                        if type(r_type.eleType) is not type(l_type.eleType):
                            
                            raise TypeMismatchInStatement(ctx)

            else:
                if r_type is None:
                    if l_type is None:
                        
                        raise TypeCannotBeInferred(ctx)
                    else:
                        if type(ctx.varInit) in [Id, CallExpr, ArrayLiteral, ArrayCell]:
                            self.infer(ctx.varInit, l_type, o)
                            if self.inferred == False:
                                raise TypeCannotBeInferred(ctx)
                        else:
                            raise TypeCannotBeInferred(ctx)
                else:
                    for varsym in o[0]:
                        if varsym.name == ctx.name.name and type(varsym) is Var:
                            varsym.typ = r_type
        self.arrayLiteral = []

    def visitFuncDecl(self, ctx, o):
        func = self.lookup(ctx.name.name, o[-1], lambda x: x.name)
        
        # if func is not None and self.isCalled == False:
        #     if func.body is not None or ctx.body is None:
        #         raise Redeclared(Function(), ctx.name.name)
            
        if func is not None and ctx.body is None and self.isCalled == False:
            #print("func 1")    
            
            raise Redeclared(Function(), ctx.name.name)
            
        params = []
        for param in ctx.param:
            if self.lookup(param.name.name, params, lambda x: x.name) is not None:
                #print(o[-1])
                raise Redeclared(Parameter(), param.name.name)
            params += [Var(param.name.name, self.visit(param.varType, o))]
        o = [params] + o

        if ctx.body is None:
            if self.isCalled == False and ctx not in self.nobody:
                self.nobody += [ctx]
                o[-1] += [Func(ctx.name.name, params, None, None)]
                
        else:
            self.currentFunction = ctx.name.name
            for f in self.nobody:
                if f.name.name == ctx.name.name:
                    self.nobody.remove(f)

            func_found = False
            for idx in range(len(o[-1])):
                func_sym = o[-1][idx]
                if type(func_sym) is Func and func_sym.name == ctx.name.name:
                    func_found = True

                    if func_sym.body is not None:
                        #print("func 2")    
                        raise Redeclared(Function(), ctx.name.name)

                    if len(func_sym.param) != len(params):
                        #print("func 3")    
                        raise Redeclared(Function(), ctx.name.name)

                    for param_idx in range(len(params)):
                        l_type = func_sym.param[param_idx].typ
                        r_type = params[param_idx].typ

                        if type(l_type) is not type(r_type):
                            #print("func 4")    
                            raise Redeclared(Function(), ctx.name.name)

                        if type(l_type) is ArrayType and (
                            l_type.size != r_type.size
                            or type(r_type.eleType) is not type(l_type.eleType)
                        ):
                            #print("6")
                            raise TypeMismatchInStatement(ctx)

                    self.visit(ctx.body, o)

                    func_sym.typ = (
                        self.returnType
                        if self.returnType
                        else (VoidType() if self.returnList == [] else None)
                    )
                    func_sym.body = ctx.body
                    o[-1][idx] = func_sym
                    break

            if not func_found:
                o[-1] += [Func(ctx.name.name, params, self.returnType, ctx.body)]
                self.visit(ctx.body, o)
                ret_type = (
                    self.returnType
                    if self.returnType
                    else (VoidType() if self.returnList == [] else None)
                )
                if o[-1][-1].typ is None:
                    o[-1][-1] = Func(ctx.name.name, params, ret_type, ctx.body)
        self.returnType = None
        self.hasReturn = False
        o = o[1:]
        self.returnList = []


    def visitArrayLiteral(self, ctx,o):
        value = [self.visit(x, o) for x in ctx.value]
        if len(value) == 0:
            return ArrayType([0], None)


        ele_type = value[0] if type(value[0]) is not ArrayType else value[0].eleType
        current_array_size = [len(value)]
        if type(value[0]) is not ArrayType:
            for val in value:
                if type(val) is not type(ele_type):
                    raise TypeMismatchInExpression(ctx)
        else:
            num_dim = len(value[0].size)
            for val in value:
                if val.eleType != ele_type or (len(val.size) != num_dim):
                    raise TypeMismatchInExpression(ctx)
            for idx in range(num_dim):
                current_array_size.append(max(current_array_size[idx], val.size[idx]))
                    

        return ArrayType(current_array_size, ele_type)

    def visitBinaryOp(self, ctx, o):
        l_type = self.visit(ctx.left, o)
        r_type = self.visit(ctx.right, o)
        if ctx.op in ["+", "-", "*", "/", "%", "=", "!=", "<", ">", "<=", ">="]:
            if l_type is None:
                if type(ctx.left) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.left, NumberType(), o)
                if self.inferred == False:
                    return None
                l_type = NumberType()
            if r_type is None:
                if type(ctx.right) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.right, NumberType(), o)
                if self.inferred == False:
                    return None
                r_type = NumberType()
            if type(l_type) is not NumberType or type(r_type) is not NumberType:
                #print("7")
                raise TypeMismatchInExpression(ctx)
            return NumberType() if ctx.op in ["+", "-", "*", "/", "%"] else BoolType()

        elif ctx.op in ["and", "or"]:
            if l_type is None:
                if type(ctx.left) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.left, BoolType(), o)
                if self.inferred == False:
                    return None
                l_type = BoolType()
            if r_type is None:
                if type(ctx.right) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.right, BoolType(), o)
                if self.inferred == False:
                    return None
                r_type = BoolType()
                
            if type(l_type) is not BoolType or type(r_type) is not BoolType:
                print("8")
                raise TypeMismatchInExpression(ctx)
            return BoolType()

        else:
            if l_type is None:
                if type(ctx.left) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.left, StringType(), o)
                if self.inferred == False:
                    return None
                l_type = StringType()
            if r_type is None:
                if type(ctx.right) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.right, StringType(), o)
                if self.inferred == False:
                    return None
                r_type = StringType()
            if type(l_type) is not StringType or type(r_type) is not StringType:
                raise TypeMismatchInExpression(ctx)
            return StringType() if ctx.op == "..." else BoolType()


    def visitUnaryOp(self, ctx: UnaryOp, o):
        expr_type = self.visit(ctx.operand, o)
        if ctx.op == "-":
            if expr_type is None:
                if type(ctx.operand) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.operand, NumberType(), o)
                if self.inferred == False:
                    return None
                return NumberType()
            else:
                if type(expr_type) is not NumberType:
                    raise TypeMismatchInExpression(ctx)
            return NumberType()

        else:
            if expr_type is None:
                if type(ctx.operand) not in [Id, CallExpr, ArrayCell]:
                    return None
                self.infer(ctx.operand, BoolType(), o)
                if self.inferred == False:
                    return None
                return BoolType()
            else:
                if type(expr_type) is not BoolType:
                    raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitCallExpr(self, ctx: CallExpr, o):
        if self.currentFunction is not None and ctx.name.name == self.currentFunction:
            raise TypeMismatchInExpression(ctx)

        self.inferred = False
        local_o = o[:-1]
        for para in local_o:
            if self.lookup(ctx.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInExpression(ctx)

        found = self.lookup(ctx.name.name, o[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not Func):
            raise Undeclared(Function(), ctx.name.name)

        if type(found.typ) is VoidType:
            raise TypeMismatchInExpression(ctx)
        if len(ctx.args) != len(found.param):
            raise TypeMismatchInExpression(ctx)

        for idx in range(len(ctx.args)):
            arg_typ = self.visit(ctx.args[idx], o)
            if arg_typ is None:
                if type(ctx.args[idx]) not in [Id, CallExpr, ArrayLiteral]:
                    return None
                self.infer(ctx.args[idx], found.param[idx].typ, o)
                if self.inferred == False:
                    return None
                arg_typ = found.param[idx].typ
            else:
                if type(arg_typ) is not type(found.param[idx].typ):
                    raise TypeMismatchInExpression(ctx)
                if type(arg_typ) is ArrayType:
                    if (
                        arg_typ.size[: len(found.param[idx].typ.size)]
                        != found.param[idx].typ.size
                    ):
                        raise TypeMismatchInExpression(ctx)
                    if arg_typ.eleType is None:
                        if type(ctx.value) not in [Id, CallExpr, ArrayLiteral]:
                            return None
                        self.infer(ctx.value, found.param[idx].typ, o)
                        if self.inferred == False:
                            return None
                        arg_typ = found.param[idx].typ
                    if (
                        type(arg_typ.eleType) is not type(found.param[idx].typ.eleType)
                        or arg_typ.size != found.param[idx].typ.size
                    ):
                        raise TypeMismatchInExpression(ctx)
        return found.typ

    # name: str
    def visitId(self, ctx: Id, o):
        # Find Id in the o
        self.inferred = False
        for sym in o:
            varsym = self.lookup(ctx.name, sym, lambda x: x.name)
            if varsym is not None and type(varsym) is Var:
                return varsym.typ
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx: ArrayCell, o):
        self.inferred = True
        arr_typ = self.visit(ctx.arr, o)
        if arr_typ is None:
            self.inferred = False
            return None
        if type(arr_typ) is not ArrayType or len(arr_typ.size) < len(ctx.idx):
            raise TypeMismatchInExpression(ctx)

        for cell in ctx.idx:
            typ = self.visit(cell, o)
            if typ is None:
                if type(cell) not in [Id, CallExpr]:
                    return None
                self.infer(cell, NumberType(), o)
                if self.inferred == False:
                    return None
                typ = NumberType()
            if type(typ) is not NumberType:
                raise TypeMismatchInExpression(ctx)
        if len(arr_typ.size) == len(ctx.idx):
            return arr_typ.eleType
        return ArrayType(arr_typ.size[len(ctx.idx) :], arr_typ.eleType)

    def visitBlock(self, ctx, o):
        o = [[]] + o
        for stmt in ctx.stmt:
            self.visit(stmt, o)
        self.hasReturn = False
        o = o[1:]
        self.arrayLiteral = []

    def visitIf(self, ctx, o):
        cond_typ = self.visit(ctx.expr, o)
        if cond_typ is None:
            if type(ctx.expr) not in [Id, CallExpr, ArrayLiteral]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.expr, BoolType(), o)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            cond_typ = BoolType()
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt, o)
        self.hasReturn = False
        for elif_expr, elif_stmt in ctx.elifStmt:
            cond_typ = self.visit(elif_expr, o)
            if cond_typ is None:
                if type(elif_expr) not in [Id, CallExpr]:
                    raise TypeCannotBeInferred(ctx)
                self.infer(elif_expr, BoolType(), o)
                if self.inferred == False:
                    raise TypeCannotBeInferred(ctx)
                cond_typ = BoolType()
            if type(cond_typ) is not BoolType:
                raise TypeMismatchInStatement(ctx)
            self.visit(elif_stmt, o)
        if ctx.elseStmt:
            self.visit(ctx.elseStmt, o)
        self.arrayLiteral = []


    def visitFor(self, ctx, o):
        self.inLoop = [1]
        itr = self.visit(ctx.name, o)
        if itr is None:
            self.infer(ctx.name, NumberType(), o)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            itr = NumberType()
        if type(itr) is not NumberType:
            raise TypeMismatchInStatement(ctx)

        cond_typ = self.visit(ctx.condExpr, o)
        if cond_typ is None:
            if type(ctx.condExpr) not in [Id, CallExpr]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.condExpr, BoolType(), o)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            cond_typ = BoolType()
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ctx)

        update_typ = self.visit(ctx.updExpr, o)
        if update_typ is None:
            if type(ctx.updExpr) not in [Id, CallExpr]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.updExpr, NumberType(), o)
            if self.inferred == False:
                raise TypeCannotBeInferred(ctx)
            update_typ = NumberType()
        if type(update_typ) is not NumberType:
            raise TypeMismatchInStatement(ctx)

        self.visit(ctx.body, o)
        self.arrayLiteral = []
        self.inLoop = self.inLoop[:-1]

    def visitContinue(self, ctx: Continue, o):
        if self.inLoop == []:
            return MustInLoop(ctx)
        self.arrayLiteral = []

    def visitBreak(self, ctx: Break, o):
        if self.inLoop == []:
            return MustInLoop(ctx)
        self.arrayLiteral = []

    def visitReturn(self, ctx, o):
        if self.hasReturn:
            return
        self.hasReturn = True
        func = self.lookup(self.currentFunction, o[-1], lambda x: x.name)
        # if VoidType()
        if ctx.expr is None:
            if func.typ is not None and type(func.typ) is not VoidType:
                #print("aaaaa")
                raise TypeMismatchInStatement(ctx)
            self.returnType = VoidType()
            
        else:
            ret_type = self.visit(ctx.expr, o)
            if func.typ is None:
                if ret_type is None:
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                    self.returnList += [ctx]
            
                else:
                    self.returnType = ret_type
                    func.typ = ret_type
                    while self.returnList != []:
                        if type(self.returnList[0].expr) not in [
                            Id,
                            CallExpr,
                            ArrayLiteral,
                        ]:
                            raise TypeCannotBeInferred(self.returnList[0])
                        self.infer(self.returnList[0], ret_type, o)
                        if self.inferred == False:
                            raise TypeCannotBeInferred(ctx)
                        self.returnList = self.returnList[1:]
            else:
                if type(func.typ) is VoidType:
                    #print("bbbb")
                    raise TypeMismatchInStatement(ctx)
                if ret_type is None:
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                    if type(ctx.expr) not in [Id, CallExpr, ArrayLiteral]:
                        raise TypeCannotBeInferred(ctx)
                    self.infer(ctx.expr, func.typ, o)
                    if self.inferred == False:
                        raise TypeCannotBeInferred(ctx)
                else:
                    if type(func.typ) is not type(ret_type):
                        #print("cccc")
                        raise TypeMismatchInStatement(ctx)
                if type(func) is ArrayType:
                    if func.size[: len(ret_type.size)] != ret_type.size:
                        #print("dddd")
                        raise TypeMismatchInStatement(ctx)
                    if func.eleType is None:
                        if type(ctx.value) not in [Id, CallExpr, ArrayLiteral]:
                            return None
                        self.infer(ctx.value, ret_type, o)
                        if self.inferred == False:
                            return None
                        func = ret_type
                    if (
                        type(func.eleType) is not type(ret_type.eleType)
                        or func.size != ret_type.size
                    ):
                        #print("eeee")
                        raise TypeMismatchInStatement(ctx)
        self.arrayLiteral = []

    def visitAssign(self, ctx: Assign, o):
        r_type, l_type = self.visit(ctx.rhs, o), self.visit(ctx.lhs, o)
        if r_type is None and l_type is None:
            raise TypeCannotBeInferred(ctx)
        if r_type is not None and l_type is None:
            if type(ctx.lhs) not in [Id, ArrayCell]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.lhs, r_type, o)
            if not self.inferred:
                raise TypeCannotBeInferred(ctx)
        elif r_type is None and l_type is not None:
            if type(ctx.rhs) not in [Id, CallExpr, ArrayLiteral, ArrayCell]:
                raise TypeCannotBeInferred(ctx)
            self.infer(ctx.rhs, l_type, o)
            if not self.inferred:
                raise TypeCannotBeInferred(ctx)
        else:
            if type(r_type) is VoidType:
                raise TypeMismatchInStatement(ctx)
            if type(l_type) is not type(r_type):
                raise TypeMismatchInStatement(ctx)
            if type(l_type) is ArrayType:
                if l_type.size[: len(r_type.size)] != r_type.size:
                    raise TypeMismatchInStatement(ctx)
                if r_type.eleType is None:
                    if type(ctx.rhs) not in [Id, CallExpr, ArrayLiteral]:
                        raise TypeCannotBeInferred(ctx)
                    self.infer(ctx.rhs, r_type, o)
                    if not self.inferred:
                        raise TypeCannotBeInferred(ctx)
                    r_type = l_type
                else:
                    if (
                        type(r_type.eleType) is not type(l_type.eleType)
                        or l_type.size != r_type.size
                    ):
                        raise TypeMismatchInStatement(ctx)
        self.arrayLiteral = []


    def visitCallStmt(self, ctx: CallStmt, o):
        self.inferred = False
        local_o = o[:-1]
        for para in local_o:
            if self.lookup(ctx.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInStatement(ctx)

        found = self.lookup(ctx.name.name, o[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not Func):
            raise Undeclared(Function(), ctx.name.name)

        if found.typ is not None and type(found.typ) is not VoidType:
            raise TypeMismatchInStatement(ctx)

        if len(ctx.args) != len(found.param):
            raise TypeMismatchInStatement(ctx)

        for idx in range(len(ctx.args)):
            arg_typ = self.visit(ctx.args[idx], o)
            if arg_typ is None:
                if type(ctx.args[idx]) not in [Id, CallExpr, ArrayLiteral]:
                    return None
                self.infer(ctx.args[idx], found.param[idx].typ, o)
                if self.inferred == False:
                    return None
                arg_typ = found.param[idx].typ
            else:
                if type(arg_typ) is not type(found.param[idx].typ):
                    raise TypeMismatchInStatement(ctx)
                if type(arg_typ) is ArrayType:
                    if (
                        arg_typ.size[: len(found.param[idx].typ.size)]
                        != found.param[idx].typ.size
                    ):
                        raise TypeMismatchInStatement(ctx)
                    if arg_typ.eleType is None:
                        if type(ctx.value) in [Id, CallExpr, ArrayLiteral]:
                            self.infer(ctx.value, found.param[idx].typ, o)
                            if self.inferred == False:
                                return None
                            arg_typ = found.param[idx].typ
                        return None
                    if (
                        type(arg_typ.eleType) is not type(found.param[idx].typ.eleType)
                        or arg_typ.size != found.param[idx].typ.size
                    ):
                        raise TypeMismatchInStatement(ctx)
        if found.typ is None:
            self.infer(ctx, VoidType(), o)
        self.arrayLiteral = []


    def visitArrayLiteral(self, ctx: ArrayLiteral, o):
        if ctx not in self.arrayLiteral:
            self.arrayLiteral += [ctx]

        typ = None
        for val in ctx.value:
            typ = self.visit(val, o)
            if typ is not None:
                break

        if typ is not None:
            for val in ctx.value:
                val_typ = self.visit(val, o)
                if val_typ is None:
                    if type(val) not in [Id, CallExpr, ArrayLiteral]:
                        return None
                    self.infer(val, typ, o)
                    if self.inferred == False:
                        return None
                    val_typ = typ
                if type(val_typ) is not type(typ):
                    raise TypeMismatchInExpression(self.arrayLiteral[0])
                if type(val_typ) is ArrayType:
                    if val_typ.size[: len(typ.size)] != typ.size:
                        raise TypeMismatchInExpression(self.arrayLiteral[0])
                    if val_typ.eleType is None:
                        if type(ctx.value) not in [Id, CallExpr, ArrayLiteral]:
                            return None
                        self.infer(ctx.value, typ, o)
                        if self.inferred == False:
                            return None
                        val_typ = typ
                    if (
                        type(val_typ.eleType) is not type(typ.eleType)
                        or val_typ.size != typ.size
                    ):
                        raise TypeMismatchInExpression(self.arrayLiteral[0])

            if type(typ) is not ArrayType:
                self.arrayLiteral = self.arrayLiteral[:-1]
                return ArrayType([len(ctx.value)], typ)
            self.arrayLiteral = self.arrayLiteral[:-1]
            return ArrayType([len(ctx.value)] + typ.size, typ.eleType)


    def visitNumberLiteral(self, ctx: NumberLiteral, o):
        return NumberType()

    def visitBooleanLiteral(self, ctx: BooleanLiteral, o):
        return BoolType()

    def visitStringLiteral(self, ctx: StringLiteral, o):
        return StringType()
    
    def visitNumberType(self, ctx: NumberType, o):
        return NumberType()

    def visitBoolType(self, ctx: BoolType, o):
        return BoolType()

    def visitStringType(self, ctx: StringType, o):
        return StringType()