from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
from functools import reduce


class ASTGeneration(ZCodeVisitor):
    # # # = = = = = PROGRAM = = = = = # # #
    # program: declare_list EOF;
    #   declare_list: declaration declare_list | declaration;
    #       declaration: variable_decl | function_decl | NEWLINE;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(list(filter(None, self.visit(ctx.declare_list()))))
    def visitDeclare_list(self, ctx: ZCodeParser.Declare_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declaration())]
        return [self.visit(ctx.declaration())] + self.visit(ctx.declare_list())
    def visitDeclaration(self, ctx: ZCodeParser.DeclarationContext):
        if ctx.variable_decl():
            return self.visit(ctx.variable_decl())
        elif ctx.function_decl():
            return self.visit(ctx.function_decl())
        return None

    # # # = = = = = VARIABLES DECLARATION = = = = = # # #
    # variable_decl: (var | dynamic | normal_type | array_type) atleast_newline;
    def visitVariable_decl(self, ctx: ZCodeParser.Variable_declContext):
        if ctx.var():
            return self.visit(ctx.var())
        elif ctx.dynamic():
            return self.visit(ctx.dynamic())
        elif ctx.normal_type():
            return self.visit(ctx.normal_type())
        return self.visit(ctx.array_type())
    # var: VAR IDENTIFIER ASSIGN expression;
    def visitVar(self, ctx: ZCodeParser.VarContext):
        id = Id(ctx.IDENTIFIER().getText())
        init = self.visit(ctx.expression())
        return VarDecl(id, None, 'var', init)
    # dynamic: DYNAMIC IDENTIFIER nullable_vardecl_expr;
    #   nullable_vardecl_expr: ASSIGN expression | ;
    def visitDynamic(self, ctx: ZCodeParser.DynamicContext):
        id = Id(ctx.IDENTIFIER().getText())
        varInit = self.visit(ctx.nullable_vardecl_expr())
        return VarDecl(id, None, 'dynamic', varInit)
    def visitNullable_vardecl_expr(self, ctx: ZCodeParser.Nullable_vardecl_exprContext):
        if ctx.ASSIGN():
            return self.visit(ctx.expression())
        return None
    # normal_type: type_list IDENTIFIER nullable_vardecl_expr;
    #   type_list: NUMBER | BOOLEAN | STRING;
    def visitNormal_type(self, ctx: ZCodeParser.Normal_typeContext):
        id = Id(ctx.IDENTIFIER().getText())
        type = self.visit(ctx.type_list())
        varInit = self.visit(ctx.nullable_vardecl_expr())
        return VarDecl(id, type, None, varInit)
    def visitType_list(self, ctx: ZCodeParser.Type_listContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOLEAN():
            return BoolType()
        return StringType()
        
    # array_type: type_list IDENTIFIER OPEN_SQUARE_BRACKET size CLOSE_SQUARE_BRACKET array_rhs;
    #   size: NUMBER_LITERAL COMMA size | NUMBER_LITERAL;
    #   array_rhs: ASSIGN array_literal | ASSIGN expression | ;
    #       array_literal: OPEN_SQUARE_BRACKET array_elements CLOSE_SQUARE_BRACKET;
    #           array_elements: one_element | multiple_elements;
    #               one_element: expression COMMA one_element | expression;
    #               multiple_elements: OPEN_SQUARE_BRACKET one_element CLOSE_SQUARE_BRACKET COMMA multiple_elements | OPEN_SQUARE_BRACKET one_element CLOSE_SQUARE_BRACKET;
    def visitArray_type(self, ctx: ZCodeParser.Array_typeContext):
        id = Id(ctx.IDENTIFIER().getText())
        size = self.visit(ctx.size())
        type = self.visit(ctx.type_list())
        arr_type = ArrayType(size, type)
        initVar = self.visit(ctx.array_rhs())
        return VarDecl(id, arr_type, None, initVar)
    def visitSize(self, ctx: ZCodeParser.SizeContext):
        if ctx.size():
            return [float(ctx.NUMBER_LITERAL().getText())] + self.visit(ctx.size())
        return [float(ctx.NUMBER_LITERAL().getText())]
    def visitArray_rhs(self, ctx: ZCodeParser.Array_rhsContext):
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None
    def visitArray_literal(self, ctx: ZCodeParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.array_elements()))
    def visitArray_elements(self, ctx: ZCodeParser.Array_elementsContext):
        if ctx.one_element():
            return self.visit(ctx.one_element())
        return self.visit(ctx.multiple_elements())
    def visitOne_element(self, ctx: ZCodeParser.One_elementContext):
        if ctx.one_element():
            return [self.visit(ctx.expression())] + self.visit(ctx.one_element())
        return [self.visit(ctx.expression())]
    def visitMultiple_elements(self, ctx: ZCodeParser.Multiple_elementsContext):
        if ctx.multiple_elements():
            return self.visit(ctx.one_element()) + self.visit(ctx.multiple_elements())
        return self.visit(ctx.one_element())
    
    # parameter_list: parameter_prime | ;
    #   parameter_prime: parameter COMMA parameter_prime| parameter;
    #       parameter: type_list (IDENTIFIER | IDENTIFIER OPEN_SQUARE_BRACKET size CLOSE_SQUARE_BRACKET);
    def visitParameter_list(self, ctx: ZCodeParser.Parameter_listContext):
        if ctx.parameter_prime():
            return self.visit(ctx.parameter_prime())
        return []
    def visitParameter_prime(self, ctx: ZCodeParser.Parameter_primeContext):
        if ctx.parameter_prime():
            return [self.visit(ctx.parameter())] + self.visit(ctx.parameter_prime())
        return [self.visit(ctx.parameter())]
    def visitParameter(self, ctx: ZCodeParser.ParameterContext):
        if ctx.size():
            id = Id(ctx.IDENTIFIER().getText())
            size = self.visit(ctx.size())
            type = self.visit(ctx.type_list())
            arr_type = ArrayType(size, type)
            return VarDecl(id, arr_type, None, None)
        else:
            id = Id(ctx.IDENTIFIER().getText())
            type = self.visit(ctx.type_list())
            return VarDecl(id, type, None, None)
        
    # # # = = = = = NEWLINE DECLARATION = = = = = # # #
    # atleast_newline: NEWLINE atleast_newline | NEWLINE;
    def visitAtleast_newline(self, ctx: ZCodeParser.Atleast_newlineContext):
        return None
    # nullable_newline: atleast_newline | ;
    def visitNullable_newline(self, ctx: ZCodeParser.Nullable_newlineContext):
        return None

    # # # = = = = = FUNCTION DECLARATION = = = = = # # #
    # function_decl: FUNC IDENTIFIER OPEN_ROUND_BRACKET parameter_list CLOSE_ROUND_BRACKET function_body;
    def visitFunction_decl(self, ctx: ZCodeParser.Function_declContext):
        id = Id(ctx.IDENTIFIER().getText())
        param = self.visit(ctx.parameter_list())
        body = self.visit(ctx.function_body())
        return FuncDecl(id, param, body)
    # function_body: atleast_newline | nullable_newline return_stmt | nullable_newline block_stmt;
    def visitFunction_body(self, ctx: ZCodeParser.Function_bodyContext):
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        return None

    # # # = = = = = STATEMENT = = = = = # # #
    # statement: variable_decl_stmt | assignment_stmt | break_stmt | if_stmt | for_stmt | continue_stmt | return_stmt | function_call_stmt | block_stmt;
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))
    # variable_decl_stmt: var | dynamic | normal_type | array_type;
    def visitVariable_decl_stmt(self, ctx: ZCodeParser.Variable_decl_stmtContext):
        return self.visit(ctx.getChild(0))
    # assignment_stmt: assignment_type ASSIGN expression;
    #   assignment_type: IDENTIFIER | index_operators_expr;
    def visitAssignment_stmt(self, ctx: ZCodeParser.Assignment_stmtContext):
        lhs = self.visit(ctx.assignment_type())
        expr = self.visit(ctx.expression())
        return Assign(lhs, expr)
    def visitAssignment_type(self, ctx: ZCodeParser.Assignment_typeContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.index_operators_expr())

    # if_stmt: IF OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET nullable_newline statement elif_list else_list;
    #     elif_list: atleast_newline elif_part elif_list | ;
    #         elif_part: ELIF OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET nullable_newline statement; 
    #     else_list: atleast_newline else_part | ;
    #         else_part: ELSE nullable_newline statement;
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.statement())
        elifStmt = self.visit(ctx.elif_list())
        elseStmt = self.visit(ctx.else_list())
        return If(expr, thenStmt, elifStmt, elseStmt)
    def visitElif_list(self, ctx: ZCodeParser.Elif_listContext):
        if ctx.elif_part():
            return [self.visit(ctx.elif_part())] + self.visit(ctx.elif_list())
        return []
    def visitElif_part(self, ctx: ZCodeParser.Elif_partContext):
        return (self.visit(ctx.expression()), self.visit(ctx.statement())) # tuple
    def visitElse_list(self, ctx: ZCodeParser.Else_listContext):
        if ctx.else_part():
            return self.visit(ctx.else_part())
        return None
    def visitElse_part(self, ctx: ZCodeParser.Else_partContext):
        return self.visit(ctx.statement())
    # for_stmt: FOR IDENTIFIER UNTIL expression BY expression nullable_newline statement;
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        id = Id(ctx.IDENTIFIER().getText())
        condExpr = self.visit(ctx.expression(0))
        upExpr = self.visit(ctx.expression(1))
        body = self.visit(ctx.statement())
        return For(id, condExpr, upExpr, body)
    # break_stmt: BREAK;
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()
    # continue_stmt: CONTINUE;
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()
    # return_stmt: RETURN | RETURN expression;
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)
    # function_call_stmt: IDENTIFIER OPEN_ROUND_BRACKET expression_list CLOSE_ROUND_BRACKET;
    def visitFunction_call_stmt(self, ctx: ZCodeParser.Function_call_stmtContext):
        id = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.expression_list())
        return CallStmt(id, args)
    # block_stmt: BEGIN atleast_newline block_body END;
    #   block_body: statement atleast_newline block_body | ;
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.block_body()))
    def visitBlock_body(self, ctx: ZCodeParser.Block_bodyContext):
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.block_body())
        return []

    # # # = = = = = EXPRESSION = = = = = # # #
    # expression_list: expression_prime COMMA expression_list | expression_prime;
    #   expression_prime: expression | ;
    def visitExpression_list(self, ctx: ZCodeParser.Expression_listContext):
        if ctx.expression_list():
            return self.visit(ctx.expression_prime()) + self.visit(ctx.expression_list())
        return self.visit(ctx.expression_prime())
    def visitExpression_prime(self, ctx: ZCodeParser.Expression_primeContext):
        if ctx.expression():
            return [self.visit(ctx.expression())]
        return []
    # expression: expression2 CONCAT expression2 | expression2;
    def visitExpression(self, ctx: ZCodeParser.ExpressionContext):
        if ctx.CONCAT():
            op = ctx.CONCAT().getText()
            left = self.visit(ctx.expression2(0))
            right = self.visit(ctx.expression2(1))
            return BinaryOp(op, left, right)
        return self.visit(ctx.expression2(0))
    # expression2: expression3 relational_sign expression3 | expression3;
    #   relational_sign: EQUAL | EQUAL_STRING | NEQ | LESS | GREATER | LEQ | GEQ;
    def visitExpression2(self, ctx: ZCodeParser.Expression2Context):
        if ctx.relational_sign():
            op = self.visit(ctx.relational_sign())
            left = self.visit(ctx.expression3(0))
            right = self.visit(ctx.expression3(1))
            return BinaryOp(op, left, right)
        return self.visit(ctx.expression3(0))
    def visitRelational_sign(self, ctx: ZCodeParser.Relational_signContext):
        return ctx.getChild(0).getText()
    # expression3: expression3 (AND | OR) expression4 | expression4;
    def visitExpression3(self, ctx: ZCodeParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)
            
    # expression4: expression4 (PLUS | MINUS) expression5 | expression5;
    def visitExpression4(self, ctx: ZCodeParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(op, left, right)
    # expression5: expression5 (MUL | DIV | MOD) expression6 | expression6;
    def visitExpression5(self, ctx: ZCodeParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression5())
        right = self.visit(ctx.expression6())
        return BinaryOp(op, left, right)
    
    # expression6: NOT expression6 | expression7;
    def visitExpression6(self, ctx: ZCodeParser.Expression6Context):
        if ctx.expression7():
            return self.visit(ctx.expression7())
        op = 'not'
        operand = self.visit(ctx.expression6())
        return UnaryOp(op, operand)
    # expression7: (MINUS | PLUS) expression7 | expression8;
    def visitExpression7(self, ctx: ZCodeParser.Expression7Context):
        if ctx.expression8():
            return self.visit(ctx.expression8())
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expression7())
        return UnaryOp(op, operand)
    # expression8: expression8 index_operators_expr | expression9;
    #   index_operators_expr: (IDENTIFIER | function_call_expr) OPEN_SQUARE_BRACKET index_operators CLOSE_SQUARE_BRACKET;
    #       index_operators: expression COMMA index_operators | expression;
    def visitExpression8(self, ctx: ZCodeParser.Expression8Context):
        if ctx.expression9():
            return self.visit(ctx.expression9())
        return self.visit(ctx.expression8()) + self.visit(ctx.index_operators_expr())
    def visitIndex_operators_expr(self, ctx: ZCodeParser.Index_operators_exprContext):
        arr = Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.function_call_expr())
        idx = self.visit(ctx.index_operators())
        return ArrayCell(arr, idx)
    def visitIndex_operators(self, ctx: ZCodeParser.Index_operatorsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.index_operators())
    # expression9: IDENTIFIER | NUMBER_LITERAL | TRUE | FALSE | STRING_LITERAL | array_literal | index_operators_expr | function_call_expr | sub_expr;
    #   function_call_expr: IDENTIFIER OPEN_ROUND_BRACKET expression_list CLOSE_ROUND_BRACKET;
    #   sub_expr: OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET;
    def visitExpression9(self, ctx: ZCodeParser.Expression9Context):
        if ctx.IDENTIFIER():
            id = ctx.IDENTIFIER().getText()
            return Id(id)
        elif ctx.NUMBER_LITERAL():
            value = float(ctx.NUMBER_LITERAL().getText())
            return NumberLiteral(value)
        elif ctx.TRUE() or ctx.FALSE():
            value = ctx.TRUE().getText() if ctx.TRUE() else ctx.FALSE().getText()
            return BooleanLiteral(value == 'true')
        elif ctx.STRING_LITERAL():
            value = ctx.STRING_LITERAL().getText()
            return StringLiteral(value)
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.index_operators_expr():
            return self.visit(ctx.index_operators_expr())
        elif ctx.function_call_expr():
            return self.visit(ctx.function_call_expr())
        return self.visit(ctx.sub_expr())
    def visitFunction_call_expr(self, ctx: ZCodeParser.Function_call_exprContext):
        id = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.expression_list())
        return CallExpr(id, args)
    def visitSub_expr(self, ctx: ZCodeParser.Sub_exprContext):
        return self.visit(ctx.expression())