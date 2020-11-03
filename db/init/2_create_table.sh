#!/bin/bash
psql -U postgres -d learn_flask << "EOSQL"
CREATE TABLE users (
        id SERIAL NOT NULL, 
        email VARCHAR(256), 
        name VARCHAR(256), 
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        PRIMARY KEY (id)
);
EOSQL