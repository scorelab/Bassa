#!/bin/bash
distro=$(cat /etc/*-release | grep "DISTRIB_ID=" | cut -d"=" -f2);
echo "Select the Database Client you prefer:";
options=("MySQL" "SQLite" "MariaDB" "PostgreSQL");
select opt in "${options[@]}"
do
    case $opt in
        "MySQL")
            user_preference="MySQL"
	    break
            ;;
        "SQLite")
            user_preference="SQLite"
	    break
            ;;
        "MariaDB")
            user_preference="MariaDB"
	    break
            ;;
        "PostgreSQL")
            user_preference="MySQL"
	    break
            ;;
        *)
            echo "invalid option"
            ;;
    esac
done
echo "";
echo "These are the results-"
echo "Distro: $distro";
echo "Database Client: "$user_preference;
