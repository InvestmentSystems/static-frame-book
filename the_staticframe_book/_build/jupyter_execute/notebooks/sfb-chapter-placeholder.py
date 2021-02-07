# staticframe (chapter placeholder)

```{warning}
Main Heading (start with the single # and then go to ##. dont skip to ###)
```

import static_frame as sf

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum...

```{warning}
This notebook is only a placeholder for actual chapters.
```

```{note}
This is an example note.
```

## Second Heading (ie creating a sample frame)

f = sf.Frame.from_dict(dict(a=(2,2),b=(True,False),c=('10','20')))
f

### Third Heading (ie selecting column data)

f.loc[:,'c']

### Third Heading (ie selecting multiple columns)

f[['b', 'c']]

### Third Heading (ie selecting row data)

f.loc[1,:]

### Third Heading (ie selecting something else)

