from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL="sqlite:///databases.db"

engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
    )
    
    Sessionlocal=sessionmaker(
        autocommit=False
        autoflush=False
        bind=engine
        )
        Base=declarative_base()
        
        def get_db():
            db=Sessionlocal()
            try:
                yield db
            finally:
                db.close()
                
                
