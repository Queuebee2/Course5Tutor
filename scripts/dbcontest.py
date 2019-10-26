from DbConnector import DbConnector


db = DbConnector()
actual_id = 'anotherdbTest'
header = 'headertest'
seq = 'seqtest'
iteration = -1
GO_STUF_D = {'go(biological process)':"test;test;test",
             'go(cellular component)':"test2comp;tes2t",
             'go(molecular function)':"IDUYEI*UYWGFWGHF"}
pos_2c = -1
q = f"""INSERT INTO PROTEIN VALUES(
                        NULL,
                        '{actual_id}',
                        '{header}',
                        '{seq}',
                        {iteration},
                        '{GO_STUF_D['go(biological process)']}',
                        '{GO_STUF_D['go(cellular component)']}',
                        '{GO_STUF_D['go(molecular function)']}',
                        {pos_2c});
                        """
print(q)
db.commit_query(q)
mess = db.exists_protein('testgfId')
print(mess)
