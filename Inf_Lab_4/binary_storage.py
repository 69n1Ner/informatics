import pickle

def serialize_binary(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def deserialize_binary(path):
    with open(path, "rb") as f:
        return pickle.load(f)
