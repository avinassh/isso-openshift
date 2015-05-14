Isso Openshift Deployment Kit
=============================

This repo helps you installing [Isso](http://github.com/posativ/isso) on Openshift with just one click. 

# Instructions

 - If you are using openshift web interface, pick [Python 2.7 cartridge](https://openshift.redhat.com/app/console/application_type/cart!python-2.7) and provide url of this repo in `Source Code` field. Thats all!  
 - If you are using `rhc` then run following:

        rhc create-app appname python-2.7 --from-code https://github.com/avinassh/isso-openshift.git

# Notes
 - Why `dbpath` in `production.cfg` is setup like that and uses relative path?

    Read [this link](https://help.openshift.com/hc/en-us/articles/202398490-Persistant-storage-for-OpenShift-applications) to understand why database path is setup like that. TLDR; Everytime you make changes, the repo directory will be wiped clean and re-created and that's why Openshift provides specific location to store persistent data. The location of current running repo will be at `~/app-root/runtime/repo/` (check environment variable `$OPENSHIFT_REPO_DIR`) and location to store persistent data is at `~/app-root/data/` (check environment variable `$OPENSHIFT_DATA_DIR`).

# Credits
Thanks to Martin Zimmermann (posativ) for awesome Isso. He also helped me during initial deployments and troubleshooting, answering my noobie questions. Also thanks to user cyrozap on official [#isso IRC channel](http://webchat.freenode.net/?channels=#isso). An important part of code uses [Custom Application example](http://gunicorn-docs.readthedocs.org/en/latest/custom.html) from Gunicorn documents.

# License
The MIT License (MIT). Check `LICENSE`