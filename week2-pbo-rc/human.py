class Human:
    def __init__(self, alleles: str):
        self.__alleles = alleles
        self.__blood_types = self.__generate_blood_types()

    @property
    def blood_types(self):
        return self.__blood_types

    @property
    def alleles(self):
        return self.__alleles

    def __generate_blood_types(self):
        if self.__alleles == "AA":
            return "A" 
        elif self.__alleles == "AO" or self.__alleles == "OA":
            return "A"
        elif self.__alleles == "AB" or self.__alleles == "BA":
            return "AB"
        elif self.__alleles == "BB":
            return "B"
        elif self.__alleles == "BO" or self.__alleles == "OB":
            return "B"
        elif self.__alleles == "OO":
            return "O"