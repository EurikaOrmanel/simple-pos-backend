CREATE USER simple_pos WITH PASSWORD 'asdiojfkaelsd23';
ALTER USER simple_pos WITH SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE simple_pos_db TO simple_pos; 