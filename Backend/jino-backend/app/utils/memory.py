def merge_memory(old, new):
    old.update(new)  # new keys overwrite old ones
    return old
