#!/bin/bash

list_users() {
    echo "List of human users:"
    getent passwd | awk -F: '$3 >= 1000 {print $1}'
}

remove_user() {
    read -p "Enter the username to remove: " username
    if [ -d "/home/$username" ]; then
        sudo userdel -r $username
        echo "User $username has been removed."
    else
        echo "User $username not found or does not have a home directory."
    fi
}

check_password_strength() {
    read -s -p "Enter a password to check its strength: " password
    echo
    if [[ ${#password} -ge 8 && "$password" =~ [0-9] && "$password" =~ [A-Z] && "$password" =~ [a-z] && "$password" =~ [\!\@\#\$\%\^\&\*\(\)\_\+\.\,\;\:] ]]; then
        echo "Password strength: Strong"
    else
        echo "Password strength: Weak"
    fi
}

update_password() {
    read -p "Enter the username to update the password: " username
    sudo passwd $username
    echo "Password for user $username has been updated."
}

while true; do
    echo "1. List all users"
    echo "2. Remove a user"
    echo "3. Check password strength"
    echo "4. Update password"
    echo "5. Exit"

    read -p "Choose an option (1-5): " choice

    case $choice in
        1) list_users ;;
        2) remove_user ;;
        3) check_password_strength ;;
        4) update_password ;;
        5) echo ""; exit ;;
        *) echo "Invalid choice. Please enter a number between 1 and 5." ;;
    esac
done