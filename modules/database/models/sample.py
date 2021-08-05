from modules.database.basemodel import *

class Sample(BaseModel):
    name = CharField(unique=True)
    address = CharField(unique=True)
    age = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'sample'
