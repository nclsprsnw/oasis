# Modeling Approach for Real Estate Price Forecasting in France

## Objective

To forecast the evolution of the average price per square meter (€/m²) for every municipality in France over a 5-year period (2025-2029). The model relies exclusively on available historical data (2014-2024) and is designed to be **robust, transparent, and reproducible**.

## Data Used

* **Dataset**: A real-world database of property transactions from 2014 to 2024, aggregated by municipality.
* **Key Columns**:
    * INSEE municipal code
    * Year
    * Average price per square meter (€/m²)
    * Number of transactions
    * Latitude & Longitude
* **No External Data**: The model does not incorporate macroeconomic indicators or any speculative future forecasts.

## Approach and Pipeline

1. Data Cleaning and Dynamic Feature Engineering
For each municipality, the model reconstructs its history using dynamic variables:
* Average price per square meter from the last 1, 2, and 3 years (using lags and rolling means).
* Percentage change (%) over 1 and 2 years.
* Number of transactions and sales volume trends.
* **No Data Leakage**: Only data known at a specific point in time (T) is used, preventing any information from the future from influencing past predictions.

2. Strict Chronological Train/Validation/Test Split
* **Training Set**: 2014-2020
* **Validation Set**: 2021-2022 (to evaluate the model during tuning)
* **Test Set**: 2023-2024 (to assess the model's ability to predict the true future)

## Modeling

* **Chosen Model**: **LightGBM Regressor
    * **Why?** It is efficient, fast, and robust for both tabular data and time series applications.
* **Training Process**: The model is trained on all municipalities simultaneously, using only causal features from the past.
* **Evaluation**: Performance is measured on years the model has never seen, based on three key metrics:
    * **MAE** (Mean Absolute Error)
    * **RMSE** (Root Mean Square Error)
    * **R²** (Coefficient of Determination - measures the model's explanatory power)

## Forecasting the Future (2025-2029)

The model uses a **"rolling" forecast** method. Each year is predicted based on the previous year's data in a step-by-step fashion, mimicking a real-world, no-cheating scenario. This ensures the unique local dynamics of each municipality are respected.

## Results and Visualization

* **Output**: A price-per-square-meter forecast for every municipality for each year through 2029.
* **Interactive Map** (using Plotly/Folium):
    * Displays all of France.
    * On hovering over a municipality, the map shows:
        * The actual price in 2024.
        * All future predicted prices (2025-2029).
        * The percentage change (%) of the forecast.
    * A **heatmap or colored dots** are used to highlight dynamic zones (growth, stagnation, decline).

## Model Strengths and Limitations

### Strengths

* **Robust and Honest**: No data leakage or reliance on "magic" guesses.
* **Municipality-Specific**: The model learns the true local dynamics of different areas (e.g., Paris, its suburbs, rural zones).
* **Rigorously Evaluated**: Tested on a true future period (2023-2024).

### Limitations

* **No External Variables**: Does not account for socio-economic or geopolitical factors (unemployment, population, income, urban policy, etc.).
* **Cannot Predict Shocks**: Does not anticipate highly abnormal dynamics or external shocks (major crises, new housing policies, etc.).
* **Extrapolates Past Trends**: The model projects forward based on past behavior; it cannot predict a sudden break from a trend it has not yet observed.

## Conclusion

This model provides a powerful tool to:

1.  **Map and quantify** real estate dynamics at the local municipal level.
2.  **Deliver a realistic forecasting tool** based on actual history, which can be used by elected officials, industry professionals, or citizens.
3.  **Instantly visualize** areas of growth, stagnation, or decline in the property market.