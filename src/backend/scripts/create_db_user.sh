#!/bin/bash
set -e

DB_NAME="${1:-stock_analysis}"          # Defaults to 'myapp' if not specified
DB_USER="${2:-fastapi_user}"   # Defaults to 'fastapi_user'

read -s -p "Enter password for user $DB_USER: " DB_PASS
echo ""

# Run commands as the postgres system user
sudo -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASS';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

echo "Database '$DB_NAME' and user '$DB_USER' created with privileges."
