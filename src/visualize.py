import matplotlib.pyplot as plt
import numpy as np

def visualize_stream(data, anomalies):
    """Visualizes the data stream with detected anomalies, including error handling and validation."""
    
    # Validate input data
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("The 'data' parameter must be a list or a numpy array.")
    if not isinstance(anomalies, dict):
        raise ValueError("The 'anomalies' parameter must be a dictionary with indices as keys and values as anomaly data points.")
    
    if len(data) == 0:
        raise ValueError("The 'data' array cannot be empty.")
    
    if any(not isinstance(i, (int, float)) for i in data):
        raise ValueError("All elements in 'data' must be numeric.")

    if any(not isinstance(k, int) or not isinstance(v, (int, float)) for k, v in anomalies.items()):
        raise ValueError("Anomalies keys must be integers (indices), and values must be numeric.")

    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data, label="Data Stream", color='blue')
        
        # Plot anomalies if there are any
        if anomalies:
            plt.scatter(anomalies.keys(), anomalies.values(), color='r', label="Anomalies", zorder=5)
        
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Real-Time Data Stream with Anomalies')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    except Exception as e:
        print(f" errror during vis: {e}")


 
