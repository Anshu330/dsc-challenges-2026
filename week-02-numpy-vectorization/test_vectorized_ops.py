"""
test_vectorized_ops.py — Automated Unit Tests & Speed Benchmarks
Data Science Club (DSC KLE) — Sprint Challenge Week 2
"""

import time
import numpy as np
import pytest
from vectorized_ops import (
    STUDENT_USN,
    get_student_seed,
    euclidean_distance_loop,
    euclidean_distance_vectorized,
    pairwise_distance_matrix,
    fit_ols
)

def test_student_usn_configured():
    assert "XXXX" not in STUDENT_USN, (
        "Please update STUDENT_USN in vectorized_ops.py with your real university USN!"
    )

def test_euclidean_distance_correctness():
    seed = get_student_seed(STUDENT_USN)
    rng = np.random.default_rng(seed)
    
    a = rng.standard_normal(1000)
    b = rng.standard_normal(1000)
    
    dist_loop = euclidean_distance_loop(a, b)
    dist_vec = euclidean_distance_vectorized(a, b)
    
    assert np.isclose(dist_loop, dist_vec, rtol=1e-5), "Vectorized distance does not match mathematical ground truth!"

def test_vectorization_speedup():
    rng = np.random.default_rng(42)
    N = 500_000
    a = rng.standard_normal(N)
    b = rng.standard_normal(N)
    
    # Time loop
    t0 = time.perf_counter()
    _ = euclidean_distance_loop(a[:50_000], b[:50_000])  # smaller sample to avoid slow tests
    loop_time = (time.perf_counter() - t0) * 10  # extrapolate to 500k
    
    # Time vectorized
    t0 = time.perf_counter()
    _ = euclidean_distance_vectorized(a, b)
    vec_time = time.perf_counter() - t0
    
    speedup = loop_time / max(vec_time, 1e-6)
    print(f"\n[BENCHMARK] Loop: {loop_time*1000:.2f}ms | Vectorized: {vec_time*1000:.2f}ms | Speedup: {speedup:.1f}x")
    assert speedup >= 15.0, f"Vectorized operation was only {speedup:.1f}x faster. Ensure you are not using Python loops!"

def test_pairwise_distance_matrix_shape_and_values():
    X = np.array([
        [0.0, 0.0],
        [3.0, 0.0],
        [0.0, 4.0]
    ])
    
    dist_matrix = pairwise_distance_matrix(X)
    assert dist_matrix.shape == (3, 3), f"Expected shape (3, 3), got {dist_matrix.shape}"
    
    # Check known values
    assert np.isclose(dist_matrix[0, 1], 3.0)
    assert np.isclose(dist_matrix[0, 2], 4.0)
    assert np.isclose(dist_matrix[1, 2], 5.0)  # 3-4-5 right triangle!
    assert np.allclose(np.diag(dist_matrix), 0.0), "Diagonal distances must be 0!"

def test_fit_ols():
    rng = np.random.default_rng(123)
    N, D = 100, 3
    X = rng.standard_normal((N, D))
    true_theta = np.array([2.5, -1.2, 0.8])
    y = X @ true_theta + rng.normal(0, 0.01, size=N)
    
    estimated_theta = fit_ols(X, y)
    assert estimated_theta.shape == (D,), f"Expected weights shape ({D},), got {estimated_theta.shape}"
    assert np.allclose(estimated_theta, true_theta, atol=0.05), "OLS weights deviation exceeds tolerance!"
