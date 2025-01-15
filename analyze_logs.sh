# Подсчет общего количества запросов
total_requests=$(wc -l < access.log)

# Подсчет уникальных IP-адресов с использованием awk
unique_ips=$(awk '{print $1}' access.log | sort -u | wc -l)

# Подсчет количества запросов по методам с использованием awk
method_counts=$(awk '{print $6}' access.log | sort | uniq -c)

# Нахождение самого популярного URL с использованием awk
popular_url=$(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 1)

# Создание отчета
{   
    echo "Отчет о логе веб-сервера"
    echo "========================"
    echo "Общее количество запросов: $total_requests"
    echo "Количество уникальных IP-адресов: $unique_ips"
    echo "Количество запросов по методам:"
    echo "$method_counts"
    echo "Самый популярный URL: $popular_url"
} > report.txt

echo "Отчет создан в файле report.txt"
