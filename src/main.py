from data_stream import generate_data_stream
from knn_anomaly_detector import KNNAnomalyDetector
import matplotlib.pyplot as plt
 

if __name__ == "__main__":
    stream_length = 1000
    seasonal_period = 50
    noise_level = 0.2
    window_size = 50
    n_neighbors = 5
    threshold_percentile = 99

    # Generating the data stream
    data_stream = generate_data_stream(length=stream_length, seasonal_period=seasonal_period, noise_level=noise_level)

    knn_detector = KNNAnomalyDetector(window_size=window_size, n_neighbors=n_neighbors, threshold_percentile=threshold_percentile)

    # Initialize the plot for real-time visualization
    plt.ion()   
    fig, ax = plt.subplots(figsize=(10, 6))
    data_line, = ax.plot([], [], label="Data Stream", color='blue')
    anomaly_points, = ax.plot([], [], 'ro', label="Anomalies")  
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Real-Time Data Stream with Anomalies')
    plt.legend()
    plt.grid(True)
    
    data_points = []
    anomaly_x = []
    anomaly_y = []

    for i, point in enumerate(data_stream):
        # Append the new data point and find for anomaly
        data_points.append(point)
        is_anomaly, _ = knn_detector.detect_anomaly(point)
        if is_anomaly:
            anomaly_x.append(i)
            anomaly_y.append(point)
            print(f"Time {i}: Value {point}, Anomaly Detected")

        # Update the plot
        data_line.set_xdata(range(len(data_points)))
        data_line.set_ydata(data_points)
        anomaly_points.set_xdata(anomaly_x)
        anomaly_points.set_ydata(anomaly_y)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)  

    plt.ioff()   
    plt.show()  # Keep the plot open after processing all data

