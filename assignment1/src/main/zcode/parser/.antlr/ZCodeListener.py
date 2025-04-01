# Generated from /Users/thuckhue/Desktop/HCMUT/HK232/Principles of Programming Language/Assignments/Assignment 1/assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaration.
    def enterDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaration.
    def exitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variable_decl.
    def enterVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variable_decl.
    def exitVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var.
    def enterVar(self, ctx:ZCodeParser.VarContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var.
    def exitVar(self, ctx:ZCodeParser.VarContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dynamic.
    def enterDynamic(self, ctx:ZCodeParser.DynamicContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dynamic.
    def exitDynamic(self, ctx:ZCodeParser.DynamicContext):
        pass


    # Enter a parse tree produced by ZCodeParser#normal_type.
    def enterNormal_type(self, ctx:ZCodeParser.Normal_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#normal_type.
    def exitNormal_type(self, ctx:ZCodeParser.Normal_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#type_list.
    def enterType_list(self, ctx:ZCodeParser.Type_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#type_list.
    def exitType_list(self, ctx:ZCodeParser.Type_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_type.
    def enterArray_type(self, ctx:ZCodeParser.Array_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_type.
    def exitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_variable.
    def enterArray_variable(self, ctx:ZCodeParser.Array_variableContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_variable.
    def exitArray_variable(self, ctx:ZCodeParser.Array_variableContext):
        pass


    # Enter a parse tree produced by ZCodeParser#size.
    def enterSize(self, ctx:ZCodeParser.SizeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#size.
    def exitSize(self, ctx:ZCodeParser.SizeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_literal.
    def enterArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_literal.
    def exitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_elements.
    def enterArray_elements(self, ctx:ZCodeParser.Array_elementsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_elements.
    def exitArray_elements(self, ctx:ZCodeParser.Array_elementsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#one_element.
    def enterOne_element(self, ctx:ZCodeParser.One_elementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#one_element.
    def exitOne_element(self, ctx:ZCodeParser.One_elementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multiple_elements.
    def enterMultiple_elements(self, ctx:ZCodeParser.Multiple_elementsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multiple_elements.
    def exitMultiple_elements(self, ctx:ZCodeParser.Multiple_elementsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_rhs.
    def enterArray_rhs(self, ctx:ZCodeParser.Array_rhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_rhs.
    def exitArray_rhs(self, ctx:ZCodeParser.Array_rhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter_list.
    def enterParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter_list.
    def exitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter_prime.
    def enterParameter_prime(self, ctx:ZCodeParser.Parameter_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter_prime.
    def exitParameter_prime(self, ctx:ZCodeParser.Parameter_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter.
    def enterParameter(self, ctx:ZCodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter.
    def exitParameter(self, ctx:ZCodeParser.ParameterContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullable_vardecl_expr.
    def enterNullable_vardecl_expr(self, ctx:ZCodeParser.Nullable_vardecl_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullable_vardecl_expr.
    def exitNullable_vardecl_expr(self, ctx:ZCodeParser.Nullable_vardecl_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#atleast_newline.
    def enterAtleast_newline(self, ctx:ZCodeParser.Atleast_newlineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#atleast_newline.
    def exitAtleast_newline(self, ctx:ZCodeParser.Atleast_newlineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullable_newline.
    def enterNullable_newline(self, ctx:ZCodeParser.Nullable_newlineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullable_newline.
    def exitNullable_newline(self, ctx:ZCodeParser.Nullable_newlineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_decl.
    def enterFunction_decl(self, ctx:ZCodeParser.Function_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_decl.
    def exitFunction_decl(self, ctx:ZCodeParser.Function_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_body.
    def enterFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_body.
    def exitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_list.
    def enterStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_list.
    def exitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment_type.
    def enterAssignment_type(self, ctx:ZCodeParser.Assignment_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment_type.
    def exitAssignment_type(self, ctx:ZCodeParser.Assignment_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_stmt.
    def enterIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_stmt.
    def exitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_part.
    def enterIf_part(self, ctx:ZCodeParser.If_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_part.
    def exitIf_part(self, ctx:ZCodeParser.If_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_list.
    def enterElif_list(self, ctx:ZCodeParser.Elif_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_list.
    def exitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_part.
    def enterElif_part(self, ctx:ZCodeParser.Elif_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_part.
    def exitElif_part(self, ctx:ZCodeParser.Elif_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#else_list.
    def enterElse_list(self, ctx:ZCodeParser.Else_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#else_list.
    def exitElse_list(self, ctx:ZCodeParser.Else_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#else_part.
    def enterElse_part(self, ctx:ZCodeParser.Else_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#else_part.
    def exitElse_part(self, ctx:ZCodeParser.Else_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_stmt.
    def enterFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_stmt.
    def exitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_stmt.
    def enterBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_stmt.
    def exitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continue_stmt.
    def enterContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continue_stmt.
    def exitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_stmt.
    def enterReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_stmt.
    def exitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_call_stmt.
    def enterFunction_call_stmt(self, ctx:ZCodeParser.Function_call_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_call_stmt.
    def exitFunction_call_stmt(self, ctx:ZCodeParser.Function_call_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_stmt.
    def enterBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_stmt.
    def exitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression_list.
    def enterExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression_list.
    def exitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression_prime.
    def enterExpression_prime(self, ctx:ZCodeParser.Expression_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression_prime.
    def exitExpression_prime(self, ctx:ZCodeParser.Expression_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression2.
    def enterExpression2(self, ctx:ZCodeParser.Expression2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression2.
    def exitExpression2(self, ctx:ZCodeParser.Expression2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression3.
    def enterExpression3(self, ctx:ZCodeParser.Expression3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression3.
    def exitExpression3(self, ctx:ZCodeParser.Expression3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression4.
    def enterExpression4(self, ctx:ZCodeParser.Expression4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression4.
    def exitExpression4(self, ctx:ZCodeParser.Expression4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression5.
    def enterExpression5(self, ctx:ZCodeParser.Expression5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression5.
    def exitExpression5(self, ctx:ZCodeParser.Expression5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression6.
    def enterExpression6(self, ctx:ZCodeParser.Expression6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression6.
    def exitExpression6(self, ctx:ZCodeParser.Expression6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression7.
    def enterExpression7(self, ctx:ZCodeParser.Expression7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression7.
    def exitExpression7(self, ctx:ZCodeParser.Expression7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression8.
    def enterExpression8(self, ctx:ZCodeParser.Expression8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression8.
    def exitExpression8(self, ctx:ZCodeParser.Expression8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expression9.
    def enterExpression9(self, ctx:ZCodeParser.Expression9Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expression9.
    def exitExpression9(self, ctx:ZCodeParser.Expression9Context):
        pass


    # Enter a parse tree produced by ZCodeParser#relational_sign.
    def enterRelational_sign(self, ctx:ZCodeParser.Relational_signContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relational_sign.
    def exitRelational_sign(self, ctx:ZCodeParser.Relational_signContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_operators_expr.
    def enterIndex_operators_expr(self, ctx:ZCodeParser.Index_operators_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_operators_expr.
    def exitIndex_operators_expr(self, ctx:ZCodeParser.Index_operators_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_operators.
    def enterIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_operators.
    def exitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sub_expr.
    def enterSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sub_expr.
    def exitSub_expr(self, ctx:ZCodeParser.Sub_exprContext):
        pass



del ZCodeParser