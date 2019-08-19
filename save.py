


with open("data/mario.chr","rb") as f:
    with open("data/r.chr", "wb") as s:
        for line in f:
            s.write(line)

    s.close()