# Software Engineering Project

Database : Drugbank CA Database

## NOTES

Fill your password inside sql.py

## DATABASES

In your local MySQL installation, Create a database called DRUGBANK.
In this db, create 4 tables DRUG, DRUG_CLASS, DRUG_INTERACTIONS, DRUG_TARGET

The schema for the tables is given below:

`
    CREATE TABLE DRUG (
        name TEXT,
        id varchar(20) PRIMARY KEY,
    )

    CREATE TABLE DRUG_CLASS (
        directparent TEXT,
        kingdom TEXT,
        superclass TEXT,
        class TEXT,
        subclass TEXT,
        id varchar(20) PRIMARY KEY,
    )

    CREATE TABLE DRUG_TARGET (
        position INT(11),
        organism TEXT,
        name TEXT,
        id varchar(20) PRIMARY KEY,
    )

    CREATE TABLE DRUG_INTERACTIONS (
        name TEXT,
        description TEXT,
        id varchar(20) PRIMARY KEY,
    )
`

Make sure you create these tables before proceeding

## INSTALLATION

Execute `pip install -r install.txt` to install pre-requisites of this project