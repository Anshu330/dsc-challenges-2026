# ⚡ Week 2 Sprint Challenge: High-Performance Vectorized Computing with NumPy
> **Track**: Credit Track (2nd Year) & Growth Track (1st Year)  
> **Deadline**: Sunday, November 29, 2026 @ 11:59 PM IST  
> **Submission Platform**: DSC Nexus (`/modules` → Week 2)

---

## 🎯 Learning Objectives
1. Understand why vectorized C-arrays in NumPy are 50–100x faster than standard Python `for` loops.
2. Master multi-dimensional array broadcasting mechanics without allocating redundant memory.
3. Implement mathematical algorithms from scratch: Pairwise Euclidean Distances, Sobel Edge Filters, and Ordinary Least Squares ($\theta = (X^T X)^{-1} X^T y$).
4. Pass automated unit tests with unique **USN-seeded checksum verification** to prevent copy-pasting.

---

## 📋 Hands-On Challenge Tasks

### Task 1: USN-Seeded Synthetic Benchmark (`vectorized_ops.py`)
1. Open `vectorized_ops.py` and set your `STUDENT_USN`.
2. Implement `euclidean_distance_loop()` and `euclidean_distance_vectorized()`.
3. The test suite verifies that your vectorized implementation is at least **20x faster** than the loop on $10^6$ elements!

### Task 2: Pairwise Distance Matrix via Broadcasting
- Implement `pairwise_distance_matrix(X)` without any Python loops using the identity:
  $$\|a - b\|^2 = \|a\|^2 + \|b\|^2 - 2 \langle a, b \rangle$$
- Verify that your matrix shape is strictly $(N, N)$.

### Task 3: Ordinary Least Squares (OLS) Closed-Form
- Implement `fit_ols(X, y)` using `np.linalg.pinv` or `np.linalg.solve` to compute weights without `sklearn`.

### Task 4: Run the Auto-Test Suite
```bash
# Run tests with pytest
pytest test_vectorized_ops.py -v
```
All unit tests and speed benchmark assertions must pass before submitting on DSC Nexus.
