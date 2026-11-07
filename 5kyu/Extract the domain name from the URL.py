def domain_name(url):
    step1 = url.replace("/","").replace(":", ".")
    step2 = step1.split(".")
    skip = ["http", "https", "www"]
    for i in range(len(step2)):
        if step2[i] not in skip:
            return step2[i]
