import math

# Deklarasi variabel float
angle = 45.0

# Konversi derajat ke radian
radian = math.radians(angle)

# Menghitung sinus, cosinus, dan tangen
sin_value = math.sin(radian)
cos_value = math.cos(radian)
tan_value = math.tan(radian)

print(f"Sinus dari {angle} derajat adalah {sin_value}")
print(f"Cosinus dari {angle} derajat adalah {cos_value}")
print(f"Tangen dari {angle} derajat adalah {tan_value}")