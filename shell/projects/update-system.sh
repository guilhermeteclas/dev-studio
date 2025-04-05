#!/bin/bash

print_header() {
    local message=$1
    local length=$(printf "%s" "$message" | wc -m)
    local border=$(printf '═%.0s' $(seq 1 $length))

    echo "╔═$border═╗"
    echo "║ $message ║"
    echo "╚═$border═╝"
}

update_apt() {
    print_header "Atualizando apt"
    if sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y; then
        echo "APT atualizado com sucesso."
    else
        echo "Erro ao atualizar o APT." >&2
    fi
}

update_dnf() {
    print_header "Atualizando dnf"
    if sudo dnf upgrade -y && sudo dnf autoremove -y; then
        echo "DNF atualizado com sucesso."
    else
        echo "Erro ao atualizar o DNF." >&2
    fi
}

update_flatpak() {
    print_header "Atualizando flatpak"
    if flatpak update -y && flatpak remove --unused --delete-data; then
        echo "Flatpak atualizado com sucesso."
    else
        echo "Erro ao atualizar o Flatpak." >&2
    fi
}

update_apt
update_dnf
update_flatpak

