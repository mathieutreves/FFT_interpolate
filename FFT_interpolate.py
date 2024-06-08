import numpy as np

def calculate_X_k(X, N, N2):
    """
    Calculate X(k) based on the given formula.

    Parameters:
    X (numpy array): Input sequence.
    N (int): Length of the sequence.
    N2 (int): new length

    Returns:
    numpy array: Calculated X(k) values.
    """

    k = np.linspace(0, N, num=N2)
    X_k = np.zeros(N2, dtype=complex)
    for i in range(N2):
        sum_term = 0
        for m in range(N):
            numerator = X[m]
            denominator = 1 - np.exp(-2j * np.pi * (k[i] - m) / N)
            if denominator != 0:  # Avoid division by zero
                sum_term += numerator / denominator
        X_k[i] = (1 - np.exp(-2j * np.pi * k[i])) / N * sum_term
    return X_k