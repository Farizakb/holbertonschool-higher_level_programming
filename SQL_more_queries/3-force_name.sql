-- 3-force_name.sql
-- Script that creates the table force_name
-- The name column cannot be NULL

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
