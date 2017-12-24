#!/bin/bash
distrofull=$(cat /etc/issue);
distro=${distrofull:: -6};
echo "Enter number of the Database Client you prefer:";
echo "1. MySQL";
echo "2. SQLite";
echo "3. MariaDB";
echo "4. PostgreSQL";
read user_preference;
echo "";
if [ "$user_preference" -eq "1" ]; 
then user_preference="MySQL";
else if [ "$user_preference" -eq "2" ];
then user_preference="SQLite";
else if [ "$user_preference" -eq "3" ];
then user_preference="MariaDB";
else if [ "$user_preference" -eq "2" ];
then user_preference="PostgreSQL";
fi
fi
fi
fi
echo "These are the results-"
echo "Distro: $distro";
echo "Database Client: "$user_preference;
