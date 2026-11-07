def cakes(recipe, available):
    results = []
    for k, v in recipe.items():
        if k not in available:
            return 0
        else:
            my_result = available[k] // v
            results.append(my_result)
    return min(results)
