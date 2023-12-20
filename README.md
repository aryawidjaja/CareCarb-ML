# CareCarb - Carbon Footprint Tracker App
![CareCarb Logo](https://github.com/aryawidjaja/CareCarb-ML/assets/130090399/2e70fbc0-c795-45c4-a494-c5c968778a02)

CareCarb is an innovative mobile application designed to help users track and manage their carbon footprint. The app utilizes a multi-class classifier machine learning algorithm to predict the carbon footprint associated with both transportation and food consumption. By providing insights and recommendations, CareCarb empowers users to make environmentally conscious choices and reduce their overall impact on the planet.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Account Creation and Login](#account-creation-and-login)
  - [Vehicle Input](#vehicle-input)
  - [Homepage](#homepage)
  - [Transportation Tracking](#transportation-tracking)
  - [Food Carbon Footprint Tracking](#food-carbon-footprint-tracking)
  - [Recommendations](#recommendations)
- [Machine Learning Model](#machine-learning-model)
  - [Download Model](#download-model)
  - [Required Files](#required-files)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following dependencies installed:

- [Python](https://www.python.org/) (version 3.9.13)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

### Installation

1. Clone the CareCarb repository to your local machine:

   ```bash
   git clone https://github.com/aryawidjaja/CareCarb-ML.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CareCarb-ML
   ```

3. Create a virtual environment:

   ```bash
   virtualenv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Account Creation and Login

- Users can create an account or log in using their existing credentials.

### Vehicle Input

- After logging in, users can input details about the vehicles they own.

### Homepage

- The homepage provides an overview of the user's carbon footprint, including both transportation and food-related emissions.

### Transportation Tracking

- Users can enable location access permission to automatically track their transportation carbon footprint.

### Food Carbon Footprint Tracking

- Users can upload images of their food to track the associated carbon footprint.

### Recommendations

- CareCarb provides personalized recommendations based on the user's carbon habits.

## Machine Learning Model

### Download Model

- The machine learning model can be downloaded from the [CareCarb Transport Model](https://github.com/aryawidjaja/CareCarb-ML/blob/main/ImprovedTransportModel.h5).

### Required Files

- Ensure that the following files are available in your project directory:
  - `ImprovedTransportationModel.h5`
  - `scaler.npy`
  - `label_encoder_classes.npy`
  - `user_data.csv`
  - `emission.csv`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to CareCarb team for their contributions to CareCarb.
- Hat tip to anyone whose code was used.
- Inspiration for the project.
