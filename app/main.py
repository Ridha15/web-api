from fastapi import FastAPI,Query

from api.api_handler import FedditAPI
from datetime import datetime

app = FastAPI(title="Feddit Comments API")

@app.get("/comments_sentiment/")
async def get_comments(
    subfeddit_name: str,
    limit: int = Query(25, description="Max number of comments in the response"),
    start_time: datetime = Query(None, description="Start time for filtering comments"),
    end_time: datetime = Query(None, description="End time for filtering comments"),
    sort_by_score: bool = Query(False, description="Sort comments by polarity score"),
):
    """
    Get sentiment analysis for comments in a subfeddit.

    Parameters:
    - subfeddit_name: Name of the subfeddit.
    - limit: Max number of comments in the response.
    - start_time: Start time for filtering comments.
    - end_time: End time for filtering comments.
    - sort_by_score: Sort comments by polarity score.

    Returns:
    - List of comments with sentiment analysis.
    """
    fedditapi = FedditAPI()
    result = fedditapi.get_comments_for_subfeddit(subfeddit_name, limit=limit, start_time=start_time, end_time=end_time, sort_by_score=sort_by_score)
    return result
