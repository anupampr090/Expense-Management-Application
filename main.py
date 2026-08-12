from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import engine,Base, get_db
from models import Expense

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Expense Management Application",
    description="FastAPI Expense Management Application",
    version="1.0.0"
    )
    
@app.get("/")
async def root():
    return{"message":"Expense Management API"}
    
@app.post("/expenses/")
async def create_expense(
    expense:ExpenseCreate,
    db:Session =Depends(get_db):
        new_expense=Expense(
            name=expexse.name
            amount=expense.amount
            category=expense.category
            )
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        
        return new-expense
    )
    
@app.get("/expenses/month/{year}/{month}")
async def get_expenses_by_month(
    year:int,
    month:int,
    db:ession =Depends(get_db):
    return
        )


  
    
