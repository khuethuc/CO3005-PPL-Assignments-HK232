# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_decl.
    def visitVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var.
    def visitVar(self, ctx:ZCodeParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic.
    def visitDynamic(self, ctx:ZCodeParser.DynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normal_type.
    def visitNormal_type(self, ctx:ZCodeParser.Normal_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_list.
    def visitType_list(self, ctx:ZCodeParser.Type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_variable_decl.
    def visitArray_variable_decl(self, ctx:ZCodeParser.Array_variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#size.
    def visitSize(self, ctx:ZCodeParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_elements.
    def visitArray_elements(self, ctx:ZCodeParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#one_element.
    def visitOne_element(self, ctx:ZCodeParser.One_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiple_elements.
    def visitMultiple_elements(self, ctx:ZCodeParser.Multiple_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_rhs.
    def visitArray_rhs(self, ctx:ZCodeParser.Array_rhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_list.
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_prime.
    def visitParameter_prime(self, ctx:ZCodeParser.Parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_vardecl_expr.
    def visitNullable_vardecl_expr(self, ctx:ZCodeParser.Nullable_vardecl_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#atleast_newline.
    def visitAtleast_newline(self, ctx:ZCodeParser.Atleast_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline.
    def visitNullable_newline(self, ctx:ZCodeParser.Nullable_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_decl.
    def visitFunction_decl(self, ctx:ZCodeParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_body.
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_decl_stmt.
    def visitVariable_decl_stmt(self, ctx:ZCodeParser.Variable_decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_type.
    def visitAssignment_type(self, ctx:ZCodeParser.Assignment_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_part.
    def visitIf_part(self, ctx:ZCodeParser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_part.
    def visitElif_part(self, ctx:ZCodeParser.Elif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_list.
    def visitElse_list(self, ctx:ZCodeParser.Else_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_part.
    def visitElse_part(self, ctx:ZCodeParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call_stmt.
    def visitFunction_call_stmt(self, ctx:ZCodeParser.Function_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_body.
    def visitBlock_body(self, ctx:ZCodeParser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_list.
    def visitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_prime.
    def visitExpression_prime(self, ctx:ZCodeParser.Expression_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression8.
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression9.
    def visitExpression9(self, ctx:ZCodeParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_sign.
    def visitRelational_sign(self, ctx:ZCodeParser.Relational_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators_expr.
    def visitIndex_operators_expr(self, ctx:ZCodeParser.Index_operators_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sub_expr.
    def visitSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        return self.visitChildren(ctx)



del ZCodeParser