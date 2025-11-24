import datetime

def decode_linkedin_urn(urn_id):
    """
    Decodes the LinkedIn URN (Snowflake ID) to extract the exact creation timestamp.
    """
    try:
        # LinkedIn IDs are 64-bit integers. 
        # The first 41 bits represent the timestamp in milliseconds since the epoch (1970-01-01).
        id_int = int(urn_id)
        binary = bin(id_int)[2:].zfill(64)
        first_41_bits = binary[:41]
        timestamp_ms = int(first_41_bits, 2)
        
        dt_object = datetime.datetime.fromtimestamp(timestamp_ms / 1000.0, tz=datetime.timezone.utc)
        return dt_object
    except Exception as e:
        return f"Error decoding: {e}"

if __name__ == "__main__":
    # IDs from the Case Study
    article_id = "7398143692458549250"
    response_id = "7398149258073477120"
    
    print(f"--- FORENSIC TIMELINE VERIFICATION ---")
    t1 = decode_linkedin_urn(article_id)
    t2 = decode_linkedin_urn(response_id)
    
    print(f"Article Published: {t1} UTC")
    print(f"Rebuttal Posted:   {t2} UTC")
    
    diff = t2 - t1
    print(f"Delta: {diff} (~{diff.seconds // 60} minutes)")
    print(f"--------------------------------------")
