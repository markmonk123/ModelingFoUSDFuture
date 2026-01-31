"""
Integrated Economic Model
This module integrates Adam Smith's invisible hand, Nash equilibrium game theory,
and Bueno de Mesquita's expected utility theory to model economic outcomes.
"""

import numpy as np
from typing import Dict, List, Tuple
from adam_smith_model import AdamSmithModel
from nash_equilibrium_model import NashEquilibriumModel
from bueno_mesquita_model import BuenoMesquitaModel
from macroeconomic_model import MacroeconomicModel

class IntegratedEconomicModel:
    """
    Integrates multiple economic and game theory frameworks to predict:
    - GDP impacts
    - Inflation dynamics
    - Interest rate movements
    - Dollar valuation
    - Convergence points across all theories
    """
    
    def __init__(self, num_agents: int = 100, num_firms: int = 10):
        """
        Initialize the integrated economic model.
        
        Args:
            num_agents: Number of economic agents
            num_firms: Number of firms in the market
        """
        self.num_agents = num_agents
        self.num_firms = num_firms
        
        # Initialize sub-models
        self.smith_model = AdamSmithModel(num_agents=num_agents)
        self.nash_model = NashEquilibriumModel(num_players=2)
        self.mesquita_model = BuenoMesquitaModel()
        self.macro_model = MacroeconomicModel()
        
    def model_market_competition(self, num_firms: int = None) -> Dict[str, any]:
        """
        Model market competition using Nash equilibrium (firms compete on quantity).
        
        Args:
            num_firms: Number of firms (uses default if not specified)
            
        Returns:
            Dictionary with market competition results
        """
        if num_firms is None:
            num_firms = self.num_firms
        
        # Generate firm costs (random but realistic)
        np.random.seed(42)
        firms_costs = np.random.uniform(10, 30, num_firms)
        market_demand = 100.0
        
        # Compute Nash equilibrium quantities
        equilibrium_quantities, market_price = self.nash_model.compute_market_nash_equilibrium(
            firms_costs, market_demand
        )
        
        # Calculate total output and firm profits
        total_output = np.sum(equilibrium_quantities)
        firm_revenues = equilibrium_quantities * market_price
        firm_costs_total = equilibrium_quantities * firms_costs
        firm_profits = firm_revenues - firm_costs_total
        
        # Consumer surplus
        max_willingness_to_pay = market_demand
        consumer_surplus = 0.5 * total_output * (max_willingness_to_pay - market_price)
        
        # Producer surplus (total profits)
        producer_surplus = np.sum(firm_profits)
        
        # Total welfare (Smith's invisible hand)
        total_welfare = consumer_surplus + producer_surplus
        
        return {
            'equilibrium_quantities': equilibrium_quantities,
            'market_price': market_price,
            'total_output': total_output,
            'firm_profits': firm_profits,
            'consumer_surplus': consumer_surplus,
            'producer_surplus': producer_surplus,
            'total_welfare': total_welfare,
            'market_efficiency': total_welfare / (market_demand * max_willingness_to_pay / 2)
        }
    
    def model_policy_consensus(self, num_stakeholders: int = 20) -> Dict[str, any]:
        """
        Model policy consensus using Bueno de Mesquita's expected utility theory.
        
        Args:
            num_stakeholders: Number of policy stakeholders
            
        Returns:
            Dictionary with policy consensus results
        """
        # Generate stakeholder attributes
        np.random.seed(43)
        positions = np.random.uniform(0, 100, num_stakeholders)  # Policy positions
        power = np.random.uniform(0.5, 1.5, num_stakeholders)
        power = power / np.sum(power)  # Normalize
        salience = np.random.uniform(0.3, 1.0, num_stakeholders)
        risk_tolerance = np.random.uniform(0.1, 0.9, num_stakeholders)
        
        # Predict policy outcome
        policy_prediction = self.mesquita_model.predict_policy_outcome(
            positions, power, salience, risk_tolerance
        )
        
        # Find convergence
        convergence_point, convergence_history = self.mesquita_model.predict_convergence(
            positions, power, salience
        )
        
        # Coalition analysis
        coalitions = self.mesquita_model.coalition_formation(positions, power)
        
        return {
            'predicted_policy_outcome': policy_prediction['predicted_outcome'],
            'convergence_point': convergence_point,
            'convergence_history': convergence_history,
            'weighted_utility': policy_prediction['weighted_utility'],
            'support_ratio': policy_prediction['support_ratio'],
            'number_of_coalitions': len(coalitions),
            'largest_coalition_size': max(len(c) for c in coalitions) if coalitions else 0
        }
    
    def analyze_market_equilibrium(self) -> Dict[str, any]:
        """
        Analyze market equilibrium using Adam Smith's principles.
        
        Returns:
            Dictionary with market equilibrium analysis
        """
        # Generate supply and demand curves
        price_points = 100
        prices = np.linspace(0, 100, price_points)
        
        # Supply: increases with price
        supply = 20 + prices * 0.8 + np.random.normal(0, 2, price_points)
        supply = np.maximum(supply, 0)
        
        # Demand: decreases with price
        demand = 100 - prices * 0.6 + np.random.normal(0, 2, price_points)
        demand = np.maximum(demand, 0)
        
        # Find equilibrium
        equilibrium_price, equilibrium_quantity = self.smith_model.calculate_market_equilibrium(
            supply, demand
        )
        
        # Invisible hand adjustment simulation
        current_price = 30.0
        price_adjustment_path = [current_price]
        for _ in range(20):
            current_price = self.smith_model.invisible_hand_adjustment(
                current_price, equilibrium_price, adjustment_rate=0.15
            )
            price_adjustment_path.append(current_price)
        
        # Calculate productivity from specialization
        specialization_levels = np.linspace(0, 1, 10)
        productivity_gains = [
            self.smith_model.division_of_labor_productivity(level)
            for level in specialization_levels
        ]
        
        return {
            'equilibrium_price': equilibrium_price,
            'equilibrium_quantity': equilibrium_quantity,
            'price_adjustment_path': price_adjustment_path,
            'final_adjusted_price': price_adjustment_path[-1],
            'productivity_gains': productivity_gains,
            'max_productivity': max(productivity_gains)
        }
    
    def predict_macroeconomic_impacts(self, policy_position: float,
                                     market_efficiency: float) -> Dict[str, any]:
        """
        Predict macroeconomic impacts using integrated model insights.
        
        Args:
            policy_position: Policy outcome position (0-100, e.g., 0=restrictive, 100=expansionary)
            market_efficiency: Market efficiency score (0-1)
            
        Returns:
            Dictionary with macroeconomic predictions
        """
        # Map policy position to monetary/fiscal parameters
        # Higher position = more expansionary policy
        money_growth_shock = (policy_position - 50) / 500  # -0.1 to +0.1
        productivity_shock = (market_efficiency - 0.5) / 25  # Based on market efficiency
        
        # Simulate economy
        periods = 50
        simulation_results = self.macro_model.simulate_economy(
            periods=periods,
            shock_params={
                'money_shock': money_growth_shock,
                'productivity_shock': productivity_shock
            }
        )
        
        # Calculate steady state values (last 10 periods average)
        steady_state_gdp = np.mean(simulation_results['gdp'][-10:])
        steady_state_inflation = np.mean(simulation_results['inflation'][-10:])
        steady_state_interest = np.mean(simulation_results['interest_rate'][-10:])
        steady_state_dollar = np.mean(simulation_results['dollar_index'][-10:])
        
        # Find equilibrium
        equilibrium = self.macro_model.find_equilibrium_state()
        
        return {
            'time_series': simulation_results,
            'steady_state_gdp': steady_state_gdp,
            'steady_state_inflation': steady_state_inflation,
            'steady_state_interest_rate': steady_state_interest,
            'steady_state_dollar_index': steady_state_dollar,
            'equilibrium': equilibrium,
            'gdp_growth_rate': ((simulation_results['gdp'][-1] - simulation_results['gdp'][0]) / 
                               simulation_results['gdp'][0] * 100),
            'inflation_volatility': np.std(simulation_results['inflation']),
            'interest_rate_volatility': np.std(simulation_results['interest_rate'])
        }
    
    def find_all_convergence_points(self) -> Dict[str, any]:
        """
        Find all convergence points across the integrated model.
        
        Returns:
            Dictionary with all convergence points and analysis
        """
        # 1. Market competition Nash equilibrium
        market_results = self.model_market_competition()
        
        # 2. Policy consensus convergence
        policy_results = self.model_policy_consensus()
        
        # 3. Market equilibrium (Smith)
        equilibrium_results = self.analyze_market_equilibrium()
        
        # 4. Macroeconomic impacts
        macro_results = self.predict_macroeconomic_impacts(
            policy_position=policy_results['predicted_policy_outcome'],
            market_efficiency=market_results['market_efficiency']
        )
        
        # Compile all convergence points
        convergence_points = {
            'market_nash_equilibrium': {
                'price': market_results['market_price'],
                'quantity': market_results['total_output'],
                'welfare': market_results['total_welfare']
            },
            'policy_convergence': {
                'position': policy_results['convergence_point'],
                'support': policy_results['support_ratio'],
                'iterations': len(policy_results['convergence_history'])
            },
            'price_equilibrium': {
                'price': equilibrium_results['equilibrium_price'],
                'quantity': equilibrium_results['equilibrium_quantity']
            },
            'macroeconomic_equilibrium': {
                'gdp': macro_results['equilibrium']['equilibrium_gdp'],
                'inflation': macro_results['equilibrium']['equilibrium_inflation'],
                'interest_rate': macro_results['equilibrium']['equilibrium_interest_rate'],
                'dollar_index': macro_results['equilibrium']['equilibrium_dollar_index']
            }
        }
        
        return {
            'convergence_points': convergence_points,
            'market_results': market_results,
            'policy_results': policy_results,
            'equilibrium_results': equilibrium_results,
            'macro_results': macro_results
        }
    
    def comprehensive_analysis(self) -> Dict[str, any]:
        """
        Run comprehensive analysis integrating all models.
        
        Returns:
            Complete analysis results
        """
        print("Running comprehensive economic model analysis...")
        print("=" * 60)
        
        # Get all convergence points and results
        results = self.find_all_convergence_points()
        
        # Summary statistics
        summary = {
            'model_framework': 'Integrated Economic Model',
            'theories_integrated': [
                'Adam Smith - Invisible Hand & Market Equilibrium',
                'John Nash - Game Theory & Nash Equilibrium',
                'Bruce Bueno de Mesquita - Expected Utility Theory'
            ],
            'convergence_points': results['convergence_points'],
            'key_findings': {
                'market_efficiency': results['market_results']['market_efficiency'],
                'policy_support': results['policy_results']['support_ratio'],
                'gdp_steady_state': results['macro_results']['steady_state_gdp'],
                'inflation_steady_state': results['macro_results']['steady_state_inflation'],
                'interest_rate_steady_state': results['macro_results']['steady_state_interest_rate'],
                'dollar_index_steady_state': results['macro_results']['steady_state_dollar_index']
            }
        }
        
        results['summary'] = summary
        return results
