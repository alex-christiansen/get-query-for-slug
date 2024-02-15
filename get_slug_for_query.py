import argparse
import looker_sdk
from looker_sdk import models40 as models
from urllib.parse import urlparse

# Configuration loading
sdk = looker_sdk.init40("example.ini")


def extract_slug_from_share_url(share_url: str) -> str:
    """Extracts the slug from a Looker share URL.
    Args:
        share_url: The Looker share URL.
    Returns:
        The extracted slug.
    Raises:
        ValueError: If the share URL is not in the expected format.
    """
    parsed_url = urlparse(share_url)
    path_components = parsed_url.path.split("/")
    if len(path_components) < 3:
        raise ValueError("Invalid share URL format")
    return path_components[2]

def validate_query_by_slug(query_id: int, slug: str) -> bool:
    """Validates a query ID against a slug.
    Args:
        query_id: The Looker query ID.
        slug: The slug to validate.
    Returns:
        True if the query ID matches the slug, False otherwise.
    """
    try:
        response = sdk.query_for_slug(slug=slug)
        return int(response.id) == int(query_id)
    except looker_sdk.rtl.ApiError as e:
        print(f"Error validating query: {e}")
        return False


def main(query_id: int):
    """Main program logic.

    Args:
        query_id: The Looker query ID.
    """

    try:
        query = sdk.query(query_id=str(query_id))
        slug = extract_slug_from_share_url(query.share_url)

        if validate_query_by_slug(query_id, slug):
            print("Validation successful")
            print(f"The slug for query id {query_id} is {slug}")
        else:
            print("Error, try a new query ID or use system activity link.")

    except looker_sdk.rtl.ApiError as e:
        print(f"Error fetching query: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get and validate slug for a Looker query.")
    parser.add_argument("query_id", type=int, help="The ID of the Looker query.")
    args = parser.parse_args()
    main(args.query_id)
