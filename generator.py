def generate_synthetic_data(
    df: pd.DataFrame,
    sensitive_features: list = [],
    target_col: str = None,
    method: str = 'ctgan',
    sample_size: int = None,
    fairness_boost: bool = True
) -> pd.DataFrame:
    """
    Generate synthetic data with optional fairness adjustments.

    Parameters:
    - df: Input DataFrame
    - sensitive_features: List of sensitive columns
    - target_col: Classification/regression label
    - method: 'ctgan' | 'copula'
    - sample_size: Optional size of output
    - fairness_boost: Whether to balance representation

    Returns:
    - Synthetic DataFrame
    """
