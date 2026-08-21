import matplotlib.pyplot as plt

# Do vectors
vector_a = [2, 3]
vector_b = [1, -2]

# Addition
vector_sum = [vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]]

# Plot
plt.quiver(0, 0, vector_a[0], vector_a[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector A [2,3]')
plt.quiver(0, 0, vector_b[0], vector_b[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector B [1,-2]')
plt.quiver(0, 0, vector_sum[0], vector_sum[1], angles='xy', scale_units='xy', scale=1, color='g', label=f'Sum {vector_sum}')

plt.xlim(-1, 5)
plt.ylim(-3, 5)
plt.grid()
plt.legend()
plt.title("My First Vector Addition - vision_lab")
plt.show()

print(f"Vector A + Vector B = {vector_sum}")
