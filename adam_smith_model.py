"""
Adam Smith Module - Invisible Hand Theory
This module implements concepts from Adam Smith's "The Wealth of Nations"
including the invisible hand, self-interest, and market equilibrium.
"""

import numpy as np
from typing import Dict, Tuple

class AdamSmithModel:
    """
    Implements Adam Smith's economic principles:
    - Invisible Hand: Self-interested actions lead to social benefit
    - Division of Labor: Specialization increases productivity
    - Market Competition: Supply and demand reach equilibrium
    """
    
    def __init__(self, num_agents: int = 100):
        """
        Initialize the Adam Smith economic model.
        
        Args:
            num_agents: Number of economic agents in the market
        """
        self.num_agents = num_agents
        self.productivity_factor = 1.0
        
    def calculate_market_equilibrium(self, supply: np.ndarray, demand: np.ndarray) -> Tuple[float, float]:
        """
        Calculate market equilibrium price and quantity using supply-demand intersection.
        
        Args:
            supply: Array of supply quantities at different price points
            demand: Array of demand quantities at different price points
            
        Returns:
            Tuple of (equilibrium_price, equilibrium_quantity)
        """
        # Find intersection point where supply equals demand
        price_range = np.linspace(0, 100, len(supply))
        diff = np.abs(supply - demand)
        equilibrium_idx = np.argmin(diff)
        
        equilibrium_price = price_range[equilibrium_idx]
        equilibrium_quantity = (supply[equilibrium_idx] + demand[equilibrium_idx]) / 2
        
        return equilibrium_price, equilibrium_quantity
    
    def invisible_hand_adjustment(self, current_price: float, equilibrium_price: float, 
                                  adjustment_rate: float = 0.1) -> float:
        """
        Simulate the invisible hand adjusting prices toward equilibrium.
        
        Args:
            current_price: Current market price
            equilibrium_price: Target equilibrium price
            adjustment_rate: Rate of price adjustment (0-1)
            
        Returns:
            Adjusted price moving toward equilibrium
        """
        price_gap = equilibrium_price - current_price
        adjustment = price_gap * adjustment_rate
        return current_price + adjustment
    
    def division_of_labor_productivity(self, specialization_level: float) -> float:
        """
        Calculate productivity gains from division of labor.
        
        Args:
            specialization_level: Level of specialization (0-1)
            
        Returns:
            Productivity multiplier
        """
        # Productivity increases with specialization but with diminishing returns
        return 1.0 + (specialization_level * 2.0) * (1 - 0.3 * specialization_level)
    
    def self_interest_optimization(self, agent_utilities: np.ndarray) -> Dict[str, float]:
        """
        Model how self-interested agents optimize their utilities.
        
        Args:
            agent_utilities: Array of utility values for each agent
            
        Returns:
            Dictionary with aggregate market metrics
        """
        total_utility = np.sum(agent_utilities)
        avg_utility = np.mean(agent_utilities)
        utility_variance = np.var(agent_utilities)
        
        # Social benefit emerges from individual self-interest
        social_benefit = total_utility * 0.8  # Market efficiency factor
        
        return {
            'total_utility': total_utility,
            'average_utility': avg_utility,
            'utility_variance': utility_variance,
            'social_benefit': social_benefit
        }
    
    def compute_wealth_distribution(self, initial_wealth: float, 
                                   market_participation: np.ndarray) -> np.ndarray:
        """
        Calculate wealth distribution based on market participation.
        
        Args:
            initial_wealth: Starting wealth per agent
            market_participation: Array of participation levels (0-1) for each agent
            
        Returns:
            Array of wealth values for each agent
        """
        # Wealth grows based on market participation and productivity
        wealth = initial_wealth * market_participation * self.productivity_factor
        return wealth
