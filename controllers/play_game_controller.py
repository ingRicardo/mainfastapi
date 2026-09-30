import random
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/playgame",
    tags=["Tuto_3"]
)

CHOICES = ["Rock", "Paper", "Scissors"]

# Pydantic model for request validation
class PlayRequest(BaseModel):
    choice: int = Field(..., ge=1, le=3, description="1 for Rock, 2 for Paper, 3 for Scissors")

@router.post("/play")
def play_game(payload: PlayRequest):
    user_choice_idx = payload.choice
    user_choice = CHOICES[user_choice_idx - 1]

    # Computer choice (1 to 3)
    comp_choice_idx = random.randint(1, 3)
    computer_choice = CHOICES[comp_choice_idx - 1]

    # Determine winner
    if user_choice_idx == comp_choice_idx:
        result = "It's a Tie!"
    elif (
        (user_choice_idx == 1 and comp_choice_idx == 3) or
        (user_choice_idx == 2 and comp_choice_idx == 1) or
        (user_choice_idx == 3 and comp_choice_idx == 2)
    ):
        result = "User Wins!"
    else:
        result = "Computer Wins!"

    return {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "rules_summary": f"{user_choice} vs {computer_choice}"
    }
