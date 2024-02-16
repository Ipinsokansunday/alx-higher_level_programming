# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Assign the argument to a variable
DATABASE=$1

# MySQL command to create the table if it doesn't exist
mysql -e "USE $DATABASE; CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));"
