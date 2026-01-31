"""
Example Usage of the Integrated Economic Model
This script demonstrates various ways to use the economic modeling framework.
"""

from integrated_model import IntegratedEconomicModel
from adam_smith_model import AdamSmithModel
from nash_equilibrium_model import NashEquilibriumModel
from bueno_mesquita_model import BuenoMesquitaModel
from macroeconomic_model import MacroeconomicModel
from visualizations import EconomicVisualizer
import numpy as np

def example_1_basic_usage():
    """Example 1: Basic integrated model usage."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Integrated Model Usage")
    print("="*70)
    
    # Initialize the integrated model
    model = IntegratedEconomicModel(num_agents=100, num_firms=10)
    
    # Run comprehensive analysis
    results = model.comprehensive_analysis()
    
    # Access specific results
    print(f"\nMarket Efficiency: {results['market_results']['market_efficiency']:.2%}")
    print(f"Policy Support: {results['policy_results']['support_ratio']:.2%}")
    print(f"Equilibrium GDP: ${results['convergence_points']['macroeconomic_equilibrium']['gdp']:.2f}B")
    
    return results

def example_2_market_competition():
    """Example 2: Analyze market competition with different number of firms."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Market Competition Analysis")
    print("="*70)
    
    model = IntegratedEconomicModel()
    
    # Compare markets with different numbers of firms
    for num_firms in [3, 5, 10, 20]:
        results = model.model_market_competition(num_firms=num_firms)
        print(f"\n{num_firms} Firms:")
        print(f"  Market Price: ${results['market_price']:.2f}")
        print(f"  Total Output: {results['total_output']:.2f}")
        print(f"  Market Efficiency: {results['market_efficiency']:.2%}")
        print(f"  Consumer Surplus: ${results['consumer_surplus']:.2f}")

def example_3_policy_scenarios():
    """Example 3: Analyze different policy scenarios."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Policy Scenario Analysis")
    print("="*70)
    
    model = IntegratedEconomicModel()
    
    # Test different policy positions
    policy_positions = [20, 40, 60, 80]  # Restrictive to Expansionary
    
    for position in policy_positions:
        macro_results = model.predict_macroeconomic_impacts(
            policy_position=position,
            market_efficiency=0.7
        )
        
        policy_type = "Restrictive" if position < 40 else "Moderate" if position < 60 else "Expansionary"
        print(f"\n{policy_type} Policy (Position: {position}):")
        print(f"  GDP Growth: {macro_results['gdp_growth_rate']:.2f}%")
        print(f"  Inflation: {macro_results['steady_state_inflation']:.2f}%")
        print(f"  Interest Rate: {macro_results['steady_state_interest_rate']:.2f}%")

def example_4_individual_models():
    """Example 4: Using individual models separately."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Individual Model Components")
    print("="*70)
    
    # Adam Smith Model
    print("\n--- Adam Smith Model ---")
    smith = AdamSmithModel(num_agents=100)
    
    # Generate supply and demand
    supply = np.linspace(20, 100, 50)
    demand = np.linspace(100, 20, 50)
    
    eq_price, eq_quantity = smith.calculate_market_equilibrium(supply, demand)
    print(f"Equilibrium Price: ${eq_price:.2f}")
    print(f"Equilibrium Quantity: {eq_quantity:.2f}")
    
    # Calculate productivity from specialization
    specialization = 0.8
    productivity = smith.division_of_labor_productivity(specialization)
    print(f"Productivity Multiplier: {productivity:.2f}x")
    
    # Nash Equilibrium Model
    print("\n--- Nash Equilibrium Model ---")
    nash = NashEquilibriumModel(num_players=2)
    
    # Create a simple payoff matrix (Prisoner's Dilemma variant)
    payoff_p1 = np.array([[3, 0], [5, 1]])
    payoff_p2 = np.array([[3, 5], [0, 1]])
    
    strategy_p1, strategy_p2 = nash.compute_nash_equilibrium_2player(payoff_p1, payoff_p2)
    print(f"Player 1 Strategy: {strategy_p1}")
    print(f"Player 2 Strategy: {strategy_p2}")
    
    # Bueno de Mesquita Model
    print("\n--- Bueno de Mesquita Model ---")
    mesquita = BuenoMesquitaModel()
    
    # Define stakeholders
    positions = np.array([20, 40, 60, 80])
    power = np.array([0.4, 0.3, 0.2, 0.1])
    salience = np.array([0.9, 0.8, 0.7, 0.6])
    risk_tolerance = np.array([0.5, 0.5, 0.5, 0.5])
    
    prediction = mesquita.predict_policy_outcome(positions, power, salience, risk_tolerance)
    print(f"Predicted Outcome: {prediction['predicted_outcome']:.2f}")
    print(f"Support Ratio: {prediction['support_ratio']:.2%}")
    
    # Macroeconomic Model
    print("\n--- Macroeconomic Model ---")
    macro = MacroeconomicModel()
    
    # Calculate interest rate using Taylor Rule
    interest_rate = macro.calculate_interest_rate(
        inflation=2.5,
        gdp_growth=3.0,
        unemployment_rate=4.0
    )
    print(f"Recommended Interest Rate: {interest_rate:.2f}%")

def example_5_convergence_analysis():
    """Example 5: Detailed convergence analysis."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Convergence Analysis")
    print("="*70)
    
    model = IntegratedEconomicModel()
    
    # Get all convergence points
    results = model.find_all_convergence_points()
    
    convergence = results['convergence_points']
    
    print("\nAll Convergence Points:")
    print("-" * 70)
    
    print("\n1. Nash Equilibrium Convergence:")
    print(f"   Price converges to: ${convergence['market_nash_equilibrium']['price']:.2f}")
    print(f"   Quantity converges to: {convergence['market_nash_equilibrium']['quantity']:.2f}")
    
    print("\n2. Policy Position Convergence:")
    print(f"   Position converges to: {convergence['policy_convergence']['position']:.2f}")
    print(f"   With support of: {convergence['policy_convergence']['support']:.2%}")
    
    print("\n3. Market Price Convergence:")
    print(f"   Price converges to: ${convergence['price_equilibrium']['price']:.2f}")
    
    print("\n4. Macroeconomic Convergence:")
    print(f"   GDP: ${convergence['macroeconomic_equilibrium']['gdp']:.2f}B")
    print(f"   Inflation: {convergence['macroeconomic_equilibrium']['inflation']:.2f}%")
    print(f"   Interest Rate: {convergence['macroeconomic_equilibrium']['interest_rate']:.2f}%")
    print(f"   Dollar Index: {convergence['macroeconomic_equilibrium']['dollar_index']:.2f}")

def example_6_visualization():
    """Example 6: Creating custom visualizations."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Custom Visualizations")
    print("="*70)
    
    model = IntegratedEconomicModel()
    results = model.find_all_convergence_points()
    
    # Create visualizations
    visualizer = EconomicVisualizer()
    
    print("\nCreating visualizations...")
    
    # Time series
    visualizer.plot_macroeconomic_time_series(
        results['macro_results']['time_series'],
        filename='custom_macro_series.png'
    )
    
    # Convergence path
    visualizer.plot_convergence_analysis(
        results['policy_results']['convergence_history'],
        filename='custom_convergence.png'
    )
    
    print("\n✓ Visualizations saved!")

def main():
    """Run all examples."""
    print("\n" + "="*70)
    print("  ECONOMIC MODEL - EXAMPLE USAGE")
    print("="*70)
    
    # Run examples
    example_1_basic_usage()
    example_2_market_competition()
    example_3_policy_scenarios()
    example_4_individual_models()
    example_5_convergence_analysis()
    
    # Uncomment to create visualizations
    # example_6_visualization()
    
    print("\n" + "="*70)
    print("  All Examples Complete!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
