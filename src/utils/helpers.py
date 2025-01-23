def log_metrics(metrics, epoch):
    """Logs training metrics for a given epoch."""
    print(f"Epoch {epoch}: {metrics}")

def save_model(model, filepath):
    """Saves the trained model to the specified filepath."""
    import joblib
    joblib.dump(model, filepath)