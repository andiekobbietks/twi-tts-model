credit = 300
hourly_rate = 1.671

# Calculate the total hours of compute time available based on the credit and hourly rate
total_hours = credit / hourly_rate

# Calculate the total days of compute time available based on the total hours
total_days = total_hours / 24

print(f"Total Hours: {total_hours:.2f}")
print(f"Total Days: {total_days:.2f}")
