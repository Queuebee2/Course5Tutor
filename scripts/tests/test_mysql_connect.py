import mysql.connector as sql


# deze waarden aanpassen
vijf_letter_code = "svbiw"
pwd = "luvinformatica"

HOST_DEFAULT = "hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com"
USER_DEFAULT = vijf_letter_code + "@hannl-hlo-bioinformatica-mysqlsrv"
DATABASE_DEFAULT = vijf_letter_code


sql.connect(host=HOST_DEFAULT,
            password=pwd,
            user=USER_DEFAULT,
            db=DATABASE_DEFAULT)
print('done')

