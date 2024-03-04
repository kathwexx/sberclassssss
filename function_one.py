def function_one(numbers):
  counts = {}
    
  for num in numbers:
      if num in counts:
          counts[num] += 1
      else:
          counts[num] = 1
  
  # Проходим по словарю и ищем число с нечетным количеством вхождений
  for num, count in counts.items():
      if count % 2 != 0:
          return num
