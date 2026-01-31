"""
Visualization Module
Create visualizations for the economic model results.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict
import json

class EconomicVisualizer:
    """Create visualizations for economic model outputs."""
    
    def __init__(self):
        """Initialize the visualizer."""
        self.fig_size = (12, 8)
        
    def plot_macroeconomic_time_series(self, time_series: Dict[str, np.ndarray], 
                                      filename: str = 'macro_time_series.png'):
        """
        Plot macroeconomic indicators over time.
        
        Args:
            time_series: Dictionary with GDP, inflation, interest rate, dollar index arrays
            filename: Output filename
        """
        fig, axes = plt.subplots(2, 2, figsize=self.fig_size)
        fig.suptitle('Macroeconomic Indicators Time Series', fontsize=16, fontweight='bold')
        
        # GDP
        axes[0, 0].plot(time_series['gdp'], linewidth=2, color='#2E86AB')
        axes[0, 0].set_title('GDP Over Time', fontweight='bold')
        axes[0, 0].set_xlabel('Time Period')
        axes[0, 0].set_ylabel('GDP ($ Billions)')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Inflation
        axes[0, 1].plot(time_series['inflation'], linewidth=2, color='#A23B72')
        axes[0, 1].set_title('Inflation Rate Over Time', fontweight='bold')
        axes[0, 1].set_xlabel('Time Period')
        axes[0, 1].set_ylabel('Inflation Rate (%)')
        axes[0, 1].axhline(y=2.0, color='red', linestyle='--', label='Target (2%)')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Interest Rate
        axes[1, 0].plot(time_series['interest_rate'], linewidth=2, color='#F18F01')
        axes[1, 0].set_title('Interest Rate Over Time', fontweight='bold')
        axes[1, 0].set_xlabel('Time Period')
        axes[1, 0].set_ylabel('Interest Rate (%)')
        axes[1, 0].grid(True, alpha=0.3)
        
        # Dollar Index
        axes[1, 1].plot(time_series['dollar_index'], linewidth=2, color='#06A77D')
        axes[1, 1].set_title('Dollar Index Over Time', fontweight='bold')
        axes[1, 1].set_xlabel('Time Period')
        axes[1, 1].set_ylabel('Dollar Index (100 = baseline)')
        axes[1, 1].axhline(y=100, color='red', linestyle='--', label='Baseline')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✓ Saved macroeconomic time series plot to {filename}")
        plt.close()
    
    def plot_convergence_analysis(self, convergence_history: list,
                                  filename: str = 'convergence_analysis.png'):
        """
        Plot convergence path for policy positions.
        
        Args:
            convergence_history: List of positions over iterations
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        iterations = range(len(convergence_history))
        ax.plot(iterations, convergence_history, marker='o', linewidth=2, 
                markersize=6, color='#2E86AB')
        
        # Mark start and end
        ax.scatter([0], [convergence_history[0]], s=200, c='green', 
                  marker='o', label='Start', zorder=5)
        ax.scatter([len(convergence_history)-1], [convergence_history[-1]], 
                  s=200, c='red', marker='*', label='Convergence Point', zorder=5)
        
        ax.set_title('Policy Position Convergence Path\n(Bueno de Mesquita Expected Utility)',
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Policy Position')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✓ Saved convergence analysis plot to {filename}")
        plt.close()
    
    def plot_market_equilibrium(self, equilibrium_price: float, equilibrium_quantity: float,
                               filename: str = 'market_equilibrium.png'):
        """
        Plot supply-demand curves and equilibrium.
        
        Args:
            equilibrium_price: Equilibrium price
            equilibrium_quantity: Equilibrium quantity
            filename: Output filename
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Generate supply and demand curves
        prices = np.linspace(0, 100, 100)
        supply = 20 + prices * 0.8
        demand = 100 - prices * 0.6
        
        # Plot curves
        ax.plot(supply, prices, linewidth=2.5, color='#06A77D', label='Supply')
        ax.plot(demand, prices, linewidth=2.5, color='#A23B72', label='Demand')
        
        # Mark equilibrium
        ax.scatter([equilibrium_quantity], [equilibrium_price], s=300, c='red', 
                  marker='*', label='Equilibrium', zorder=5)
        ax.axhline(y=equilibrium_price, color='red', linestyle='--', alpha=0.5)
        ax.axvline(x=equilibrium_quantity, color='red', linestyle='--', alpha=0.5)
        
        ax.set_title('Market Equilibrium (Adam Smith - Invisible Hand)',
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Quantity')
        ax.set_ylabel('Price ($)')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        
        # Add equilibrium point annotation
        ax.annotate(f'Equilibrium\nP=${equilibrium_price:.2f}\nQ={equilibrium_quantity:.2f}',
                   xy=(equilibrium_quantity, equilibrium_price),
                   xytext=(equilibrium_quantity + 10, equilibrium_price + 10),
                   fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✓ Saved market equilibrium plot to {filename}")
        plt.close()
    
    def plot_convergence_points_summary(self, convergence_points: Dict,
                                       filename: str = 'convergence_summary.png'):
        """
        Create a summary visualization of all convergence points.
        
        Args:
            convergence_points: Dictionary of all convergence points
            filename: Output filename
        """
        fig = plt.figure(figsize=(14, 10))
        
        # Create text summary
        summary_text = "CONVERGENCE POINTS SUMMARY\n\n"
        summary_text += "=" * 60 + "\n\n"
        
        summary_text += "1. Market Nash Equilibrium (Game Theory)\n"
        summary_text += f"   • Price: ${convergence_points['market_nash_equilibrium']['price']:.2f}\n"
        summary_text += f"   • Quantity: {convergence_points['market_nash_equilibrium']['quantity']:.2f}\n"
        summary_text += f"   • Welfare: ${convergence_points['market_nash_equilibrium']['welfare']:.2f}\n\n"
        
        summary_text += "2. Policy Convergence (Expected Utility)\n"
        summary_text += f"   • Position: {convergence_points['policy_convergence']['position']:.2f}\n"
        summary_text += f"   • Support: {convergence_points['policy_convergence']['support']:.1%}\n"
        summary_text += f"   • Iterations: {convergence_points['policy_convergence']['iterations']}\n\n"
        
        summary_text += "3. Price Equilibrium (Invisible Hand)\n"
        summary_text += f"   • Price: ${convergence_points['price_equilibrium']['price']:.2f}\n"
        summary_text += f"   • Quantity: {convergence_points['price_equilibrium']['quantity']:.2f}\n\n"
        
        summary_text += "4. Macroeconomic Equilibrium\n"
        summary_text += f"   • GDP: ${convergence_points['macroeconomic_equilibrium']['gdp']:.2f}B\n"
        summary_text += f"   • Inflation: {convergence_points['macroeconomic_equilibrium']['inflation']:.2f}%\n"
        summary_text += f"   • Interest Rate: {convergence_points['macroeconomic_equilibrium']['interest_rate']:.2f}%\n"
        summary_text += f"   • Dollar Index: {convergence_points['macroeconomic_equilibrium']['dollar_index']:.2f}\n"
        
        plt.text(0.1, 0.5, summary_text, fontsize=12, family='monospace',
                verticalalignment='center', transform=fig.transFigure,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✓ Saved convergence summary to {filename}")
        plt.close()
    
    def create_all_visualizations(self, results: Dict):
        """
        Create all visualizations from model results.
        
        Args:
            results: Complete results dictionary from integrated model
        """
        print("\n" + "=" * 70)
        print("  GENERATING VISUALIZATIONS")
        print("=" * 70 + "\n")
        
        # Macroeconomic time series
        self.plot_macroeconomic_time_series(
            results['macro_results']['time_series']
        )
        
        # Convergence analysis
        self.plot_convergence_analysis(
            results['policy_results']['convergence_history']
        )
        
        # Market equilibrium
        self.plot_market_equilibrium(
            results['equilibrium_results']['equilibrium_price'],
            results['equilibrium_results']['equilibrium_quantity']
        )
        
        # Convergence points summary
        self.plot_convergence_points_summary(
            results['convergence_points']
        )
        
        print("\n✓ All visualizations created successfully!")

def visualize_results(results_file: str = 'economic_model_results.json'):
    """
    Load results from file and create visualizations.
    
    Args:
        results_file: Path to results JSON file
    """
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    visualizer = EconomicVisualizer()
    visualizer.create_all_visualizations(results)

if __name__ == "__main__":
    # Example usage
    visualize_results()
