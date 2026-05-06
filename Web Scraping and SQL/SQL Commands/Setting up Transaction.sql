select * from [Restaurant_DB].[dbo].[geographic]

BEGIN TRANSACTION
    insert into [Restaurant_DB].[dbo].[geographic] values ('roha', 'maximoff county', 'sing valley');
    -- Creating a savepoint fro insert
    SAVE TRANSACTION T1;
  
    --
    SELECT * FROM [Restaurant_DB].[dbo].[geographic]
    update [Restaurant_DB].[dbo].[geographic] set county = 'contra costa county' where city = 'roha');

    ROLLBACK TRANSACTION T1
    -- View the table to confirm rollback
    SELECT * FROM [Restaurant_DB].[dbo].[geographic]

COMMIT

delete from [Restaurant_DB].[dbo].[geographic] where city IN ('chennai', 'roha');
