"""
vectorized_ops.py — High-Performance NumPy Mathematical Kernels
Data Science Club (DSC KLE) — Sprint Challenge Week 2

Instructions for Recruits:
1. Update STUDENT_USN with your KLE USN.
2. Complete the functions marked with # TODO.
3. Test using `pytest test_vectorized_ops.py -v`.
"""

import hashlib
import numpy as np

# ==============================================================================
# RECRUIT IDENTIFIER
# ==============================================================================
STUDENT_USN = "01FEXXXXXXXX"  # e.g., "01FE25BCS122"


def get_student_seed(usn: str) -> int:
    """Generates a deterministic integer seed from a student USN."""
    h = hashlib.md5(usn.strip().upper().encode("utf-8")).hexdigest()
    return int(h[:8], 16) % 100000


def euclidean_distance_loop(a: np.ndarray, b: np.ndarray) -> float:
    """Computes Euclidean distance using pure Python loops (slow baseline)."""
    assert len(a) == len(b)
    total = 0.0
    for i in range(len(a)):
        diff = a[i] - b[i]
        total += diff * diff
    return float(total ** 0.5)


def euclidean_distance_vectorized(a: np.ndarray, b: np.ndarray) -> float:
    """
    Computes Euclidean distance using vectorized NumPy operations.
    Must be 20x-100x faster than euclidean_distance_loop.
    """
    # TODO: Implement using np.linalg.norm or vector subtraction + np.sum
    return float(np.linalg.norm(a - b))


def pairwise_distance_matrix(X: np.ndarray) -> np.ndarray:
    """
    Computes all pairwise Euclidean distances between N points in D dimensions.
    
    Args:
        X (np.ndarray): Shape (N, D)
        
    Returns:
        np.ndarray: Pairwise distance matrix of shape (N, N).
                    Must NOT use any Python for loops!
    """
    # TODO: Implement via broadcasting: (X[:, np.newaxis, :] - X[np.newaxis, :, :])
    diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
    return np.sqrt(np.sum(diff ** 2, axis=-1))


def fit_ols(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Computes Ordinary Least Squares weights theta = (X^T X)^{-1} X^T y.
    
    Args:
        X (np.ndarray): Shape (N, D) design matrix (including intercept column)
        y (np.ndarray): Shape (N,) or (N, 1) target vector
        
    Returns:
        np.ndarray: Parameter weights theta of shape (D,)
    """
    # TODO: Implement closed-form OLS using np.linalg.pinv and np.dot
    theta = np.linalg.pinv(X.T @ X) @ X.T @ y
    return theta.flatten()
