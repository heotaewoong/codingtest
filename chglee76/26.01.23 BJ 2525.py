hour, minute = map(int, input().split())
cooking_time = int(input())

total_minute = minute + cooking_time

total_hour = hour + total_minute // 60
end_minute = total_minute % 60

end_hour = total_hour % 24

print(end_hour, end_minute)