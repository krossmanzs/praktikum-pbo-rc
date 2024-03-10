from human import Human
import random

class Child(Human):
    def __init__(self, father: Human, mother: Human):
        self.__father = father
        self.__mother = mother
        super().__init__(self.__generate_child_alleles())

    def __generate_child_alleles(self):
        father_rate = random.randrange(1,100)
        mother_rate = random.randrange(1,100)

        child_alleles = str()

        # get father's first allele
        if father_rate <= 50:
            child_alleles += self.__father.alleles[0]
        else:
            child_alleles += self.__father.alleles[1]

        # get mother's allele
        if mother_rate <= 50:
            child_alleles += self.__mother.alleles[0]
        else:
            child_alleles += self.__mother.alleles[1]

        return child_alleles