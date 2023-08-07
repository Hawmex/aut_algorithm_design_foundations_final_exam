# Principles of Algorithm Design

## Final Exam, Question 6

## Student Name

Hamed Araab

## Student Number

9925003

## Introduction

This documentation provides an overview of the code implementation for performing linear regression using the principles of Algorithm Design. The code defines a `LinearRegressor` class that fits a linear regression model to the given data and provides methods for prediction and evaluation.

## Code Structure

The code consists of the following components:

1. `LinearRegressor` class: Represents a linear regression model.
2. `__init__` method: Initializes the linear regression model by fitting the data and calculating coefficients, RMSE (Root Mean Square Error), and R2 score.
3. `coefficients` property: Returns the coefficients of the linear regression model.
4. `rmse` property: Returns the Root Mean Square Error (RMSE) of the linear regression model.
5. `r2` property: Returns the R2 score (coefficient of determination) of the linear regression model.
6. `_fit_scaler_X` method: Fits the scaler for input feature normalization.
7. `_fit_scaler_Y` method: Fits the scaler for target variable normalization.
8. `_normalize_X` method: Normalizes the input features using the fitted scaler.
9. `_normalize_Y` method: Normalizes the target variable using the fitted scaler.
10. `_undo_normalization_Y` method: Reverses the normalization of the target variable.
11. `predict` method: Predicts the target variable for a given set of input features.

## `LinearRegressor` Class

### Class Description

The `LinearRegressor` class represents a linear regression model. It provides methods for fitting the model to the given data, calculating model evaluation metrics, and making predictions.

### `__init__` Method

#### Method Description

The `__init__` method initializes the `LinearRegressor` object. It fits the data, calculates the coefficients, RMSE, and R2 score of the linear regression model.

#### Method Parameters

- `X`: The input features for the linear regression model.
- `Y`: The target variable for the linear regression model.

#### Method Steps

1. Convert the input features `X` and target variable `Y` to arrays.
2. Append a column of ones to the input features `X` to incorporate the intercept term in the linear regression model.
3. Fit the scaler for input feature normalization using the `_fit_scaler_X` method.
4. Normalize the input features `X` using the `_normalize_X` method.
5. Fit the scaler for target variable normalization using the `_fit_scaler_Y` method.
6. Normalize the target variable `Y` using the `_normalize_Y` method.
7. Calculate the coefficients of the linear regression model using the formula: `inv(X.T @ X) @ X.T @ Y`.
8. Perform prediction using the normalized input features `X` and the calculated coefficients.
9. Undo the normalization of the predicted target variable using the `_undo_normalization_Y` method.
10. Undo the normalization of the target variable `Y`.
11. Calculate the Root Mean Square Error (RMSE) using the formula: `((Y - Y_prediction) ** 2).mean() ** 0.5`.
12. Calculate the R2 score (coefficient of determination) using the formula: `1 - (((Y - Y_prediction) ** 2).sum() / ((Y - Y.mean()) ** 2).sum())`.

### `coefficients` Property

#### Property Description

The `coefficients` property returns the coefficients of the linear regression model.

### `rmse` Property

#### Property Description

The `rmse` property returns the Root Mean Square Error (RMSE) of the linear regression model.

### `r2` Property

#### Property Description

The `r2` property returns the R2 score (coefficient of determination) of the linear regression model.

### `_fit_scaler_X` Method

#### Method Description

The `_fit_scaler_X` method fits the scaler for input feature normalization.

#### Method Parameters

- `X`: The input features for the linear regression model.

#### Method Steps

1. Calculate the mean of the input features `X` and store it in the `_mean_X` variable.
2. Calculate the standard deviation of the input features `X` and store it in the `_std_X` variable.

### `_fit_scaler_Y` Method

#### Method Description

The `_fit_scaler_Y` method fits the scaler for target variable normalization.

#### Method Parameters

- `Y`: The target variable for the linear regression model.

#### Method Steps

1. Calculate the mean of the target variable `Y` and store it in the `_mean_Y` variable.
2. Calculate the standard deviation of the target variable `Y` and store it in the `_std_Y` variable.

### `_normalize_X` Method

#### Method Description

The `_normalize_X` method normalizes the input features using the fitted scaler.

#### Method Parameters

- `X`: The input features for the linear regression model.

#### Method Steps

1. Subtract the mean of the input features `_mean_X` from the input features `X`.
2. Divide the result by the standard deviation of the input features `_std_X`.
3. Return the normalized input features.

### `_normalize_Y` Method

#### Method Description

The `_normalize_Y` method normalizes the target variable using the fitted scaler.

#### Method Parameters

- `Y`: The target variable for the linear regression model.

#### Method Steps

1. Subtract the mean of the target variable `_mean_Y` from the target variable `Y`.
2. Divide the result by the standard deviation of the target variable `_std_Y`.
3. Return the normalized target variable.

### `_undo_normalization_Y` Method

#### Method Description

The `_undo_normalization_Y` method reverses the normalization of the target variable.

#### Method Parameters

- `Y`: The normalized target variable.

#### Method Steps

1. Multiply the normalized target variable `Y` by the standard deviation of the target variable `_std_Y`.
2. Add the mean of the target variable `_mean_Y`.
3. Return the unnormalized target variable.

### `predict` Method

#### Method Description

The `predict` method predicts the target variable for a given set of input features.

#### Method Parameters

- `X`: The input features for which to predict the target variable.

#### Method Steps

1. Convert the input features `X` to an array.
2. Append a column of ones to the input features `X` to incorporate the intercept term in the linear regression model.
3. Normalize the input features `X` using the `_normalize_X` method.
4. Perform prediction using the normalized input features `X` and the coefficients of the linear regression model.
5. Undo the normalization of the predicted target variable using the `_undo_normalization_Y` method.
6. Return the predicted target variable.

## Usage Example

```python
model1 = LinearRegressor(X[["sqft_living"]], Y)
print(f"R2: {model1.r2}")
print(f"RMSE: {model1.rmse}")

model2 = LinearRegressor(X, Y)
print(f"R2: {model2.r2}")
print(f"RMSE: {model2.rmse}")
```

The code creates two instances of the `LinearRegressor` class. The first instance (`model1`) fits a linear regression model using only the "sqft_living" feature from the input features `X` and the target variable`Y`. The second instance (`model2`) fits a linear regression model using all the input features from `X`and the target variable`Y`. The R2 score and RMSE are then printed for both models.
