def filter(**lookups):
    for k, v in lookups.items():
        print(k.split('__'), v)

filter(name__startswith='Re', age__lt=40, city__endswith='aulo')
