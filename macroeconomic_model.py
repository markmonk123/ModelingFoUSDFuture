"""
Macroeconomic Indicators Module
This module models key macroeconomic indicators including GDP, inflation,
interest rates, and dollar value.
"""

import numpy as np
from typing import Dict, Tuple

class MacroeconomicModel:
    """
    Models macroeconomic indicators and their interactions:
    - GDP growth and factors
    - Inflation dynamics
    - Interest rate determination
    - Currency (dollar) valuation
    """
    
    def __init__(self, initial_gdp: float = 20000.0, initial_inflation: float = 2.0,
                 initial_interest_rate: float = 2.5, initial_dollar_index: float = 100.0):
        """
        Initialize macroeconomic model with base values.
        
        Args:
            initial_gdp: Initial GDP in billions
            initial_inflation: Initial inflation rate (%)
            initial_interest_rate: Initial interest rate (%)
            initial_dollar_index: Initial dollar index (100 = baseline)
        """
        self.gdp = initial_gdp
        self.inflation = initial_inflation
        self.interest_rate = initial_interest_rate
        self.dollar_index = initial_dollar_index
        
    def calculate_gdp_growth(self, investment: float, consumption: float,
                           government_spending: float, net_exports: float,
                           productivity_growth: float) -> Tuple[float, float]:
        """
        Calculate GDP growth using expenditure approach and productivity.
        
        Args:
            investment: Investment spending
            consumption: Consumer spending
            government_spending: Government spending
            net_exports: Net exports (exports - imports)
            productivity_growth: Productivity growth rate
            
        Returns:
            Tuple of (new GDP, GDP growth rate)
        """
        # GDP = C + I + G + NX
        new_gdp = consumption + investment + government_spending + net_exports
        
        # Adjust for productivity
        new_gdp *= (1 + productivity_growth)
        
        # Calculate growth rate
        gdp_growth_rate = ((new_gdp - self.gdp) / self.gdp) * 100
        
        return new_gdp, gdp_growth_rate
    
    def calculate_inflation(self, money_supply_growth: float, gdp_growth: float,
                           velocity_change: float = 0.0) -> float:
        """
        Calculate inflation using quantity theory of money and demand-pull factors.
        
        Args:
            money_supply_growth: Growth rate of money supply (%)
            gdp_growth: GDP growth rate (%)
            velocity_change: Change in velocity of money (%)
            
        Returns:
            Inflation rate (%)
        """
        # Quantity theory: MV = PY
        # Inflation ≈ money_growth + velocity_change - real_gdp_growth
        inflation = money_supply_growth + velocity_change - gdp_growth
        
        # Add demand-pull component
        if gdp_growth > 3.0:  # Strong growth creates inflation pressure
            inflation += (gdp_growth - 3.0) * 0.5
        
        # Floor at -2% (deflation limit)
        inflation = max(inflation, -2.0)
        
        return inflation
    
    def calculate_interest_rate(self, inflation: float, gdp_growth: float,
                               unemployment_rate: float,
                               natural_rate: float = 2.5) -> float:
        """
        Calculate interest rate using Taylor Rule.
        
        Args:
            inflation: Current inflation rate (%)
            gdp_growth: GDP growth rate (%)
            unemployment_rate: Unemployment rate (%)
            natural_rate: Natural/neutral interest rate (%)
            
        Returns:
            Target interest rate (%)
        """
        # Taylor Rule: r = r* + π + 0.5(π - π*) + 0.5(y - y*)
        target_inflation = 2.0
        target_growth = 2.5
        
        # Inflation gap
        inflation_gap = inflation - target_inflation
        
        # Output gap (approximated by GDP growth vs target)
        output_gap = gdp_growth - target_growth
        
        # Taylor rule calculation
        interest_rate = (natural_rate + inflation + 
                        0.5 * inflation_gap + 
                        0.5 * output_gap)
        
        # Adjust for unemployment (Phillips curve relationship)
        natural_unemployment = 4.5
        unemployment_gap = unemployment_rate - natural_unemployment
        interest_rate -= 0.3 * unemployment_gap
        
        # Floor at 0% (zero lower bound)
        interest_rate = max(interest_rate, 0.0)
        
        return interest_rate
    
    def calculate_dollar_value(self, interest_rate: float, inflation: float,
                              trade_balance: float, foreign_interest_rate: float = 2.0,
                              foreign_inflation: float = 2.0) -> float:
        """
        Calculate dollar index value based on economic factors.
        
        Args:
            interest_rate: Domestic interest rate (%)
            inflation: Domestic inflation rate (%)
            trade_balance: Trade balance (positive = surplus)
            foreign_interest_rate: Average foreign interest rate (%)
            foreign_inflation: Average foreign inflation rate (%)
            
        Returns:
            Dollar index value (100 = baseline)
        """
        # Interest rate differential (higher rates strengthen currency)
        rate_differential = interest_rate - foreign_interest_rate
        
        # Inflation differential (lower inflation strengthens currency)
        inflation_differential = foreign_inflation - inflation
        
        # Trade balance effect
        trade_effect = trade_balance * 0.01
        
        # Calculate dollar index change (limit to reasonable range)
        dollar_change = (rate_differential * 2.0 + 
                        inflation_differential * 1.5 + 
                        trade_effect)
        
        # Limit change to prevent overflow
        dollar_change = np.clip(dollar_change, -10, 10)
        
        # Update dollar index
        new_dollar_index = self.dollar_index * (1 + dollar_change / 100)
        
        # Keep dollar index within reasonable bounds
        new_dollar_index = np.clip(new_dollar_index, 50, 200)
        
        return new_dollar_index
    
    def simulate_economy(self, periods: int, shock_params: Dict = None) -> Dict[str, np.ndarray]:
        """
        Simulate the economy over multiple periods.
        
        Args:
            periods: Number of time periods to simulate
            shock_params: Optional dictionary of shock parameters
            
        Returns:
            Dictionary with time series of economic indicators
        """
        if shock_params is None:
            shock_params = {}
        
        # Initialize arrays
        gdp_series = np.zeros(periods)
        inflation_series = np.zeros(periods)
        interest_rate_series = np.zeros(periods)
        dollar_series = np.zeros(periods)
        
        # Set initial values
        gdp_series[0] = self.gdp
        inflation_series[0] = self.inflation
        interest_rate_series[0] = self.interest_rate
        dollar_series[0] = self.dollar_index
        
        # Simulation parameters
        base_consumption_ratio = 0.65
        base_investment_ratio = 0.20
        base_govt_ratio = 0.20
        base_exports_ratio = 0.10
        base_productivity_growth = 0.02
        base_money_growth = 0.03
        base_unemployment = 4.5
        
        for t in range(1, periods):
            # Get shock values
            money_shock = shock_params.get('money_shock', 0.0) if t > periods // 2 else 0.0
            productivity_shock = shock_params.get('productivity_shock', 0.0) if t > periods // 2 else 0.0
            
            # Calculate components
            consumption = gdp_series[t-1] * base_consumption_ratio
            investment = gdp_series[t-1] * base_investment_ratio
            govt_spending = gdp_series[t-1] * base_govt_ratio
            net_exports = gdp_series[t-1] * base_exports_ratio
            
            # GDP calculation
            productivity_growth = base_productivity_growth + productivity_shock
            gdp_series[t], gdp_growth = self.calculate_gdp_growth(
                investment, consumption, govt_spending, net_exports, productivity_growth
            )
            
            # Inflation calculation
            money_growth = base_money_growth + money_shock
            inflation_series[t] = self.calculate_inflation(
                money_growth * 100, gdp_growth
            )
            
            # Interest rate calculation
            interest_rate_series[t] = self.calculate_interest_rate(
                inflation_series[t], gdp_growth, base_unemployment
            )
            
            # Dollar value calculation
            trade_balance = net_exports
            dollar_series[t] = self.calculate_dollar_value(
                interest_rate_series[t], inflation_series[t], trade_balance
            )
            
            # Update state for next period
            self.gdp = gdp_series[t]
            self.inflation = inflation_series[t]
            self.interest_rate = interest_rate_series[t]
            self.dollar_index = dollar_series[t]
        
        return {
            'gdp': gdp_series,
            'inflation': inflation_series,
            'interest_rate': interest_rate_series,
            'dollar_index': dollar_series
        }
    
    def find_equilibrium_state(self, tolerance: float = 0.01, max_iterations: int = 100) -> Dict[str, float]:
        """
        Find long-run equilibrium values for all indicators.
        
        Args:
            tolerance: Convergence tolerance
            max_iterations: Maximum iterations
            
        Returns:
            Dictionary of equilibrium values
        """
        # Iterate until convergence
        for iteration in range(max_iterations):
            old_gdp = self.gdp
            old_inflation = self.inflation
            old_interest = self.interest_rate
            old_dollar = self.dollar_index
            
            # Simulate one period with equilibrium assumptions
            result = self.simulate_economy(periods=2, shock_params={})
            
            # Check convergence
            gdp_change = abs(result['gdp'][1] - old_gdp) / (old_gdp + 1e-10)
            inflation_change = abs(result['inflation'][1] - old_inflation)
            interest_change = abs(result['interest_rate'][1] - old_interest)
            dollar_change = abs(result['dollar_index'][1] - old_dollar) / (old_dollar + 1e-10)
            
            if (gdp_change < tolerance and inflation_change < tolerance and
                interest_change < tolerance and dollar_change < tolerance):
                break
        
        return {
            'equilibrium_gdp': self.gdp,
            'equilibrium_inflation': self.inflation,
            'equilibrium_interest_rate': self.interest_rate,
            'equilibrium_dollar_index': self.dollar_index,
            'iterations_to_converge': iteration + 1
        }
