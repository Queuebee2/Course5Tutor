-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-10-26 03:29:40.623

-- tables
-- Table: PROTEIN
-- version 10
CREATE TABLE PROTEIN (
    id int NOT NULL AUTO_INCREMENT,
    db_id varchar(25) NOT NULL,
    header text NOT NULL,
    sequence text NOT NULL,
    iteration int NOT NULL,
    GO_bio_process text DEFAULT NULL,
    GO_cell_comp text DEFAULT NULL,
    GO_mol_func text DEFAULT NULL,
    pos_2c int DEFAULT NULL COMMENT '-1  indicates there is no CxxC pattern in this protein',
    CONSTRAINT PROTEIN_pk PRIMARY KEY (id)
);

-- End of file.

