from child import Child
from mother import Mother
from father import Father

print(f"{'='*59}")
print(f"{'='*10} Child Blood Types Inheritance Program {'='*10}")

while True:
    print(f"{'='*59}")
    father_alleles = input("Enter the father's allele: ")
    mother_alleles = input("Enter the mother's allele: ")
    f1 = Father(father_alleles)
    m1 = Mother(mother_alleles)
    c1 = Child(f1,m1)
    print(f"Child's allele: {c1.alleles}")
    print(f"Child's blood type: {c1.blood_types}")

    c = input("Input again? (y/n): ").lower()

    if c == "n":
        print("Thank you, have a good day ^^")
        break

print(f"{'='*59}")