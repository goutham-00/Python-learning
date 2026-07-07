# Sales Data Tracking Project

day1_sales = 1200
day2_sales = 1500
day3_sales = 1100
day4_sales = 1700
day5_sales = 1600

# 1. Total sales
total_sales = day1_sales + day2_sales + day3_sales + day4_sales + day5_sales
print("Total Sales for 5 days:")
print(total_sales)

# 2. Average sales
average_sales = total_sales / 5
print("Average Sales per day:")
print(average_sales)

# 3. Best sales day
best_day = max(day1_sales, day2_sales, day3_sales, day4_sales, day5_sales)
print("Best day sales:")
print(best_day)

# 4. Did we cross 1500 target?
target_crossed = best_day > 1500
print("Did we cross 1500 target:")
print(target_crossed)
