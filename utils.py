def summary(col):
    print '-' * 30
    print 'name:            ', col.name
    print 'dtype:           ', col.dtype
    print 'num. rows:       ', len(col)
    print 'N/A count:       ', col.isnull().sum()
    print 'N/A ratio:       ', 1.0 * col.isnull().sum() / len(col)
    print 'distinct values: ', len(col.value_counts())
    if col.dtype == 'object':
        print '-' * 30, '\n', 'top 10 values:'
        print col.value_counts().head(10)
        print '-' * 30, '\n', 'bottom 10 values:'
        print col.value_counts().tail(10)
    else:
        print '-' * 30, '\n', 'top 3 values:'
        print col.value_counts().head(3)
        print '-' * 30, '\n', 'bottom 3 values:'
        print col.value_counts().tail(3)
        print '-' * 30
        print col.describe()
    print '-' * 30

