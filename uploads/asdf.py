n = int(input("Enter the number of rows: "))
s = input("symbol to use to generate pattern: ")
printed = None
print(f"\n\n {'-'*(round(n/2)+5)} Your Pattern {'-'*(round(n/2)+5)} \n\n")
for x in range(0, n*2, 2):
    if x >= n: times = n-(x-n+1)
    else: times = x+1
    string = " ".join([x for x in s*times])
    space_needed = " " * round((n*2-len(string))/2)
    final_string = space_needed + string
    if final_string != printed: print(final_string)
    printed = final_string
