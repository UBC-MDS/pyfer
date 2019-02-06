Pyfer

Function description:

### Specify

Input parameter

Dataframe

response: Selected Response variable

Output

Dataframe with 2 columns

With response variable in column 1 (i.e. ordered)

### Generate

Input parameter

Dataframe with 2 columns (ordered)

Number of resamples Type: Integer

Type: "Perm" or "Bootstrap" Default: "Bootstrap"

Output

Dataframe with 3 columns (Columns: x, y, sample_id)

### Calculate

After grouping by each sample, we calculate the mean of the each sample's response variable.

Input parameter

Dataframe with 3 columns (Columns: x, y, sample_id)

Statistic: String. "Mean" or "Median"

Output

Dataframe with length equal to number of resampled groups.

### get_ci

Input parameter

Dataframe with length equal to number of resampled groups.

Interval: Percentage Float (0-100)

Output

Dataframe (with 3 columns): Statistic (Point Estimate), Lower Bound, Upper Bound


