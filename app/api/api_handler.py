from fastapi import HTTPException, Query
import requests
import logging
from sentiment_analysis.classification import SentimentAnalyzer

logger = logging.getLogger(__name__)

class FedditAPI:
    @staticmethod
    def get_comments_for_subfeddit(subfeddit_name, skip=0, limit=25, start_time=None, end_time=None, sort_by_score=False):
        subfeddit_id = FedditAPI.get_subfeddit_id(subfeddit_name)
        # Make a request to the Feddit API to get comments for the specified subfeddit_id
        api_url = f"http://feddit:8080/api/v1/comments/?subfeddit_id={subfeddit_id}&skip={skip}&limit={limit}"

        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            # Extract relevant information
            comments = data.get("comments", [])
            result = []
            # Apply sentiment analysis and add polarity scores to each comment
            for comment in comments:
                comment_text = comment.get("text", "")
                polarity, classification = SentimentAnalyzer.analyze_sentiment(comment_text)
                processed_comment = {
            "id": comment.get("id"),
            "text": comment_text,
            "polarity_score": polarity,
            "classification": classification
        }

            # Optional: Filter comments by time range
                if start_time and end_time:
                    comment_timestamp = comment.get("created_at", 0)
                    if start_time.timestamp() <= comment_timestamp <= end_time.timestamp():
                        result.append(processed_comment)
                else:
                    result.append(processed_comment)

            # Optional: Sort comments by polarity score
            if sort_by_score:
                result.sort(key=lambda x: x["polarity_score"], reverse=True)

            return result
        
        except requests.RequestException as e:
            # Handle exceptions, log errors, etc.
            logger.error(f"Error fetching comments from Feddit API: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

        
    @staticmethod  
    def get_subfeddit_id(subfeddit_name):
    
    # Make a request to the Feddit API to get detailed information for the specified subfeddit_name
        api_url = f"http://feddit:8080/api/v1/subfeddits/"

        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
        
            for subfeddit in data.get("subfeddits", []):
                if subfeddit.get("title") == subfeddit_name:
                    return subfeddit.get("id")
            return None
        except requests.RequestException as e:
        # Handle exceptions, log errors, etc.
            logger.error(f"Error fetching subfeddit information from Feddit API: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

