import boto3

def delete_bucket(bucket_name, s3_client, s3_resource):
    """Deletes all objects and versions in a bucket, then deletes the bucket itself."""
    bucket = s3_resource.Bucket(bucket_name)

    # Delete all object versions (required for versioned buckets)
    try:
        bucket.object_versions.delete()
        print(f"Deleted all objects and versions in {bucket_name}")
    except Exception as e:
        print(f"Error deleting objects in {bucket_name}: {e}")

    # Delete the bucket itself
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Deleted bucket: {bucket_name}")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")

def delete_matching_buckets(search_string, omit_buckets):
    s3_client = boto3.client("s3")
    s3_resource = boto3.resource("s3")
    response = s3_client.list_buckets()

    for bucket in response.get('Buckets', []):
        bucket_name = bucket['Name']
        if bucket_name in omit_buckets:
            print(f"Found matching bucket but omitted: {bucket_name}")
        elif search_string in bucket_name:
            print(f"Found matching bucket: {bucket_name}")
            delete_bucket(bucket_name, s3_client, s3_resource)

if __name__ == "__main__":
    search_term = "luit"
    omit_buckets = ["luit-automation"]
    delete_matching_buckets(search_term, omit_buckets)
