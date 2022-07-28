class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        sum_complex = complex(new_real, new_imaginary)
        return sum_complex

    def __mul__(self, other):
        new_real_m = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary_m = self.imaginary * other.real + self.real * other.imaginary
        mult_complex = complex(new_real_m, new_imaginary_m)
        return mult_complex

cn_1 = ComplexNumber(2, 3)
cn_2 = ComplexNumber(3, 4)

print(cn_1 + cn_2)
print(cn_1 * cn_2)
