import numpy as np

def generate_data_stream(length=1000, seasonal_period=80, noise_level=0.1):
    """Generates a stream of data with seasonal variations, noise, and occasional spikes to simulate real-world conditions."""
    
    time = np.arange(0, length)
    
    # Seasonal component with multiple harmonics to simulate complexity
    seasonal = np.sin(2 * np.pi * time / seasonal_period)  
    seasonal += 0.5 * np.sin(4 * np.pi * time / seasonal_period)   
    seasonal += 0.25 * np.sin(8 * np.pi * time / seasonal_period) 
    
    # Random noise
    noise = np.random.normal(0, noise_level, length)
    
    # Gradual upward trend
    trend = np.linspace(0,2, length)
    
    # Occasional spikes
    spikes = np.zeros(length)
    num_spikes = np.random.randint(1, 5)   
    spike_indices = np.random.choice(length, num_spikes, replace=False)
    spike_magnitudes = np.random.uniform(5, 10, num_spikes)   
    spikes[spike_indices] = spike_magnitudes
    
    # Combining all components
    data = seasonal + noise + trend + spikes

    #normalize data
    data = (data - np.mean(data)) / np.std(data)
    
    return data
