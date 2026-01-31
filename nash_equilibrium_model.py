"""
Nash Equilibrium Module - Game Theory
This module implements John Nash's game theory concepts including
Nash equilibrium, strategic interaction, and non-cooperative games.
"""

import numpy as np
from typing import List, Tuple, Dict
from scipy.optimize import fsolve

class NashEquilibriumModel:
    """
    Implements Nash equilibrium concepts for economic modeling:
    - Nash Equilibrium: No player can improve by unilateral deviation
    - Strategic Interaction: Players consider others' actions
    - Best Response Dynamics: Players optimize given others' strategies
    """
    
    def __init__(self, num_players: int = 2):
        """
        Initialize Nash equilibrium model.
        
        Args:
            num_players: Number of players in the game
        """
        self.num_players = num_players
        
    def compute_nash_equilibrium_2player(self, payoff_matrix_p1: np.ndarray, 
                                        payoff_matrix_p2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute Nash equilibrium for 2-player game using payoff matrices.
        
        Args:
            payoff_matrix_p1: Payoff matrix for player 1
            payoff_matrix_p2: Payoff matrix for player 2
            
        Returns:
            Tuple of (strategy_p1, strategy_p2) at Nash equilibrium
        """
        # For mixed strategy Nash equilibrium
        num_strategies_p1 = payoff_matrix_p1.shape[0]
        num_strategies_p2 = payoff_matrix_p2.shape[1]
        
        # Find pure strategy Nash equilibria
        nash_equilibria = []
        for i in range(num_strategies_p1):
            for j in range(num_strategies_p2):
                # Check if (i, j) is a Nash equilibrium
                is_nash = True
                
                # Check player 1's best response
                current_payoff_p1 = payoff_matrix_p1[i, j]
                for i_alt in range(num_strategies_p1):
                    if payoff_matrix_p1[i_alt, j] > current_payoff_p1:
                        is_nash = False
                        break
                
                # Check player 2's best response
                if is_nash:
                    current_payoff_p2 = payoff_matrix_p2[i, j]
                    for j_alt in range(num_strategies_p2):
                        if payoff_matrix_p2[i, j_alt] > current_payoff_p2:
                            is_nash = False
                            break
                
                if is_nash:
                    nash_equilibria.append((i, j))
        
        # Return first Nash equilibrium found, or uniform mixed strategy
        if nash_equilibria:
            i, j = nash_equilibria[0]
            strategy_p1 = np.zeros(num_strategies_p1)
            strategy_p1[i] = 1.0
            strategy_p2 = np.zeros(num_strategies_p2)
            strategy_p2[j] = 1.0
        else:
            # Use uniform mixed strategy if no pure Nash equilibrium
            strategy_p1 = np.ones(num_strategies_p1) / num_strategies_p1
            strategy_p2 = np.ones(num_strategies_p2) / num_strategies_p2
        
        return strategy_p1, strategy_p2
    
    def best_response(self, player_strategy: np.ndarray, opponent_strategy: np.ndarray,
                     payoff_matrix: np.ndarray) -> np.ndarray:
        """
        Calculate best response strategy for a player given opponent's strategy.
        
        Args:
            player_strategy: Current strategy of the player
            opponent_strategy: Current strategy of the opponent
            payoff_matrix: Payoff matrix for the player
            
        Returns:
            Best response strategy
        """
        # Calculate expected payoffs for each strategy
        expected_payoffs = payoff_matrix @ opponent_strategy
        
        # Best response is pure strategy with highest expected payoff
        best_strategy_idx = np.argmax(expected_payoffs)
        best_response = np.zeros_like(player_strategy)
        best_response[best_strategy_idx] = 1.0
        
        return best_response
    
    def iterate_best_response(self, initial_strategies: List[np.ndarray],
                             payoff_matrices: List[np.ndarray],
                             max_iterations: int = 100,
                             tolerance: float = 1e-6) -> List[np.ndarray]:
        """
        Iterate best response dynamics to find Nash equilibrium.
        
        Args:
            initial_strategies: Initial strategies for all players
            payoff_matrices: Payoff matrices for all players
            max_iterations: Maximum number of iterations
            tolerance: Convergence tolerance
            
        Returns:
            List of equilibrium strategies for each player
        """
        strategies = [s.copy() for s in initial_strategies]
        
        for iteration in range(max_iterations):
            old_strategies = [s.copy() for s in strategies]
            
            # Update each player's strategy
            for i in range(self.num_players):
                # For simplicity, assume 2-player game
                if self.num_players == 2:
                    opponent_idx = 1 - i
                    strategies[i] = self.best_response(
                        strategies[i],
                        strategies[opponent_idx],
                        payoff_matrices[i]
                    )
            
            # Check convergence
            converged = all(
                np.allclose(strategies[i], old_strategies[i], atol=tolerance)
                for i in range(self.num_players)
            )
            
            if converged:
                break
        
        return strategies
    
    def compute_market_nash_equilibrium(self, firms_costs: np.ndarray,
                                       market_demand: float) -> Tuple[np.ndarray, float]:
        """
        Compute Nash equilibrium for firms competing in a market (Cournot competition).
        
        Args:
            firms_costs: Array of production costs for each firm
            market_demand: Total market demand parameter
            
        Returns:
            Tuple of (quantities produced by each firm, market price)
        """
        num_firms = len(firms_costs)
        
        def equations(quantities):
            """System of equations for Nash equilibrium in Cournot competition."""
            eqs = []
            total_quantity = np.sum(quantities)
            
            for i in range(num_firms):
                # Price as function of total quantity
                price = market_demand - total_quantity
                
                # First order condition: MR = MC
                # MR_i = price - q_i (derivative of revenue w.r.t. q_i)
                marginal_revenue = price - quantities[i]
                marginal_cost = firms_costs[i]
                
                # At equilibrium: MR = MC
                eqs.append(marginal_revenue - marginal_cost)
            
            return eqs
        
        # Initial guess: equal split of market
        initial_guess = np.ones(num_firms) * (market_demand / (num_firms + 1))
        
        # Solve for equilibrium quantities
        try:
            equilibrium_quantities = fsolve(equations, initial_guess)
            equilibrium_quantities = np.maximum(equilibrium_quantities, 0)  # Non-negative
            market_price = market_demand - np.sum(equilibrium_quantities)
        except:
            # Fallback to simple equal split
            equilibrium_quantities = initial_guess
            market_price = market_demand - np.sum(equilibrium_quantities)
        
        return equilibrium_quantities, market_price
    
    def strategic_stability(self, strategies: List[np.ndarray],
                           payoff_matrices: List[np.ndarray]) -> Dict[str, float]:
        """
        Analyze the strategic stability of an equilibrium.
        
        Args:
            strategies: Current strategies for all players
            payoff_matrices: Payoff matrices for all players
            
        Returns:
            Dictionary with stability metrics
        """
        deviation_incentives = []
        
        for i in range(self.num_players):
            if self.num_players == 2:
                opponent_idx = 1 - i
                current_payoff = strategies[i] @ payoff_matrices[i] @ strategies[opponent_idx]
                
                # Check payoff from best response
                best_resp = self.best_response(strategies[i], strategies[opponent_idx], 
                                              payoff_matrices[i])
                best_payoff = best_resp @ payoff_matrices[i] @ strategies[opponent_idx]
                
                deviation_incentive = best_payoff - current_payoff
                deviation_incentives.append(max(0, deviation_incentive))
        
        return {
            'is_nash': all(inc < 1e-6 for inc in deviation_incentives),
            'max_deviation_incentive': max(deviation_incentives) if deviation_incentives else 0,
            'stability_score': 1.0 / (1.0 + sum(deviation_incentives))
        }
