# Critical Issues in Time Series Modeling

Here's a breakdown of critical issues in your time series modeling approach.

## Train/Test Split & Data Leakage

A primary concern is the non-chronological splitting of the data. For time series forecasting (from 2014-2024), it is crucial that the model is **never exposed to future data during training**.

-   **Data Leakage Example**: If you randomly shuffle all years to create a training and testing set, you are essentially using information from the future to predict the past. This will lead to deceptively high-performance metrics that do not reflect real-world performance.
-   **Correct Approach**: Always split the data chronologically. For instance:
    -   **Training Set**: 2014-2020
    -   **Validation Set**: 2021-2022
    -   **Test Set**: 2023-2024

## Dataset Structure & Per-Municipality Prediction

Each municipality exhibits its own unique temporal dynamics—some may be stable, others might be experiencing rapid growth, and some could be in decline.

-   **The Problem with a Single Model**: By training a single model on all municipalities without accounting for these individual trends, you risk:
    -   **Flattening Predictions**: The model may produce averaged-out forecasts that miss the specific volatility of each location.
    -   **Irrelevant Correlations**: The model might learn spurious relationships between different municipalities that are not meaningful.

## Feature Engineering

A potential issue is the use of "static" features, such as averages calculated over the entire period or variables that do not change from year to year. In time series analysis, you must **only use information that was known at a specific point in time (T)**.

-   **Warning**: Be cautious with features aggregated over the entire dataset, as they are a common source of data leakage.


## Model Selection

While **LightGBM** is a powerful model for standard tabular data, it is **not inherently a sequential model**. It does not capture time-dependent patterns as effectively as specialized time series models.

-   **More Suitable Alternatives**: For forecasting future values for individual time series (like each municipality), consider models designed for this purpose, such as:
    -   Prophet
    -   ARIMA
    -   LSTM (a type of recurrent neural network)

### Critique of the Forecast: Is the Trend Too Flat or Too Linear?

A key issue with the forecast is its overly simplistic nature. The model, particularly if it's Prophet, operates by **extrapolating the average slope of the preceding years**.

This leads to a few observations:

* **Lack of Dynamic Behavior**: The forecast shows no signs of a **rebound, plateau, or acceleration**. It simply extends the past trend forward.
* **Reflection of Historical Data**: This suggests that the historical data for this municipality between 2014 and 2024 was itself either very linear or had low volatility. The model is merely reflecting the simplicity of the data it was trained on.

**Conclusion**: While this approach is methodologically sound from a **"no data leakage"** perspective, the resulting forecast is likely **unrealistic**. Real-world trends are rarely this linear and are subject to shifts and changes that this simple extrapolation fails to capture.

## Validation and Evaluation

It appears there may not be a proper out-of-time validation strategy. It is essential to evaluate the model's performance exclusively on years that come *after* the training data.

-   **Example Workflow**:
    1.  Train the model on data up to 2021.
    2.  Validate its performance on 2022-2023 (to evaluate the model during tuning).
    3.  Test the final model on 2024 (to assess the model's ability to predict the true future).
    4.  Once validated, you can then proceed to forecast 2025 and beyond.

## Summary of Key Errors

-   **Data Leakage**: Caused by a non-chronological train/test split.
-   **Non-Causal Feature Engineering**: Using future information to construct features for past events.
-   **Biased Validation**: Evaluating the model without a proper out-of-time test set.

