# Software Engineering Project

Database : Drugbank CA Database

## NOTES

Fill your password inside sql.py

## local_settings.json

You need to create this file and place it in the root of the project before proceeding. The file looks like:

    {
        "host" : "localhost",
        "user" : "root",
        "password" : "PASSWORD OF MYSQL root",
        "database" : "DRUGBANK"
    }

## DATABASES

In your local MySQL installation, Create a database called DRUGBANK.
In this db, create 4 tables DRUG, DRUG_CLASS, DRUG_INTERACTIONS, DRUG_TARGET

The schema for the tables is given below:

    CREATE DATABASE DRUGBANK;
    USE DRUGBANK;

    CREATE TABLE DRUG (
        name TEXT,
        id varchar(20) PRIMARY KEY
    );

    CREATE TABLE DRUG_CLASS (
        directparent TEXT,
        kingdom TEXT,
        superclass TEXT,
        class TEXT,
        subclass TEXT,
        id varchar(20) PRIMARY KEY REFERENCES DRUG(id)
    );

    CREATE TABLE DRUG_TARGET (
        position INT(11),
        organism TEXT,
        name TEXT,
        drugbank_id varchar(20) REFERENCES DRUG(id),
        id varchar(20) REFERENCES DRUG(id),
        PRIMARY KEY(drugbank_id , id)
    );

    CREATE TABLE DRUG_INTERACTIONS (
        name TEXT,
        description TEXT,
        id varchar(20) REFERENCES DRUG(id),
        drugbank_id varchar(20) REFERENCES DRUG(id),
        PRIMARY KEY(drugbank_id , id)
    );

Make sure you create these tables before proceeding

## INSTALLATION

Execute `pip3 install -r install.txt` to install pre-requisites of this project