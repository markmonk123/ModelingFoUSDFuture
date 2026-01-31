# ModelingFoUSDFuture

## Integrated Economic Model with Game Theory

A comprehensive economic modeling framework that integrates classical economic theory with modern game theory to predict macroeconomic impacts on GDP, inflation, interest rates, and dollar valuation.

### Theoretical Foundations

This model integrates three major theoretical frameworks:

1. **Adam Smith - The Invisible Hand & Market Equilibrium**
   - Self-interested actions leading to social benefit
   - Division of labor and specialization
   - Supply-demand equilibrium through market forces

2. **John Nash - Game Theory & Nash Equilibrium**
   - Strategic interaction between economic agents
   - Nash equilibrium in market competition
   - Non-cooperative game dynamics

3. **Bruce Bueno de Mesquita - Expected Utility Theory**
   - Predictive modeling based on stakeholder positions and power
   - Iterative bargaining and convergence
   - Coalition formation and policy consensus

### Features

- **Comprehensive Economic Modeling**: Integrates multiple economic theories into a unified framework
- **Macroeconomic Predictions**: Predicts GDP, inflation, interest rates, and dollar index values
- **Convergence Analysis**: Identifies equilibrium points across all theoretical models
- **Market Competition**: Models firm behavior using Nash equilibrium concepts
- **Policy Analysis**: Predicts policy outcomes using expected utility theory
- **Visualization Tools**: Creates comprehensive charts and graphs of model outputs

### Installation

1. Clone the repository:
```bash
git clone https://github.com/markmonk123/ModelingFoUSDFuture.git
cd ModelingFoUSDFuture
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Basic Usage

Run the integrated economic model:

```bash
python run_simulation.py
```

This will:
1. Initialize all sub-models (Smith, Nash, Bueno de Mesquita, Macroeconomic)
2. Run comprehensive analysis
3. Display convergence points for all models
4. Show macroeconomic impacts
5. Save results to `economic_model_results.json`

#### Create Visualizations

Generate visualization charts:

```bash
python visualizations.py
```

This creates:
- `macro_time_series.png` - GDP, inflation, interest rates, and dollar index over time
- `convergence_analysis.png` - Policy position convergence path
- `market_equilibrium.png` - Supply-demand curves with equilibrium point
- `convergence_summary.png` - Summary of all convergence points

#### Using Individual Modules

```python
from integrated_model import IntegratedEconomicModel

# Initialize model
model = IntegratedEconomicModel(num_agents=100, num_firms=10)

# Run specific analyses
market_results = model.model_market_competition()
policy_results = model.model_policy_consensus()
equilibrium_results = model.analyze_market_equilibrium()
macro_results = model.predict_macroeconomic_impacts(
    policy_position=50.0,
    market_efficiency=0.8
)

# Find all convergence points
all_results = model.find_all_convergence_points()
```

### Model Architecture

```
integrated_model.py
├── adam_smith_model.py          # Invisible hand, market equilibrium
├── nash_equilibrium_model.py    # Game theory, Nash equilibrium
├── bueno_mesquita_model.py      # Expected utility, policy prediction
└── macroeconomic_model.py       # GDP, inflation, interest rates, dollar
```

### Output Metrics

#### Convergence Points

1. **Market Nash Equilibrium**
   - Equilibrium price and quantity
   - Total welfare (consumer + producer surplus)
   - Market efficiency score

2. **Policy Convergence**
   - Predicted policy outcome position
   - Support ratio among stakeholders
   - Number of iterations to convergence

3. **Price Equilibrium**
   - Market clearing price
   - Market clearing quantity

4. **Macroeconomic Equilibrium**
   - Steady-state GDP
   - Steady-state inflation rate
   - Steady-state interest rate
   - Steady-state dollar index

#### Macroeconomic Impacts

- GDP time series and growth rate
- Inflation dynamics and volatility
- Interest rate path and volatility
- Dollar index movements

### Example Output

```
==================================================================
  CONVERGENCE POINTS ANALYSIS
==================================================================

1. Market Nash Equilibrium (Game Theory - John Nash)
   - Equilibrium Price: $42.37
   - Equilibrium Quantity: 47.63
   - Total Welfare: $1234.56

2. Policy Convergence (Expected Utility - Bruce Bueno de Mesquita)
   - Convergence Position: 52.34
   - Support Ratio: 67.3%
   - Iterations to Converge: 15

3. Price Equilibrium (Invisible Hand - Adam Smith)
   - Equilibrium Price: $51.42
   - Equilibrium Quantity: 53.71

4. Macroeconomic Equilibrium (Integrated Model)
   - GDP: $21,234.56 billion
   - Inflation Rate: 2.15%
   - Interest Rate: 3.45%
   - Dollar Index: 102.34
```

### Technical Details

#### Adam Smith Model

Implements:
- Market equilibrium calculation (supply-demand intersection)
- Invisible hand price adjustment mechanism
- Division of labor productivity gains
- Wealth distribution based on market participation

#### Nash Equilibrium Model

Implements:
- Pure and mixed strategy Nash equilibria
- Best response dynamics
- Cournot competition (quantity competition)
- Strategic stability analysis

#### Bueno de Mesquita Model

Implements:
- Expected utility calculations
- Weighted median voter theorem
- Iterative bargaining convergence
- Coalition formation analysis
- Scenario sensitivity analysis

#### Macroeconomic Model

Implements:
- GDP calculation (expenditure approach)
- Inflation modeling (quantity theory of money)
- Interest rate determination (Taylor Rule)
- Dollar valuation (purchasing power parity + interest differentials)
- Economic simulation over time

### Mathematical Framework

The model uses several key equations:

**GDP Growth**: GDP = C + I + G + NX (adjusted for productivity)

**Inflation**: π ≈ ΔM + ΔV - ΔY (quantity theory)

**Interest Rate**: r = r* + π + 0.5(π - π*) + 0.5(y - y*) (Taylor Rule)

**Nash Equilibrium**: No player can improve utility through unilateral deviation

**Expected Utility**: EU = Σ(power × salience × utility)

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

### License

MIT License

### References

- Smith, A. (1776). *The Wealth of Nations*
- Nash, J. (1950). *Equilibrium points in n-person games*
- Bueno de Mesquita, B. (2002). *Predicting Politics*
- Taylor, J. B. (1993). *Discretion versus policy rules in practice*

### Contact

For questions or feedback, please open an issue on GitHub.