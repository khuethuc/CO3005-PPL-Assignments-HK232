import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test401(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test402(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test403(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test404(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test405(self):
        input = """
            number abc
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test406(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test407(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test408(self):
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test409(self):
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 409))  
    def test410(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test411(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test412(self):
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test413(self):
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test414(self):   
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test415(self):    
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test416(self):  
        input = """
            number a
            func d() return
            func main()begin
                number a
                number c
                string d
                begin
                    number c
                    string d
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test417(self):
        input = """
            number a
            func foo() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test418(self):
        input = """
            number a
            func foo() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test419(self): 
        input = """
            number a
            func foo() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test420(self):  
        input = """
            number a
            func foo(number a, number foo, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test421(self):  
        input = """
            number a
            func foo(number a, number foo, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test422(self):  
        input = """
            number a
            func f(number a, number f, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test423(self):  
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test425(self):  
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test426(self):  
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test427(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 427))    
    def test428(self):
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test429(self):
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test430(self): 
        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test431(self):
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test432(self):
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test433(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test434(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test435(self):
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test436(self):
        input = """
            dynamic k
            var a <- k

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(k))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test437(self):
        input = """
            number hi
            var a <- hi
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test438(self):
        input = """
            dynamic num
            number a <- num
            number b <- num

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test439(self):
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test440(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 440))  
    def test442(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test443(self):
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test444(self):
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test445(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test447(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 447))   
    def test448(self):
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 448)) 
    def test449(self):
        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 449))    
    def test450(self):
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 450))     
    def test451(self):
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 451))    
    def test452(self):
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))               
    def test453(self):
        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))     
    def test454(self):
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 454))                 
    def test455(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test456(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test457(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test458(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test459(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test460(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test461(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test462(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test463(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test464(self):
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test465(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test466(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test467(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test468(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test469(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test470(self):
        input = """
            func a()
            func main() begin
                number a_ <- a()
            end
            func a() begin
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a_), NumberType, None, CallExpr(Id(a), []))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test471(self):
        input = """
            dynamic a
            var x <- a + a * a
            number y <- a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test473(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test474(self):
        input = """
            dynamic p
            var x <- p + p * p
            number y <- p
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test475(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic hi
                var c <- a[hi, 1]
                hi <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test476(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test477(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test478(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test479(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test480(self):
        input = """
            number abc
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test481(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test482(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test488(self):
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test489(self):
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 489))  
    def test490(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test491(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test492(self):
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test493(self):
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test494(self):   
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test495(self):    
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test496(self):  
        input = """
            number a
            func d() return
            func main()begin
                number a
                number c
                string d
                begin
                    number c
                    string d
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test497(self):
        input = """
            number a
            func foo() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test498(self):
        input = """
            number a
            func foo() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test499(self): 
        input = """
            number a
            func foo() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 499))
    def test500(self):  
        input = """
            number a
            func foo(number a, number foo, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 500))
    def test501(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501))
    def test502(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))
    def test503(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 503))
    def test504(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 504))
    def test505(self):
        input = """
            number abc
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 505))
    def test506(self):
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 506))
    def test507(self):
        input = """
func isPrime(number x)

func main()
    begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
    end

func isPrime(number x)
    begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        return true
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 507))
    def test508(self):
        input = """
        func main()
            begin
                dynamic x
                number a <- [x]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 508))        
    def test509(self):
        input = """
            dynamic x
            number a[3] <- [x]
            func main()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 509))        
    def test510(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 510))     
    def test511(self):
        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 511))   
    def test512(self):
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 512))   
    def test513(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 513))  
    def test514(self):
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 514))  
    def test515(self):
        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 515))    
    def test516(self):
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 516))     
    def test519(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 519)) 
    def test520(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 520)) 
    def test532(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 532)) 
    def test533(self):
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 533)) 
    def test535(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 535))   
    def test536(self):
        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 536))   
    def test540(self):
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 540))          
