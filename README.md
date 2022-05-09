Blender packaged as a python wheel.

This package explicitly pins to the specific version of python that would normally be distributed with blender itself.

## Use in non-rendering scenarios

Scripts that utilize no rendering capabilities at all (including baking) should work without issue.

## Use in GPU-based rendering scenarios

# With cycles

So long as there is a reachable GPU, cycles will load and render the scene.
If your deployment target is a container, check the relevant runtime documentation.

# With EEVEE

On standard desktops, this package should be able to render just fine.

However, Blender EEVEE itself doesn't currently support "headless" - that is, machines without an active user display session - scenarios, and this limitation is reflected in this package.
This is particularly reflected in container deployments, especially when the host is a server without a display.
It's possible to work around these limitations in some cases, but this isn't officially a supported scenario.
