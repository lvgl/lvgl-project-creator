# Project creator

### Kickstart your LVGL projects with ease!

Accelerate your LVGL development with the Project Creator. Select, configure, and launch your projects in just a few clicks. It works on Windows, Linux, Mac and in VSCode too. More projects are coming soon! 🚀

![Untitled](https://github.com/user-attachments/assets/84871ddb-d096-4f69-a587-63a672bd7658)


## Features
### Just works
Works on any OS, and in VSCode without git or any other extra tools.

### Faster than git clone
Pre-packaged with LVGL, it saves you time by skipping repetitive downloads.


### Tailor to your needs
Customize your project’s initial setup through an intuitive and user-friendly interface.

## Technical overview

### List of projects and project properties

- There are `manifest.json` files in some repositories
- We collect the URL of these manifests [here](https://github.com/lvgl/lvgl-project-creator/blob/master/manifests)
- [This script](https://github.com/lvgl/lvgl-project-creator/blob/master/build_manifest_all.py) concatenates the manifests in [manifest_all.json](https://github.com/lvgl/lvgl-project-creator/blob/master/manifest_all.json)
- `manifest_all.json` is loaded into the project creator app
- The Project Creator clones the repository pointed by the `urlToClone` tag in the manifests
- The Project Creator stores a local copy of LVGL and copied it to the correct location of the cloned project   

## Frequently Asked Questions

### Will you add more projects?
Yes, we have started working on adding the LVGL projects from the major chip vendors’ SDKs and RTOS projects. Stay tuned, hundreds of projects will be available soon.

###  Can I submit my own LVGL project?
You can’t at this moment. We added projects for which we know that they will be maintained either by us or by a mature project or vendor. However if you would like to see a specific board or project, contact us, and we will also contact the related manufacturer or maintainer.

### How can I give feedback and ask for help?
Please use the [Project Creator](https://forum.lvgl.io/c/project-creator) category on our Forum.

### Is this tool open source?
Not yet, but we are considering making it open-source in the near future.
