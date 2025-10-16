import matplotlib.pyplot as plt

alpha = [i/10 for i in range(0, 11)]

I1_max, I1_min = 120, -20
I2_max, I2_min = 100, 10
I3_max, I3_min = 160, -80

I1 = [a*I1_max + (1-a)*I1_min for a in alpha]
I2 = [a*I2_max + (1-a)*I2_min for a in alpha]
I3 = [a*I3_max + (1-a)*I3_min for a in alpha]

plt.plot(alpha, I1, marker='o', label='І₁')
plt.plot(alpha, I2, marker='o', label='І₂')
plt.plot(alpha, I3, marker='o', label='І₃')

plt.title('Залежність рішення від коефіцієнта оптимізму α (Критерій Гурвіца)')
plt.xlabel('α (коефіцієнт оптимізму)')
plt.ylabel('Hᵢ (узагальнений результат, тис. грн)')
plt.legend()
plt.grid(True)
plt.show()