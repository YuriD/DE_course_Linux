#!/bin/bash

#1
# total_requests=$(wc -l < access.log)
total_requests=$(awk 'END {print NR}' access.log)

#2
unique_ips=$(awk '{ips[$1]++} END {print length(ips)}' access.log)

#3
methods=$(awk '{gsub(/"/, "", $6); methods[$6]++} END {for (m in methods) print "  " methods[m], m}' access.log | sort -rn)

#4
popular_url=$(awk '{urls[$7]++} END {max=0; url=""; for (u in urls) if (urls[u] > max) {max=urls[u]; url=u} print max, url}' access.log)

echo "Отчет о логе веб-сервера" > report.txt
echo "========================" >> report.txt
echo "Общее количество запросов:   $total_requests" >> report.txt
echo "Количество уникальных IP-адресов:   $unique_ips" >> report.txt
echo "" >> report.txt
echo "Количество запросов по методам:" >> report.txt
echo "$methods" >> report.txt
echo "" >> report.txt
echo "Самый популярный URL:   $popular_url" >> report.txt
echo "Отчет сохранен в файл report.txt"
