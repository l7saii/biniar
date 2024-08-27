def binary_addition(bin1, bin2):

    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
 
    result = num1 + num2
    
  
    binary_result = bin(result)[2:]  
    

    binary_result = binary_result.zfill(8)
    
    return binary_result
#ali el mahdaoui
examples = [
    ("0010", "0010"),
    ("00010001", "0001"),

    ("0110", "1001"),
    ("1011", "0010"),
    ("1111", "0101"),
    ("1100", "0100")
]


for bin1, bin2 in examples:
    result = binary_addition(bin1, bin2)
    print(f"{bin1} + {bin2} = {result}")
