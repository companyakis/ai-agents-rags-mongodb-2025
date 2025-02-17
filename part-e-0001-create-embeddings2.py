# Extract the total_tokens from response_dict

print(response_dict["usage"]["total_tokens"])

# Extract the embeddings from response_dict

print(response_dict["data"][0]["embedding"])
