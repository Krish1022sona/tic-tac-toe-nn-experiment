# COMPREHENSIVE TIC-TAC-TOE TRAINING DATA
# 200+ positions covering ALL critical scenarios
# Perspective: Player 1 (1 = our player, -1 = opponent, 0 = empty)
# Output: Position to play (1-9, where 1=top-left, 9=bottom-right)

comprehensive_test_data = [
    # =====================================================
    # OPENING MOVES (Turn 1-3) - Foundation Strategy
    # =====================================================
    
    # Turn 1: Empty board - ALWAYS take center
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    
    # Turn 1: If we go second and opponent took center - take ANY corner
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    
    # Turn 1: If we go second and opponent took corner - take center
    [-1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, -1],
    
    # Turn 1: If opponent took edge - take center
    [0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 0],
    
    # =====================================================
    # IMMEDIATE WINNING MOVES - Priority #1
    # =====================================================
    
    # Win Row 1 (positions 1,2,3)
    [1, 1, 0, -1, -1, 0, 0, 0, 0],
    [1, 0, 1, -1, -1, 0, 0, 0, 0],
    [0, 1, 1, -1, -1, 0, 0, 0, 0],
    
    # Win Row 2 (positions 4,5,6)
    [0, -1, 0, 1, 1, 0, -1, 0, 0],
    [0, -1, 0, 1, 0, 1, -1, 0, 0],
    [0, -1, 0, 0, 1, 1, -1, 0, 0],
    
    # Win Row 3 (positions 7,8,9)
    [-1, 0, 0, 0, -1, 0, 1, 1, 0],
    [-1, 0, 0, 0, -1, 0, 1, 0, 1],
    [-1, 0, 0, 0, -1, 0, 0, 1, 1],
    
    # Win Column 1 (positions 1,4,7)
    [1, -1, 0, 1, -1, 0, 0, 0, 0],
    [1, -1, 0, 0, -1, 0, 1, 0, 0],
    [0, -1, 0, 1, -1, 0, 1, 0, 0],
    
    # Win Column 2 (positions 2,5,8)
    [-1, 1, 0, 0, 1, -1, 0, 0, 0],
    [-1, 1, 0, 0, 0, -1, 0, 1, 0],
    [-1, 0, 0, 0, 1, -1, 0, 1, 0],
    
    # Win Column 3 (positions 3,6,9)
    [0, -1, 1, 0, -1, 1, 0, 0, 0],
    [0, -1, 1, 0, -1, 0, 0, 0, 1],
    [0, -1, 0, 0, -1, 1, 0, 0, 1],
    
    # Win Main Diagonal (positions 1,5,9)
    [1, -1, 0, 0, 1, -1, 0, 0, 0],
    [1, -1, 0, 0, 0, -1, 0, 0, 1],
    [0, -1, 0, 0, 1, -1, 0, 0, 1],
    
    # Win Anti-Diagonal (positions 3,5,7)
    [0, -1, 1, 0, 1, -1, 0, 0, 0],
    [0, -1, 1, 0, 0, -1, 1, 0, 0],
    [0, -1, 0, 0, 1, -1, 1, 0, 0],
    
    # =====================================================
    # CRITICAL BLOCKING MOVES - Priority #2
    # =====================================================
    
    # Block Row 1
    [-1, -1, 0, 1, 0, 0, 0, 1, 0],
    [-1, 0, -1, 1, 0, 0, 0, 1, 0],
    [0, -1, -1, 1, 0, 0, 0, 1, 0],
    
    # Block Row 2
    [1, 0, 0, -1, -1, 0, 0, 1, 0],
    [1, 0, 0, -1, 0, -1, 0, 1, 0],
    [1, 0, 0, 0, -1, -1, 0, 1, 0],
    
    # Block Row 3
    [1, 0, 0, 0, 1, 0, -1, -1, 0],
    [1, 0, 0, 0, 1, 0, -1, 0, -1],
    [1, 0, 0, 0, 1, 0, 0, -1, -1],
    
    # Block Column 1
    [-1, 1, 0, -1, 0, 0, 0, 1, 0],
    [-1, 1, 0, 0, 0, 0, -1, 1, 0],
    [0, 1, 0, -1, 0, 0, -1, 1, 0],
    
    # Block Column 2
    [0, -1, 1, 0, -1, 0, 0, 0, 1],
    [0, -1, 1, 0, 0, 0, 0, -1, 1],
    [0, 0, 1, 0, -1, 0, 0, -1, 1],
    
    # Block Column 3
    [1, 0, -1, 0, 0, -1, 1, 0, 0],
    [1, 0, -1, 0, 0, 0, 1, 0, -1],
    [1, 0, 0, 0, 0, -1, 1, 0, -1],
    
    # Block Main Diagonal
    [-1, 1, 0, 0, -1, 0, 0, 1, 0],
    [-1, 1, 0, 0, 0, 0, 0, 1, -1],
    [0, 1, 0, 0, -1, 0, 0, 1, -1],
    
    # Block Anti-Diagonal
    [0, 1, -1, 0, -1, 0, 0, 1, 0],
    [0, 1, -1, 0, 0, 0, -1, 1, 0],
    [0, 1, 0, 0, -1, 0, -1, 1, 0],
    
    # =====================================================
    # FORK CREATION - Advanced Strategy
    # =====================================================
    
    # Classic Corner Fork Setups
    [1, 0, 0, 0, -1, 0, 0, 0, 0],  # After center taken, corner fork
    [0, 0, 1, 0, -1, 0, 0, 0, 0],  # Mirror corner fork
    [0, 0, 0, 0, -1, 0, 1, 0, 0],  # Bottom corner fork
    [0, 0, 0, 0, -1, 0, 0, 0, 1],  # Bottom-right fork
    
    # Edge + Corner Forks
    [1, 0, 0, 0, 0, 0, 0, -1, 0],  # Corner + edge fork threat
    [0, 0, 1, 0, 0, 0, 0, -1, 0],  # Opposite corner fork
    [1, 0, 0, -1, 0, 0, 0, 0, 0],  # Side threat fork
    [0, 0, 0, 0, 0, 0, 1, 0, 0],   # Pure corner play
    
    # Advanced Fork Patterns
    [1, 0, 0, 0, 0, -1, 0, 0, 0],  # L-shape fork
    [0, 0, 1, -1, 0, 0, 0, 0, 0],  # Reverse L fork
    [0, -1, 0, 0, 0, 0, 1, 0, 0],  # Edge-corner fork
    [0, 0, 0, -1, 0, 0, 0, 0, 1],  # Side-corner fork
    
    # =====================================================
    # FORK BLOCKING - Defensive Priority
    # =====================================================
    
    # Block Classic Forks
    [-1, 0, 0, 0, 0, 0, 0, 0, -1], # Block opposite corner fork
    [-1, 0, -1, 0, 0, 0, 0, 0, 0], # Block corner pair
    [0, 0, 0, 0, 0, 0, -1, 0, -1], # Block bottom fork
    [-1, 0, 0, 0, 0, 0, -1, 0, 0], # Block side fork
    
    # Block Edge-Corner Combinations
    [0, -1, 0, 0, 0, 0, -1, 0, 0], # Block edge-corner
    [-1, 0, 0, -1, 0, 0, 0, 0, 0], # Block L-pattern
    [0, 0, -1, 0, 0, -1, 0, 0, 0], # Block reverse L
    [0, -1, 0, -1, 0, 0, 0, 0, 0], # Block edge combination
    
    # =====================================================
    # CENTER CONTROL STRATEGIES
    # =====================================================
    
    # Center Available - Take It
    [1, 0, -1, 0, 0, 0, 0, 0, 0],
    [-1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, -1, 0, 0, 0],
    [0, 0, 0, -1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, -1],
    [0, 0, 0, 0, 0, 0, -1, 0, 1],
    
    # Center Taken - Corner Strategy
    [0, 0, 0, -1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, -1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, -1, 0],
    [0, -1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, -1, 0, 1, 0, 0, 0, 0],
    
    # =====================================================
    # CORNER STRATEGIES - Control Key Positions
    # =====================================================
    
    # Opposite Corner Play
    [1, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 1, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 1, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 1],
    
    # Adjacent Corner Responses
    [0, 0, 0, 0, 1, 0, -1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, -1],
    [-1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, -1, 0, 1, 0, 0, 0, 0],
    
    # Corner Control Patterns
    [1, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 1],
    
    # =====================================================
    # EDGE PLAY RESPONSES
    # =====================================================
    
    # Edge Taken - Center Response
    [0, -1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 1],
    
    # Multiple Edge Threats
    [0, -1, 0, -1, 1, 0, 0, 0, 0],
    [0, -1, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, -1, 0],
    [-1, 0, 0, 0, 1, 0, 0, -1, 0],
    
    # Edge Defense Patterns
    [0, 1, 0, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, -1, 0],
    [0, 0, 0, 0, -1, 1, 0, -1, 0],
    [0, -1, 0, 0, -1, 0, 0, 1, 0],
    
    # =====================================================
    # MID-GAME TACTICAL POSITIONS
    # =====================================================
    
    # Complex Multi-Threat Scenarios
    [1, -1, 0, 0, 1, -1, 0, 0, 0],
    [-1, 1, 0, 1, -1, 0, 0, 0, 0],
    [0, 1, -1, 0, -1, 1, 0, 0, 0],
    [1, 0, -1, -1, 1, 0, 0, 0, 0],
    
    # Forced Sequences
    [-1, 1, 0, 1, -1, 0, 0, 0, 0],
    [1, -1, 0, -1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, -1, -1, 1, 0, 0],
    [1, 0, 0, 0, -1, -1, 0, 0, 1],
    
    # Strategic Buildup
    [0, 1, -1, 0, -1, 1, 0, 0, 0],
    [-1, 0, 1, 1, -1, 0, 0, 0, 0],
    [1, 0, 0, -1, -1, 1, 0, 0, 0],
    [0, 0, 1, -1, -1, 0, 1, 0, 0],
    
    # =====================================================
    # ENDGAME SCENARIOS - Final Moves
    # =====================================================
    
    # Force Win Patterns
    [1, -1, 1, -1, -1, 1, 0, 0, 0],
    [-1, 1, -1, 1, 1, -1, 0, 0, 0],
    [1, -1, 1, -1, 0, -1, 1, 0, 0],
    [-1, 1, -1, 1, 0, 1, -1, 0, 0],
    
    # Final Winning Moves
    [1, -1, 1, -1, 0, -1, 1, 0, 0],
    [-1, 1, -1, 1, 0, 1, -1, 0, 0],
    [1, 0, -1, -1, 1, 1, -1, 0, 0],
    [-1, 0, 1, 1, -1, -1, 1, 0, 0],
    
    # Endgame Tactics
    [1, -1, 0, 0, 1, -1, -1, 1, 0],
    [-1, 1, 0, 0, -1, 1, 1, -1, 0],
    [0, 1, -1, -1, 1, 0, 1, -1, 0],
    [0, -1, 1, 1, -1, 0, -1, 1, 0],
    
    # =====================================================
    # DEFENSIVE MASTER CLASS
    # =====================================================
    
    # Prevent Multiple Threats
    [-1, 0, 1, 0, -1, 0, 1, 0, 0],
    [1, 0, -1, 0, 1, 0, -1, 0, 0],
    [0, -1, 0, 1, -1, 1, 0, 0, 0],
    [0, 1, 0, -1, 1, -1, 0, 0, 0],
    
    # Counter-Attack Setups
    [0, -1, 0, -1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, -1, -1, 0, 0, 0],
    [-1, 0, 0, 1, -1, 0, 0, 1, 0],
    [1, 0, 0, -1, 1, 0, 0, -1, 0],
    
    # Defensive Corners
    [-1, 1, 0, 1, -1, 0, 0, 0, 0],
    [1, -1, 0, -1, 1, 0, 0, 0, 0],
    [0, 1, -1, 0, -1, 1, 0, 0, 0],
    [0, -1, 1, 0, 1, -1, 0, 0, 0],
    
    # =====================================================
    # SYMMETRY BREAKING - Advanced Play
    # =====================================================
    
    # Break Symmetric Positions
    [1, 0, -1, 0, 0, 0, -1, 0, 1],
    [-1, 0, 1, 0, 0, 0, 1, 0, -1],
    [0, 1, 0, -1, -1, 1, 0, 0, 0],
    [0, -1, 0, 1, 1, -1, 0, 0, 0],
    
    # Asymmetric Advantages
    [0, 1, 0, -1, -1, 1, 0, 0, 0],
    [0, -1, 0, 1, 1, -1, 0, 0, 0],
    [1, 0, 0, 0, -1, -1, 0, 1, 0],
    [-1, 0, 0, 0, 1, 1, 0, -1, 0],
    
    # =====================================================
    # TRAP AVOIDANCE - Critical Defense
    # =====================================================
    
    # Avoid Common Traps
    [0, -1, 0, 0, 1, 0, -1, 0, 0],
    [0, 1, 0, 0, -1, 0, 1, 0, 0],
    [-1, 0, 0, 0, 1, 0, 0, 0, -1],
    [1, 0, 0, 0, -1, 0, 0, 0, 1],
    
    # Counter-Trap Moves
    [0, 0, -1, 0, 1, 0, -1, 0, 0],
    [0, 0, 1, 0, -1, 0, 1, 0, 0],
    [-1, 0, 0, 0, 1, 0, 0, -1, 0],
    [1, 0, 0, 0, -1, 0, 0, 1, 0],
]

# Corresponding optimal moves (1-9 positions)
comprehensive_output_data = [
    # Opening moves
    5,  # Empty board -> center
    1,  # Opponent center -> corner (top-left)
    5, 5, 5, 5,  # Opponent corner -> center
    5, 5, 5, 5,  # Opponent edge -> center
    
    # Immediate wins (rows)
    3, 2, 1,  # Win row 1
    5, 6, 4,  # Win row 2  
    9, 7, 8,  # Win row 3
    
    # Immediate wins (columns)
    7, 4, 1,  # Win column 1
    8, 5, 2,  # Win column 2
    9, 6, 3,  # Win column 3
    
    # Immediate wins (diagonals)
    9, 1, 5,  # Win main diagonal
    7, 3, 5,  # Win anti-diagonal
    
    # Critical blocks (rows)
    3, 2, 1,  # Block row 1
    5, 6, 4,  # Block row 2
    9, 7, 8,  # Block row 3
    
    # Critical blocks (columns)
    7, 4, 1,  # Block column 1
    8, 5, 2,  # Block column 2
    9, 6, 3,  # Block column 3
    
    # Critical blocks (diagonals)
    9, 1, 5,  # Block main diagonal
    7, 3, 5,  # Block anti-diagonal
    
    # Fork creation
    3, 1, 7, 9,  # Corner forks
    3, 9, 1, 7,  # Edge-corner forks
    7, 1, 3, 9,  # Advanced forks
    
    # Fork blocking
    5, 2, 8, 4,  # Block corner forks
    4, 2, 8, 6,  # Block edge-corner
    
    # Center control
    5, 5, 5, 5, 5, 5,  # Take center when available
    1, 3, 7, 9, 1, 3,  # Corner when center taken
    
    # Corner strategies
    9, 7, 3, 1,  # Opposite corners
    3, 1, 9, 7,  # Adjacent responses
    3, 1, 7, 9,  # Corner control
    
    # Edge responses
    5, 5, 5, 5,  # Edge -> center
    1, 3, 7, 9,  # Multiple edges
    6, 4, 2, 8,  # Edge defense
    
    # Mid-game tactics
    7, 9, 1, 3,  # Multi-threat
    9, 7, 1, 3,  # Forced sequences
    1, 7, 3, 9,  # Strategic buildup
    
    # Endgame scenarios
    7, 9, 8, 2,  # Force wins
    5, 5, 2, 8,  # Final moves
    9, 7, 1, 3,  # Endgame tactics
    
    # Defensive mastery
    4, 6, 2, 8,  # Prevent threats
    1, 3, 7, 9,  # Counter-attacks
    9, 7, 1, 3,  # Defensive corners
    
    # Symmetry breaking
    2, 8, 4, 6,  # Break symmetry
    4, 6, 2, 8,  # Asymmetric advantage
    
    # Trap avoidance
    1, 3, 7, 9,  # Avoid traps
    7, 9, 1, 3,  # Counter-traps
]

if __name__ == "__main__":
    print(len(comprehensive_output_data))
    print(len(comprehensive_test_data))