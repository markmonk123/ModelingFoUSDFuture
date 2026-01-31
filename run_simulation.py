"""
Economic Model Simulation
Main script to run the integrated economic model and display results.
"""

import numpy as np
import json
from integrated_model import IntegratedEconomicModel

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def print_convergence_points(convergence_points):
    """Print all convergence points in a readable format."""
    print_section("CONVERGENCE POINTS ANALYSIS")
    
    print("\n1. Market Nash Equilibrium (Game Theory - John Nash)")
    print(f"   - Equilibrium Price: ${convergence_points['market_nash_equilibrium']['price']:.2f}")
    print(f"   - Equilibrium Quantity: {convergence_points['market_nash_equilibrium']['quantity']:.2f}")
    print(f"   - Total Welfare: ${convergence_points['market_nash_equilibrium']['welfare']:.2f}")
    
    print("\n2. Policy Convergence (Expected Utility - Bruce Bueno de Mesquita)")
    print(f"   - Convergence Position: {convergence_points['policy_convergence']['position']:.2f}")
    print(f"   - Support Ratio: {convergence_points['policy_convergence']['support']:.2%}")
    print(f"   - Iterations to Converge: {convergence_points['policy_convergence']['iterations']}")
    
    print("\n3. Price Equilibrium (Invisible Hand - Adam Smith)")
    print(f"   - Equilibrium Price: ${convergence_points['price_equilibrium']['price']:.2f}")
    print(f"   - Equilibrium Quantity: {convergence_points['price_equilibrium']['quantity']:.2f}")
    
    print("\n4. Macroeconomic Equilibrium (Integrated Model)")
    print(f"   - GDP: ${convergence_points['macroeconomic_equilibrium']['gdp']:.2f} billion")
    print(f"   - Inflation Rate: {convergence_points['macroeconomic_equilibrium']['inflation']:.2f}%")
    print(f"   - Interest Rate: {convergence_points['macroeconomic_equilibrium']['interest_rate']:.2f}%")
    print(f"   - Dollar Index: {convergence_points['macroeconomic_equilibrium']['dollar_index']:.2f}")

def print_macroeconomic_impacts(macro_results):
    """Print macroeconomic impacts."""
    print_section("MACROECONOMIC IMPACTS")
    
    print("\nSteady State Values:")
    print(f"   - GDP: ${macro_results['steady_state_gdp']:.2f} billion")
    print(f"   - Inflation: {macro_results['steady_state_inflation']:.2f}%")
    print(f"   - Interest Rate: {macro_results['steady_state_interest_rate']:.2f}%")
    print(f"   - Dollar Index: {macro_results['steady_state_dollar_index']:.2f}")
    
    print("\nDynamic Metrics:")
    print(f"   - GDP Growth Rate: {macro_results['gdp_growth_rate']:.2f}%")
    print(f"   - Inflation Volatility: {macro_results['inflation_volatility']:.2f}")
    print(f"   - Interest Rate Volatility: {macro_results['interest_rate_volatility']:.2f}")

def print_market_analysis(market_results):
    """Print market competition analysis."""
    print_section("MARKET COMPETITION ANALYSIS (Nash Equilibrium)")
    
    print(f"\nMarket Structure:")
    print(f"   - Number of Firms: {len(market_results['equilibrium_quantities'])}")
    print(f"   - Market Price: ${market_results['market_price']:.2f}")
    print(f"   - Total Output: {market_results['total_output']:.2f}")
    
    print(f"\nWelfare Analysis (Adam Smith's Invisible Hand):")
    print(f"   - Consumer Surplus: ${market_results['consumer_surplus']:.2f}")
    print(f"   - Producer Surplus: ${market_results['producer_surplus']:.2f}")
    print(f"   - Total Welfare: ${market_results['total_welfare']:.2f}")
    print(f"   - Market Efficiency: {market_results['market_efficiency']:.2%}")

def print_policy_analysis(policy_results):
    """Print policy consensus analysis."""
    print_section("POLICY CONSENSUS ANALYSIS (Expected Utility Theory)")
    
    print(f"\nPolicy Prediction:")
    print(f"   - Predicted Outcome: {policy_results['predicted_policy_outcome']:.2f}")
    print(f"   - Convergence Point: {policy_results['convergence_point']:.2f}")
    print(f"   - Weighted Utility: {policy_results['weighted_utility']:.2f}")
    print(f"   - Support Ratio: {policy_results['support_ratio']:.2%}")
    
    print(f"\nCoalition Structure:")
    print(f"   - Number of Coalitions: {policy_results['number_of_coalitions']}")
    print(f"   - Largest Coalition Size: {policy_results['largest_coalition_size']}")

def print_theoretical_foundations(summary):
    """Print theoretical foundations."""
    print_section("THEORETICAL FOUNDATIONS")
    
    print(f"\nModel Framework: {summary['model_framework']}")
    print("\nIntegrated Theories:")
    for i, theory in enumerate(summary['theories_integrated'], 1):
        print(f"   {i}. {theory}")

def save_results_to_file(results, filename='economic_model_results.json'):
    """Save results to JSON file."""
    # Convert numpy arrays to lists for JSON serialization
    def convert_numpy(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {k: convert_numpy(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_numpy(item) for item in obj]
        return obj
    
    results_serializable = convert_numpy(results)
    
    with open(filename, 'w') as f:
        json.dump(results_serializable, f, indent=2)
    
    print(f"\n✓ Results saved to {filename}")

def main():
    """Main simulation function."""
    print("\n" + "=" * 70)
    print("  INTEGRATED ECONOMIC MODEL")
    print("  Game Theory & Macroeconomic Analysis")
    print("=" * 70)
    print("\n  Integrating:")
    print("    • Adam Smith - Invisible Hand & Market Equilibrium")
    print("    • John Nash - Game Theory & Nash Equilibrium")
    print("    • Bruce Bueno de Mesquita - Expected Utility Theory")
    print("=" * 70)
    
    # Initialize and run the integrated model
    print("\nInitializing integrated economic model...")
    model = IntegratedEconomicModel(num_agents=100, num_firms=10)
    
    print("Running comprehensive analysis...")
    results = model.comprehensive_analysis()
    
    # Display results
    print_theoretical_foundations(results['summary'])
    print_convergence_points(results['convergence_points'])
    print_market_analysis(results['market_results'])
    print_policy_analysis(results['policy_results'])
    print_macroeconomic_impacts(results['macro_results'])
    
    # Key findings summary
    print_section("KEY FINDINGS SUMMARY")
    findings = results['summary']['key_findings']
    print(f"\n• Market Efficiency: {findings['market_efficiency']:.2%}")
    print(f"• Policy Support: {findings['policy_support']:.2%}")
    print(f"• GDP (Steady State): ${findings['gdp_steady_state']:.2f} billion")
    print(f"• Inflation (Steady State): {findings['inflation_steady_state']:.2f}%")
    print(f"• Interest Rate (Steady State): {findings['interest_rate_steady_state']:.2f}%")
    print(f"• Dollar Index (Steady State): {findings['dollar_index_steady_state']:.2f}")
    
    # Save results
    print_section("SAVING RESULTS")
    save_results_to_file(results)
    
    print("\n" + "=" * 70)
    print("  Analysis Complete!")
    print("=" * 70 + "\n")
    
    return results

if __name__ == "__main__":
    results = main()
