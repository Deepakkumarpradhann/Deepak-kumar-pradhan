//Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
  //(examples)
  //input: [1,2,8,9,12,46,76,82,15,20,30]
  //Output: 
   // {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

def count_multiples(numbers):
    result = {i: 0 for i in range(1, 10)}  # dictionary 1–9
    
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    return result


if __name__ == "__main__":
    numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    output = count_multiples(numbers)
    print(output)
