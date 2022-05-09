import os

from skbuild import setup

package_dir = "src"
package = "blenderpy"
source_directory = os.path.join(package_dir, package)

setup(
    packages=[package],
    package_dir={"": package_dir},
    cmake_install_dir=source_directory,
    cmake_source_dir="/blender_wheel/blender",
    cmake_args=[
        "-C/blender_wheel/blender/build_files/cmake/config/bpy_module.cmake",
        "-DWITH_INSTALL_PORTABLE=ON",
    ]
)
