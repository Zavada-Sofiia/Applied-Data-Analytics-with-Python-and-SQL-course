select * from geographic

ALTER TABLE generalinfo ADD chef varchar(40);
  
ALTER TABLE generalinfo ALTER COLUMN food_type varchar(50);

UPDATE geographic
SET county = 'conta costa county';

UPDATE geographic
SET county = 'bangalore';
