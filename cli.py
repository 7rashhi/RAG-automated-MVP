
import argparse
from retrieval import retrieve_similar_snippets

def main():
    """CLI for Intelligent Code Review Assistant"""
    parser = argparse.ArgumentParser(description="AI-Powered Code Review Assistant")
    parser.add_argument("code", type=str, help="Enter the code snippet for review")
    
    args = parser.parse_args()
    user_code = args.code

    # Retrieve similar code snippets
    retrieved_code = retrieve_similar_snippets(user_code)

    print("\n\033[92m🔍 Retrieved Code Snippets:\033[0m")  

    # Handle empty or invalid results
    if not retrieved_code or isinstance(retrieved_code, str):
        print("\033[91m❌ No relevant code found.\033[0m")
        return

    # Print retrieved snippets
    for index, snippet in enumerate(retrieved_code, start=1):
        if isinstance(snippet, dict):
            print(f"\n\033[94m📌 Snippet {index} from:\033[0m {snippet.get('repo', 'Unknown Repo')} | {snippet.get('file', 'Unknown File')}")
            print("\033[96m💻 Code:\033[0m\n", snippet.get("code", "No code available"))
            print("\033[90m🔗 Source URL:\033[0m", snippet.get("url", "No URL available"))
        else:
            print("\033[91m⚠️ Unexpected data format:\033[0m", snippet)

if __name__ == "__main__":
    main()
