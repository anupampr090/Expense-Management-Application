from pydantic import BaseModal

class ExpenseCreate(BaseModal):
    name:str
    amount:float
    category:str