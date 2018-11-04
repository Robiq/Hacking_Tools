#!/bin/bash

str2hex_echo() {
    # USAGE: hex_repr=$(str2hex_echo "ABC")
    #        returns "0x410x420x43"
    local str=${1:-""}
    local fmt="%%%x"
    local chr
    local -i i
    for i in `seq 0 $((${#str}-1))`; do
        chr=${str:i:1}
        printf  "${fmt}" "'${chr}"
    done
}

hex2str_echo() {
    # USAGE: ASCII_repr=$(hex2str_echo "0x410x420x43")
    #        returns "ABC"
    echo -en "'${1:-""//0x/\\x}'"
}

if [ $1!='' ];
	then
	hex_repr=$(str2hex_echo "$1")
	echo $hex_repr
fi
