import unittest 

def is_palindrome(mystring):
    for indice in range(0,len(mystring)):
        print(mystring[ indice] + " --> " + mystring[-(indice +1)])
        if mystring[indice] != mystring [-(indice +1)]:
         print("no es")
         return False
    return True
    #return mystring[0] == mystring[-1]
    
    
class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado,True)
        
    def test_b(self):
        resultado = is_palindrome('B')
        self.assertEqual(resultado,True)
        
    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado,True)
        
    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado,False)
        
    def test_aCa(self):
        resultado = is_palindrome('aCa')
        self.assertEqual(resultado,True)
        
    def test_aCs(self):
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado,False)
        
    def test_ABBA(self):
        resultado = is_palindrome('ABBA')
        self.assertEqual(resultado,True)
        
    def test_ABCA(self):
        resultado = is_palindrome('ABCA')
        self.assertEqual(resultado,False)
        
    def test_ABCBA(self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual(resultado,True)
        
    def test_ABCCBA(self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual(resultado,True)
        
    def test_ZBCCBA(self):
        resultado = is_palindrome('ZBCCBA')
        self.assertEqual(resultado,False)
        
    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado,True)
    
    def test_neuqueM(self):
        resultado = is_palindrome('neuqueM')
        self.assertEqual(resultado,False)
        
    def test_rallar(self):
        resultado = is_palindrome('rallar')
        self.assertEqual(resultado,True)
        
    def test_Oso(self):
        resultado = is_palindrome('oso')
        self.assertEqual(resultado,True)
    
    def test_reconocer(self):
        resultado = is_palindrome('reco nocer')
        self.assertEqual(resultado,False)
        
    def test_salas(self):
        resultado = is_palindrome('salas')
        self.assertEqual(resultado,True)
        
    def test_seres(self):
        resultado = is_palindrome('s e r e s')
        self.assertEqual(resultado,True)
        
        
unittest.main()
        
        
        
        
        
        
        
        
        
        
        