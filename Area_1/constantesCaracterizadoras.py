def bin_para_decimal(bin_str):
    if '.' not in bin_str:
        return int(bin_str, 2)
    
    inteira, fracionaria = bin_str.split('.')
    decimal = int(inteira, 2)
    
    for i, digito in enumerate(fracionaria):
        decimal += int(digito) * (2 ** -(i + 1))
        
    return decimal

def ponto_fixo():
    print("Enter |E|.")
    E = int(input())
    print("Enter |D|.")
    D = int(input())
    
    p = E + D
    print(f"p = {p}")
    minr = bin_para_decimal('0' * E + '.' + '0' * (D - 1) + '1')
    print(f"MINR = {minr:.{D}f}")
    maxr = bin_para_decimal('1' * E + '.' + '1' * D)
    print(f"MAXR = {maxr:.{D}f}")
    
    ulp = minr
    print(f"ULP = {ulp}")
    print(f"epsilon = {ulp}")

def ponto_flutuante():
    print("Enter base (b)")
    b = int(input())
    print("Enter mantissa bits (M)")
    M = int(input())
    print("Enter exponent bits (E)")
    E = int(input())
    
    p = abs(M) + 1
    print(f"p = {p}")
    mine = - (2 ** E - 1)
    print(f"MINE = {mine}")
    maxe = (2 ** E - 1)
    print(f"MAXE = {maxe}")
    minr = 0.5 * (b ** mine)
    print(f"MINR = {minr:.{maxe + 1}f}")
    maxr = (1 - b ** (-(M + 1))) * (b ** maxe)
    print(f"MAXR = {maxr:.{maxe + 1}f}")
    ulp = (2 ** -p) * (2 ** E)
    print(f"ULP = {ulp}")
    epsilon = 2 ** -(p + 1)
    print(f"epsilon = {epsilon}")
    
    
def main():
    print("ponto fixo ou ponto flutuante?")
    choice = input().strip().lower()
    if choice == 'ponto fixo':
        ponto_fixo()
    else:
        ponto_flutuante()
    
if __name__ == "__main__":
    main()