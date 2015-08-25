use lcf;

load data infile '/Users/nadia/Play/repos/lcf/util/db_nontesting.txt'
into table cruelty_free_company 
(category, name, phone, url);