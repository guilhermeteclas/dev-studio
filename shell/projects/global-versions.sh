#!/bin/bash

output_file="global-versions.md"
> "$output_file"

print_header() {
    local title=$1
    local length=$(printf "%s" "$title" | wc -m)
    local border=$(printf '═%.0s' $(seq 1 $length))

    echo "╔═$border═╗"
    echo "║ $title ║"
    echo "╚═$border═╝"
    echo 

    echo "##" $title >> $output_file
}


check_version() {
    local name=$1
    local command=$2
    local green="\033[1;32m"  
    local reset="\033[0m"

    echo "${green}${name}${reset}"
    $command | head -n 1
    echo "**$name**  " >> "$output_file"
    $command >> $output_file
    echo >> "$output_file"  
    echo 
}

echo
echo $(lsb_release -d | awk -F ':' '{print $2}' | sed 's/^ //')  # Remove espaços extras
echo "#" $(lsb_release -d | awk -F ':' '{print $2}' | sed 's/^ //') >> $output_file
echo

check_version "Docker" "docker --version"


print_header "Programming Languages"
check_version "C" "gcc --version"
check_version "Java" "java --version"
check_version "Python" "python3 --version"
check_version "PHP" "php --version"
check_version "Ruby" "ruby --version"

print_header "Runtimes"
check_version "Node" "node -v" 
check_version "Deno" "deno -v" 
check_version "Bun" "bun -v" 

print_header "Frameworks"
check_version "Rails" "rails --version" 

print_header "Databases"
check_version "Sqlite" "sqlite3 --version"
check_version "MySQL" "mysql --version"
check_version "Postgres" "psql --version"
check_version "Mongo" "mongod --version"

print_header "Package managers"
check_version "composer" "composer --version"
check_version "rbenv" "rbenv --version"
check_version "bundler" "bundler --version"
check_version "gem" "gem --version"
check_version "pip" "pip3 --version"
check_version "poetry" "poetry --version"
check_version "npm" "npm --version"


