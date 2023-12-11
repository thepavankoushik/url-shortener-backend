import uuid

unique_id = uuid.uuid4()
base62_id = uuid.uuid4().int
short_base62_id = str(base62_id)[:7]
print(short_base62_id)