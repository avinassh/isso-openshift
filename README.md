Isso Openshift Deployment Kit
=============================

**THIS PROJECT IS NO LONGER MAINTAINED ANYMORE**

This repo helps you installing [Isso](http://github.com/posativ/isso) on Openshift with just one click. 

# Instructions

There are three ways to perform installation, following is the method I prefer:
- Install `rhc`([instructions](https://developers.openshift.com/en/managing-client-tools.html)), then run following, you will get an Open Shift instance installed with Isso:

        rhc create-app appname python-2.7 --from-code https://github.com/avinassh/isso-openshift.git

- Above step also clones Git repository of your Open Shift instance, in current directory. Make changes to the config file and push back to Openshift, it will be redeployed with new settings.

### Alternative ways:

 - If you are using openshift web interface, pick [Python 2.7 cartridge](https://openshift.redhat.com/app/console/application_type/cart!python-2.7) and provide url of this repo in `Source Code` field. Thats all, Isso will be installed in your Open Shift instance!  
 - Now, from Open Shift App's main page, get it's Git address. Clone it your local machine and make changes to Isso config file. Do Git commit and push it back to Open Shift, it will be redeployed with new settings. 

Another way is, [fork the current repo](https://github.com/avinassh/isso-openshift) and make changes to config file as desired. And now use either method #1 or #2. However you may end up pushing sensitive information to public repo. So, be careful. 



# Notes
 - Why `dbpath` in `production.cfg` is setup like that and uses relative path?

    Read [this link](https://help.openshift.com/hc/en-us/articles/202398490-Persistant-storage-for-OpenShift-applications) to understand why database path is setup like that. TLDR; Everytime you make changes, the repo directory will be wiped clean and re-created and that's why Openshift provides specific location to store persistent data. The location of current running repo will be at `~/app-root/runtime/repo/` (check environment variable `$OPENSHIFT_REPO_DIR`) and location to store persistent data is at `~/app-root/data/` (check environment variable `$OPENSHIFT_DATA_DIR`).

# Credits
Thanks to Martin Zimmermann (posativ) for awesome Isso. He also helped me during initial deployments and troubleshooting, answering my noobie questions. Also thanks to user cyrozap on official [#isso IRC channel](http://webchat.freenode.net/?channels=#isso). An important part of code uses [Custom Application example](http://gunicorn-docs.readthedocs.org/en/latest/custom.html) from Gunicorn documents.

# License
The MIT License (MIT). Check `LICENSE`
