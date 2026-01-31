# Quick Start Guide

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/markmonk123/ModelingFoUSDFuture.git
   cd ModelingFoUSDFuture
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Model

### Option 1: Run Full Simulation (Recommended for First Use)

```bash
python run_simulation.py
```

This will:
- Run the complete integrated economic model
- Display all convergence points
- Show macroeconomic impacts
- Save results to `economic_model_results.json`

### Option 2: Generate Visualizations

```bash
python visualizations.py
```

This creates:
- `macro_time_series.png` - Time series of all macroeconomic indicators
- `convergence_analysis.png` - Policy convergence path
- `market_equilibrium.png` - Supply-demand equilibrium
- `convergence_summary.png` - Summary of all convergence points

### Option 3: Run Examples

```bash
python examples.py
```

This demonstrates:
- Basic model usage
- Market competition analysis
- Policy scenario testing
- Individual model components
- Convergence analysis

## Understanding the Output

### Convergence Points

The model identifies four types of convergence:

1. **Market Nash Equilibrium** - Where firms reach competitive equilibrium
2. **Policy Convergence** - Where stakeholders reach consensus
3. **Price Equilibrium** - Where supply equals demand
4. **Macroeconomic Equilibrium** - Long-run steady state values

### Key Metrics

- **GDP**: Gross Domestic Product in billions
- **Inflation Rate**: Annual percentage change in price level
- **Interest Rate**: Federal funds rate or policy rate
- **Dollar Index**: Currency strength (100 = baseline)
- **Market Efficiency**: How close to optimal welfare
- **Policy Support**: Percentage of stakeholders supporting outcome

## Using the Model Programmatically

### Basic Usage

```python
from integrated_model import IntegratedEconomicModel

# Initialize model
model = IntegratedEconomicModel(num_agents=100, num_firms=10)

# Run analysis
results = model.comprehensive_analysis()

# Access results
print(f"GDP: ${results['convergence_points']['macroeconomic_equilibrium']['gdp']:.2f}B")
print(f"Inflation: {results['convergence_points']['macroeconomic_equilibrium']['inflation']:.2f}%")
```

### Analyzing Market Competition

```python
# Compare different market structures
market_results = model.model_market_competition(num_firms=10)
print(f"Market Price: ${market_results['market_price']:.2f}")
print(f"Efficiency: {market_results['market_efficiency']:.2%}")
```

### Policy Analysis

```python
# Test policy scenarios
macro_results = model.predict_macroeconomic_impacts(
    policy_position=60,  # 0=restrictive, 100=expansionary
    market_efficiency=0.8
)
print(f"GDP Growth: {macro_results['gdp_growth_rate']:.2f}%")
```

### Finding Convergence

```python
# Get all convergence points
all_results = model.find_all_convergence_points()
convergence = all_results['convergence_points']

# Access specific convergence values
nash_price = convergence['market_nash_equilibrium']['price']
policy_position = convergence['policy_convergence']['position']
```

## Understanding the Theory

### Adam Smith - Invisible Hand
- Self-interested actions lead to social benefit
- Markets naturally move toward equilibrium
- Division of labor increases productivity

### John Nash - Game Theory
- Strategic interaction between agents
- Nash equilibrium: no one can improve by changing strategy alone
- Models competition and cooperation

### Bruce Bueno de Mesquita - Expected Utility
- Actors have positions, power, and preferences
- Predictions based on weighted stakeholder analysis
- Iterative bargaining leads to convergence

## Customizing the Model

### Adjust Initial Parameters

```python
from macroeconomic_model import MacroeconomicModel

# Custom starting values
macro = MacroeconomicModel(
    initial_gdp=25000.0,      # $25 trillion
    initial_inflation=3.0,     # 3%
    initial_interest_rate=4.0, # 4%
    initial_dollar_index=105.0 # 105
)
```

### Run Custom Simulations

```python
# Simulate with shocks
results = macro.simulate_economy(
    periods=100,
    shock_params={
        'money_shock': 0.02,      # 2% increase in money supply
        'productivity_shock': 0.01 # 1% productivity increase
    }
)
```

### Create Custom Visualizations

```python
from visualizations import EconomicVisualizer

visualizer = EconomicVisualizer()
visualizer.plot_macroeconomic_time_series(
    time_series_data,
    filename='my_custom_plot.png'
)
```

## Interpreting Results

### High Market Efficiency (>80%)
- Markets are functioning well
- Competition is healthy
- Resources allocated efficiently

### Low Policy Support (<50%)
- Policy faces opposition
- May need adjustment
- Consider coalition building

### Inflation Near Target (~2%)
- Economy is balanced
- Monetary policy effective
- Stable growth expected

### Rising Dollar Index
- Strong currency
- High interest rates or low inflation
- May impact exports

## Common Issues

### Import Errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Numerical Warnings
The model includes safeguards against overflow. Warnings are normal for extreme scenarios.

### Visualization Issues
Ensure matplotlib is properly configured:
```bash
pip install --upgrade matplotlib
```

## Next Steps

1. **Experiment**: Try different parameters and scenarios
2. **Extend**: Add your own economic indicators or models
3. **Analyze**: Use the results for research or decision-making
4. **Visualize**: Create custom charts for your specific needs

## Support

For questions or issues, please open an issue on GitHub:
https://github.com/markmonk123/ModelingFoUSDFuture/issues
