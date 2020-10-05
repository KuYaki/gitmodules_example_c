# gitmodules_example_c
This is the third (and the last) example for the 
<a href=https://github.com/KuYaki/gitmodules>gitmodules</a> project.
However it is just a part of a complex construction with root at 
<a href=https://github.com/KuYaki/gitmodules_example_a>gitmodules_example_a</a>.

## Dependencies
This project has no any dependencies and its only submodule is an ordinary submodule.
<a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a> 
should be imported as a gitmodule like in the
<a href=https://github.com/KuYaki/gitmodules_example_b>gitmodules_example_b</a> project.

## Description
<a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a>
can be executed as a main script but if you will try to import it in any other project as a git submodule
you will be forced to append its path to the <b>sys.path</b>:

```python
import sys
sys.path.append("gitmodules_example_c")
from gitmodules_example_c import c
```

Or you can simply use <a href=https://github.com/KuYaki/gitmodules>gitmodules</a> instead:

```python
import gitmodules
from gitmodules_example_c import c
```
