# Spam Classifier

This project is a machine learning-based spam classifier that uses the RandomForestClassifier algorithm to identify spam messages from the SMS Spam Collection Dataset provided by UCI Machine Learning Repository. The model achieves a precision score of 1 and an accuracy of 97.71%. The project is implemented in Python, utilizing the scikit-learn and Streamlit packages.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to develop a spam classifier that can accurately distinguish between spam and legitimate messages. The classifier is built using the RandomForestClassifier algorithm from the scikit-learn library. A Streamlit application is also provided to interact with the model through a web interface.

## Dataset

The dataset used in this project is the SMS Spam Collection Dataset by UCI Machine Learning Repository. It consists of 5,574 SMS messages, which are labeled as either 'spam' or 'ham' (legitimate).

- **Source:** [UCI Machine Learning Repository: SMS Spam Collection Data Set](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

## Installation

To run this project, ensure you have Python installed on your system. Then, follow the steps below:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/spam-classifier.git
    cd spam-classifier
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application:

1. Start the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to use the spam classifier interface.

3. Enter an SMS message into the text box and click the 'Classify' button to see if it is classified as spam or ham.

## Model Performance

The performance of the RandomForestClassifier on the SMS Spam Collection Dataset is as follows:

- **Precision:** 1
- **Accuracy:** 97.71%

These metrics indicate that the model is highly effective at distinguishing between spam and legitimate messages.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
