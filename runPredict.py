from math import radians, sin, cos, sqrt, atan2
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from PIL import Image, ImageDraw
import time


# Function to calculate haversine distance
def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius = 6371000.0  # Radius of the Earth in meters
    distance = radius * c
    return distance


# Initialize start_time outside the loop
start_time = time.time()

# Initialize an empty list to store the results
results_list = []

# Initialize total_distance and total_time_count outside the loop
total_distance = 0
total_time_count = 0

# Initialize coordinates_list
coordinates_list = []

# Initialize variables to track consecutive predictions and travel times
previous_prediction = None
consecutive_predictions = 0
previous_travel_time = 0
traffic_detected = False

# Load model
model = load_model('/CareCarb-ML/ImprovedTransportModel.h5')
scaler = np.load('/CareCarb-ML/scaler.npy', allow_pickle=True).item()
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('/CareCarb-ML/label_encoder_classes.npy', allow_pickle=True)

# Continuous loop
while True:
    total_time_count = 0

    input_coordinates = input('Enter coordinates: ') # GANTI SESUAI METODE COLLECT COORDINATE

    iteration_end_time = time.time()

    iteration_time = iteration_end_time - start_time

    total_time_count += iteration_time

    lat, lon = map(float, input_coordinates.split(','))

    coordinates_list.append({'Latitude': lat, 'Longitude': lon})

    if len(coordinates_list) > 1:
        current_coordinates = coordinates_list[-1]
        previous_coordinates = coordinates_list[-2]
        distance = haversine_distance(
            current_coordinates['Latitude'], current_coordinates['Longitude'],
            previous_coordinates['Latitude'], previous_coordinates['Longitude']
        )
        total_distance += distance

        total_time_count_minutes = total_time_count / 60.0

        print(f'Distance: {total_distance:.2f} meters for {total_time_count_minutes:.2f} minutes')

        if total_distance >= 800:
            new_data = {'Distance': [total_distance], 'TravelTime': [total_time_count_minutes]}
            new_df = pd.DataFrame(new_data)

            # Standardize features
            new_data_scaled = scaler.transform(new_df)

            # Predict
            predictions = model.predict(new_data_scaled)
            predicted_class_index = predictions.argmax(axis=1)[0]
            predicted_transportation = label_encoder.classes_[predicted_class_index]

            # Check if the prediction is consistent for the last 5 iterations
            if consecutive_predictions < 3 or predicted_transportation == previous_prediction:
                consecutive_predictions += 1
            else:
                consecutive_predictions = 1  # Reset if the prediction changes
                traffic_detected = False

            # Check if there is a significant change in travel time
            if consecutive_predictions == 3 and not traffic_detected:
                travel_time_change = total_time_count_minutes - previous_travel_time
                if travel_time_change > 1:  # Adjust this threshold as needed
                    traffic_detected = True
                    print(f'Traffic detected! Travel time increased by {travel_time_change:.2f} minutes.')

            # Store the results in the list
            results_list.append({
                'Origin': previous_coordinates,
                'Destination': current_coordinates,
                'Distance': total_distance,
                'TravelTime': total_time_count_minutes,
                'PredictedTransportation': predicted_transportation
            })

            print(f'Predicted Transportation: {predicted_transportation}')

            # Reset total_distance and total_time_count after each prediction
            total_distance = 0
            total_time_count = 0

            # Convert the results list to a DataFrame
            results_df = pd.DataFrame(results_list)

            # Save the results to a CSV file
            results_df.to_csv('predicted_results.csv', index=False)
            # Update the start_time for the next iteration
            start_time = time.time()
            # Update the previous prediction for the next iteration
            previous_prediction = predicted_transportation
            previous_travel_time = total_time_count_minutes
