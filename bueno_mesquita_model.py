"""
Bruce Bueno de Mesquita Expected Utility Module
This module implements the expected utility theory and predictive modeling
based on Bruce Bueno de Mesquita's work on political and economic forecasting.
"""

import numpy as np
from typing import Dict, List, Tuple

class BuenoMesquitaModel:
    """
    Implements Bruce Bueno de Mesquita's expected utility theory:
    - Actors have different positions, power, and preferences
    - Predictions based on weighted positions and strategic interactions
    - Iterative bargaining and coalition formation
    """
    
    def __init__(self):
        """Initialize the Bueno de Mesquita expected utility model."""
        pass
    
    def expected_utility(self, actor_position: float, outcome: float,
                        actor_risk_tolerance: float) -> float:
        """
        Calculate expected utility for an actor given an outcome.
        
        Args:
            actor_position: Actor's preferred position (0-100)
            outcome: Potential outcome position (0-100)
            actor_risk_tolerance: Risk tolerance (0-1, higher means more risk-averse)
            
        Returns:
            Expected utility value
        """
        # Utility decreases with distance from preferred position
        distance = abs(outcome - actor_position)
        
        # Risk-adjusted utility
        base_utility = 100 - distance
        risk_adjustment = 1 - (actor_risk_tolerance * 0.5)
        
        return base_utility * risk_adjustment
    
    def compute_median_voter_position(self, actors_positions: np.ndarray,
                                     actors_power: np.ndarray,
                                     actors_salience: np.ndarray) -> float:
        """
        Calculate the median voter position weighted by power and salience.
        
        Args:
            actors_positions: Array of preferred positions for each actor
            actors_power: Array of power/influence for each actor
            actors_salience: Array of salience/importance for each actor
            
        Returns:
            Weighted median position
        """
        # Weight by power and salience
        weights = actors_power * actors_salience
        weights = weights / np.sum(weights)
        
        # Sort by position
        sorted_indices = np.argsort(actors_positions)
        sorted_positions = actors_positions[sorted_indices]
        sorted_weights = weights[sorted_indices]
        
        # Find median by cumulative weight
        cumulative_weights = np.cumsum(sorted_weights)
        median_idx = np.searchsorted(cumulative_weights, 0.5)
        
        return sorted_positions[median_idx]
    
    def predict_convergence(self, actors_positions: np.ndarray,
                          actors_power: np.ndarray,
                          actors_salience: np.ndarray,
                          max_iterations: int = 50) -> Tuple[float, List[float]]:
        """
        Predict the convergence point through iterative bargaining.
        
        Args:
            actors_positions: Array of preferred positions for each actor
            actors_power: Array of power/influence for each actor
            actors_salience: Array of salience/importance for each actor
            max_iterations: Maximum number of bargaining iterations
            
        Returns:
            Tuple of (final convergence position, history of positions)
        """
        current_positions = actors_positions.copy()
        position_history = [self.compute_median_voter_position(
            current_positions, actors_power, actors_salience
        )]
        
        for iteration in range(max_iterations):
            # Each actor adjusts position based on expected utility
            median_position = self.compute_median_voter_position(
                current_positions, actors_power, actors_salience
            )
            
            # Actors move toward median based on their power and salience
            for i in range(len(current_positions)):
                movement = (median_position - current_positions[i]) * actors_salience[i] * 0.1
                current_positions[i] += movement
            
            new_median = self.compute_median_voter_position(
                current_positions, actors_power, actors_salience
            )
            position_history.append(new_median)
            
            # Check convergence
            if abs(new_median - median_position) < 0.01:
                break
        
        final_position = position_history[-1]
        return final_position, position_history
    
    def coalition_formation(self, actors_positions: np.ndarray,
                          actors_power: np.ndarray,
                          threshold: float = 0.5) -> List[List[int]]:
        """
        Identify potential coalitions based on position similarity.
        
        Args:
            actors_positions: Array of preferred positions for each actor
            actors_power: Array of power/influence for each actor
            threshold: Similarity threshold for coalition membership
            
        Returns:
            List of coalitions (each coalition is a list of actor indices)
        """
        num_actors = len(actors_positions)
        coalitions = []
        assigned = set()
        
        # Sort actors by power (descending)
        power_order = np.argsort(-actors_power)
        
        for leader_idx in power_order:
            if leader_idx in assigned:
                continue
            
            # Start new coalition with this leader
            coalition = [leader_idx]
            assigned.add(leader_idx)
            leader_position = actors_positions[leader_idx]
            
            # Find similar actors
            for other_idx in range(num_actors):
                if other_idx in assigned:
                    continue
                
                position_distance = abs(actors_positions[other_idx] - leader_position)
                if position_distance <= threshold * 100:  # Positions are 0-100
                    coalition.append(other_idx)
                    assigned.add(other_idx)
            
            if len(coalition) > 0:
                coalitions.append(coalition)
        
        return coalitions
    
    def predict_policy_outcome(self, actors_positions: np.ndarray,
                              actors_power: np.ndarray,
                              actors_salience: np.ndarray,
                              actors_risk_tolerance: np.ndarray) -> Dict[str, float]:
        """
        Predict policy outcome incorporating all actor attributes.
        
        Args:
            actors_positions: Array of preferred positions for each actor
            actors_power: Array of power/influence for each actor
            actors_salience: Array of salience/importance for each actor
            actors_risk_tolerance: Array of risk tolerance for each actor
            
        Returns:
            Dictionary with prediction metrics
        """
        # Compute convergence
        predicted_outcome, history = self.predict_convergence(
            actors_positions, actors_power, actors_salience
        )
        
        # Calculate utilities at predicted outcome
        utilities = []
        for i in range(len(actors_positions)):
            utility = self.expected_utility(
                actors_positions[i],
                predicted_outcome,
                actors_risk_tolerance[i]
            )
            utilities.append(utility)
        
        utilities = np.array(utilities)
        
        # Weight by power
        weighted_utility = np.sum(utilities * actors_power) / np.sum(actors_power)
        
        # Calculate support (actors close to outcome)
        support_threshold = 20  # Position distance
        supporters = np.sum(
            actors_power[np.abs(actors_positions - predicted_outcome) <= support_threshold]
        )
        total_power = np.sum(actors_power)
        
        return {
            'predicted_outcome': predicted_outcome,
            'weighted_utility': weighted_utility,
            'support_ratio': supporters / total_power if total_power > 0 else 0,
            'convergence_iterations': len(history),
            'position_variance': np.var(actors_positions)
        }
    
    def scenario_analysis(self, base_positions: np.ndarray,
                         actors_power: np.ndarray,
                         actors_salience: np.ndarray,
                         perturbations: List[Tuple[int, float]]) -> Dict[str, float]:
        """
        Analyze how the outcome changes under different scenarios.
        
        Args:
            base_positions: Base case positions
            actors_power: Power array
            actors_salience: Salience array
            perturbations: List of (actor_index, position_change) tuples
            
        Returns:
            Comparison of base case vs perturbed outcome
        """
        # Base case
        base_outcome = self.compute_median_voter_position(
            base_positions, actors_power, actors_salience
        )
        
        # Perturbed case
        perturbed_positions = base_positions.copy()
        for actor_idx, change in perturbations:
            perturbed_positions[actor_idx] += change
        
        perturbed_outcome = self.compute_median_voter_position(
            perturbed_positions, actors_power, actors_salience
        )
        
        return {
            'base_outcome': base_outcome,
            'perturbed_outcome': perturbed_outcome,
            'outcome_shift': perturbed_outcome - base_outcome,
            'sensitivity': abs(perturbed_outcome - base_outcome) / (
                sum(abs(change) for _, change in perturbations) + 1e-10
            )
        }
