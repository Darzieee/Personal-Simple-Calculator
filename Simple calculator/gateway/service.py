from re import I
from nameko.web.handlers import http
from werkzeug.wrappers import Response
import uuid

from gateway.dependencies.session import SessionProvider

class Service:
    name = "gateway_service"

    session_provider = SessionProvider()
    
    @http('GET', '/login')
    def login(self, request):
        user_data = {
            'id': 1,
            'username': 'User'
        }
        
        session_id = self.session_provider.set_session(user_data)
        response = Response(str(user_data))
        response.set_cookie('SESSID', session_id)
        return response

    @http('GET', '/prime/<angka>')
    def prima(self, request,angka):
        
        count=2
        countPrime=0
        temp=-1
        angka=int(angka)

        while (temp==-1):
            if (self.is_prime(count)) :
                if (countPrime==angka) :
                    temp=count
                countPrime=countPrime+1
            count=count+1
            
        response = Response("Result : "+str(temp))
        return response
    
    def is_prime(self,angka):
        for i in range(2,angka):
            if (angka % i) == 0:
                return False
        return True

    @http('GET', '/primepalindrome/<angka>')
    def primepalindrome(self, request,angka):
        
        count=2
        countPrime=0
        temp=-1
        angka=int(angka)

        while (temp==-1):
            if (self.is_PrimePalindrome(count)) :
                if (countPrime==angka) :
                    temp=count
                countPrime=countPrime+1
            count=count+1
            
        response = Response("Result : " + str(temp))
        return response
        
    def is_PrimePalindrome(self,angka):
        Prime = True
        for i in range(2,angka):
            if (angka % i) == 0:
                Prime= False
        
        if(str(angka) != str(angka)[::-1]):
            Prime=False
        
        return Prime