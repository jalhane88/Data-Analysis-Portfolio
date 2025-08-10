
# ==============================================================================
# ml_utils.py - Reusable Machine Learning Functions
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import (
    mean_squared_error, r2_score,
    accuracy_score, classification_report, confusion_matrix,
    roc_curve, auc
)


# === UNIVERSAL FUNCTIONS ===
def create_preprocessor(numerical_features, categorical_features):
    """Creates a scikit-learn preprocessor pipeline for numerical and categorical data."""
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
        ],
        remainder='passthrough'
    )
    return preprocessor


# === REGRESSION FUNCTIONS (REFACTORED) ===
def evaluate_regressor(y_true, y_pred, model_name="Model", log_transformed=False):
    """
    Calculates metrics and plots a Residual Plot and Predicted vs. Actual Plot side-by-side.
    """
    print(f"--- {model_name} Evaluation ---")

    y_true_eval = np.expm1(y_true) if log_transformed else y_true
    y_pred_eval = np.expm1(y_pred) if log_transformed else y_pred
    if log_transformed: print("Note: Metrics are on the back-transformed scale.")

    rmse = np.sqrt(mean_squared_error(y_true_eval, y_pred_eval))
    r2 = r2_score(y_true_eval, y_pred_eval)

    print(f"R-squared (R²): {r2:.4f}")
    print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")

    # --- Create a figure with two subplots (side-by-side) ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    fig.suptitle(f'Diagnostic Plots for {model_name}', fontsize=16)

    # --- Plot 1: Residual Plot ---
    residuals = y_true_eval - y_pred_eval
    sns.scatterplot(x=y_pred_eval, y=residuals, ax=ax1, alpha=0.6)
    ax1.axhline(0, color='red', linestyle='--')
    ax1.set_xlabel('Predicted Values')
    ax1.set_ylabel('Residuals')
    ax1.set_title('Residual Plot')
    ax1.grid(True)

    # --- Plot 2: Predicted vs. Actual Plot ---
    sns.scatterplot(x=y_true_eval, y=y_pred_eval, ax=ax2, alpha=0.6)
    perfect_line = np.linspace(min(y_true_eval.min(), y_pred_eval.min()),
                               max(y_true_eval.max(), y_pred_eval.max()), 100)
    ax2.plot(perfect_line, perfect_line, color='red', linestyle='--', label='Perfect Prediction')
    ax2.set_xlabel('Actual Values')
    ax2.set_ylabel('Predicted Values')
    ax2.set_title('Predicted vs. Actual Values')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    return rmse, r2


# === CLASSIFICATION FUNCTIONS (REFACTORED) ===
def evaluate_classifier(y_true, y_pred, y_pred_proba, model_name="Model"):
    """
    Calculates metrics and plots a Confusion Matrix and ROC Curve side-by-side.
    """
    print(f"--- {model_name} Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, zero_division=0))

    # --- Create a figure with two subplots (side-by-side) ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))
    fig.suptitle(f'Evaluation Plots for {model_name}', fontsize=16)

    # --- Plot 1: Confusion Matrix ---
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['No Churn', 'Churn'], yticklabels=['No Churn', 'Churn'],
                ax=ax1)
    ax1.set_title('Confusion Matrix')
    ax1.set_xlabel('Predicted Label')
    ax1.set_ylabel('True Label')

    # --- Plot 2: ROC Curve ---
    fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    ax2.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    ax2.set_xlabel('False Positive Rate')
    ax2.set_ylabel('True Positive Rate')
    ax2.set_title('Receiver Operating Characteristic (ROC) Curve')
    ax2.legend(loc="lower right")
    ax2.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    plt.show()
