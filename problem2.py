// Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
  //Output: (examples)
   // 1) input a = 1, then output : 1
   // 2) input a = 2, then output : 1, 3
    //3) input a = 3, then output : 1, 3, 5
    // 4) input a = 4, then output : 1, 3, 5, 7
   // .
   // .
   // 5) input a = x, then output : 1, 3, 5, 7, .......




def generate_series(n: int):
    series = []
    for i in range(n):
        series.append(2 * i + 1)   
    return series


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    result = generate_series(a)
    print("Output:", ", ".join(map(str, result)))
