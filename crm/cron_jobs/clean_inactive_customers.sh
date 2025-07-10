#!/bin/bash

# Calculate the date one year ago
ONE_YEAR_AGO=$(date -d "1 year ago" '+%Y-%m-%d')

# Execute Django command to delete inactive customers and capture the count
DELETED_COUNT=$(python manage.py shell -c "from django.utils import timezone; from datetime import datetime; from crm.models import Customer; count = Customer.objects.filter(last_order_date__lt=datetime.strptime('$ONE_YEAR_AGO', '%Y-%m-%d').date()).delete()[0]; print(count)")

# Log the result with a timestamp
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $DELETED_COUNT inactive customers" >> /tmp/customer_cleanup_log.txt